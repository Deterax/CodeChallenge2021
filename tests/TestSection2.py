import time
import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from Pages.AnyPage import Page


class test_section2 (unittest.TestCase, Page):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="../Drivers/chromedriver.exe")
        self.driver.get(Page.urlArticle)

    def tearDown(self):
        self.driver.close()

    # finds disclaimer and check the link
    def test_disclaimer(self):
        # find the disclaimer.
        self.assertTrue(Page.is_element_present(self, By.XPATH, Page.disclaimer))
        # verify link is valid.
        self.assertTrue(Page.link_works(self, Page.disclaimerLink))

    # finds footer and check the text for match
    def test_footer(self):
        # find footer
        self.assertTrue(Page.is_element_present(self, By.XPATH, Page.footer))
        # check text
        self.assertTrue(Page.check_text(self, Page.footer))

    # finds social links and check the link is accessible
    def test_socialLink(self):
        # check social media links
        self.assertTrue(Page.is_element_present(self, By.XPATH, Page.facebook))
        self.assertTrue(Page.is_element_present(self, By.XPATH, Page.twitter))
        # test each one
        self.assertTrue(Page.link_works(self, Page.facebook))
        self.assertTrue(Page.link_works(self, Page.twitter))

    # finds "find my match section", tests the button
    def test_findMatch(self):
        # check for zipcode field exist
        self.assertTrue(Page.is_element_present(self, By.XPATH, Page.zipcode))
        self.assertTrue(Page.is_clickable(self, Page.matchbutton))
        # test button with no zipcode
        self.driver.find_element_by_xpath(Page.matchbutton).click()
        self.assertFalse(Page.is_new_tab(self))
        # write a valid zipcode
        self.write_zipcode()
        # test button with zipcode
        self.driver.find_element_by_xpath(Page.matchbutton).click()
        time.sleep(4)
        self.driver.switch_to_window(self.driver.window_handles[1])
        time.sleep(4)
        self.assertTrue(Page.is_new_tab(self))

    # on related news section, checks first element
    def test_firstEelem(self):
        # find first element on side
        self.assertTrue(Page.is_element_present(self, By.XPATH, Page.latestNewsFirst))
        # test the link
        self.assertTrue(Page.link_works(self, Page.latestNewsFirst))

    # on related news section, checks last element
    def test_lastElem(self):
        # find last element on side
        self.assertTrue(Page.is_element_present(self, By.XPATH, Page.latestNewsLast))
        # test the link
        self.assertTrue(Page.link_works(self, Page.latestNewsLast))


# this is the class to run
class MyTestSuite(unittest.TestCase):

    def test_suit_excecuter(self):
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(test_section2),
        ])
        runner1 = HtmlTestRunner.HTMLTestRunner(output="../Reports")
        runner1.run(smoke_test)



