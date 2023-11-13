from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#Код полностью набран по примеру из youtube, вроде разобрался,
# но запустить и проверить не смог, не смог разобраться с разными версиями webdriver
class YandexAuthorization:

    def __init__(self):
        self.browser = webdriver.Chrome() #executable_path ='chromedriver.exe'

    def login(self, email, password):
        self.browser.get('https://passport.yandex.ru.auth'
                         '?origin=home_desktop_ru'
                         '&retpath=https%3A%2F%2Fmail.yandex.ru%2F'
                         '&backpath=https%3A%2F%2Fyandex.ru')
        self.browser.find_element_by_xpath('//input[@data-t="field:input-login"]')\
            .send_keys(email)
        self.browser.find_element_by_xpath('//button[@data-t="button:action"]') \
            .click()
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@data-t="field:input-passwd"]')))
        self.browser.find_element_by_xpath('//input[@data-t="field:input-passwd"]') \
            .send_keys(password)
        self.browser.find_element_by_xpath('//button[@data-t="button:action"]') \
            .click()


if __name__ == '__main__':
    yandex = YandexAuthorization()
    yandex.login('', '')