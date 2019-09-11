# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 23:30:51 2019

@author: tanma
"""

import urllib.request

urls = ['http://164.100.79.153/judis/chennai/index.php/casestatus/viewpdf/463100',\
'http://164.100.79.153/judis/chennai/index.php/casestatus/viewpdf/463101',\
'http://164.100.79.153/judis/chennai/index.php/casestatus/viewpdf/463102',\
'http://164.100.79.153/judis/chennai/index.php/casestatus/viewpdf/463103',\
'http://164.100.79.153/judis/chennai/index.php/casestatus/viewpdf/463104',\
'http://164.100.79.153/judis/chennai/index.php/casestatus/viewpdf/463105',\
'http://164.100.79.153/judis/chennai/index.php/casestatus/viewpdf/463106',\
'http://164.100.79.153/judis/chennai/index.php/casestatus/viewpdf/463107',\
'http://164.100.79.153/judis/chennai/index.php/casestatus/viewpdf/463108',\
'http://164.100.79.153/judis/chennai/index.php/casestatus/viewpdf/463109',\
'http://164.100.79.153/judis/chennai/index.php/casestatus/viewpdf/463110',\
'http://164.100.79.153/judis/chennai/index.php/casestatus/viewpdf/463111',\
'http://164.100.79.153/judis/chennai/index.php/casestatus/viewpdf/463112',\
'http://164.100.79.153/judis/chennai/index.php/casestatus/viewpdf/463113',\
'http://164.100.79.153/judis/chennai/index.php/casestatus/viewpdf/463114',\
'http://164.100.79.153/judis/chennai/index.php/casestatus/viewpdf/463115',\
'http://164.100.79.153/judis/chennai/index.php/casestatus/viewpdf/463116',\
'http://164.100.79.153/judis/chennai/index.php/casestatus/viewpdf/463117',\
'http://164.100.79.153/judis/chennai/index.php/casestatus/viewpdf/463118',\
'http://164.100.79.153/judis/chennai/index.php/casestatus/viewpdf/463119',\
'http://164.100.79.153/judis/chennai/index.php/casestatus/viewpdf/463120',\
'http://164.100.79.153/judis/chennai/index.php/casestatus/viewpdf/463121',\
'http://164.100.79.153/judis/chennai/index.php/casestatus/viewpdf/463122',\
'http://164.100.79.153/judis/chennai/index.php/casestatus/viewpdf/463123',\
'http://164.100.79.153/judis/chennai/index.php/casestatus/viewpdf/463124',\
'http://164.100.79.153/judis/chennai/index.php/casestatus/viewpdf/463125',\
'http://164.100.79.153/judis/chennai/index.php/casestatus/viewpdf/463126',\
'http://164.100.79.153/judis/chennai/index.php/casestatus/viewpdf/463127',\
'http://164.100.79.153/judis/chennai/index.php/casestatus/viewpdf/463128',\
'http://164.100.79.153/judis/chennai/index.php/casestatus/viewpdf/463129']

for i in urls:
    urllib.request.urlretrieve(i, 'C://Users//tanma.TANMAY-STATION//Desktop//GitHub//Summarizer//NER//'+str(urls.index(i))+'.pdf')