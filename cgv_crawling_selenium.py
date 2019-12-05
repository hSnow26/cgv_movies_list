#
# Author : soel <kshzg@naver.com>
#
# 필요 패키지
# pip install requests
# pip install bs4  
# pip install lxml
#
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

dirver_path = '/usr/local/bin/chromedriver'
# movies_url = 'http://section.cgv.co.kr/theater/popup/r_MovieTimeTable.aspx'
movies_url = 'http://www.cgv.co.kr/reserve/show-times/movies.aspx'
# headers = 'user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 12_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1'
# headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'}
headers = 'user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
options.add_argument("lang=ko_KR")
options.add_argument(headers)

driver = webdriver.Chrome(dirver_path, options=options)

driver.get(movies_url) #영화 목록
driver.execute_script("Object.defineProperty(navigator, 'plugins', {get: function() {return[1, 2, 3, 4, 5];},});")

# lanuages 속성을 업데이트해주기
driver.execute_script("Object.defineProperty(navigator, 'languages', {get: function() {return ['ko-KR', 'ko']}})")

#웹 자원 로드를 시간 기다림
driver.implicitly_wait(3)

# print('user-agent : ', driver.find_element_by_css_selector('#user-agent').text)

movie_list_html = driver.page_source
# print(movie_list_html)

soup = BeautifulSoup(movie_list_html, 'lxml')


movie_list_contents = soup.select(
    # '#form1 > div.pop_th_wrap > div > div > div > div > div.th_preveiw_tab_popup > div.scroll > ul > li > a > span'
    '#movie_list > div.viewport > div > ul > li > a > strong'
    )
movie_list = []
for content in movie_list_contents:
    movie_list.append(content.text)
    print(content.text)

theaters_url = 'http://www.cgv.co.kr/reserve/show-times/movies.aspx'
driver.get(theaters_url) #영화관 목록
driver.execute_script("Object.defineProperty(navigator, 'plugins', {get: function() {return[1, 2, 3, 4, 5];},});")

# lanuages 속성을 업데이트해주기
driver.execute_script("Object.defineProperty(navigator, 'languages', {get: function() {return ['ko-KR', 'ko']}})")
# driver.find_element_by_xpath('//*[@id="contents"]/div[1]/div/ul/li[1]/a').click()


# def init_driver():

# def get_data_lists(url):
#     dd
    


# User Agent check
user_agent = driver.execute_script("return navigator.userAgent;")
print(user_agent)
lang = driver.execute_script("return navigator.languages;")
print(lang)
plugin_length = driver.execute_script("return navigator.plugins.length;")
print(plugin_length)



driver.quit()