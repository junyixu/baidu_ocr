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

import requests
import base64
import pyperclip as pc
import subprocess
import logging
import os
pc.set_clipboard("xclip")
logger = logging.getLogger(__name__)

# def write_to_file(file_name):
#     return subprocess.check_output(
#         'xclip -selection clipboard -o -t image/jpg ' + file_name,
#         env={
#             'LANG': 'en_US.UTF-8'
#         }).decode('utf-8')

# def run_cmd(cmd):
#     logger.debug('running cmd: %r', cmd)
#     subprocess.check_call(cmd)


def write_to_file(file_name):
    cmd = 'flameshot gui -r | xclip -selection clipboard && xclip -selection clipboard -o -t image/jpg > ' + file_name
    os.system(cmd)
    # run_cmd(cmd)


def baidu_response(file_name):
    with open('./baidu_access_token.txt') as file_obj:
        access_token_val = file_obj.read()
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"
    # 二进制方式打开图片文件
    with open(file_name, 'rb') as file_obj:
        img = base64.b64encode(file_obj.read())
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
    file_name = '/tmp/img_to_ocr.jpg'
    write_to_file(file_name)
    response = baidu_response(file_name)
    if response:
        words_lst = [txt['words'] for txt in response.json()['words_result']]

    text = "".join(words_lst)
    # copying text to clipboard
    pc.copy(text)


if __name__ == "__main__":
    main()
