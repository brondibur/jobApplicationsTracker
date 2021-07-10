import requests
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 
import json
global totalApplications
global totalOpenings
totalApplications = 0
totalOpenings = 0
global starttime
starttime = time.time()
url = "/display/apptime.html"
jores = webdriver.Chrome('chromedriver')  
driver = webdriver.Chrome('chromedriver') 
driver.minimize_window()
jores.get(url)
jores.maximize_window()
with open("details.json", "r") as tfile:
    dets = json.load(tfile)
if "Amazon" in dets:
    amazonuid = dets['Amazon'].strip("]'[").split("','")[0]
    amazonpwd = dets['Amazon'].strip("]'[").split("','")[1]
if "Linkedin" in dets:
    linkedinuid = dets['Linkedin'].strip("]'[").split("','")[0]
    linkedinpwd = dets['Linkedin'].strip("]'[").split("','")[1]
if "Dell" in dets:
    delluid = dets['Dell'].strip("]'[").split("','")[0]
    dellpwd = dets['Dell'].strip("]'[").split("','")[1]
if "Adobe" in dets:
    adobeuid = dets['Adobe'].strip("]'[").split("','")[0]
    adobepwd = dets['Adobe'].strip("]'[").split("','")[1]
if "Master" in dets:
    masteruid = dets['Master'].strip("]'[").split("','")[0]
    masterpwd = dets['Master'].strip("]'[").split("','")[1]
if "Reuters" in dets:
    reuteruid = dets['Reuters'].strip("]'[").split("','")[0]
    reuterpwd = dets['Reuters'].strip("]'[").split("','")[1]
if "Boeing" in dets:
    boeinguid = dets['Boeing'].strip("]'[").split("','")[0]
    boeingpwd = dets['Boeing'].strip("]'[").split("','")[1]
if "PayPal" in dets:
    paypaluid = dets['PayPal'].strip("]'[").split("','")[0]
    paypalpwd = dets['PayPal'].strip("]'[").split("','")[1]
if "Finastra" in dets:
    finastrauid = dets['Finastra'].strip("]'[").split("','")[0]
    finastrapwd = dets['Finastra'].strip("]'[").split("','")[1]
if "Honeywell" in dets:
    honeyuid = dets['Honeywell'].strip("]'[").split("','")[0]
    honeypwd = dets['Honeywell'].strip("]'[").split("','")[1]
if "Naukri" in dets:
    naukriuid = dets['Naukri'].strip("]'[").split("','")[0]
    naukripwd = dets['Naukri'].strip("]'[").split("','")[1]
