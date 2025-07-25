"""
Name:
Course:
Date: July 25th, 2025
Description: Set of test cases for this link https://magento.softwaretestingboard.com/
"""

#regionImports
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#EndRegion Imports


#Region TEST SUITE
class TestDefaultSuite(object):
    def setup_method(self, method):
        """Class Setup - runs before all tests"""
        self.driver = webdriver.Edge()
        self.vars = {}

    def teardown_method(self, method):
        """Class TearDown - runs after all test"""
        self.driver.quit()



#EndRegion TEST SUITE