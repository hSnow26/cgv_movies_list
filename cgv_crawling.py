#
# author : seol <kshzg26@gmail.com>
# crawling movie list
#
# TODO
# pip install bs4  
# pip install selenium
#
from bs4 import BeautifulSoup
from selenium import webdriver
from handler.cgv_crawling_handler import CgvCrawlingHandler
from const.CgvCrawlingConst import CgvCrawlingConst


driver_path = CgvCrawlingConst.DRIVER_PATH
movies_url = CgvCrawlingConst.MOVIE_URL
theaters_url = CgvCrawlingConst.THEATERS_URL
user_agent = 'user-agent='+CgvCrawlingConst.USER_AGENT_WEB

handler = CgvCrawlingHandler()

driver = handler.init_driver(driver_path, user_agent)
movie_list_html = handler.get_url_info(driver, movies_url)

handler.get_text(movie_list_html, CgvCrawlingConst.MOVIE_LIST_SELECTOR)

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