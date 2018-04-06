"""This was written for automating logix website activity."""
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from conversion import NumConvert

"""This is for filling out your username and password on the credential page."""
def credentials():
    driver = webdriver.Firefox()
    driver.get("http://")   #Enter website here
    driver.implicitly_wait(8)
    enter_username = ActionChains(driver)
    enter_password = ActionChains(driver)
    click_login = ActionChains(driver)
    numconvert = NumConvert()
    username = ''   #Enter your username here
    conv_username = numconvert.convert(username)
    password = ''   #Enter password here
    conv_password = numconvert.convert(password)
    usernamebox = driver.find_element_by_css_selector('#username')
    passwordbox = driver.find_element_by_css_selector('#password')
    loginbox = driver.find_element_by_css_selector('#submit')
    enter_username.move_to_element(usernamebox) \
                  .click(usernamebox) \
                  .send_keys_to_element('#username', conv_username) \
                  .perform()
    enter_password.move_to_element(passwordbox) \
                  .click(passwordbox) \
                  .send_keys_to_element('#password', conv_password ) \
                  .perform()
    driver.implicitly_wait(3)
    click_login.click(loginbox).perform()
    driver.implicitly_wait(15)

"""Main funtion."""
def main():
    credentials()

main()