appres = {"Total":{'Resume Viewed':0,'Submitted':0,'Application Viewed':0},"Amazon":{'Resume Viewed':0,'Submitted':0,'Application Viewed':0},"Linkedin":{'Resume Viewed':0,'Submitted':0,'Application Viewed':0},"Dell":{'Resume Viewed':0,'Submitted':0,'Application Viewed':0},"Adobe":{'Resume Viewed':0,'Submitted':0,'Application Viewed':0},"Master":{'Resume Viewed':0,'Submitted':0,'Application Viewed':0},"Reuters":{'Resume Viewed':0,'Submitted':0,'Application Viewed':0},"Boeing":{'Resume Viewed':0,'Submitted':0,'Application Viewed':0},"PayPal":{'Resume Viewed':0,'Submitted':0,'Application Viewed':0},"Finastra":{'Resume Viewed':0,'Submitted':0,'Application Viewed':0},"Honeywell":{'Resume Viewed':0,'Submitted':0,'Application Viewed':0},"Naukri":{'Resume Viewed':0,'Submitted':0,'Application Viewed':0}}
# Amazon Application Status
if 'amazonuid' in locals():
    global amazonApplications
    global amazonJobIds
    global amazonList
    amazonApplications = 0
    amazonJobIds = []
    amazonList = []
    url = "https://account.amazon.jobs/en-US"
    driver.get(url)
    print("Entering Username", end='')
    for i in range(5):
        print(".",end='')
        time.sleep(1) 
    print()
    sbox = driver.find_element_by_class_name("form-control")
    sbox.send_keys(amazonuid)
    print("Username Entered")
    submit = driver.find_element_by_class_name("btn-info")
    submit.click()
    print("Entering Password",end='')
    for i in range(15):
        print(".",end='')
        time.sleep(1) 
    print()
    pbox = driver.find_element_by_id("loginFormPasswordInputField")
    pbox.send_keys(amazonpwd)
    print("Password Entered")
    submit = driver.find_element_by_class_name("btn-main")
    submit.click()
    print("Logging In",end='')
    for i in range(10):
        print(".",end='')
        time.sleep(1) 
    print()
    print("Logged In")
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    job_profiles = soup.find_all('div', {'class' : 'application card'})
    count = 0
    print("Working on it",end='')
    for job_profile in job_profiles :
        amazonList.append({'Serial':count+1,'Title':job_profile.find('div', {'class' : 'job-title'}).text,'Location':job_profile.find('p', {'class' : 'location-text'}).text.split(', ')[-1],'ID':job_profile.find('p', {'class' : 'job-id'}).text.split(': ')[1],'Applied':job_profile.find('p', {'class' : 'application-date'}).text.split(': ')[1],'Status':job_profile.find('p', {'class' : 'application-status-text'}).text.split(job_profile.find('div', {'class' : 'job-title'}).text.split(" ")[0])[0]})
        amazonJobIds.append(job_profile.find('p', {'class' : 'job-id'}).text.split(': ')[1])
        count += 1
        print('.',end='')
        if(count == 10) :
            break
    totals = int(driver.find_element_by_xpath("//div[@class='col-sm-12 job-count-info']").text.split("of ")[1].split(" ")[0])
    nopa = totals//10
    while nopa > 0:
        submit = driver.find_element_by_xpath("//button[@class='btn circle right']")
        submit.click()
        time.sleep(2)
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        job_profiles = soup.find_all('div', {'class' : 'application card'})
        for job_profile in job_profiles :
            amazonList.append({'Serial':count+1,'Title':job_profile.find('div', {'class' : 'job-title'}).text,'Location':job_profile.find('p', {'class' : 'location-text'}).text.split(', ')[-1],'ID':job_profile.find('p', {'class' : 'job-id'}).text.split(': ')[1],'Applied':job_profile.find('p', {'class' : 'application-date'}).text.split(': ')[1],'Status':job_profile.find('p', {'class' : 'application-status-text'}).text.split(job_profile.find('div', {'class' : 'job-title'}).text.split(" ")[0])[0]})
            amazonJobIds.append(job_profile.find('p', {'class' : 'job-id'}).text.split(': ')[1])
            count += 1
            print('.',end='')
            if(count % 10 == 0) :
                break
        nopa -= 1
    amazonApplications = count
    totalApplications += amazonApplications
    print()
    print("Amazon Application Status Updated")
    with open("applications/amazon.json", "w") as tfile:
        tfile.write('{"Amazon":[')
        for i in range(len(amazonList)):
            if(i != len(amazonList) - 1):
                tfile.write(re.sub("'",'"',str(amazonList[i]))+",")
            else:
                tfile.write(re.sub("'",'"',str(amazonList[i])))
            if(re.search('submitted',amazonList[i]['Status'])):
                appres['Amazon']['Submitted'] += 1
                appres['Total']['Submitted'] += 1
            else:
                if(amazonList[i]['Status'] in appres['Amazon']):
                    appres['Amazon'][amazonList[i]['Status']] += 1
                else:
                    appres['Amazon'][amazonList[i]['Status']] = 1
                if(amazonList[i]['Status'] in appres['Total']):
                    appres['Total'][amazonList[i]['Status']] += 1
                else:
                    appres['Total'][amazonList[i]['Status']] = 1
        tfile.write("]}")
