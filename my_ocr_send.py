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
# pip install pillow
from PIL import ImageGrab

img = ImageGrab.grab()
# or ImageGrab.grab() to grab the whole screen!

# print(img)
# <PIL.BmpImagePlugin.DibImageFile image mode=RGB size=380x173 at 0x16A43064DA0>
with open('baidu_access_token.txt') as file_obj:
    access_token_val = file_obj.read()

request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"

## 文件
# file_name = '1.jpg'
# 二进制方式打开图片文件
# with open(file_name, 'rb') as file_obj:
#     img = base64.b64encode(file_obj.read())

## 剪贴板
img = base64.b64encode(img)

params = {"image": img}
request_url = request_url + "?access_token=" + access_token_val
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print(response.json())

words_lst = [txt['words'] for txt in response.json()['words_result']]

text = "".join(words_lst)

imgclip = pc.paste()
pc.copy(text)
