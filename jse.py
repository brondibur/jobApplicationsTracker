import requests
import pandas as pd 
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
url = "file:///E:/Projects/jobApplictionsTracker/display/jsetime.html"
jores = webdriver.Chrome('chromedriver')  
driver = webdriver.Chrome('chromedriver') 
driver.minimize_window()
jores.get(url)
jores.maximize_window()
# Amazon - Software Development Engineer Job Search
global amazonOpeningsTotal
global amazonOpenings
amazonOpeningsTotal = 0
amazonOpenings = []
url = "https://www.amazon.jobs/en/search?offset=0&result_limit=10&sort=recent&category%5B%5D=software-development&category%5B%5D=machine-learning-science&category%5B%5D=data-science&job_type%5B%5D=Full-Time&cities%5B%5D=Noida%2C%20Uttar%20Pradesh%2C%20IND&cities%5B%5D=Mumbai%2C%20Maharashtra%2C%20IND&cities%5B%5D=Pune%2C%20Maharashtra%2C%20IND&cities%5B%5D=Gurugram%2C%20Haryana%2C%20IND&cities%5B%5D=Bengaluru%2C%20Karnataka%2C%20IND&category_type=Corporate&distanceType=Mi&radius=24km&latitude=&longitude=&loc_group_id=&loc_query=India&base_query=Software%20Development%20Engineer&city=&country=IND&region=&county=&query_options=&"
driver.get(url) 
print('Updating Amazon Openings')
time.sleep(10)
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
all_divs = soup.find_all('div', {'class' : 'job-tile'})
job_profiles = []
for divs in all_divs:
    job_profiles += divs.find_all('a')

totals = int(soup.find('div', {'class' : 'job-count-info'}).text.split("of ")[1].split(" ")[0])
count = 0
jono = 1
print("Working on it", end=' ')
print(' ', end='')
for job_profile in job_profiles :
    a = job_profile.find('h3', {'class' : 'job-title'}).text
    if a=="Software Development Engineer" or a=="Software Dev Engineer" or re.search("Software Development Engineer Graduate",a) or a=="Software Development Engineer I" or re.search("Software Development Engineer I ",a) or re.search("Amazon Tech U Graduate Program",a) or a=="SDE-I" or a=="SDE" or re.search("Software Development Engineer -",a) or re.search("Software Development Engineer I,",a):
        c = job_profile.find('p', {'class' : 'location-and-id'}).text.split(', ')[2].split(' | ')[1].split(": ")[1]
        g = a.lower().split(" ")
        h = ""
        for i in g:
            h += i
            h+= "-"
        i = "https://www.amazon.jobs/en/jobs/"+c+"/"+h
        amazonOpenings.append({"Serial":jono,"Title":a,"Location":job_profile.find('p', {'class' : 'location-and-id'}).text.split(', ')[2].split(' | ')[0],"ID":c,"Posted":job_profile.find('h2', {'class' : 'posting-date'}).text.split('Posted ')[1],"Description":job_profile.find('p', {'class' : 'description'}).text.split("Read more")[0],"Updated":job_profile.find('p', {'class' : 'time-elapsed'}).text,"Link":i})
        jono += 1
    count = count + 1
    print('.',end='')
    if(count == 10) :
        break

