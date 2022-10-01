import requests
from bs4 import BeautifulSoup as BS
r = requests.get('https://stopgame.ru/review/new/izumitelno/p1')
html = BS(r.content, 'html.parser')
for el in html.select(".items > .article-summary"):
    title = el.select('.caption > a')
    print(title[0].text)




















#card-video-ad-animations card-video-2-view__content-wrap



#class YoutubeScraper:
 #   def __init__(self, url):
  #      self.url = url
   # def scrape_video_count(self):
    #    content = requests.get(self.url)
     #   soup = BeautifulSoup(content.text, "html.parser")
      #  view_count = soup.find("div", {"class": "watch-view-count"}).text
       # return view_count
#url = "https://dzen.ru/video/watch/632b1e19c5543a6d1fe60e8f?t=60"
#x = YoutubeScraper(url)
#x.scrape_video_count()