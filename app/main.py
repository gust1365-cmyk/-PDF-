#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import os
import webview

def resource_path(filename):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, filename)
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)

def main():
    html_path = resource_path('INTOPS_발주서생성기.html')
    html_url  = 'file:///' + html_path.replace('\\', '/')
    webview.create_window(
        title='INTOPS 발주서 생성기',
        url=html_url,
        width=1280,
        height=900,
        min_size=(900, 600),
    )
    webview.start(debug=False)

if __name__ == '__main__':
    main()
