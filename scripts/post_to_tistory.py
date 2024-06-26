from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
import os

kakao_id = os.getenv('KAKAO_ID')
kakao_password = os.getenv('KAKAO_PASSWORD')

def kakao_login(driver, email, password):
    driver.get('https://accounts.kakao.com/login?continue=https://www.tistory.com/auth/login')
    
    # 이메일 입력
    email_input = driver.find_element(By.ID, 'loginId--1')
    email_input.send_keys(email)
    time.sleep(3)
    
    # 비밀번호 입력
    password_input = driver.find_element(By.ID, 'password--2')
    password_input.send_keys(password)
    time.sleep(2)
    password_input.send_keys(Keys.ENTER)
    time.sleep(2)
      # 로그인 완료 대기

def post_to_tistory(title, content, email, password):
    driver = webdriver.Chrome()
    
    # 카카오 로그인
    kakao_login(driver, email, password)

    # 티스토리로 이동하여 글 작성
    driver.get('')
    time.sleep(2)  # 페이지 로드 대기

    # 글 작성 자동화
    driver.find_element(By.ID, 'post-title-inp').send_keys(title)
    driver.switch_to.frame(driver.find_element(By.ID, 'editor'))
    driver.find_element(By.ID, 'tinymce').send_keys(content)
    driver.switch_to.default_content()
    driver.find_element(By.XPATH, '//button[text()="완료"]').click()

    driver.quit()

if __name__ == "__main__":
    sample_title = "오늘의 핫토픽: test"
    sample_content = "This is an test"
    kakao_email = kakao_id
    kakao_password = kakao_password
    print(kakao_email,kakao_password)
    post_to_tistory(sample_title, sample_content, kakao_email, kakao_password)