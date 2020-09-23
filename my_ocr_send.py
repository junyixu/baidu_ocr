#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 junyi <junyi@Junix>
#
# Distributed under terms of the MIT license.
'''
通用文字识别
'''

from io import StringIO
import requests
import base64
import pyperclip as pc
# import subprocess
# import logging
import os
import subprocess
# pc.set_clipboard("xclip")
# logger = logging.getLogger(__name__)

# def write_to_file(file_name):
#     return subprocess.check_output(
#         'xclip -selection clipboard -o -t image/jpg ' + file_name,
#         env={
#             'LANG': 'en_US.UTF-8'
#         }).decode('utf-8')

# def run_cmd(cmd):
#     logger.debug('running cmd: %r', cmd)
#     subprocess.check_call(cmd)


def call_flameshot():
    cmd = 'flameshot gui -r'
    res = subprocess.Popen(
        cmd, shell=True, stdout=subprocess.PIPE, close_fds=True)
    raw_text = res.stdout.readlines()
    text = b''
    for i in range(len(raw_text)):
        text = text+raw_text[i]
    return text
    # run_cmd(cmd)


def baidu_response(text_result):
    with open('./baidu_access_token.txt') as file_obj:
        access_token_val = file_obj.read()
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"
    # 二进制方式打开图片文件
    img = base64.b64encode(text_result)
    params = {"image": img}
    request_url = request_url + "?access_token=" + access_token_val
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    return response


# pasting the text from clipboard
# imgclip = pc.paste()

# with open(file_name, 'w') as f:
#     f.write(imgclip)


def main():
    text_result = call_flameshot()
    response = ""
    try:
        response = baidu_response(text_result)
    except Exception as e:
        subprocess.Popen(
            ['notify-send', "从百度获取响应失败！"])
        return -1
    words_lst = [txt['words'] for txt in response.json()['words_result']]

    text = "".join(words_lst)
    # copying text to clipboard
    pc.copy(text)


if __name__ == "__main__":
    main()
