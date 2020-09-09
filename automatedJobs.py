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

def scroll_element_into_view(element):
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    time.sleep(1)

try:
    jobs = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[7]/header/div[2]/nav/ul/li[3]/a"))
    )
    jobs.click()

    jobs = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "careers"))
    )

    job = jobs.find_element_by_class_name("job-card-square__title")
    job.click()
    
    listedJobs = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "jobs-search-results"))
    )

    jobsList = []

    pages = listedJobs.find_elements_by_class_name("artdeco-pagination__indicator--number")

    for page in range(len(pages)):
        total_elements = listedJobs.find_elements_by_class_name("occludable-update")      

        #scroll to the bottom of the page on the left pane window
        for item in range(len(total_elements)):
            print("Total elements:", len(total_elements))
            listedJobs = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "jobs-search-results"))
            )
            #total_elements holds the number of results per page which is 24 results for each page 
            total_elements = listedJobs.find_elements_by_class_name("occludable-update")
            
            scroll_element_into_view(total_elements[item])

            titlePath = '/html/body/div[7]/div[3]/div[3]/div/div/div/div[1]/section/div/ul/li[' + str(item + 1) + ']/div/div/div[1]/div[2]/div[1]/a'
            title = listedJobs.find_element_by_xpath(titlePath)

            logo = listedJobs.find_elements_by_class_name("job-flavors__logo-image")
            print("Lenght of logos:", len(logo))
            
            jobTitle = title.text

            if jobTitle not in jobsList:
                jobsList.append(jobTitle)

                logo_path = '/html/body/div[7]/div[3]/div[3]/div/div/div/div[1]/section/div/ul/li[' + str(item + 1) + ']/div/div/div[2]/div/div/a'
                try:
                    l = listedJobs.find_element_by_xpath(logo_path)
                    actions = ActionChains(driver)
                    actions.move_to_element(l)
                    actions.click()
                    actions.perform()
                    results = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "search-results-container")))
                    profile_names = results.find_elements_by_class_name("actor-name-with-distance")
                    driver.back()
                except:
                    pass
                

                # results = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "search-results-container")))
                # profile_names = results.find_elements_by_class_name("actor-name-with-distance")
                
                # employees = driver.current_url
                #print(jobsList)
                

                #Loop through the list of names so I can visit each person's profile 
                # id_counter = 0
                # for name in range(len(profile_names)):
                #     #wait for search results to show 
                #     results = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "search-results-container")))

                #     #create list of profiles for every iterations due to ids changing dynamically every time we return to the results page
                #     #profile_id = results.find_elements_by_class_name("presence-entity--size-4")
                #     profile_id = results.find_elements_by_class_name("ivm-view-attr__img-wrapper--use-img-tag")
                #     print("Num of profile ids:", len(profile_id))
                #     #grab the id of the next listed result
                #     ID = profile_id[id_counter].get_attribute('id')

                #     #find web element unique id 
                #     profile = results.find_element_by_id(ID)

                #     #increment id_counter to move to next result in list of profile_id
                #     id_counter += 1

                #     #create new action chain 
                #     profile_action = ActionChains(driver)
                #     driver.implicitly_wait(5)
                #     profile_action.move_to_element(profile)
                #     profile_action.click()
                #     profile_action.perform()
                    
                #     time.sleep(5)
                #     driver.back()
                
                    #profile_name = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "actor-name")))

                #Move on to next companies in jobs that has not yet been visited and have UCI alumni
                # driver.back()
        print("List of companies:", jobsList)
            
        
        '''
        Here we have to check the current index bc once we reach page 4 
        the index would grab page 5 instead due to the list of pages changing 
        dynamically.
        '''
        listedJobs = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "jobs-search-results"))
        )
        pages = listedJobs.find_elements_by_class_name("artdeco-pagination__indicator--number")
        actions = ActionChains(driver)
        if page <= 2:
            next_page = pages[page + 1]
            actions.move_to_element(next_page)
            actions.click()
            actions.perform()
        else:
            next_page = pages[page - 1]
            actions.move_to_element(next_page)
            actions.click()
            actions.perform()
        nextPageToLoad = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "jobs-search-results__list")) 
        )
finally:
    print("done")
    #driver.close()