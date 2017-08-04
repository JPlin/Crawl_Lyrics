#对歌词进行清洗
__author__ = 'jplin'

import numpy as np 
import pandas as pd 

import re

information = pd.read_excel('lin_3.xlsx')	#7th place to change
lys = information['歌词']
lyric_after = []
for ly in lys:
	pat = re.compile(r'\作曲.*?.*?\[')
	ly = pat.sub('',ly)
	pat = re.compile(r'\作词.*?.*?\[')
	ly = pat.sub('',ly)
	pat = re.compile(r'林忆莲')	#8th place to change
	ly = pat.sub('',ly)
	pat = re.compile(r'\制作.*?.*?\[')
	ly = pat.sub('',ly)
	pat = re.compile(r'\歌词.*?.*?\[')
	ly = pat.sub('',ly)
	pat = re.compile(r'[^\u4e00-\u9fa5]')
	ly = pat.sub('',ly)
	print(ly)
	lyric_after.append(ly)

information['歌词']=lyric_after
i =0
for ly in information['歌词']:
	if len(ly) < 30:
		information = information.drop(i,axis=0)
	i+=1

information.to_excel('lin_4.xlsx')	#9th place to change