#!/usr/bin/python3

from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get("https://www.nike.com/in/launch?s=in-stock")

login_btn = driver.find_element_by_css_selector("button.join-log-in.text-color-grey.prl3-sm.pt2-sm.pb2-sm.fs12-sm.d-sm-b")
login_btn.click()

# Login In.
email = WebDriverWait(driver, 10).until(
    expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "input[data-componentname='emailAddress']"))
)
email.send_keys("your-email-address")
password = WebDriverWait(driver, 10).until(
    expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "input[data-componentname='password']"))
)
password.send_keys("your-password")
login_btn = WebDriverWait(driver, 10).until(
    expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "div.nike-unite-submit-button.loginSubmit.nike-unite-component input[type='button']"))
)
login_btn.click()

login_dialog = WebDriverWait(driver, 10).until(
    expected_conditions.invisibility_of_element_located((By.CSS_SELECTOR, "div[class='d-md-tc u-full-width u-full-height va-sm-m']"))
)
product = WebDriverWait(driver, 10).until(
    expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/in/launch/t/lebron-7-mvp']"))
)
product.click()
sizes_btn = driver.find_elements_by_css_selector("button[data-qa='size-dropdown']")
for btn in sizes_btn:
    if btn.text == "US 11":
        btn.click()

add_to_cart = WebDriverWait(driver, 10).until(
    expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "button[data-qa='add-to-cart']"))
)
add_to_cart.click()

go_to_cart = driver.find_element_by_css_selector("a[href='https://www.nike.com/in/en/cart']")
go_to_cart.click()

# Clicking on the Member Checkout Button.
member_checkout_btn = WebDriverWait(driver, 10).until(
    expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "button[data-automation='checkout-button']"))
)
# if member_checkout_btn.get_attribute("disabled") != None:
#     member_checkout_btn.click()
# print("[BOT]: The 'Member Checkout' button is either loading or the cart is empty.")
msg_printed = False
while member_checkout_btn.get_attribute("disabled") != None:
    if msg_printed == False:
        print("[BOT]: The 'Member Checkout' button is either loading.", end='')
        msg_printed = True
    print(".", end='')
    time.sleep(0.01)
print()
member_checkout_btn.click()
