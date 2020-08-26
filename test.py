from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "/Users/emmanuelreyes/Desktop/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://store.steampowered.com/")
#print(driver.title)

search = driver.find_element_by_id("store_nav_search_term")
search.clear()
search.send_keys("fall guys")
search.send_keys(Keys.RETURN)

try:
    results = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "search_resultsRows"))
    )
    #print(results.text)

    link = results.find_element_by_tag_name("a")
    link.click()

    results = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "game_area_description"))
    )
    
    discord = results.find_element_by_tag_name("a")
    discord.click()



    # titles = results.find_elements_by_tag_name("a")
    # #print(titles)
    # for title in titles:
    #     t = title.find_element_by_class_name("title")
    #     print(t.text)

finally:
    driver.close()

#time.sleep(5)


#closes google chrome tab 
#driver.close()

#driver.quit() - closes google chrome window