nopa = totals//10
while nopa > 0:
    url = "https://www.amazon.jobs/en/search?offset="+str(count)+"&result_limit=10&sort=recent&category%5B%5D=software-development&category%5B%5D=machine-learning-science&category%5B%5D=data-science&job_type%5B%5D=Full-Time&cities%5B%5D=Noida%2C%20Uttar%20Pradesh%2C%20IND&cities%5B%5D=Mumbai%2C%20Maharashtra%2C%20IND&cities%5B%5D=Pune%2C%20Maharashtra%2C%20IND&cities%5B%5D=Gurugram%2C%20Haryana%2C%20IND&cities%5B%5D=Bengaluru%2C%20Karnataka%2C%20IND&category_type=Corporate&distanceType=Mi&radius=24km&latitude=&longitude=&loc_group_id=&loc_query=India&base_query=Software%20Development%20Engineer&city=&country=IND&region=&county=&query_options=&"
    driver.get(url) 
    time.sleep(10) 
    
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    all_divs = soup.find_all('div', {'class' : 'job-tile'})
    job_profiles = []
    for divs in all_divs:
        job_profiles += divs.find_all('a')

    totals = int(soup.find('div', {'class' : 'job-count-info'}).text.split("of ")[1].split(" ")[0])
    for job_profile in job_profiles :
        a = job_profile.find('h3', {'class' : 'job-title'}).text
        if a=="Software Development Engineer" or a=="Software Dev Engineer" or a=="SOFTWARE DEVELOPMENT ENGINEER" or re.search("Software Development Engineer Graduate",a) or a=="Software Development Engineer I" or re.search("Software Development Engineer I ",a) or re.search("Amazon Tech U Graduate Program",a) or a=="SDE-I" or a=="SDE" or re.search("Software Development Engineer -",a) or re.search("Software Development Engineer I,",a):
            c = job_profile.find('p', {'class' : 'location-and-id'}).text.split(', ')[2].split(' | ')[1].split(": ")[1]
            g = a.lower().split(" ")
            h = ""
            for i in g:
                h += i
                h+= "-"
            i = "https://www.amazon.jobs/en/jobs/"+c+"/"+h
            amazonOpenings.append({"Serial":jono,"Title":a,"Location":job_profile.find('p', {'class' : 'location-and-id'}).text.split(', ')[2].split(' | ')[0],"ID":c,"Posted":job_profile.find('h2', {'class' : 'posting-date'}).text.split('Posted ')[1],"Description":job_profile.find('p', {'class' : 'description'}).text.split("Read more")[0],"Updated":job_profile.find('p', {'class' : 'time-elapsed'}).text,"Link":i})
            jono += 1
        count = count + 1
        print('.',end='')
        if(count == 10) :
            break
    print("%i pages left"%nopa)
    nopa -= 1
print()
print("Amazon Openings Updated")
amazonOpeningsTotal = count
totalOpenings += amazonOpeningsTotal
# Dell - Software Development Engineer Job Search
global dellOpeningsTotal
global dellOpenings
dellOpeningsTotal = 0
dellOpenings = []
url = "https://dell.wd1.myworkdayjobs.com/External/"
driver.get(url) 
print('Updating Dell Openings', end='')
for i in range(10):
    print(".",end='')
    time.sleep(1) 
print()
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
submit = driver.find_element_by_id('wd-FacetValue-CheckBox-Location_Country::c4f78be1a8f14da0ab49ce1162348a5e-input')
driver.execute_script("arguments[0].click();", submit);
time.sleep(3) 
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
submit = driver.find_element_by_id('wd-FacetValue-CheckBox-Job_Profiles::914289f44c2f016f83a24faa9c395ce6-input')
driver.execute_script("arguments[0].click();", submit);
time.sleep(3) 
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
totals = int(soup.find('span', {'class' : 'gwt-InlineLabel WMNO WNNO'}).text.split(" ")[0])
nopa = totals//50
while nopa > 0:
    elementer = driver.find_element_by_class_name('WAOO WENO')
    driver.execute_script("window.scrollTo(0, arguments[0].scrollHeight);", elementer);
    time.sleep(2)
    driver.execute_script("window.scrollTo(0,0);");
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    nopa -= 1
count = 0
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
print("Working on it ", end='')
job_profiles = soup.find_all('li', {'class' : 'WP4F WBPO WAAB WGAG'})
for job_profile in job_profiles :
    dellOpenings.append({"Serial":count+1,"Title":job_profile.find('div', {'class' : 'gwt-Label WACP WJAP'}).text,"Location":job_profile.find('span', {'class' : 'gwt-InlineLabel WDAG WC5F'}).text.split(' | ')[1].split(',')[0],"ID":job_profile.find('span', {'class' : 'gwt-InlineLabel WDAG WC5F'}).text.split(' | ')[0],"Posted":job_profile.find('span', {'class' : 'gwt-InlineLabel WDAG WC5F'}).text.split(' | ')[2].split("Posted ")[1]})
    count = count + 1
    print('.',end='')
