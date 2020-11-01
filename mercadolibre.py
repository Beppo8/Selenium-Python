class TestingMercadoLibre(unittes.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = "./chromedriver")
        driver = self.driver
        driver.get('https://www.mercadolibre.com')
        driver.maximize.window()

    def test_search_ps4(self):
        driver = self.driver

        country = driver.find_element_by_id('CO')
        country.click()

        search_field = driver.find_element_by_name('as_word')
        search_field.click()
        search_field.clear()
        search_field.send_keys('playstation 4')
        search_field.submit()

        location = driver.find_element_by_partial_link_text('Bogota D.C')
        location.click()
        sleep(3)

        condition = driver.find_element_by_partial_link_text('Nuevo')
        condition.click()
        sleep(3)

        order_menu = driver.find_element_by_class_name()
        order_menu.click()
        higher_price = driver.find_element_by_css_selector('#inner-main > aside > section.view-options > dl > div > div > div > div > ul > li.ui-list__item.ui-list__item--selected > span')
        higher_price.click()
        sleep(3)

        articles = []
        prices = []

        for i in range(5):
            article_name = driver.find_element_by_xpath(f'/html/body/main/div/div/section/ol/li[{i + 1}]/div/div/div[2]/div[1]/a/h2').text
            articles.append(article_name)
            article_price = driver.find_element_by_xpath(f'/html/body/main/div/div/section/ol/li[{i + 1}]/div/div/div[2]/div[2]/div/div/span[1]/span[2]').text
            prices.append(article_price)

        print(articles, prices)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()