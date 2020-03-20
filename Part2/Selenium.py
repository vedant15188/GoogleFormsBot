import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import csv

csv_file = open("./data.csv", "r")

driver = webdriver.Firefox()

reader = csv.reader(csv_file)

j = 0
for i in reader:
    driver.get("https://forms.gle/6w2rXDyoCYvFNGHv5")

    web = driver.find_element_by_tag_name("html")
    fields = driver.find_elements_by_tag_name("input")

    if(j == 0):
        j += 1
        continue
    else:
        j += 1
        arr = i
        x = 0
        print(arr)
        for i in fields:
            if(i.get_attribute("type") == "hidden"):
                continue
            else:
                i.send_keys(arr[x])
            x += 1

        submit = driver.find_element_by_xpath(
            "//*[@class='appsMaterialWizButtonPaperbuttonLabel quantumWizButtonPaperbuttonLabel exportLabel']")
        submit.click()

driver.close()