print()
print("Dell Openings Updated")
dellOpeningsTotal = count
totalOpenings += dellOpeningsTotal
# Disney + Hoststar Openings
urls = ["https://jobs.lever.co/hotstar/?location=Bangalore%2FMumbai%2F%20Gurgaon&department=1.%20Engineering&team=Web","https://jobs.lever.co/hotstar/?location=Bangalore%2FMumbai%2F%20Gurgaon&department=1.%20Engineering&team=Ad%20Tech","https://jobs.lever.co/hotstar/?location=Bangalore%2FMumbai%2F%20Gurgaon&department=1.%20Engineering&team=Cloud%20Infrastructure","https://jobs.lever.co/hotstar/?location=Bangalore%2FMumbai%2F%20Gurgaon&department=1.%20Engineering&team=Engineering%20Productivity","https://jobs.lever.co/hotstar/?location=Bangalore%2FMumbai%2F%20Gurgaon&department=1.%20Engineering&team=International%20and%20Growth","https://jobs.lever.co/hotstar/?location=Bangalore%2FMumbai%2F%20Gurgaon&department=1.%20Engineering&team=Living%20Room%20Devices","https://jobs.lever.co/hotstar/?location=Bangalore%2FMumbai%2F%20Gurgaon&department=1.%20Engineering&team=Machine%20Learning","https://jobs.lever.co/hotstar/?location=Bangalore%2FMumbai%2F%20Gurgaon&department=1.%20Engineering&team=Personalization","https://jobs.lever.co/hotstar/?location=Bangalore%2FMumbai%2F%20Gurgaon&department=1.%20Engineering&team=Social","https://jobs.lever.co/hotstar/?location=Bangalore%2FMumbai%2F%20Gurgaon&department=1.%20Engineering&team=User%20and%20Subscriptions%20Management"]
global hotstarOpeningsTotal
global hotstarOpenings
hotstarOpeningsTotal = 0
hotstarOpenings = []
nojo = 1
print('Updating Disney + Hotstar Openings')
for url in urls:
    driver.get(url) 
    print("Working on page "+str(urls.index(url)+1), end=' ')
    for i in range(10):
        print(".",end='')
        time.sleep(1) 
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    count = 0
    job_profiles = soup.find_all('div', {'class' : 'posting'})
    if len(job_profiles) > 0:
        for job_profile in job_profiles :
            b = job_profile.find('span', {'class' : 'sort-by-location'}).text
            a = job_profile.find('a', {'class' : 'posting-title'}).text.split(b)[0]
            if (not re.search("Senior",a)) and (not re.search("Manager",a)):
                hotstarOpenings.append({"Serial":nojo,"Title":a,"Location":b,"Link":driver.find_element_by_xpath("//a[@class='posting-btn-submit template-btn-submit black']").get_attribute("href")})
                nojo += 1
            count = count + 1
            print('.',end='')
    print()
    print("Page "+str(urls.index(url)+1)+" done")
hotstarOpeningsTotal += nojo
totalOpenings += hotstarOpeningsTotal
print()
print("Disney + Hotstar Openings Updated")
# Facebook - Software Development Engineer Job Search
global fbOpeningsTotal
global fbOpenings
fbOpeningsTotal = 0
fbOpenings = []
url = "https://www.facebook.com/careers/jobs?page=1&results_per_page=100&sub_teams[0]=Artificial%20Intelligence&sub_teams[1]=Computer%20Vision&sub_teams[2]=Data%20Science&sub_teams[3]=Engineering&sub_teams[4]=IT&sub_teams[5]=Machine%20Learning&sub_teams[6]=Solutions%20Engineering&sub_teams[7]=User%20Experience&offices[0]=Bangalore%2C%20India&offices[1]=Hyderabad%2C%20India&offices[2]=New%20Delhi%2C%20India&offices[3]=Mumbai%2C%20India&offices[4]=Gurgaon%2C%20India#search_result"
urll = 'https://www.facebook.com/careers/jobs?results_per_page=100&sub_teams[0]=Artificial%20Intelligence&sub_teams[1]=Computer%20Vision&sub_teams[2]=Data%20Science&sub_teams[3]=Engineering&sub_teams[4]=IT&sub_teams[5]=Machine%20Learning&sub_teams[6]=Solutions%20Engineering&sub_teams[7]=User%20Experience&sub_teams[8]=Client%20Solutions&offices[0]=Bangalore%2C%20India&offices[1]=Hyderabad%2C%20India&offices[2]=New%20Delhi%2C%20India&offices[3]=Mumbai%2C%20India&offices[4]=Gurgaon%2C%20India#search_result' 
driver.get(urll)
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
count = 0
print("Working on it ", end='')
job_profiles = soup.find_all('a', {'class' : '_8sef'})
for job_profile in job_profiles :
    a = job_profile.find_all('div', {'class' : '_8see'})[0].text
    b = str(job_profile).split('href="')[1].split('"')[0]
    if(re.search("\+",a)):
        a = a.split('+')[0] + ' + ' + driver.find_element_by_xpath("//a[@href='"+b+"']//div//div//div[@class='_8see']//div").get_attribute("data-tooltip-content")
    fbOpenings.append({"Serial":count+1,"Title":job_profile.find('div', {'class' : '_8sel'}).text,"Location":a,"Category":job_profile.find_all('div', {'class' : '_8see'})[1].text,"Link":"https://facebook.com"+b})
    count += 1
    print('.',end='')
