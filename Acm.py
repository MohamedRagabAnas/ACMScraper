import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import sys
import csv
#options
DBLP_BASE_URL = 'https://dl.acm.org/'
PUB_SEARCH_URL = DBLP_BASE_URL + "results.cfm?within=owners.owner%3DGUIDE&srt=_score&query=persons.authors.personName:"

def readAuthorscsv(CSVFile):
    df=pd.read_csv(CSVFile)
    return df

def query_Acm(authorNamesFile="Authors.csv"):

    authorsDF=readAuthorscsv(authorNamesFile)
    Afflst = []
    authorNames=authorsDF['Name'].tolist()
    
    for authName in authorNames:
        driver = webdriver.PhantomJS() # wen need to check Phantom js which is hidden and may be faster...
        driver.get(PUB_SEARCH_URL+""+authName)
        link = driver.find_element_by_link_text(authName)
        link.click()

        affHistElems=driver.find_elements_by_xpath("/html/body/div[2]/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr/td/div/a")
        affHist=[]
        for aff in affHistElems:
            affHist.append(aff.text)
        Afflst.append(affHist)
        
    return authorNames,Afflst    


def main():
    names,affs=query_Acm()
    myDF=pd.DataFrame({"Names":names,"Affiliations":affs})
    myDF.to_csv('Auhors_Affs.csv', index=False)
    print myDF
    
if __name__ == '__main__':
        main()
