import warnings
warnings.filterwarnings('ignore')
import numpy as np 
import pandas as pd 

import jieba

inf = pd.read_excel('lin_4.xlsx')	#10th place to change
text = ''.join(inf['歌词'])

segs = jieba.cut(text,True)

word_list = []
for seg in segs:
	if len(seg) > 1:
		word_list.append(seg)

word = pd.DataFrame({'word':word_list})
word.to_excel('lin_word.xlsx')	#11th place to change