print()
print("Facebook Openings Updated")
fbOpeningsTotal = count
totalOpenings += fbOpeningsTotal
# Twitter - Software Development Engineer Job Search
global twitterOpeningsTotal
global twitterOpenings
twitterOpeningsTotal = 0
twitterOpenings = []
url = "https://careers.twitter.com/content/careers-twitter/en/roles.html#location=careers-twitter%3Asr%2Foffice%2Fin%2Fbangalore&location=careers-twitter%3Asr%2Foffice%2Fin%2Fdelhi&location=careers-twitter%3Asr%2Foffice%2Fin%2Fmumbai&location=careers-twitter%3Asr%2Foffice%2Fin%2Fremote-india&q=software%20developer&sortBy=modified&team=careers-twitter%3Asr%2Fteam%2Fdata-science-and-analytics&team=careers-twitter%3Asr%2Fteam%2Fit-it-enterprise-applications&team=careers-twitter%3Asr%2Fteam%2Fmachine-learning&team=careers-twitter%3Asr%2Fteam%2Fsoftware-engineering"
driver.get(url)
print('Updating Twitter Openings', end='')
for i in range(10):
    print(".",end='')
    time.sleep(1) 
print()
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
totals = int(soup.find('span', {'class' : 'cr01__results-count chirp--bold-50'}).text.split("of ")[1].split(" ")[0])
nopa = totals//15
if nopa > 0:
    submit = driver.find_element_by_xpath("//button[@class='chirp-btn cr01__button-more  chirp-btn--black chirp-btn--primary']")
print("Working on it ", end='')
count = 0
while nopa > 0:
    driver.execute_script("arguments[0].click();", submit);
    time.sleep(2)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    nopa -= 1
    print('.',end='')
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
job_profiles = soup.find_all('a', {'class' : 'cr01__result-body'})
nojo = 1
for job_profile in job_profiles :
    a = job_profile.find('h3', {'class' : 'cr01__result-title'}).text
    if (not re.search("Senior",a)) and (not re.search("Manager",a)):
        twitterOpenings.append({"Serial":nojo,"Title":a,"Location": job_profile.find_all('span', {'class' : 'cr01__result-subtitle'})[1].text,"Link":str(job_profile).split('href="')[1].split('"')[0]})
        nojo += 1
    count += 1
    print('.',end='')
print()
print("Twitter Openings Updated")
twitterOpeningsTotal = nojo
totalOpenings += twitterOpeningsTotal
# Adobe - Software Development Engineer Job Search
global adobeOpeningsTotal
global adobeOpenings
adobeOpeningsTotal = 0
adobeOpenings = []
url = "https://adobe.wd5.myworkdayjobs.com/en-US/external_experienced"
driver.get(url) 
print('Updating Adobe Openings', end='')
for i in range(10):
    print(".",end='')
    time.sleep(1) 
print()
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
ids = ['wd-FacetValue-CheckBox-locationCountry::c4f78be1a8f14da0ab49ce1162348a5e-input','wd-FacetValue-CheckBox-jobFamilyGroup::591af8b812fa10737af39db3d96eed9f-input','wd-FacetValue-CheckBox-jobFamilyGroup::591af8b812fa10737b0e880e0e3eeee9-input']
for eid in ids:
    submit = driver.find_element_by_id(eid)
    driver.execute_script("arguments[0].click();", submit);
    time.sleep(3) 
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
totals = int(soup.find('span', {'class' : 'gwt-InlineLabel WMNO WNNO'}).text.split(" ")[0])
nopa = totals//50
while nopa > 0:
    elementer = driver.find_element_by_xpath("//div[@class='WAOO WENO']")
    driver.execute_script("window.scrollTo(0, arguments[0].scrollHeight);", elementer);
    time.sleep(2)
    driver.execute_script("window.scrollTo(0,0);");
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    nopa -= 1
count = 0
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
print("Working on it ", end='')
jono = 1
job_profiles = soup.find_all('li', {'class' : 'WP4F WBPO WAAB WGAG'})
for job_profile in job_profiles :
    a = job_profile.find('div', {'class' : 'gwt-Label WACP WJAP'}).text
    if (not re.search("Senior",a)) and (not re.search("Manager",a)) and (not re.search("II",a)) and (not re.search("2",a)) and (not re.search("Lead",a)):
        adobeOpenings.append({"Serial":jono,"Title":a,"Location":job_profile.find('span', {'class' : 'gwt-InlineLabel WDAG WC5F'}).text.split(' | ')[1].split(',')[0],"ID":job_profile.find('span', {'class' : 'gwt-InlineLabel WDAG WC5F'}).text.split(' | ')[0],"Posted":job_profile.find('span', {'class' : 'gwt-InlineLabel WDAG WC5F'}).text.split(' | ')[2].split("Posted ")[1]})
        jono += 1
    count = count + 1
    print('.',end='')
