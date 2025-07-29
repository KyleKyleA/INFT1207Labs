"""
Name: Mathuran Chandramohan, Kyles Angeles
Course: INFT 1207
Date: July 25th, 2025
Description: Set of test cases for this link https://magento.softwaretestingboard.com/
"""

#region IMPORTS
import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
#endregion IMPORTS

#region TEST SUITE
class TestFinalRecording(unittest.TestCase):
    # ********** CLASS METHODS ********** #
    @classmethod
    def setUpClass(cls):
        """Class setup - runs before all tests"""
        cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        """Class teardown - runs after all tests"""
        cls.driver.quit()

    # ********** TEST CASES ********** #
    def test_selectArticleOfClothing(self):
        """Test navigation to 'Women's Hoodie and Sweatshirts' page"""
        # open website
        self.driver.get("https://magento.softwaretestingboard.com/")
        sleep(1)

        # hover on 'Women'
        element = self.driver.find_element(By.LINK_TEXT, "Women")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        sleep(1)

        # hover on 'Tops'
        element = self.driver.find_element(By.LINK_TEXT, "Tops")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        sleep(1)

        # click on 'Hoodies & Sweatshirts'
        element = self.driver.find_element(By.LINK_TEXT, "Hoodies & Sweatshirts")
        element.click()
        sleep(1)

    def test_customizeArticleOfClothing(self):
        """Test and assert customization and selection of an article of clothing"""
        # open website
        self.driver.get("https://magento.softwaretestingboard.com/women/tops-women/hoodies-and-sweatshirts-women.html")
        sleep(1)

        # click on 'Style' and select 'Full Zip'
        self.driver.find_element(By.XPATH, "//div[normalize-space()='Style']").click()
        sleep(1)
        self.driver.find_element(By.XPATH, "//div[@id='narrow-by-list']//div[1]//div[2]//ol[1]//li[1]//a[1]").click()
        sleep(1)

        # return to default content when ad pops up
        if "#google_vignette" in self.driver.current_url:
            self.driver.get("https://magento.softwaretestingboard.com/women/tops-women/hoodies-and-sweatshirts-women.html?style_general=128")

        # click on 'Color' and select 'Gray'
        self.driver.find_element(By.XPATH, "//div[normalize-space()='Color']").click()
        sleep(1)
        self.driver.find_element(By.XPATH, "//a[@aria-label='Gray']//div[contains(@class,'swatch-option color')]").click()
        sleep(1)

        # click on 'Size' and select 'M'
        self.driver.find_element(By.XPATH, "//div[normalize-space()='Size']").click()
        sleep(1)
        self.driver.find_element(By.XPATH, "//a[@aria-label='M']//div[contains(@class,'swatch-option text')][normalize-space()='M']").click()
        sleep(1)

        # hover on 'Circe Hooded Ice Fleece'
        element = self.driver.find_element(By.XPATH, "//img[@alt='Circe Hooded Ice Fleece-M-Gray']")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        sleep(1)

        # click 'Add to Cart'
        self.driver.find_element(By.XPATH, '// *[ @ id = "maincontent"] / div[3] / div[1] / div[3] / ol / li[1] / div / div / div[3] / div / div[1] / form / button').click()
        sleep(5)

        # click on shopping cart icon
        self.driver.find_element(By.XPATH, "//a[@class='action showcart']").click()
        sleep(1)

        # click on 'Proceed to Checkout' button
        self.driver.find_element(By.XPATH, "//button[@id='top-cart-btn-checkout']").click()
        sleep(1)

        # collapse order summary
        self.driver.find_element(By.XPATH, "//div[@class='title']").click()
        sleep(1)

        # assert successful order
        target = self.driver.find_element(By.CLASS_NAME, "product-item-name")
        self.assertEqual("Circe Hooded Ice Fleece", target.text)
#endregion TEST SUITE
