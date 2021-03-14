from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import pprint

def getElementBySelector(driver, selector, expression):
    try:
        element = driver.find_element(selector, expression)
    except NoSuchElementException:
        element = 'Not Found'
    
    return element

def getElementsBySelector(driver, selector, expression):
    try:
        elements = driver.find_elements(selector, expression)
    except NoSuchElementException:
        elements = 'Not Found'
    
    return elements

def getElementText(driver, selector, expression):
    text = ''
    element = getElementBySelector(driver, selector, expression)
    
    if element == 'Not Found':
        text = element
    else:
        text = element.text 
    
    return text

def getElementAttribute(driver, selector, expression, attribute):
    attribute_value = ''
    element = getElementBySelector(driver, selector, expression)
    
    if element == 'Not Found':
        attribute_value = element
    else:
        attribute_value = element.get_attribute(attribute)
    
    return attribute_value

driver = webdriver.Chrome()
driver.get("https://www.linkedin.com/jobs/search?keywords=Python&location=Brasil&trk=public_jobs_jobs-search-bar_search-submit&f_TP=1&redirect=false&position=1&pageNum=0")

results = getElementsBySelector(driver, By.CLASS_NAME, 'result-card__full-card-link')
jobs = []
for result in results:
    result.click()
    time.sleep(5)

    jobs.append(
        {
            'title': getElementText(driver, By.CSS_SELECTOR, '.topcard__content-left h3 span:first-child'),
            'linkedin_link' : getElementAttribute(driver, By.CSS_SELECTOR, '.topcard__content-left a:first-child', 'href'),
            'company': getElementText(driver, By.CLASS_NAME, 'topcard__org-name-link'),
            'location': getElementText(driver, By.CLASS_NAME, 'topcard__flavor--bullet'),
            'description' : getElementText(driver, By.CSS_SELECTOR, 'section.description div.show-more-less-html__markup'),
        }

    )
    pprint.pprint(jobs)
driver.close()