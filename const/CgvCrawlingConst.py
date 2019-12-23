#
# author : seol <kshzg26@gmail.com>
# crawling const
#
class CgvCrawlingConst:
    DRIVER_PATH = '/srv/www/server/chromedriver' #server
    DRIVER_PATH_MAC = '/usr/local/bin/chromedriver' #아이맥
    DRIVER_PATH_DELL = 'C:/Users/kshzg/_development/chromedriver' #델

    MOVIE_URL = 'http://www.cgv.co.kr/reserve/show-times/movies.aspx' #영화 목록
    MOVIE_LIST_SELECTOR = '#movie_list > div.viewport > div > ul > li > a > strong' #webdriver parse
    MOVIE_LIST_SELECTOR_LXML = '#movie_list > ul > li > a > strong' #lxml parse
    
    THEATERS_URL = 'http://www.cgv.co.kr/reserve/show-times/' #영화관 목록

    USER_AGENT_WEB = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    USER_AGENT_MOBILE = 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1'