print()
print("Adobe Openings Updated")
adobeOpeningsTotal = jono
totalOpenings += adobeOpeningsTotal
# MasterCard - Software Development Engineer Job Search
global masterOpeningsTotal
global masterOpenings
masterOpeningsTotal = 0
masterOpenings = []
url = "https://mastercard.wd1.myworkdayjobs.com/CorporateCareers/"
driver.get(url) 
print('Updating MasterCard Openings', end='')
for i in range(10):
    print(".",end='')
    time.sleep(1) 
print()
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
submit = driver.find_element_by_id('wd-FacetValue-CheckBox-locations::8eab563831bf10acbc722e4859721571-input')
driver.execute_script("arguments[0].click();", submit);
time.sleep(3) 
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
ids = ['wd-FacetValue-CheckBox-jobFamilyGroup::866c0ed135ff106f00587685e7483440-input','wd-FacetValue-CheckBox-locations::8eab563831bf10acb97b7fba5feff76e-input','wd-FacetValue-CheckBox-jobFamilyGroup::62eb357456311007ffe9529562417cd4-input','wd-FacetValue-CheckBox-jobFamilyGroup::866c0ed135ff106f00a52e9d27783579-input','wd-FacetValue-CheckBox-jobFamilyGroup::866c0ed135ff106f00a52e9d27783579-input','wd-FacetValue-CheckBox-jobFamilyGroup::32c63b91509d1037cdc1ee728fc05b02-input','wd-FacetValue-CheckBox-jobFamilyGroup::70c27ec1148d483eb285aaadb278ef42-input','wd-FacetValue-CheckBox-jobFamilyGroup::79159e74ef6f01a1ba398ea19325020c-input','wd-FacetValue-CheckBox-jobFamilyGroup::2008c8ccf9ae4e56b7d0ea7b3d319a98-input']
for eid in ids:
    submit = driver.find_element_by_id(eid)
    driver.execute_script("arguments[0].click();", submit);
    time.sleep(3) 
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
totals = int(soup.find('span', {'class' : 'gwt-InlineLabel WMNO WNNO'}).text.split(" ")[0])
nopa = totals//50
while nopa > 0:
    elementer = driver.find_element_by_xpath("//div[@class='WAOO WENO']")
    driver.execute_script("window.scrollTo(0, arguments[0].scrollHeight);", elementer);
    time.sleep(2)
    driver.execute_script("window.scrollTo(0,0);");
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    nopa -= 1
count = 0
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
print("Working on it ", end='')
jono = 1
job_profiles = soup.find_all('li', {'class' : 'WP4F WBPO WAAB WGAG'})
for job_profile in job_profiles :
    a = job_profile.find('div', {'class' : 'gwt-Label WACP WJAP'}).text
    if (not re.search("Senior",a)) and (not re.search("Manager",a)) and (not re.search("II",a)) and (not re.search("2",a)) and (not re.search("Lead",a)) and (not re.search("Director",a)) and (not re.search("Prinipal",a)) and (not re.search("President",a)):
        masterOpenings.append({"Serial":jono,"Title":a,"Location":job_profile.find('span', {'class' : 'gwt-InlineLabel WDAG WC5F'}).text.split(' | ')[1].split(',')[0],"ID":job_profile.find('span', {'class' : 'gwt-InlineLabel WDAG WC5F'}).text.split(' | ')[0],"Posted":job_profile.find('span', {'class' : 'gwt-InlineLabel WDAG WC5F'}).text.split(' | ')[2].split("Posted ")[1]})
        jono += 1
    count = count + 1
    print('.',end='')
print()
print("MasterCard Openings Updated")
masterOpeningsTotal = jono
totalOpenings += masterOpeningsTotal
# ThomsonReuters - Software Development Engineer Job Search
global reuterOpeningsTotal
global reuterOpenings
reuterOpeningsTotal = 0
reuterOpenings = []
url = "https://thomsonreuters.wd5.myworkdayjobs.com/External_Career_Site/5/refreshFacet/318c8bb6f553100021d223d9780d30be"
driver.get(url) 
print('Updating ThomsonReuters Openings', end='')
for i in range(10):
    print(".",end='')
    time.sleep(1) 
