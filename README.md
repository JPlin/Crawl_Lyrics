# Crawl_Lyrics
利用Python 爬虫对歌手的所有歌曲的歌词进行爬取并进行可视化，制作成词云

目标 :抓取某个歌手（孙燕姿）的所有歌词，并进行分析，
参考教程 ：http://www.jianshu.com/p/bc1878af50fb

文件结构说明：

1.read_song_info.py
	:抓取歌手的信息，并将歌词的链接保存

2.read_lyrics.py
  :根据歌词的链接，抓取全部的歌词，并保存

3.clean_lyrics.py
	:进行进一步的数据清洗

4.analyze_lyrics.py
	:对歌词进行整理，分析歌词

操作步骤：

  first:
    execute read_song_info.py
    
  second:
    ETL the  producted Excel
    
  third:
    execute read_lyrics.py
    
  forth:
    execute clean_lyrics.py
    
  fifth:
    execute analyze_lyrics.py
    
  sixth:
    open the website:https://wordart.com/create ,and make the word cloud,then download the png file
