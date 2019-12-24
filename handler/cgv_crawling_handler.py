#
# author : seol <kshzg26@gmail.com>
# crawling movie list
# handling webdriver
#
# TODO
# pip install bs4  
# pip install selenium


from bs4 import BeautifulSoup
from selenium import webdriver

class CgvCrawlingHandler:
    def init_driver(self, driver_path, user_agent):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('window-size=1920x1080')
        options.add_argument("disable-gpu")
        options.add_argument("lang=ko_KR")
        options.add_argument(user_agent)

        self.driver = webdriver.Chrome(driver_path, options=options)

        return self.driver

    def get_html(self, url):
        self.driver.get(url)
        self.driver.execute_script("Object.defineProperty(navigator, 'plugins', {get: function() {return[1, 2, 3, 4, 5];},});")

        # lanuages 속성을 업데이트해주기
        self.driver.execute_script("Object.defineProperty(navigator, 'languages', {get: function() {return ['ko-KR', 'ko']}})")

        #웹 자원 로드를 시간 기다림
        self.driver.implicitly_wait(3)

        self.html = self.driver.page_source

        return self.html

    def get_movie_list(self, selector):
        soup = BeautifulSoup(self.html, 'lxml')
        contents = soup.select(
            selector
            )
        content_list = []
        for content in contents:
            content_list.append(content.text)
            print(content.text)

        self.driver.quit()

        return content_list