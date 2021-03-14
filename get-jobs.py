from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

def getElementBySelector(selector, expression, driver):
    try:
        element = driver.find_element(selector, expression)
    except NoSuchElementException:
        element = 'Not Found'
    
    return element

def getElementsBySelector(selector,expression, driver):
    try:
        elements = driver.find_elements(selector, expression)
    except NoSuchElementException:
        elements = 'Not Found'
    
    return elements

def getElementText(selector, expression, driver):
    text = ''
    element = getElementBySelector(selector, expression, driver)
    
    if element == 'Not Found':
        text = element
    else:
        text = element.text 
    
    return text

def getElementAttribute(attribute, selector, expression, driver):
    attribute_value = ''
    element = getElementBySelector(selector, expression, driver)
    
    if element == 'Not Found':
        attribute_value = element
    else:
        attribute_value = element.get_attribute(attribute)
    
    return attribute_value

driver = webdriver.Chrome()
driver.get("https://www.linkedin.com/jobs/search?keywords=Python&location=Brasil&trk=public_jobs_jobs-search-bar_search-submit&f_TP=1&redirect=false&position=1&pageNum=0")

search_results = getElementsBySelector(By.CLASS_NAME, 'result-card__full-card-link', driver)
jobs = []
for result in search_results:
    result.click()
    time.sleep(5)

    jobs.append(
        {
            'title': getElementText(By.CSS_SELECTOR, '.topcard__content-left h3 span:first-child', driver),
            'linkedin_link' : getElementAttribute('href', By.CSS_SELECTOR, '.topcard__content-left a:first-child', driver),
            'company': getElementText(By.CLASS_NAME, 'topcard__org-name-link', driver),
            'location': getElementText(By.CLASS_NAME, 'topcard__flavor--bullet', driver),
            'description' : getElementText(By.CSS_SELECTOR, 'section.description div.show-more-less-html__markup', driver),
        }

    )
    
driver.close()