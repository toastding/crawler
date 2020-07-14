from bs4 import BeautifulSoup
import requests as rq
import numpy as np
import pandas as pd

url = "https://www.ptt.cc/bbs/Lifeismoney/index.html"
response = rq.get(url)
content = response.text
soup = BeautifulSoup(response.text, "lxml")

author_ids = []
title = []
date = []
recommends = []
posts = soup.find_all("div", class_ = "r-ent")
for post in posts:
	try:
	    author_ids.append(post.find("div", class_ = "author").string)
	except:
		author_ids.append(np.nan)
	try:
	    title.append(post.find("a").string)
	except:
		title.append(np.nan)
	try:
	    date.append(post.find("div", class_ = "date").string)
	except:
	  	date.append(np.nan)
	  	
recommendations = soup.find_all("div", class_ = "nrec")
for recommendation in recommendations:
	try:
           recommends.append(int(recommendation.find("span").string))
	except:
		recommends.append(np.nan)
print(author_ids)
print(title)
print(date)
print(recommends)

ptt_dict = {
	"author": author_ids,
	"recommends": recommends,
	"title": title,
	"date": date

}

ptt_df = pd.DataFrame(ptt_dict)
print(ptt_df)

