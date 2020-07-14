from bs4 import BeautifulSoup
import requests as rq

url = "https://www.ptt.cc/bbs/SEX/index.html"
my_headers = {'cookie': 'over18=1;'}
# 用requests.get抓取url
response = rq.get(url, headers = my_headers)
content = response.text
# 指定lxml作為解析器
soup = BeautifulSoup(response.text, "lxml")
# 印出html
print(soup.prettify())
# 印出tag
print(soup.title)
print(soup.title.name)
print(soup.title.string)
print("--------")
# 印出title tag 的上一層tag
print(soup.title.parent.name)
print("--------")
# 找出第一個 a
print(soup.a)
print("--------")
# 找出所有 a
print(soup.find_all('a'))
print("--------")

"""
Tag
"""
print(type(soup.a))
print("--------")
# 抓標籤名 a
print(soup.a.name)
print("--------")
# 抓 a 的id名稱
print(soup.a['id'])
print("--------")
# 標籤中的內容
print(type(soup.a.string))
print("--------")

"""
爬樹（DOM）- 樹狀結構
"""
# 往下爬
print(soup.body.a.content)
print(list(soup.body.a.children))
print(soup.body.a.string)
print("--------")

# 往上爬
print(soup.title)
print(soup.title.parent)
print("--------")

# 往旁邊爬
first_a_tag = soup.body.a
next_to_first_a_tag = first_a_tag.next_sibling
print(first_a_tag)
print("--------")
print(next_to_first_a_tag)
print("--------")
print(next_to_first_a_tag.previous_sibling)
print("--------")

# 收尋
# 第一個a
print(soup.find("a"))
print("--------")
print(soup.find_all("a"))

