import requests
from bs4 import BeautifulSoup
import codecs
import warnings
import numpy as np 
import pandas as pd 
warnings.filterwarnings('ignore')

def download_page(url):
	header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0'}
	html = requests.get(url,headers=header).content
	return html

def parsel_lyrics(html,sun,num):
	soup = BeautifulSoup(html)
	song_list=soup.find_all('tr')[1:]
	for song in song_list:
		sun['歌名'].loc[num]=song.find_all('td')[0].getText()
		sun['专辑名'].loc[num]=song.find_all('td')[1].getText()
		sun['链接'].loc[num]='http://www.lrcgc.com/'+song.find_all('td')[0].find('a')['href']
		num += 1
	return sun,num

def main():
	url_list=[]
	num=0
	sun = pd.DataFrame(
			np.zeros((300,4)),
			columns = ['歌名','专辑名','链接','歌词']
			)
	for i in np.arange(1,27).astype('str'):	#1th place to change
		urli='http://www.lrcgc.com/songlist-174-'+i+'.html' #2th place to change
		url_list.append(urli)

	for url in url_list:
		html = download_page(url)
		sun ,num = parsel_lyrics(html,sun,num)

	sun.to_excel('lin_2.xlsx')	#3th place to change
	return sun

if __name__ == '__main__':
	main()