# Linkedin Application Status
if 'linkedinuid' in locals():
    global linkedinApplications
    global linkedinList
    linkedinApplications = 0
    linkedinList = []
    url = "https://www.linkedin.com/login"
    urll = "https://www.linkedin.com/my-items/saved-jobs/"
    driver.get(url)
    print("Entering Login Credentials", end='')
    for i in range(5):
        print(".",end='')
        time.sleep(1) 
    print()
    sbox = driver.find_element_by_id("username")
    pbox = driver.find_element_by_id("password")
    sbox.send_keys(linkedinuid)
    pbox.send_keys(linkedinpwd)
    print("Credentials Entered")
    submit = driver.find_element_by_class_name("btn__primary--large")
    submit.click()
    print("Logging In",end='')
    for i in range(10):
        print(".",end='')
        time.sleep(1) 
    print()
    print("Logged In")
    driver.get(urll)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    job_profiles = soup.find_all('div', {'class' : 'entity-result__item'})
    count = 0
    print("Working on it", end='')
    for job_profile in job_profiles :
        linkedinList.append({'Serial':count+1,'Title':re.sub('\\n', '', job_profile.find('span', {'class' : 'entity-result__title-text'}).text),'Company':re.sub('\\n', '', job_profile.find('div', {'class' : 'entity-result__primary-subtitle'}).text),'Location':re.sub('\\n', '', job_profile.find('div', {'class' : 'entity-result__secondary-subtitle'}).text),'Status':re.sub('\\n', '', job_profile.find('span', {'class' : 'entity-result__simple-insight-text'}).text)})
        count += 1
        print('.',end='')
        if(count == 10) :
            break
    totals = int(driver.find_element_by_xpath("//div[@class='flex-0 pl1 t-black t-normal']").text)
    nopa = totals//10
    while nopa > 0:
        url = "https://www.linkedin.com/my-items/saved-jobs/?start="+str(count)
        driver.get(url) 
        time.sleep(5)
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        job_profiles = soup.find_all('div', {'class' : 'entity-result__item'})
        for job_profile in job_profiles :
            linkedinList.append({'Serial':count+1,'Title':re.sub('\\n', '', job_profile.find('span', {'class' : 'entity-result__title-text'}).text),'Company':re.sub('\\n', '', job_profile.find('div', {'class' : 'entity-result__primary-subtitle'}).text),'Location':re.sub('\\n', '', job_profile.find('div', {'class' : 'entity-result__secondary-subtitle'}).text),'Status':re.sub('\\n', '', job_profile.find('span', {'class' : 'entity-result__simple-insight-text'}).text)})
            count += 1
            print('.',end='')
            if(count == 10) :
                break
        nopa -= 1
    linkedinApplications = count
    totalApplications += linkedinApplications
    print()
    print("Linkedin Application Status Updated")
    with open("applications/linkedin.json", "w") as tfile:
        tfile.write('{"Linkedin":[')
        for i in range(len(linkedinList)):
            if(i != len(linkedinList) - 1):
                tfile.write(re.sub("'",'"',str(linkedinList[i]))+",")
            else:
                tfile.write(re.sub("'",'"',str(linkedinList[i])))
            if(re.search('submitted',linkedinList[i]['Status']) or re.search('Applied',linkedinList[i]['Status'])):
                appres['Linkedin']['Submitted'] += 1
                appres['Total']['Submitted'] += 1
            elif(re.search('Application viewed',linkedinList[i]['Status'])):
                appres['Linkedin']['Application Viewed'] += 1
                appres['Total']['Application Viewed'] += 1
            elif(re.search('Resume',linkedinList[i]['Status'])):
                appres['Linkedin']['Resume Viewed'] += 1
                appres['Total']['Resume Viewed'] += 1
            else:
                if(linkedinList[i]['Status'] in appres['Linkedin']):
                    appres['Linkedin'][linkedinList[i]['Status']] += 1
                else:
                    appres['Linkedin'][linkedinList[i]['Status']] = 1
                if(linkedinList[i]['Status'] in appres['Total']):
                    appres['Total'][linkedinList[i]['Status']] += 1
                else:
                    appres['Total'][linkedinList[i]['Status']] = 1
        tfile.write("]}")
# Dell Application Status
if 'delluid' in locals():
    global dellApplications
    global dellList
    dellApplications = 0
    dellList = []
    url = "https://dell.wd1.myworkdayjobs.com/en-US/External/login"
    driver.get(url)
    print("Entering Login Credentials", end='')
    for i in range(10):
        print(".",end='')
        time.sleep(1) 
    print()
    sbox = driver.find_element_by_id("input-4")
    pbox = driver.find_element_by_id("input-5")
    sbox.send_keys(delluid)
    pbox.send_keys(dellpwd)
    print("Credentials Entered")
    submit = driver.find_element_by_class_name("css-n6lkdc")
    submit.click()
    print("Logging In",end='')
    for i in range(10):
        print(".",end='')
        time.sleep(1) 
    print()
    print("Logged In")
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    job_profiles = soup.find_all('tr', {'class' : 'WED1'})
    count = 0
    print("Working on it", end='')
    for job_profile in job_profiles :
        dellList.append({'Serial':count+1,'Title':re.sub('\\n', '', job_profile.find('div', {'class' : 'gwt-Label WACP WJAP'}).text),'Status':re.sub('\\n', '', job_profile.find('div', {'class' : 'wd-Text WGH2 WLH2 WP5'}).text)})
        count += 1
        print('.',end='')
        if(count == 10) :
            break
    dellApplications = count
    totalApplications += dellApplications
    print()
    print("Dell Application Status Updated")
    with open("applications/dell.json", "w") as tfile:
        tfile.write('{"Dell":[')
        for i in range(len(dellList)):
            if(i != len(dellList) - 1):
                tfile.write(re.sub("'",'"',str(dellList[i]))+",")
            else:
                tfile.write(re.sub("'",'"',str(dellList[i])))
            if(re.search('Submitted',dellList[i]['Status'])):
                appres['Dell']['Submitted'] += 1
                appres['Total']['Submitted'] += 1
            else:
                if(dellList[i]['Status'] in appres['Dell']):
                    appres['Dell'][dellList[i]['Status']] += 1
                else:
                    appres['Dell'][dellList[i]['Status']] = 1
                if(dellList[i]['Status'] in appres['Total']):
                    appres['Total'][dellList[i]['Status']] += 1
                else:
                    appres['Total'][dellList[i]['Status']] = 1
        tfile.write("]}")
