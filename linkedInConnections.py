from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
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

actions = ActionChains(driver)
try:
    jobs = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "ember26"))
    )
    jobs.click()

    jobs = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "careers"))
    )

    job = jobs.find_element_by_class_name("job-card-square__title")
    job.click()

    # companiesList = []

    # listedJobs = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.CLASS_NAME, "jobs-search-results"))
    # )

    companiesList = []
    
    for i in range(7):
        listedJobs = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "jobs-search-results"))
        )
        element = driver.find_element_by_class_name("jobs-search-two-pane__pagination")
        driver.execute_script("arguments[0].scrollIntoView();",element)
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        companies = listedJobs.find_elements_by_class_name("job-card-container__company-name")

       
        print(companies[i].text)
        company = companies[i].text
        
        # if company not in companiesList:
        #     companiesList.append(company)
        #     print(companiesList)
        #     # alumni = listedJobs.find_element_by_class_name("job-flavors__logo-container")
        #     logo = listedJobs.find_elements_by_class_name("job-flavors__logo-image")
        #     logo_id = logo[i].get_attribute('id')
        #     print(logo_id)
        #     alumni = listedJobs.find_element_by_id(logo_id)
        #     actions.move_to_element(alumni)
        #     actions.click()
        #     actions.perform()

        #     results = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "search-results-container")))
        #     profile_names = results.find_elements_by_class_name("actor-name")
            
        #     employees = driver.current_url

        #     #Loop through the list of names so I can visit each person's profile 
        #     id_counter = 0
        #     for name in range(len(profile_names)):
        #         #wait for search results to show 
        #         results = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "search-results-container")))

        #         #create list of profiles for every iterations due to ids changing dynamically every time we return to the results page
        #         profile_id = results.find_elements_by_class_name("presence-entity--size-4")

        #         #grab the id of the next listed result
        #         ID = profile_id[id_counter].get_attribute('id')

        #         #find web element unique id 
        #         profile = results.find_element_by_id(ID)

        #         #increment id_counter to move to next result in list of profile_id
        #         id_counter += 1

        #         #create new action chain 
        #         profile_action = ActionChains(driver)
        #         driver.implicitly_wait(5)
        #         profile_action.move_to_element(profile)
        #         profile_action.click()
        #         profile_action.perform()
                
        #         time.sleep(5)
        #         driver.back()
            
        #         profile_name = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "actor-name")))

        #     #Move on to next companies in jobs that has not yet been visited and have UCI alumni
        #     driver.back()


finally:
    print("done")
    #driver.close()