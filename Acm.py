import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import sys
import csv
#options
STRINGS_FOR_TEST = "Sherif Sakr"
DBLP_BASE_URL = 'https://dl.acm.org/'
PUB_SEARCH_URL = DBLP_BASE_URL + "results.cfm?within=owners.owner%3DGUIDE&srt=_score&query=persons.authors.personName:"
# ?within=owners.owner%3DGUIDE&srt=_score&query=persons.authors.personName:

def query_Acm(authorName=STRINGS_FOR_TEST):
    driver = webdriver.Chrome()
    driver.get(PUB_SEARCH_URL+""+authorName)
    #html = driver.page_source
    link = driver.find_element_by_link_text(authorName)
    link.click()

    affHistElems=driver.find_elements_by_xpath("/html/body/div[2]/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr/td/div/a")
    affHist=[]
    for aff in affHistElems:
        affHist.append(aff.text)
    return affHist    
    #return BeautifulSoup(html,"lxml")


def main():
    affs=query_Acm("Robert Isele")
    print affs
    
if __name__ == '__main__':
        main()