print()
html = driver.page_source
ids = ['wd-FacetValue-CheckBox-Location_Country::c4f78be1a8f14da0ab49ce1162348a5e-input','wd-FacetValue-CheckBox-jobFamilyGroup::45878602fca640ccb862953105224698-input','wd-FacetValue-CheckBox-jobFamilyGroup::1efb1a6360c4495c8288c5245f7f4461-input']
for eid in ids:
    submit = driver.find_element_by_id(eid)
    driver.execute_script("arguments[0].click();", submit);
    time.sleep(3) 
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
totals = int(soup.find('span', {'class' : 'gwt-InlineLabel WMNO WNNO'}).text.split(" ")[0])
nopa = totals//50
while nopa > 0:
    elementer = driver.find_element_by_xpath("//div[@class='WAOO WENO']")
    driver.execute_script("window.scrollTo(0, arguments[0].scrollHeight);", elementer);
    time.sleep(2)
    driver.execute_script("window.scrollTo(0,0);");
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    nopa -= 1
count = 0
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
print("Working on it ", end='')
jono = 1
job_profiles = soup.find_all('li', {'class' : 'WP4F WBPO WAAB WGAG'})
for job_profile in job_profiles :
    a = job_profile.find('div', {'class' : 'gwt-Label WACP WJAP'}).text
    if (not re.search("Senior",a)) and (not re.search("Manager",a)) and (not re.search("II",a)) and (not re.search("2",a)) and (not re.search("Lead",a)):
        reuterOpenings.append({"Serial":jono,"Title":a,"Location":job_profile.find('span', {'class' : 'gwt-InlineLabel WDAG WC5F'}).text.split(' | ')[1].split(',')[0],"ID":job_profile.find('span', {'class' : 'gwt-InlineLabel WDAG WC5F'}).text.split(' | ')[0],"Posted":job_profile.find('span', {'class' : 'gwt-InlineLabel WDAG WC5F'}).text.split(' | ')[2].split("Posted ")[1]})
        jono += 1
    count = count + 1
    print('.',end='')
print()
print("ThomsonReuters Openings Updated")
reuterOpeningsTotal = jono
totalOpenings += reuterOpeningsTotal
# Boeing - Software Development Engineer Job Search
global boeingOpeningsTotal
global boeingOpenings
boeingOpeningsTotal = 0
boeingOpenings = []
url = "https://boeing.wd1.myworkdayjobs.com/EXTERNAL_CAREERS/"
driver.get(url) 
print('Updating Boeing Openings', end='')
for i in range(10):
    print(".",end='')
    time.sleep(1) 
print()
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
submit = driver.find_element_by_id('wd-FacetValue-CheckBox-locations::8b618a30e00f01736afdd74c1b3f5d89-input')
driver.execute_script("arguments[0].click();", submit);
time.sleep(3) 
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
submit = driver.find_element_by_id('wd-FacetValue-CheckBox-jobFamilyGroup::8b618a30e00f01c7277572e8143f8b25-input')
driver.execute_script("arguments[0].click();", submit);
time.sleep(3) 
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
totals = int(soup.find('span', {'class' : 'gwt-InlineLabel WMNO WNNO'}).text.split(" ")[0])
nopa = totals//50
while nopa > 0:
    elementer = driver.find_element_by_xpath("//div[@class='WAOO WENO']")
    driver.execute_script("window.scrollTo(0, arguments[0].scrollHeight);", elementer);
    time.sleep(2)
    driver.execute_script("window.scrollTo(0,0);");
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    nopa -= 1
count = 0
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
print("Working on it ", end='')
jono = 1
job_profiles = soup.find_all('li', {'class' : 'WP4F WBPO WAAB WGAG'})
for job_profile in job_profiles :
    a = job_profile.find('div', {'class' : 'gwt-Label WACP WJAP'}).text
    if (not re.search("Senior",a)) and (not re.search("Manager",a)) and (not re.search("II",a)) and (not re.search("2",a)) and (not re.search("Lead",a)):
        boeingOpenings.append({"Serial":jono,"Title":a,"ID":job_profile.find('span', {'class' : 'gwt-InlineLabel WDAG WC5F'}).text.split(' | ')[1].split(',')[0],"Location":job_profile.find('span', {'class' : 'gwt-InlineLabel WDAG WC5F'}).text.split(' | ')[0].split('- ')[1].split(',')[0],"Posted":job_profile.find('span', {'class' : 'gwt-InlineLabel WDAG WC5F'}).text.split(' | ')[2].split("Posted ")[1]})
        jono += 1
    count = count + 1
    print('.',end='')