# Adobe Application Status
if 'adobeuid' in locals():
    global adobeApplications
    global adobeList
    adobeApplications = 0
    adobeList = []
    url = "https://adobe.wd5.myworkdayjobs.com/en-US/external_experienced/login"
    driver.get(url)
    print("Entering Login Credentials", end='')
    for i in range(10):
        print(".",end='')
        time.sleep(1) 
    print()
    sbox = driver.find_element_by_id("input-4")
    pbox = driver.find_element_by_id("input-5")
    sbox.send_keys(adobeuid)
    pbox.send_keys(adobepwd)
    print("Credentials Entered")
    submit = driver.find_element_by_class_name("css-vjb50u")
    submit.click()
    print("Logging In",end='')
    for i in range(10):
        print(".",end='')
        time.sleep(1) 
    print()
    print("Logged In")
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    job_profiles = soup.find_all('tr', {'class' : 'WED1'})
    count = 0
    print("Working on it", end='')
    for job_profile in job_profiles :
        adobeList.append({'Serial':count+1,'Title':re.sub('\\n', '', job_profile.find('div', {'class' : 'gwt-Label WACP WJAP'}).text),'Status':re.sub('\\n', '', job_profile.find('div', {'class' : 'wd-Text WGH2 WLH2 WP5'}).text)})
        count += 1
        print('.',end='')
        if(count == 10) :
            break
    adobeApplications = count
    totalApplications += adobeApplications
    print()
    print("Adobe Application Status Updated")
    with open("applications/adobe.json", "w") as tfile:
        tfile.write('{"Adobe":[')
        for i in range(len(adobeList)):
            if(i != len(adobeList) - 1):
                tfile.write(re.sub("'",'"',str(adobeList[i]))+",")
            else:
                tfile.write(re.sub("'",'"',str(adobeList[i])))
            if(re.search('In Process',adobeList[i]['Status'])):
                appres['Adobe']['Submitted'] += 1
                appres['Total']['Submitted'] += 1
            else:
                if(dellList[i]['Status'] in appres['Adobe']):
                    appres['Adobe'][adobeList[i]['Status']] += 1
                else:
                    appres['Adobe'][adobeList[i]['Status']] = 1
                if(adobeList[i]['Status'] in appres['Total']):
                    appres['Total'][adobeList[i]['Status']] += 1
                else:
                    appres['Total'][adobeList[i]['Status']] = 1
        tfile.write("]}")
# MasterCard Application Status
if 'masteruid' in locals():
    global masterApplications
    global masterList
    masterApplications = 0
    masterList = []
    url = "https://mastercard.wd1.myworkdayjobs.com/en-US/CorporateCareers/login"
    driver.get(url)
    print("Entering Login Credentials", end='')
    for i in range(10):
        print(".",end='')
        time.sleep(1) 
    print()
    sbox = driver.find_element_by_xpath("//input[@class='gwt-TextBox WF-M']")
    pbox = driver.find_element_by_xpath("//input[@class='gwt-PasswordTextBox WF-M']")
    sbox.send_keys(masteruid)
    pbox.send_keys(masterpwd)
    print("Credentials Entered")
    submit = driver.find_element_by_xpath("//div[@class='WI5T WJUO']")
    submit.click()
    print("Logging In",end='')
    for i in range(10):
        print(".",end='')
        time.sleep(1) 
    print()
    print("Logged In")
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    job_profiles = soup.find_all('tr', {'class' : 'WED1'})
    count = 0
    print("Working on it", end='')
    for job_profile in job_profiles :
        masterList.append({'Serial':count+1,'Title':re.sub('\\n', '', job_profile.find('div', {'class' : 'gwt-Label WACP WJAP'}).text),'Status':re.sub('\\n', '', job_profile.find('div', {'class' : 'wd-Text WGH2 WLH2 WP5'}).text)})
        count += 1
        print('.',end='')
        if(count == 10) :
            break
    masterApplications = count
    totalApplications += masterApplications
    print()
    print("MasterCard Application Status Updated")
    with open("applications/master.json", "w") as tfile:
        tfile.write('{"Master":[')
        for i in range(len(masterList)):
            if(i != len(masterList) - 1):
                tfile.write(re.sub("'",'"',str(masterList[i]))+",")
            else:
                tfile.write(re.sub("'",'"',str(masterList[i])))
            if(re.search('Received',masterList[i]['Status'])):
                appres['Master']['Submitted'] += 1
                appres['Total']['Submitted'] += 1
            elif(re.search('another candidate',masterList[i]['Status'])):
                if('Unsuccessful' in appres['Master']):
                    appres['Master']['Unsuccessful'] += 1
                else:
                    appres['Master']['Unsuccessful'] = 1
                if('Unsuccessful' in appres['Total']):
                    appres['Total']['Unsuccessful'] += 1
                else:
                    appres['Total']['Unsuccessful'] = 1
                appres['Master']['Unsuccessful'] += 1
                appres['Total']['Unsuccessful'] += 1
            else:
                if(masterList[i]['Status'] in appres['Master']):
                    appres['Master'][masterList[i]['Status']] += 1
                else:
                    appres['Master'][masterList[i]['Status']] = 1
                if(masterList[i]['Status'] in appres['Total']):
                    appres['Total'][masterList[i]['Status']] += 1
                else:
                    appres['Total'][masterList[i]['Status']] = 1
        tfile.write("]}")
