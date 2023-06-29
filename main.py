import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
LinkedIn_url = "LinkedIn job list page"
LinkedIn_acc = "YOUR_LINKEDIN_ACCOUNT"
LinkedIn_pw = "YOUR_LINKEDIN_PASSWORD"
web_driver = "C:\Development\chromedriver.exe"
service = Service(web_driver)
connection = webdriver.Chrome(service=service, options=chrome_options)
connection.get(url=LinkedIn_url)
actions = ActionChains(connection)


login = connection.find_element(By.CLASS_NAME, "nav__button-secondary")
login.click()
username = connection.find_element(By.ID, "username")
username.send_keys(LinkedIn_acc)
password = connection.find_element(By.ID, "password")
password.send_keys(LinkedIn_pw)
sign_in = connection.find_element(By.CLASS_NAME, "login__form_action_container")
sign_in.click()
time.sleep(20)
page_list = connection.find_elements(By.CSS_SELECTOR, ".artdeco-pagination__pages li button")
for page_num in range(len(page_list)):
    page = connection.find_elements(By.CSS_SELECTOR, ".artdeco-pagination__pages li button")
    print(f"Page {page[page_num].text}")
    job_list = connection.find_elements(By.CSS_SELECTOR, ".scaffold-layout__list-container .scaffold-layout__list-item")
    job_id = [job.get_attribute('id') for job in job_list]
    print(job_id)
    for job in job_id:
        print(job)
        job = connection.find_element(By.ID, job)
        actions.move_to_element(job).perform()
        time.sleep(2)
        try:
            job.click()
            time.sleep(2)
            job_apply_btn = connection.find_element(By.CLASS_NAME, "jobs-apply-button--top-card")
            job_apply_btn.click()
            time.sleep(2)
            direct_application_check = connection.find_element(By.CLASS_NAME, "ui-attachment__download-button")
        except NoSuchElementException:
            print("Not direct apply")
            continue
        else:
            submit_application = connection.find_element(By.CSS_SELECTOR, ".justify-flex-end button")
            time.sleep(2)
            print(submit_application.text)
        finally:
            close_btn = connection.find_element(By.CSS_SELECTOR, ".jobs-easy-apply-modal button")
            close_btn.click()
            time.sleep(2)
            discard = connection.find_element(By.CSS_SELECTOR, ".artdeco-modal__actionbar .artdeco-button--secondary")
            discard.click()
            time.sleep(2)
    next_page = page_num + 1
    if page_num == 6:
        pass
    else:
        page[next_page].click()
    time.sleep(5)