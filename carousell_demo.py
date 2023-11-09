import time
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome()

url = 'https://www.carousell.com.hk'

input = 'nike air force 1'
try:
    driver.get(url)
except:
    print('url not found')
    exit

search_box = driver.find_element(By.TAG_NAME, 'input')
search_box.send_keys(input)

time.sleep(1)

send_button = driver.find_element(By.XPATH, '//button[text()="搜尋"]')
send_button.click()

time.sleep(5)

# result01 = driver.find_element(By.XPATH, '/html/body')

#result02 = driver.find_element(By.CLASS_NAME, 'D_I')

#print(f'result text : {result02.text}')

#result03_list= driver.find_elements(By.XPATH, '//div[@class="D_sG D_F"]') ~EN
#result03_list= driver.find_elements(By.XPATH, '//div[@class="D_uf D_zu"]') #~CN
#for result in result03_list:
#   print(result.text)
#   print('---------')

#print('done')
#print(f'total run of post: {len(result03_list)}')
#time.sleep(10)

#result04_list = driver.find_elements(By.XPATH, '//div[contains(@data-testid, "listing-card")]')
#for result in result04_list:
#    print(result.text)
#   print('---------')

#print(f'total run of post: {len(result04_list)}')
#time.sleep(10)

seller = []
date = []
title = []
price = []
product_page = []
img_src = []


result04_list = driver.find_elements(By.XPATH, '//div[contains(@data-testid, "listing-card")]')
for result in result04_list:
    
    
    print(result.text.split('\n'))
    a_tags_list = result.find_elements(By.TAG_NAME, 'a')
    
    img_tags_list = result.find_elements(By.TAG_NAME, 'img')
    
    # for img_tag in img_tags_list:
    #img_src = img_tag.get_attribute('src')
    #print(img_src)

    #for a_tag in a_tags_list:
    #    a_href = a_tag.get_attribute('href')
    #    print(a_href)

    # a_tags_list[0] #U
    a_tags_list[1].get_attribute('href') #P

    img_src.append(img_tags_list[0].get_attribute('src'))
    product_page.append(a_tags_list[1].get_attribute('href'))

    seller.append(result.text.split('\n')[0])
    date.append(result.text.split('\n')[1])
    title.append(result.text.split('\n')[2])
    price.append(result.text.split('\n')[3])

    print('---------')

print(f'total run of post: {len(result04_list)}')
import pandas as pd
df = pd.DataFrame({'seller':seller, 'Date':date, 'Title':title,
'Price':price, 'Product_page':product_page, 'Img_src':img_src})
print(df)


time.sleep(10)

#post_url= driver.find_elements(By.XPATH, '//div[@class=class="D_oF"]') 
#image_url = driver.find_elements(By.XPATH, '//div[@class="D_CS D_VC"]') 
#for result in image_url:
#   print(result.text)





target_num_result = 300
# Get all the result array at this result page and count the len
result04_list = driver.find_elements(By.XPATH, '//div[contains(@data-testid, "listing-card")]')
for result in result04_list:
    print(result)
num_of_result = len(result04_list) # start from 48?

safe_brake = 10 #optional
count = 0 #optional

while (num_of_result < target_num_result and count < safe_brake):
    show_more_results_button = driver.find_element(By.XPATH, '//button[text()="顯示更多結果"]')
    show_more_results_button.click()
    time.sleep(3)

    #get the latest product list again
    result04_list = driver.find_elements(By.XPATH, '//div[contains(@data-testid, "listing-card")]')
    for result in result04_list:
        print(result)
    num_of_result = len(result04_list)
    count += 1 #optional

print(result04_list)
print(num_of_result)

driver.close

#method 1
show_more_results_button = driver.find_element(By.XPATH, '//button[text()="顯示更多結果"]')

#method 2
result01 = driver.find_element(By.XPATH, '/html/body')
result01.text # this is str

if '顯示更多結果' in result01.text:
    #there is a button
    pass
else:
    # this is no button
    pass



#goal: get 300 results
#step 1 - count how many result we have

# step 2 - if result_we_have < target
#              we get more result-by pressing the show more result button

#step 3 -we stop when: we reach our target or there is no show more result button

#