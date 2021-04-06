import unittest
import HtmlTestRunner
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from Pages.AnyPage import Page


class test_section1 (unittest.TestCase, Page):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="../Drivers/chromedriver.exe")

    def tearDown(self):
        self.driver.close()

    def test_display(self):
        # opens new website
        # validates header
        # get all links(lvl1)
        # validate the links
        # for each link
        # access link
        # validates header
        # get all links(lvl2)
        # validate the links
        # for each link
        # subtest() on each link
        # access link
        # validates header
        # get all links(lvl3)
        # validate the links
        pass


class MyTestSuite(unittest.TestCase):

    def test_suit_excecuter(self):
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(test_section1),
        ])
        runner1 = HtmlTestRunner.HTMLTestRunner(output="../Reports")
        runner1.run(smoke_test)


