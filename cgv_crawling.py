#
# Author : soel <kshzg@naver.com>
#
# 필요 패키지
# pip install bs4  
# pip install lxml
#
from bs4 import BeautifulSoup
from selenium import webdriver
import cgv_crawling_handler
from cgv_crawling_handler import *

#각 크롬 드라이버 위치로 설정
# driver_path = '/usr/local/bin/chromedriver' #아이맥

driver_path = 'C:/Users/kshzg/_development/chromedriver' #델


# movies_url = 'http://section.cgv.co.kr/theater/popup/r_MovieTimeTable.aspx'
movies_url = 'http://www.cgv.co.kr/reserve/show-times/movies.aspx' #영화 목록
theaters_url = 'http://www.cgv.co.kr/reserve/show-times/' #영화관 목록


# headers = 'user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 12_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1'
# headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'}
headers = 'user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'

driver = init_driver(driver_path, headers)
movie_list_html = get_url_info(driver, movies_url)
# print('user-agent : ', driver.find_element_by_css_selector('#user-agent').text)
get_text(movie_list_html, '#movie_list > div.viewport > div > ul > li > a > strong')

# theater_list_html = get_url_info(driver, theaters_url)
# driver.find_element_by_xpath('//*[@id="contents"]/div[1]/div/ul/li[1]/a').click()

# 지역
# get_text(theater_list_html, '#contents > div.sect-common > div > div.sect-city > ul > li > a')

# get_text(theater_list_html, '#contents > div.sect-common > div > div.sect-city > ul > li.on > div > ul > li > a')




# User Agent check
# user_agent = driver.execute_script("return navigator.userAgent;")
# print(user_agent)
# lang = driver.execute_script("return navigator.languages;")
# print(lang)
# plugin_length = driver.execute_script("return navigator.plugins.length;")
# print(plugin_length)



driver.quit()