print()
print("Boeing Openings Updated")
boeingOpeningsTotal = jono
totalOpenings += boeingOpeningsTotal
# Finastra - Software Development Engineer Job Search
global finastraOpeningsTotal
global finastraOpenings
finastraOpeningsTotal = 0
finastraOpenings = []
url = "https://dh.wd3.myworkdayjobs.com/DHC/jobs"
driver.get(url) 
print('Updating Finastra Openings', end='')
for i in range(10):
    print(".",end='')
    time.sleep(1) 
print()
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
ids = ['wd-FacetValue-CheckBox-jobFamilyGroup::074628e3389f10fa1c9fcbe9095e2186-input','wd-FacetValue-CheckBox-jobFamilyGroup::074628e3389f10fa1c9f02dbb77b2162-input','wd-FacetValue-CheckBox-locations::8061b46e841701674a93fa087a40597d-input','wd-FacetValue-CheckBox-locations::9ab6e37cf0b510c4241704726a7e106e-input','wd-FacetValue-CheckBox-locations::9883965210a71070ff94dc364880e8fa-input']
for eid in ids:
    submit = driver.find_element_by_id(eid)
    driver.execute_script("arguments[0].click();", submit);
    time.sleep(3) 
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
totals = int(soup.find('span', {'class' : 'gwt-InlineLabel WMNO WNNO'}).text.split(" ")[0])
nopa = totals//50
while nopa > 0:
    elementer = driver.find_element_by_xpath("//div[@class='WAOO WENO']")
    driver.execute_script("window.scrollTo(0, arguments[0].scrollHeight);", elementer);
    time.sleep(2)
    driver.execute_script("window.scrollTo(0,0);");
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    nopa -= 1
count = 0
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
print("Working on it ", end='')
jono = 1
job_profiles = soup.find_all('li', {'class' : 'WP4F WBPO WAAB WGAG'})
for job_profile in job_profiles :
    a = job_profile.find('div', {'class' : 'gwt-Label WACP WJAP'}).text
    if (not re.search("Senior",a)) and (not re.search("Manager",a)) and (not re.search("II",a)) and (not re.search("2",a)) and (not re.search("Lead",a)):
        finastraOpenings.append({"Serial":jono,"Title":a,"Location":job_profile.find('span', {'class' : 'gwt-InlineLabel WDAG WC5F'}).text.split(' | ')[1].split(',')[0],"ID":job_profile.find('span', {'class' : 'gwt-InlineLabel WDAG WC5F'}).text.split(' | ')[0],"Posted":job_profile.find('span', {'class' : 'gwt-InlineLabel WDAG WC5F'}).text.split(' | ')[2].split("Posted ")[1]})
        jono += 1
    count = count + 1
    print('.',end='')
print()
print("Finastra Openings Updated")
finastraOpeningsTotal = jono
totalOpenings += finastraOpeningsTotal
# PayPal - Software Development Engineer Job Search
global paypalOpeningsTotal
global paypalOpenings
paypalOpeningsTotal = 0
paypalOpenings = []
url = "https://wd1.myworkdaysite.com/recruiting/paypal/jobs"
driver.get(url) 
print('Updating PayPal Openings', end='')
for i in range(10):
    print(".",end='')
    time.sleep(1) 