# ThomsonReuters Application Status
if 'reuteruid' in locals():
    global reuterApplications
    global reuterList
    reuterApplications = 0
    reuterList = []
    url = "https://thomsonreuters.wd5.myworkdayjobs.com/en-US/External_Career_Site/login"
    driver.get(url)
    print("Entering Login Credentials", end='')
    for i in range(10):
        print(".",end='')
        time.sleep(1) 
    print()
    sbox = driver.find_element_by_id("input-4")
    pbox = driver.find_element_by_id("input-5")
    sbox.send_keys(reuteruid)
    pbox.send_keys(reuterpwd)
    print("Credentials Entered")
    submit = driver.find_element_by_class_name("css-1pskw2x")
    submit.click()
    print("Logging In",end='')
    for i in range(10):
        print(".",end='')
        time.sleep(1) 
    print()
    print("Logged In")
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    job_profiles = soup.find_all('tr', {'class' : 'WED1'})
    count = 0
    print("Working on it", end='')
    for job_profile in job_profiles :
        reuterList.append({'Serial':count+1,'Title':re.sub('\\n', '', job_profile.find('div', {'class' : 'gwt-Label WACP WJAP'}).text),'Status':re.sub('\\n', '', job_profile.find('div', {'class' : 'wd-Text WGH2 WLH2 WP5'}).text)})
        count += 1
        print('.',end='')
        if(count == 10) :
            break
    reuterApplications = count
    totalApplications += reuterApplications
    print()
    print("ThomsonReuters Application Status Updated")
    with open("applications/reuter.json", "w") as tfile:
        tfile.write('{"Reuters":[')
        for i in range(len(reuterList)):
            if(i != len(reuterList) - 1):
                tfile.write(re.sub("'",'"',str(reuterList[i]))+",")
            else:
                tfile.write(re.sub("'",'"',str(reuterList[i])))
            if(re.search('In Process',reuterList[i]['Status'])):
                appres['Reuters']['Submitted'] += 1
                appres['Total']['Submitted'] += 1
            else:
                if(reuterList[i]['Status'] in appres['Reuters']):
                    appres['Reuters'][reuterList[i]['Status']] += 1
                else:
                    appres['Reuters'][reuterList[i]['Status']] = 1
                if(reuterList[i]['Status'] in appres['Total']):
                    appres['Total'][reuterList[i]['Status']] += 1
                else:
                    appres['Total'][reuterList[i]['Status']] = 1
        tfile.write("]}")
