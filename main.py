import os
from selenium import webdriver
from selenium.webdriver.common.by import By 

# webdriver - istifadəçi interfeysinin avtomatlaşdırılmasını veb brauzerlərdə
# həyata keçirmək üçün istifadə olunur

# ChromeDriver üçün PATH dəyişəninin təyin edin 
os.environ['PATH'] += r"D:/chromedriver-win64/chromedriver-win64"
with webdriver.Chrome() as driver:
    driver.get("https://www.tennis.com/players-rankings/")
    
    # Load More ddüyməsini səhifədə bütün məlumatlar görünənə qədər kliklə
    while True:
        try:
            driver.find_element(By.XPATH, "//button[contains(., 'LOAD MORE')]").click()
        except:
            break 
        
    # Professional Tennisçilər Birliyi üzrə individual idmançıların reyting sıralama 
    # siyahısını əldə et
    with open('atp_single_rankings.txt', 'w') as f:
        f.write("Rank|Last Name|First Name|Points|Change|Nationality\n")
        