print()
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
ids = ['wd-FacetValue-CheckBox-jobFamilyGroup::faedd7c80dd5102a1e369f8dcda9ca60-input','wd-FacetValue-CheckBox-jobFamilyGroup::faedd7c80dd5102a1e3685d24992ca28-input','wd-FacetValue-CheckBox-jobFamilies::faedd7c80dd5102a1d99b3904b1de931-input','wd-FacetValue-CheckBox-jobFamilies::faedd7c80dd5102a1d99f311e73ae967-input','wd-FacetValue-CheckBox-jobFamilies::14928883eae20143118338bc6501c004-input','wd-FacetValue-CheckBox-jobFamilies::18f4ea36abe801dc71e5e3846501ed03-input','wd-FacetValue-CheckBox-jobFamilies::faedd7c80dd5102a1d99bd84478de939-input','wd-FacetValue-CheckBox-jobFamilies::8ca194056bf1016bf003108a65014a02-input','wd-FacetValue-CheckBox-locations::bcdc9518960a0115db738aaa2d241899-input','wd-FacetValue-CheckBox-locations::bcdc9518960a01a46ac477aa2d240c99-input','wd-FacetValue-CheckBox-locations::bcdc9518960a01d7641b93ac2d246c9a-input','wd-FacetValue-CheckBox-locations::bcdc9518960a0124bac97daa2d241099-input']
for eid in ids:
    submit = driver.find_element_by_id(eid)
    driver.execute_script("arguments[0].click();", submit);
    time.sleep(3) 
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
totals = int(soup.find('span', {'class' : 'gwt-InlineLabel WMNO WNNO'}).text.split(" ")[0])
nopa = totals//50
while nopa > 0:
    elementer = driver.find_element_by_xpath("//div[@class='WAOO WENO']")
    driver.execute_script("window.scrollTo(0, arguments[0].scrollHeight);", elementer);
    time.sleep(2)
    driver.execute_script("window.scrollTo(0,0);");
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    nopa -= 1
count = 0
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
print("Working on it ", end='')
jono = 1
job_profiles = soup.find_all('li', {'class' : 'WP4F WBPO WAAB WGAG'})
for job_profile in job_profiles :
    a = job_profile.find('div', {'class' : 'gwt-Label WACP WJAP'}).text
    if (not re.search("Senior",a)) and (not re.search("Manager",a)) and (not re.search("II",a)) and (not re.search("2",a)) and (not re.search("Lead",a)) and (not re.search("3",a)):
        paypalOpenings.append({"Serial":jono,"Title":a,"Location":job_profile.find('span', {'class' : 'gwt-InlineLabel WDAG WC5F'}).text.split(' | ')[1].split(',')[0],"ID":job_profile.find('span', {'class' : 'gwt-InlineLabel WDAG WC5F'}).text.split(' | ')[0],"Posted":job_profile.find('span', {'class' : 'gwt-InlineLabel WDAG WC5F'}).text.split(' | ')[2].split("Posted ")[1]})
        jono += 1
    count = count + 1
    print('.',end='')
driver.close()
print()
print("PayPal Openings Updated")
paypalOpeningsTotal = jono
totalOpenings += paypalOpeningsTotal
global tottime
tottime = (time.time() - starttime)//60
print(tottime)
newContent = "\n" + "var totjob = "+ str(totalOpenings) + ";" + "\n"  + "var amazonapp = "+ str(amazonOpenings) + "\n" + "var linkedinapp = "+ str(hotstarOpenings) + "\n" + "var dellapp = "+ str(dellOpenings) + "\n" + "var adobeapp = "+ str(adobeOpenings) + "\n" + "var masterapp = "+ str(masterOpenings) + "\n" + "var reuterapp = "+ str(reuterOpenings) + "\n" + "var boeingapp = "+ str(boeingOpenings) + "\n" + "var paypalapp = "+ str(paypalOpenings) + "\n" + "var finastraapp = "+ str(finastraOpenings) + "\n" + "var honeyapp = "+ str(fbOpenings) + "\n" + "var naukritapp = "+ str(twitterOpenings) + "\n"  + "var amazoncon = "+ str(amazonOpeningsTotal) + "\n" + "var linkedincon = "+ str(hotstarOpeningsTotal) + "\n" + "var dellcon = "+ str(dellOpeningsTotal) + "\n" + "var adobecon = "+ str(adobeOpeningsTotal) + "\n" + "var mastercon = "+ str(masterOpeningsTotal) + "\n" + "var reutercon = "+ str(reuterOpeningsTotal) + "\n" + "var boeingcon = "+ str(boeingOpeningsTotal) + "\n" + "var paypalcon = "+ str(paypalOpeningsTotal) + "\n" + "var finastracon = "+ str(finastraOpeningsTotal) + "\n" + "var honeycon = "+ str(fbOpeningsTotal) + "\n" + "var naukritcon = "+ str(twitterOpeningsTotal) + "\n"
with open("display/jse.html", encoding="utf-8") as inf:
    txt = inf.read()
    soup = BeautifulSoup(txt, "html.parser")
a = soup.find("script", {"class":"contentInput"})
a.clear()
a.append(newContent)
with open("display/jse.html", "w", encoding="utf-8") as outf:
    outf.write(str(soup))
url = "file:///E:/Projects/jobApplictionsTracker/display/jse.html"
jores.get(url)
jores.maximize_window() 