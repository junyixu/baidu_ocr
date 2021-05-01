#! /bin/bash
#
# test.bash
# Copyright (C) 2021 junyi <junyi@Junix>
#
# Distributed under terms of the MIT license.
#


BAIDU_ACCESS_TOKEN=$(python ./my_ocr_get_access_token.py)
sed -i "s/export BAIDU_ACCESS_TOKEN=.*$/export BAIDU_ACCESS_TOKEN='$BAIDU_ACCESS_TOKEN'/g" ~/.zprofile
