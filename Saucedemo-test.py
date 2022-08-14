import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class Test_a_Login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_Login_Failed(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        time.sleep(3)
        driver.find_element(By.ID,"user-name").send_keys("khansa")
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys(12345678)
        time.sleep(1)
        driver.find_element(By.ID,"login-button").click()
        time.sleep(3)

        response_data = driver.find_element(By.CSS_SELECTOR,"#login_button_container > div > form > div.error-message-container.error > h3 > button").text
        self.assertIn(response_data, "Username and password do not match")
     
    def test_b_Login_Successful(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        time.sleep(3)
        driver.find_element(By.ID,"user-name").send_keys("standard_user")
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("secret_sauce")
        time.sleep(1)
        driver.find_element(By.ID,"login-button").click()
        time.sleep(3)
        
        self.assertEqual(driver.current_url, "https://www.saucedemo.com/inventory.html")
    
    def test_c_Login_EmptyUser(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        time.sleep(3)
        driver.find_element(By.ID,"user-name").send_keys("")
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("secret_sauce")
        time.sleep(1)
        driver.find_element(By.ID,"login-button").click()
        time.sleep(3)

        response_data = driver.find_element(By.CSS_SELECTOR,"#login_button_container > div > form > div.error-message-container.error > h3 > button").text
        self.assertIn(response_data,"Username is required")
    
    def test_d_Login_EmptyPass(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        time.sleep(3)
        driver.find_element(By.ID,"user-name").send_keys("standard_user")
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("")
        time.sleep(1)
        driver.find_element(By.ID,"login-button").click()
        time.sleep(3)

        response_data = driver.find_element(By.CSS_SELECTOR,"#login_button_container > div > form > div.error-message-container.error > h3 > button").text
        self.assertIn(response_data, "Password is required")

class Test_b_AddtoCart(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
    
    def test_a_AddtoCart(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        time.sleep(3)
        driver.find_element(By.ID,"user-name").send_keys("standard_user")
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("secret_sauce")
        time.sleep(1)
        driver.find_element(By.ID,"login-button").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"#add-to-cart-sauce-labs-backpack").click()
        time.sleep(1)

        response_data = driver.find_element(By.CLASS_NAME,"shopping_cart_badge").text
        self.assertEqual(response_data, "1")

    def tearDown(self): 
        self.driver.close() 

if __name__ == "__main__":
    unittest.main()

    
