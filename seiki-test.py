#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

text = "【ネクスト】テスト（python）"
reg = '(?<=\（).+?(?=\）)'
ret = re.findall(reg, text)

if not ret:
    reg = '(?<=\().+?(?=\))'
    ret = re.findall(reg, text)

print(ret)
