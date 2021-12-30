from selenium import webdriver
from bs4 import BeautifulSoup 
import time

#키워드 입력
query_text = input("키워드를 입력하세요 : ")

#chromedriver 경로 설정
chrome_path = 'C:\\tmp\\chromedriver.exe'
driver = webdriver.Chrome(chrome_path)

#url 설정 후 driver.get()에 대입
url = 'https:\\www.naver.com'
driver.get(url)
time.sleep(2)

#검색창에 키워드 넣고 엔터
element = driver.find_element_by_id("query")
driver.find_element_by_id("query").click()
element.send_keys(query_text)
element.send_keys("\n")

#뉴스 검색창 선택
driver.find_element_by_link_text("뉴스").click()

#기사 추출
html_1 = driver.page_source
soup_1 = BeautifulSoup(html_1, 'html.parser')

content_1 = soup_1.find('div','group_news').find_all('li')

with open("C:\\tmp\\test2.txt","w") as f:
    for i in content_1:
        f.write(i.get_text())
        f.write("\n")
    