# Boeing Application Status
if 'boeinguid' in locals():
    global boeingApplications
    global boeingList
    boeingApplications = 0
    boeingList = []
    url = "https://boeing.wd1.myworkdayjobs.com/en-US/EXTERNAL_CAREERS/login"
    driver.get(url)
    print("Entering Login Credentials", end='')
    for i in range(10):
        print(".",end='')
        time.sleep(1) 
    print()
    sbox = driver.find_elements_by_xpath("//input[@class='gwt-TextBox WF-M']")[0]
    pbox = driver.find_elements_by_xpath("//input[@class='gwt-PasswordTextBox WF-M']")[0]
    sbox.send_keys(boeinguid)
    pbox.send_keys(boeingpwd)
    print("Credentials Entered")
    submit = driver.find_element_by_class_name("WH5T")
    submit.click()
    print("Logging In",end='')
    for i in range(10):
        print(".",end='')
        time.sleep(1) 
    print()
    print("Logged In")
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    job_profiles = soup.find_all('tr', {'class' : 'WED1'})
    count = 0
    print("Working on it", end='')
    for job_profile in job_profiles :
        boeingList.append({'Serial':count+1,'Title':re.sub('\\n', '', job_profile.find('div', {'class' : 'gwt-Label WACP WJAP'}).text),'Status':re.sub('\\n', '', job_profile.find('div', {'class' : 'wd-Text WGH2 WLH2 WP5'}).text)})
        count += 1
        print('.',end='')
        if(count == 10) :
            break
    boeingApplications = count
    totalApplications += boeingApplications
    print()
    print("Boeing Application Status Updated")
    with open("applications/boeing.json", "w") as tfile:
        tfile.write('{"Boeing":[')
        for i in range(len(boeingList)):
            if(i != len(boeingList) - 1):
                tfile.write(re.sub("'",'"',str(boeingList[i]))+",")
            else:
                tfile.write(re.sub("'",'"',str(boeingList[i])))
            if(re.search('Consideration',boeingList[i]['Status'])):
                appres['Boeing']['Submitted'] += 1
                appres['Total']['Submitted'] += 1
            else:
                if(boeingList[i]['Status'] in appres['Boeing']):
                    appres['Boeing'][boeingList[i]['Status']] += 1
                else:
                    appres['Boeing'][boeingList[i]['Status']] = 1
                if(boeingList[i]['Status'] in appres['Total']):
                    appres['Total'][boeingList[i]['Status']] += 1
                else:
                    appres['Total'][boeingList[i]['Status']] = 1
        tfile.write("]}")
# PayPal Application Status
if 'paypaluid' in locals():
    global paypalApplications
    global paypalList
    paypalApplications = 0
    paypalList = []
    url = "https://wd1.myworkdaysite.com/en-US/recruiting/paypal/jobs/login"
    driver.get(url)
    print("Entering Login Credentials", end='')
    for i in range(10):
        print(".",end='')
        time.sleep(1) 
    print()
    sbox = driver.find_elements_by_xpath("//input[@class='gwt-TextBox WF-M']")[0]
    pbox = driver.find_elements_by_xpath("//input[@class='gwt-PasswordTextBox WF-M']")[0]
    sbox.send_keys(paypaluid)
    pbox.send_keys(paypalpwd)
    print("Credentials Entered")
    submit = driver.find_element_by_class_name("WH5T")
    submit.click()
    print("Logging In",end='')
    for i in range(10):
        print(".",end='')
        time.sleep(1) 
    print()
    print("Logged In")
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    job_profiles = soup.find_all('tr', {'class' : 'WED1'})
    count = 0
    print("Working on it", end='')
    for job_profile in job_profiles :
        paypalList.append({'Serial':count+1,'Title':re.sub('\\n', '', job_profile.find('div', {'class' : 'gwt-Label WACP WJAP'}).text),'Status':re.sub('\\n', '', job_profile.find('div', {'class' : 'wd-Text WGH2 WLH2 WP5'}).text)})
        count += 1
        print('.',end='')
        if(count == 10) :
            break
    paypalApplications = count
    totalApplications += paypalApplications
    print()
    print("PayPal Application Status Updated")
    with open("applications/paypal.json", "w") as tfile:
        tfile.write('{"PayPal":[')
        for i in range(len(paypalList)):
            if(i != len(paypalList) - 1):
                tfile.write(re.sub("'",'"',str(paypalList[i]))+",")
            else:
                tfile.write(re.sub("'",'"',str(paypalList[i])))
            if(re.search('Submitted',paypalList[i]['Status'])):
                appres['PayPal']['Submitted'] += 1
                appres['Total']['Submitted'] += 1
            else:
                if(paypalList[i]['Status'] in appres['PayPal']):
                    appres['PayPal'][paypalList[i]['Status']] += 1
                else:
                    appres['PayPal'][paypalList[i]['Status']] = 1
                if(paypalList[i]['Status'] in appres['Total']):
                    appres['Total'][paypalList[i]['Status']] += 1
                else:
                    appres['Total'][paypalList[i]['Status']] = 1
        tfile.write("]}")
