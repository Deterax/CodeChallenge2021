import time
import requests
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as LeCondition
from selenium.webdriver.support.wait import WebDriverWait


class Page(object):
    #selectors
    driver = webdriver.Chrome(executable_path="../Drivers/chromedriver.exe")
    header = "//header"
    DTwitter = "api.twitter.com"
    DFacebook = "www.facebook.com"
    disclaimer = "/html/body/div[1]/div/div"
    disclaimerLink = "/html/body/div[1]/div/div/a"
    footer = "/html/body/footer/div[2]/div[1]/p[1]"
    facebook = "/html/body/main/div[3]/article/div[2]/a[1]"
    twitter = "/html/body/main/div[3]/article/div[2]/a[2]"
    zipcode = "/html/body/main/div[3]/article/div[5]/div/form/div[2]/div/div/input"
    zipNumber = "33126"
    matchbutton = "/html/body/main/div[3]/article/div[5]/div/form/div[2]/button"
    latestNewsFirst = "/html/body/main/div[3]/aside/nav[2]/a[1]"
    latestNewsLast = "/html/body/main/div[3]/aside/nav[2]/a[last()]"
    urlArticle = "https://www.consumeraffairs.com/recalls/liberty-mountain-recalls-birdie-belay-devices-032921.html"
    footerText = "ConsumerAffairs is not a government agency. Companies displayed may pay us to be Authorized or when you click a link, call a number or fill a form on our site. Our content is intended to be used for general information purposes only. It is very important to do your own analysis before making any investment based on your own personal circumstances and consult with your own investment, financial, tax and legal advisers."

    # compares if an element is preset on the website
    def is_element_present(self, how, what):
        try:
            # find element, if it can find it returns true, if not returns false
            time.sleep(2)
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            print ("element not found")
            return False
        return True

    # Validate if the link of a given element is active and replies
    def link_works(self, what):
        try:
            # wait for loading to be completed
            WebDriverWait(self.driver, 3).until(LeCondition.presence_of_element_located((By.XPATH, what)))
            for a in self.driver.find_elements_by_xpath(what):
                print(a.get_attribute('href'))
                urlCheck = requests.head(a.get_attribute('href')).status_code
                if urlCheck == 200:
                    return True
                else:
                    return False
        except NoSuchElementException as e:
            return False

    # compares the text of an element to a base saved parameter
    def check_text(self, what):
        # searches footer text and verify if text matches what is currently being displayed
        bodyText = self.driver.find_elements_by_xpath(what)
        for a in bodyText:
            if self.footerText in a.text:
                return True
            else:
                return False

    # Writes an specific zipcode to the zipcode field
    def write_zipcode(self):
        element = self.driver.find_element_by_xpath(self.zipcode)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element.clear()
        element.send_keys(self.zipNumber)
        time.sleep(1)

    # compares if an element is clickable
    def is_clickable(self, what):
        return self.driver.find_element_by_xpath(what).is_enabled()

    # compares if during navigation we had a change of tab to a new URL
    # this is compared to the base url defined above
    def is_new_tab(self):
        if self.driver.current_url == self.urlArticle:
            return False
        else:
            return True
