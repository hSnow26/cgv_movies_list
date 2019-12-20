from bs4 import BeautifulSoup
from selenium import webdriver

class CgvCrawlingHandler:
    def init_driver(self, driver_path, headers):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('window-size=1920x1080')
        options.add_argument("disable-gpu")
        options.add_argument("lang=ko_KR")
        options.add_argument(headers)

        self.driver = webdriver.Chrome(driver_path, options=options)
        return self.driver

    def get_url_info(self, driver, url):
        driver.get(url)
        driver.execute_script("Object.defineProperty(navigator, 'plugins', {get: function() {return[1, 2, 3, 4, 5];},});")

        # lanuages 속성을 업데이트해주기
        driver.execute_script("Object.defineProperty(navigator, 'languages', {get: function() {return ['ko-KR', 'ko']}})")

        #웹 자원 로드를 시간 기다림
        driver.implicitly_wait(3)

        html = driver.page_source

        return html

    def get_text(self, html, selector):
        soup = BeautifulSoup(html, 'lxml')
        contents = soup.select(
            # '#form1 > div.pop_th_wrap > div > div > div > div > div.th_preveiw_tab_popup > div.scroll > ul > li > a > span'
            selector
            )
        content_list = []
        for content in contents:
            content_list.append(content.text)
            print(content.text)

        return content_list