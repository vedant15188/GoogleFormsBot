import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import csv

csv_file = open("Part2/data.csv", "r")
driver = webdriver.Remote(command_executor='http://13.235.128.207:32184/wd/hub',
                          desired_capabilities=DesiredCapabilities.FIREFOX)
# driver = webdriver.Firefox()

reader = csv.reader(csv_file)

j = 0

for i in reader:
    try:
        driver.get(
            "https://docs.google.com/forms/d/e/1FAIpQLSeuvAsM_f2PTnqJZ9ad_zAUYIXlKbsvFoVNtTnbky7txvJWzQ/viewform?usp=sf_link")
        web = driver.find_element_by_tag_name("html")
        fields = driver.find_elements_by_tag_name("input")
        submit = driver.find_elements_by_tag_name("span")
    except:
        print("element find error")
        driver.quit()
        break
    print(web)
    print(submit)
    for span in submit:
        if(span.get_attribute("class") == "appsMaterialWizButtonPaperbuttonLabel quantumWizButtonPaperbuttonLabel exportLabel"):
            submit = span
    print(submit)
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

        try:
            submit.click()
        except:
            print("Submit error")
            # print()
            driver.quit()
            break

driver.close()
