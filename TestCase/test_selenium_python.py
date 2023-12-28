# -*- coding:utf-8 -*-
class GooglePage:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def search_for(self, keyword):
        self.driver.get("https://www.google.com")
        search_box = self.driver.find_element_by_name("")
        search_box.send_keys(keyword)
        search_box.submit()

    def close(self):
        self.driver.quit()

class GoogleController:
    def __init__(self):
        self.model = GooglePage()

    def search_and_close(self, keyword):
        self.model.search_for(keyword)
        # Add any additional logic if needed
        self.model.close()

def test_google_search():
    controller = GoogleController()
    controller.search_and_close("nicktest")

if __name__ == "__main__":
    test_google_search()