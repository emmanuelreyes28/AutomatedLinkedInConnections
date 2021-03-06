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
    time.sleep(0.5)

# actions = ActionChains(driver)
#ember26
try:
    # jobs = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.ID, "jobs-tab-icon"))
    # )
    jobs = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[7]/header/div[2]/nav/ul/li[3]/a"))
    )
    jobs.click()
    #/html/body/div[7]/header/div[2]/nav/ul/li[3]/a

    jobs = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "careers"))
    )

    job = jobs.find_element_by_class_name("job-card-square__title")
    job.click()
    
    listedJobs = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "jobs-search-results"))
    )

    companiesList = []
    listNum = 0
    page_number = 1
    pages = listedJobs.find_elements_by_class_name("artdeco-pagination__indicator--number")
    #print("Starting amount of pages =", len(pages))
    for page in range(len(pages)):
        #print("Current page:",page_number)
        page_number += 1
        total_elements = listedJobs.find_elements_by_class_name("occludable-update")
        #total_elements = listedJobs.find_elements_by_class_name("job-card-list__insight")
        #print(len(total_elements))
        pages = listedJobs.find_elements_by_class_name("artdeco-pagination__indicator--number")
        #print("Current index:", page)
        #print("This is the current page:",pages[page].text)

        #scroll to the bottom of the page on the left pane window
        num = 0
        i = 0 #move this on top of for loop above this one
        for item in range(len(total_elements)):
            print("Total elements:", len(total_elements))
            listedJobs = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "jobs-search-results"))
            )
            #total_elements holds the number of results per page which is 24 results for each page 
            total_elements = listedJobs.find_elements_by_class_name("occludable-update")
            #total_elements = listedJobs.find_elements_by_class_name("job-card-list__insight")
            scroll_element_into_view(total_elements[item])
            
            
            companies = listedJobs.find_elements_by_class_name("job-card-container__company-name")
            print("Length of companies:", len(companies))
            #scroll_element_into_view(companies[item])

            num += 1
            #print("Num:",num, companies[item].text)

            company = companies[item].text

            if company not in companiesList:
                companiesList.append(company)
                # scroll_element_into_view(companies[listNum])
                # listNum += 1
                # #scroll_element_into_view(total_elements[item])
                # logo = listedJobs.find_elements_by_class_name("job-flavors__logo-image")
                # #need to fix indexing here
                # print("Lenght of logos:", len(logo))
                # print("Item Number:", item)
                # logo_id = logo[i].get_attribute('id')
                # print("i =", i)
                # print("Logo:", logo[i].get_attribute('title'))
                # if i < len(logo):
                #     i += 1
              
                # #logo_id = logo[item].get_attribute('id')
                # alumni = listedJobs.find_element_by_id(logo_id)
                # actions = ActionChains(driver)
                # actions.move_to_element(alumni)
                # actions.click()
                # actions.perform()
                

                # results = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "search-results-container")))
                # #profile_names = results.find_elements_by_class_name("actor-name")
                # profile_names = results.find_elements_by_class_name("actor-name-with-distance")
                
                # employees = driver.current_url
                print(companiesList)
                

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
                #driver.back()
        print("List of companies:", companiesList)
            
        
        #print("Updated amount of pages =", len(pages))  

        '''
        Here we have to check the current index bc once we reach page 4 
        the index would grab page 5 instead due to the list of pages changing 
        dynamically.
        '''
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