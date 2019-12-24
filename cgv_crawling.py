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

handler.init_driver(driver_path, user_agent)

handler.get_html(movies_url)

handler.get_movie_list(CgvCrawlingConst.MOVIE_LIST_SELECTOR)