from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

PATH = "/Users/emmanuelreyes/Desktop/chromedriver"
driver = webdriver.Chrome(PATH)

email = os.environ.get('EMAIL')
pswd = os.environ.get('PSWD')

driver.get("https://www.linkedin.com")

#sign in
username = driver.find_element_by_id("session_key")
username.clear()
username.send_keys(email)

password = driver.find_element_by_id("session_password")
password.clear()
password.send_keys(pswd)
password.send_keys(Keys.RETURN)

try:
    jobs = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "ember26"))
    )
    jobs.click()

    jobs = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "careers"))
    )

    #print(jobs)

    job = jobs.find_element_by_class_name("job-card-square__title")
    job.click()

    listedJobs = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "jobs-search-results"))
    )

    companies = []

    companyList = listedJobs.find_elements_by_class_name("job-card-container__company-name")

    for company in companyList:
        print(company.text)
        if company.text not in companies:
            companies.append(company.text)
            title = listedJobs.find_element_by_class_name("job-card-list__title")
            title.click()
    print(companies)

    # job = jobs.find_elements_by_class_name("job-card-square__title")s

    # for title in job:
    #     print(title.text)


    # insight = jobs.find_elements_by_class_name("job-flavors__logo-container")
    # #print(school_tag)

    # for item in insight:
    #     img = item.find_element_by_tag_name("img")
    #     school = img.get_attribute("title")
    #     print(school)

    # alumni = jobs.find_elements_by_class_name("job-flavors__label")
    
    # print(alumni)

    # for item in alumni:
    #     print(item.text)



finally:
    print("done")
    #driver.close()