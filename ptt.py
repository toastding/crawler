import requests as rq
from bs4 import BeautifulSoup

url = "https://www.ptt.cc/bbs/index.html"
r = rq.get(url)
web_content = r.text
# print(web_content)
sp = BeautifulSoup(web_content, 'html.parser')

"""
看板名稱
"""
boardNameElements = sp.find_all('div', class_="board-name")
# print(boardNameElements)
boardNames = list(e.text for e in boardNameElements) 
print(boardNames)
print("---------------------------------")

"""
看板人氣
"""
popularityElements = sp.find_all('div', class_='board-nuser')
popularities = list(int(p.text) for p in popularityElements)
print(popularities)

"""
利用 zip 模組將兩組list鍊結
"""
for pop, bn in zip(popularities, boardNames):
	print(pop, bn)

"""
將data輸出到sqlit
"""
import sqlite3


conn = sqlite3.connect("ptt.db")
c = conn.cursor()
sql = '''
	CREATE TABLE records(
	boardnames text,
	popularity int,
	timestamp datetime
	)
'''
# c.execute(sql)

import datetime
now_dt = datetime.datetime.now()

for bn, pop in zip(boardNames, popularities):
	c.execute('INSERT INTO records VALUES (?,?,?)', (bn, pop, now_dt))
conn.commit()
print(c.execute("select * from records;").fetchall())

conn.close()



