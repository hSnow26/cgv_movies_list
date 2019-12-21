# author : seol <kshzg26@gmail.com>
#
# TODO
# pip install requests
# pip install bs4  
# pip install lxml
#
import requests
from bs4 import BeautifulSoup
from const.CgvCrawlingConst import CgvCrawlingConst

movies_url = CgvCrawlingConst.MOVIE_URL

headers = {'User-Agent' : CgvCrawlingConst.USER_AGENT_WEB}
# HTTP GET Request
req = requests.get(movies_url, headers = headers)
# HTML 소스 가져오기
movie_list_html = req.text

soup = BeautifulSoup(movie_list_html, 'lxml')

movie_list_contents = soup.select(
    CgvCrawlingConst.MOVIE_LIST_SELECTOR_LXML
    )

for content in movie_list_contents:
    print(content.text)



# driver.quit()