# Finastra Application Status
if 'finastrauid' in locals():
    global finastraApplications
    global finastraList
    finastraApplications = 0
    finastraList = []
    url = "https://dh.wd3.myworkdayjobs.com/DHC/login"
    driver.get(url)
    print("Entering Login Credentials", end='')
    for i in range(10):
        print(".",end='')
        time.sleep(1) 
    print()
    sbox = driver.find_element_by_id("input-4")
    pbox = driver.find_element_by_id("input-5")
    sbox.send_keys(finastrauid)
    pbox.send_keys(finastrapwd)
    print("Credentials Entered")
    submit = driver.find_element_by_class_name("css-1s1r74k")
    submit.click()
    print("Logging In",end='')
    for i in range(10):
        print(".",end='')
        time.sleep(1) 
    print()
    print("Logged In")
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    job_profiles = soup.find_all('tr', {'class' : 'WED1'})
    count = 0
    print("Working on it", end='')
    for job_profile in job_profiles :
        finastraList.append({'Serial':count+1,'Title':re.sub('\\n', '', job_profile.find('div', {'class' : 'gwt-Label WACP WJAP'}).text),'Status':re.sub('\\n', '', job_profile.find('div', {'class' : 'wd-Text WGH2 WLH2 WP5'}).text)})
        count += 1
        print('.',end='')
        if(count == 10) :
            break
    finastraApplications = count
    totalApplications += finastraApplications
    print()
    print("Finastra Application Status Updated")
    with open("applications/finastra.json", "w") as tfile:
        tfile.write('{"Finastra":[')
        for i in range(len(finastraList)):
            if(i != len(finastraList) - 1):
                tfile.write(re.sub("'",'"',str(finastraList[i]))+",")
            else:
                tfile.write(re.sub("'",'"',str(finastraList[i])))
            if(re.search('Submitted',finastraList[i]['Status'])):
                appres['Finastra']['Submitted'] += 1
                appres['Total']['Submitted'] += 1
            else:
                if(finastraList[i]['Status'] in appres['Finastra']):
                    appres['Finastra'][finastraList[i]['Status']] += 1
                else:
                    appres['Finastra'][finastraList[i]['Status']] = 1
                if(finastraList[i]['Status'] in appres['Total']):
                    appres['Total'][finastraList[i]['Status']] += 1
                else:
                    appres['Total'][finastraList[i]['Status']] = 1
        tfile.write("]}")
# Naukri Application Status
if 'naukriuid' in locals():
    global naukriApplications
    global naukriList
    naukriApplications = 0
    naukriList = []
    url = "https://www.naukri.com/myapply/historypage"
    driver.get(url)
    print("Entering Login Credentials", end='')
    for i in range(5):
        print(".",end='')
        time.sleep(1) 
    print()
    sbox = driver.find_element_by_id("usernameField")
    pbox = driver.find_element_by_id("passwordField")
    sbox.send_keys(naukriuid)
    pbox.send_keys(naukripwd)
    print("Credentials Entered")
    submit = driver.find_element_by_class_name("blue-btn")
    submit.click()
    print("Logging In",end='')
    for i in range(10):
        print(".",end='')
        time.sleep(1) 
    print()
    print("Logged In")
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    totals = int(driver.find_element_by_class_name("grayLTxtBold").text)
    nopa = totals//10
    while nopa > 0:
        elementer = driver.find_element_by_class_name('jdTuplesContainer')
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", elementer);
        elementer = driver.find_element_by_class_name('appHistWrapper')
        driver.execute_script("window.scrollTo(0, arguments[0].scrollHeight);", elementer);
        time.sleep(2)
        driver.execute_script("window.scrollTo(0,0);");
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        nopa -= 1
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    job_profiles = soup.find_all('div', {'class' : 'jdTupleContainer'})
    count = 0
    print("Working on it", end='')
    for job_profile in job_profiles :
        naukriList.append({'Serial':count+1,'Title':re.sub('\\n', '', job_profile.find('div', {'class' : 'jdTitle'}).text),'Company':re.sub('\\n', '', job_profile.find('span', {'class' : 'company'}).text),'Status':re.sub('\\n', '', job_profile.find('span', {'class' : 'title fw500'}).text)})
        count += 1
        print('.',end='')
    naukriApplications = count
    totalApplications += naukriApplications
    print()
    print("Naukri Application Status Updated")
    with open("applications/naukri.json", "w") as tfile:
        tfile.write('{"Naukri":[')
        for i in range(len(naukriList)):
            if(i != len(naukriList) - 1):
                tfile.write(re.sub("'",'"',str(naukriList[i]))+",")
            else:
                tfile.write(re.sub("'",'"',str(naukriList[i])))
            if(re.search('Application Sent',naukriList[i]['Status'])):
                appres['Naukri']['Submitted'] += 1
                appres['Total']['Submitted'] += 1
            else:
                z = naukriList[i]['Status'].split(' ')
                z = str(z[0]+' '+z[1])
                if(z in appres['Naukri']):
                    appres['Naukri'][z] += 1
                else:
                    appres['Naukri'][z] = 1
                if(z in appres['Total']):
                    appres['Total'][z] += 1
                else:
                    appres['Total'][z] = 1
        tfile.write("]}")
