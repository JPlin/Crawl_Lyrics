#根据网址对歌词进行爬取
__author__ = 'jplin'

import requests
from bs4 import BeautifulSoup
import numpy as np 
import pandas as pd

import warnings
warnings.filterwarnings('ignore')

def download_page(url):
	print(url)
	header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/2010.0.0 Firefox/54.0'}
	html = requests.get(url,headers = header).content
	return html

def parsel_ly(html,lyrics_list):
	soup = BeautifulSoup(html)
	lyrics =  soup.find('p',{'class':'f14'}).getText()
	lyrics_list.append(lyrics)
	return lyrics_list

def main():
	lyrics_list=[]
	information = pd.read_excel('lin_2.xlsx')	#4th place to change
	for url in information['链接']:
		HTML = download_page(url)
		lyrics_list = parsel_ly(HTML,lyrics_list)


	information = pd.read_excel('lin_2.xlsx',sheetname=0)	#5th place to change
	information['歌词']=lyrics_list
	information.to_excel('lin_3.xlsx')	#6th place to change

if __name__ == '__main__':
	data = main()