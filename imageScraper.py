import os
import selenium
from selenium import webdriver
import time
from PIL import Image
import io
import requests
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import ElementClickInterceptedException

# #Specify Search URL 
# search_url = "https://www.google.com/search?q={q}&tbm=isch&tbs=sur%3Afc&hl=en&ved=0CAIQpwVqFwoTCKCa1c6s4-oCFQAAAAAdAAAAABAC&biw=1251&bih=568"

# driver.get(search_url.format(q='apple'))

# #Locate the images to be scraped from the current page 
# imgResults = driver.find_elements_by_xpath("//img[contains(@class,'Q4LuWd')]")
# totalResults=len(imgResults)
# print(totalResults)

# #Click on each Image to extract its corresponding link to download

# img_urls = set()
# for i in  range(0,len(imgResults)):
#     img=imgResults[i]
#     try:
#         img.click()
#         time.sleep(2)
#         actual_images = driver.find_elements_by_css_selector('img.n3VNCb')
#         for actual_image in actual_images:
#             if actual_image.get_attribute('src') and 'https' in actual_image.get_attribute('src'):
#                 img_urls.add(actual_image.get_attribute('src'))
#                 # print(actual_image.get_attribute('src'))
#     except ElementClickInterceptedException or ElementNotInteractableException as err:
#         print(err)

# print(img_urls)
# os.chdir('scrapedImages/')
# # baseDir=os.getcwd()
# # for i, url in enumerate(img_urls):
# #     file_name = f"{i:150}.jpg"    
# #     try:
# #         image_content = requests.get(url).content

# #     except Exception as e:
# #             print(f"ERROR - COULD NOT DOWNLOAD {url} - {e}")

# # try:
# #         image_file = io.BytesIO(image_content)
# #         image = Image.open(image_file).convert('RGB')
        
# #         file_path = os.path.join(baseDir, file_name)
        
# #         with open(file_path, 'wb') as f:
# #             image.save(f, "JPEG", quality=85)
# #         print(f"SAVED - {url} - AT: {file_path}")
# # except Exception as e:
# #     print(f"ERROR - COULD NOT SAVE {url} - {e}")

def scroll_to_end(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)#sleep_between_interactions

def getImageUrls(name,totalImgs):
    
    #Install driver
    opts=webdriver.ChromeOptions()
    opts.headless=True

    driver = webdriver.Chrome(ChromeDriverManager().install() ,options=opts)

    search_url = "https://www.google.com/search?q={q}&tbm=isch&tbs=sur%3Afc&hl=en&ved=0CAIQpwVqFwoTCKCa1c6s4-oCFQAAAAAdAAAAABAC&biw=1251&bih=568"
    driver.get(search_url.format(q=name))
    img_urls = set()
    img_count = 0
    results_start = 0  
    
    while(img_count<totalImgs): #Extract actual images now
        
        # scroll_to_end(driver)
        
        thumbnail_results = driver.find_elements_by_xpath("//img[contains(@class,'Q4LuWd')]")
        totalResults=len(thumbnail_results)
        print(f"Found: {totalResults} search results. Extracting links from{results_start}:{totalResults}")
        
        for img in thumbnail_results[results_start:totalResults]:
            try:
                img.click()
                time.sleep(2)
                actual_images = driver.find_elements_by_css_selector('img.n3VNCb')
                for actual_image in actual_images:
                    if actual_image.get_attribute('src') and 'https' in actual_image.get_attribute('src'):
                        img_urls.add(actual_image.get_attribute('src'))
                
                img_count=len(img_urls)
                
                if img_count >= totalImgs:
                    print(f"Found: {img_count} image links")
                    break
                else:
                    print("Found:", img_count, "looking for more image links ...")                
                    load_more_button = driver.find_element_by_css_selector(".mye4qd")
                    driver.execute_script("document.querySelector('.mye4qd').click();")
                    results_start = len(thumbnail_results)
            except ElementClickInterceptedException or ElementNotInteractableException as err:
                print(err)
    return img_urls

# print(getImageUrls("car", 50, driver))