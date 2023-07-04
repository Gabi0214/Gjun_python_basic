# 抓取PTT電影版的網頁原始碼(HTML)
import urllib.request as req
url="https://www.ptt.cc/bbs/movie/index.html"
with req.urlopen(url) as response:
    data=response.read().decode("utf-8")
print(data)
# 解析原始碼，取得每篇文章的標題