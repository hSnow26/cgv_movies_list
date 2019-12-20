#
# 2019-12-04
# Author : soel <kshzg@naver.com>
#
# 필요 패키지
# pip install requests
# pip install bs4  
# pip install lxml
#
import requests
from bs4 import BeautifulSoup

ticket_url = 'http://www.cgv.co.kr/reserve/show-times/movies.aspx'

headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
# HTTP GET Request
req = requests.get(ticket_url, headers = headers)
# HTML 소스 가져오기
movie_list_html = req.text

f = open("cgv_html.py", 'w')
f.write(movie_list_html)
f.close()
# print(req.text)

soup = BeautifulSoup(movie_list_html, 'lxml')


movie_list_contents = soup.select(
    # '#form1 > div.pop_th_wrap > div > div > div > div > div.th_preveiw_tab_popup > div.scroll > ul > li > a > span'
    '#movie_list > ul > li > a > strong'
    )

for content in movie_list_contents:
    print(content.text)



# driver.quit()