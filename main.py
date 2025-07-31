import os
from selenium import webdriver

# webdriver - istifadəçi interfeysinin avtomatlaşdırılmasını veb brauzerlərdə
# həyata keçirmək üçün istifadə olunur

# ChromeDriver üçün PATH dəyişəninin təyin edin 
os.environ['PATH'] += r"D:/chromedriver-win64/chromedriver-win64"
driver = webdriver.Chrome() 