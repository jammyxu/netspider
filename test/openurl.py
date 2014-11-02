#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2014-10-06 22:06:17
# Author  : Jimmy.Xu jimmyxu@anjuke.com
# @Version : $Id$

import urllib.request
 
url = "http://www.baidu.com"
data = urllib.request.urlopen(url).read()
data = data.decode('UTF-8')
print(data)



