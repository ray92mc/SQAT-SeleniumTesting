import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class test_SwagLabsChrome(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:\\Users\\01\\desktop\\chromedriver_win32\\chromedriver.exe")

    def tearDown(self):
        self.driver.close()

    def test_login_fail(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com")
        
        usernameInput = driver.find_element_by_id("user-name")
        usernameInput.clear()
        usernameInput.send_keys("standard_user")
        
        passwordInput = driver.find_element_by_id("password")
        passwordInput.clear()
        passwordInput.send_keys("incorrect")

        loginBtn = driver.find_element_by_id("login-button")
        loginBtn.click()

        expected_error_message = "Epic sadface: Username and password do not match any user in this service"
        error_message = driver.find_element_by_xpath("//div[@id='login_button_container']/div/form/h3").text

        if expected_error_message != error_message:
            print("text not visible...")
        else:
            pass

        expected_title = "Swag Labs"
        actual_title = driver.title

        assert expected_title in actual_title

        expected_password_clue = "secret_sauce"
        password_clue = driver.find_element_by_xpath("//div[2]/div/div[2]").text

        if expected_password_clue not in password_clue:
            print("text not visible...")
        else:
            pass

    def test_login_success(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com")
        
        usernameInput = driver.find_element_by_id("user-name")
        usernameInput.clear()
        usernameInput.send_keys("standard_user")
        
        passwordInput = driver.find_element_by_id("password")
        passwordInput.clear()
        passwordInput.send_keys("secret_sauce")

        loginBtn = driver.find_element_by_id("login-button")
        loginBtn.click()

        expected_title = "Swag Labs"
        actual_title = driver.title

        assert expected_title in actual_title

        expected_label = "Products"
        label_text = driver.find_element_by_xpath("//div[@id='inventory_filter_container']/div").text

        if expected_label != label_text:
            print("text not visible...")
        else:
            pass

        expected_footer = "© 2020 Sauce Labs. All Rights Reserved. Terms of Service | Privacy Policy"
        footer_text = driver.find_element_by_xpath("//footer/div").text

        if expected_footer != footer_text:
            print("text not visible...")
        else:
            pass

    def test_remove_from_cart_success(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/inventory.html")

        addToCartBtn = driver.find_element_by_xpath("//div[@id='inventory_container']/div/div[3]/div[3]/button")
        addToCartBtn.click()

        expected_item_description_text = "Get your testing superhero on with the Sauce Labs bolt T-shirt."
        item_description_text = driver.find_element_by_xpath("//div[@id='inventory_container']/div/div[3]/div[2]/div").text

        if expected_item_description_text not in item_description_text:
            print("text not visible...")
        else:
            pass

        cart_link = driver.find_element_by_css_selector("path")
        cart_link.click()

        expected_item_description_text = "Get your testing superhero on with the Sauce Labs bolt T-shirt."
        item_description_text = driver.find_element_by_xpath("//div[@id='cart_contents_container']/div/div/div[3]/div[2]/div").text

        if expected_item_description_text not in item_description_text:
            print("text not visible...")
        else:
            pass

        cartRemoveBtn = driver.find_element_by_xpath("//div[@id='cart_contents_container']/div/div/div[3]/div[2]/div[2]/button")
        cartRemoveBtn.click()

        expected_title = "Swag Labs"
        actual_title = driver.title

        assert expected_title in actual_title


    def test_order_complete_success(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/inventory.html")

        addToCartBtn = driver.find_element_by_xpath("//div[@id='inventory_container']/div/div[3]/div[3]/button")
        addToCartBtn.click()

        cart_link = driver.find_element_by_css_selector("path")
        cart_link.click()

        expected_item_description_text = "QTY"
        item_description_text = driver.find_element_by_xpath("//div[@id='cart_contents_container']/div/div/div").text

        if expected_item_description_text not in item_description_text:
            print("text not visible...")
        else:
            pass

        checkoutBtn = driver.find_element_by_xpath("//a[contains(text(),'CHECKOUT')]")
        checkoutBtn.click()

        fnameInput = driver.find_element_by_id("first-name")
        fnameInput.clear()
        fnameInput.send_keys("FirstName")

        lnameInput = driver.find_element_by_id("last-name")
        lnameInput.clear()
        lnameInput.send_keys("LastName")

        zipInput = driver.find_element_by_id("postal-code")
        zipInput.clear()
        zipInput.send_keys("0000")

        continueBtn = driver.find_element_by_xpath("//input[@value='CONTINUE']")
        continueBtn.click()

        expected_title = "Swag Labs"
        actual_title = driver.title

        assert expected_title in actual_title

        finishBtn = driver.find_element_by_link_text("FINISH")
        finishBtn.click()

        expected_thankyou_text = "THANK YOU FOR YOUR ORDER"
        thank_you_text = driver.find_element_by_xpath("//h2").text

        if expected_thankyou_text not in thank_you_text:
            print("text not visible...")
        else:
            pass
    
    def test_sort_product_by_price_success(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/inventory.html")

        expected_label = "Products"
        label_text = driver.find_element_by_xpath("//div[@id='inventory_filter_container']/div").text

        if expected_label != label_text:
            print("text not visible...")
        else:
            pass

        product_sort_dropbox = driver.find_element_by_css_selector(".product_sort_container")
        product_sort_dropbox.click()

        low_to_high_drop_item = driver.find_element_by_css_selector(".inventory_item:nth-child(1) > .pricebar")
        low_to_high_drop_item.click()

        driver.implicitly_wait(10)

        expected_title = "Swag Labs"
        actual_title = driver.title

        assert expected_title in actual_title

        expected_footer = "© 2020 Sauce Labs. All Rights Reserved. Terms of Service | Privacy Policy"
        footer_text = driver.find_element_by_xpath("//footer/div").text

        if expected_footer != footer_text:
            print("text not visible...")
        else:
            pass

if __name__ == "__main__":
    unittest.main()