# Honeywell Application Status
if 'honeyuid' in locals():
    global honeyApplications
    global honeyList
    honeyApplications = 0
    honeyList = []
    url = "https://honeywell.csod.com/ats/careersite/login.aspx"
    urll = 'https://honeywell.csod.com/ATS/careersite/ds.aspx?routename=ATS/CareerSite/MyProfile&c=honeywell&site=1'
    driver.get(url)
    print("Entering Login Credentials", end='')
    for i in range(10):
        print(".",end='')
        time.sleep(1) 
    print()
    sbox = driver.find_element_by_id('ctl00_siteContent_txtEmail')
    pbox = driver.find_element_by_id('ctl00_siteContent_txtPassword')
    sbox.send_keys(honeyuid)
    pbox.send_keys(honeypwd)
    print("Credentials Entered")
    submit = driver.find_element_by_xpath("//a[@class='btn-lnk c-bg-corp']")
    submit.click()
    print("Logging In",end='')
    for i in range(10):
        print(".",end='')
        time.sleep(1) 
    driver.get(urll)
    for i in range(5):
        print(".",end='')
        time.sleep(1) 
    print()
    print("Logged In")
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    job_profiles = soup.find_all('div', {'class' : 'c-bdr-gr10'})
    count = 0
    print("Working on it", end='')
    for job_profile in job_profiles :
        a = job_profile.find('div',{"class":"gt-small"}).text.split(": ")
        honeyList.append({'Serial':count+1,'Title':re.sub('\\n', '', job_profile.find('a', {'class' : 'cso-text-xlarge'}).text),'Status':a[3].split(' ')[0],"ID":a[1].split(' ')[0],"Updated":a[2].split(' ')[0]})
        count += 1
        print('.',end='')
        if(count == 10) :
            break
    honeyApplications = count
    totalApplications += honeyApplications
    print()
    print("Honeywell Application Status Updated")
    driver.close()
    with open("applications/honeywell.json", "w") as tfile:
        tfile.write('{"Honeywell":[')
        for i in range(len(honeyList)):
            if(i != len(honeyList) - 1):
                tfile.write(re.sub("'",'"',str(honeyList[i]))+",")
            else:
                tfile.write(re.sub("'",'"',str(honeyList[i])))
            if(re.search('Submitted',honeyList[i]['Status'])):
                appres['Honeywell']['Submitted'] += 1
                appres['Total']['Submitted'] += 1
            else:
                if(honeyList[i]['Status'] in appres['Finastra']):
                    appres['Honeywell'][honeyList[i]['Honeywell']] += 1
                else:
                    appres['Honeywell'][honeyList[i]['Status']] = 1
                if(honeyList[i]['Status'] in appres['Total']):
                    appres['Total'][honeyList[i]['Status']] += 1
                else:
                    appres['Total'][honeyList[i]['Status']] = 1
        tfile.write("]}")
uname = ''
if "Name" in dets:
    uname = dets['Name']
newContent = "\n" + 'var name = "'+ str(uname) + '"\n' + "var totapp = "+ str(totalApplications) + "\n"  + "var amazonapp = "+ str(amazonApplications) + "\n" + "var linkedinapp = "+ str(linkedinApplications) + "\n" + "var dellapp = "+ str(dellApplications) + "\n" + "var adobeapp = "+ str(adobeApplications) + "\n" + "var masterapp = "+ str(masterApplications) + "\n" + "var reuterapp = "+ str(reuterApplications) + "\n" + "var boeingapp = "+ str(boeingApplications) + "\n" + "var paypalapp = "+ str(paypalApplications) + "\n" + "var finastraapp = "+ str(finastraApplications) + "\n" + "var honeyapp = "+ str(honeyApplications) + "\n" + "var naukritapp = "+ str(naukriApplications) + "\n" + "var appdeet = "+ str(appres) + "\n"

with open("display/jat.html") as inf:
    txt = inf.read()
    soup = BeautifulSoup(txt, "html.parser")

a = soup.find("script", {"class":"contentInput"})
a.clear()
a.append(newContent)
with open("display/jat.html", "w") as outf:
    outf.write(str(soup))
url = "/display/jat.html"
jores.get(url)
jores.maximize_window()
