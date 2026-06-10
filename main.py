#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import os
import base64
import webview

def resource_path(filename):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, filename)
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)


class API:
    """JS에서 window.pywebview.api.xxx() 로 호출되는 Python 메서드"""

    def save_pdf(self, filename: str, b64data: str) -> dict:
        """
        JS에서 base64 인코딩된 PDF 데이터를 받아 파일 저장 다이얼로그 없이
        사용자 Documents 폴더 또는 선택 경로에 저장.
        """
        try:
            # 저장 경로: Documents/발주서 폴더
            docs = os.path.join(os.path.expanduser('~'), 'Documents', '발주서')
            os.makedirs(docs, exist_ok=True)
            safe_name = filename if filename.endswith('.pdf') else filename + '.pdf'
            out_path = os.path.join(docs, safe_name)

            pdf_bytes = base64.b64decode(b64data)
            with open(out_path, 'wb') as f:
                f.write(pdf_bytes)

            return {'ok': True, 'path': out_path}
        except Exception as e:
            return {'ok': False, 'error': str(e)}

    def save_pdf_dialog(self, filename: str, b64data: str) -> dict:
        """저장 위치를 사용자가 선택하는 버전 (다이얼로그 사용)"""
        try:
            safe_name = filename if filename.endswith('.pdf') else filename + '.pdf'
            save_path = window.create_file_dialog(
                webview.SAVE_DIALOG,
                directory=os.path.join(os.path.expanduser('~'), 'Documents'),
                save_filename=safe_name,
                file_types=('PDF (*.pdf)',)
            )
            if not save_path:
                return {'ok': False, 'error': 'cancelled'}
            path = save_path[0] if isinstance(save_path, (list, tuple)) else save_path
            pdf_bytes = base64.b64decode(b64data)
            with open(path, 'wb') as f:
                f.write(pdf_bytes)
            return {'ok': True, 'path': path}
        except Exception as e:
            return {'ok': False, 'error': str(e)}

    def open_folder(self, folder_path: str) -> dict:
        """저장된 폴더를 탐색기로 열기"""
        try:
            import subprocess
            subprocess.Popen(f'explorer "{folder_path}"')
            return {'ok': True}
        except Exception as e:
            return {'ok': False, 'error': str(e)}


api = API()
window = None

def main():
    global window
    html_path = resource_path('INTOPS_발주서생성기.html')
    html_url  = 'file:///' + html_path.replace('\\', '/')
    window = webview.create_window(
        title='INTOPS 발주서 생성기',
        url=html_url,
        width=1280,
        height=900,
        min_size=(900, 600),
        js_api=api,
    )
    webview.start(debug=False)

if __name__ == '__main__':
    main()
