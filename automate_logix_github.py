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
	    time.sleep(2)
    driver.execute_script('document.getElementById("tab2").click();')
    time.sleep(2)

def cycle():
    """Cycle a list of offers."""
    print("List of actions:\n Postvalidate,\n Readytodeploy,\n Neither\n")
    action = input("What action do you want to take?(enter string):")
    offer_list = tuple(open("C:\\Users\\108128\\Desktop\\offerstoautomate.txt", "r"))
    for i in offer_list:
        offerid = numconvert.convert(i)
        enteroffer = ActionChains(driver)
        enteroffer.send_keys_to_element('#searchterms', offerid) \
                  .perform()
        driver.execute_script('document.getElementById("search").click();')
        time.sleep(2)
        driver.execute_script('toggleDropdown()')
        if action[0] == 'p' or action[0] == 'P':
            postvalidate()
        elif action[0] == 'r' or action[0] == 'R':
            readytodeploy()
        else:
            print("you choose to neither post validate nor ready to deploy...\n\nprogram exiting\n")
            time.sleep(2)
            exit()
        driver.execute_script('document.getElementById("tab2").click();')
        time.sleep(2)

def postvalidate():
    """Does post validation."""
    status = driver.find_element_by_css_selector('#generalbody > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(5) > td:nth-child(2) > span:nth-child(1)').text
    if status == 'Pre-validate':
        driver.execute_script('document.getElementById("postValidate").click();')
        time.sleep(2)
        return
    else:
        time.sleep(2)
    
def readytodeploy():
    """Does ready to Deploy."""
    postvalidate()
    driver.execute_script('document.getElementById("readyToDeploy").click();')
    time.sleep(2)

def main():
    """Main funtion."""
    credentials()
    cycle()

main()