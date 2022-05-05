import pandas as pd
from selenium import webdriver
import time
import pandas as pd
from selenium import  webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
import random as ra
import warnings
warnings.filterwarnings('ignore')

data_wakad=pd.read_csv('wakad_data.csv')

from selenium import webdriver
import time
tm1=[1,1.5,2]
tm2=[0.5,1.1,1.6]

driver = webdriver.Edge(EdgeChromiumDriverManager().install())
# driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
url ='https://housing.com/'
driver.get(url)
time.sleep(3)
all_data=[]
for i in range(len(data_wakad)):
    
    # if i>787:
        
        driver.execute_script("window.open('');")
        time.sleep(ra.choice(tm1))
        driver.switch_to.window(driver.window_handles[1])
        driver.get(data_wakad['Link'][i])
        time.sleep(ra.choice(tm1))
        #for clicking got it button
        try:
            driver.find_element_by_xpath('//*[@id="innerApp"]/div[3]/div[1]/div/button').click()
            time.sleep(ra.choice(tm2))
            print('=====OK GOT IT=====')
        except:
            pass
        
        try:
            project_name=driver.find_element_by_css_selector('.css-js5v7e').text
            print('==project name==')
        except:
            project_name='NA'
        print('************OVERVIEW*********')
        try:
            overview=driver.find_element_by_tag_name('tbody').text
            print('===overview is scraped====')
        except:
            print('===overview is not scraped====')
            overview='NA'           
        time.sleep(ra.choice(tm2))    
        print('*******AMENITIES*************')
        try:
            x=driver.find_elements_by_xpath("//*[text()='Society Amenities']")
            x[0].click()
            time.sleep(ra.choice(tm1))
            print('======society amenity tab clicked=========')
            x=driver.find_elements_by_css_selector(".more.css-1y593mk")
            x[1].click()
            time.sleep(ra.choice(tm1))
            print('=====full page society amenities clicked=====')

            try:
                p=driver.find_elements_by_css_selector('.item-container.css-ck1qbr')
                amenities=p[1].text
            except:
                pass
                  
        except:
            try:
                driver.find_element_by_xpath("//*[text()='Amenities']").click()
                time.sleep(ra.choice(tm1))
                print('======amenity tab clicked=========')
            except:
                pass
            try:
                driver.find_element_by_css_selector(".more.css-1y593mk").click()
                time.sleep(ra.choice(tm1))
                print('=====full page amenities clicked=====')
            except:
                print('=====full page amenities not clicked===')
            try:
                amenities=driver.find_element_by_css_selector('.item-container.css-ck1qbr').text
            except:
                amenities='NA'
                print('=====amenity tab unclicked=====')
        time.sleep(ra.choice(tm2))
        try:
            brokerage=driver.find_element_by_css_selector('.css-1snadjo').text
            print('===Zero Brokerage===')
        except:
            brokerage='NA'
            
        try:
            l=driver.find_elements_by_css_selector('.css-w788ou')
            price_trend=l[1].text
            print('==price_trend_scraped==')
        except:
            price_trend='NA'
        print('*****LOCALITY******')
        try:
            
            try:
                driver.find_element_by_xpath("//*[text()='Locality']").click()
                time.sleep(ra.choice(tm2))
                print('==locality tab clicked==')
            except:
                driver.find_element_by_xpath("//*[text()='LOCALITY']").click()
                time.slee(ra.choice(tm2))
                print('==locality tab clicked==')
                

                #commute
            try:
                driver.find_element_by_css_selector('.css-1mteyrv').click()
                time.sleep(ra.choice(tm2))
                print('===commute tab clicked==')
                try:
                    driver.find_element_by_xpath("//*[text()='Bus']").click()
                    time.sleep(ra.choice(tm2))
                    print('===bus clicked===')
                    Bus_station=driver.find_element_by_css_selector('.css-1upwzlz').text 
                except:
                    Bus_station='NA'
                    print('==bus NOT clicked')
                try:
                    driver.find_element_by_xpath("//*[text()='Railway']").click()
                    time.sleep(ra.choice(tm2))
                    print('==railway clicked==')
                    railway_station=driver.find_element_by_css_selector('.css-1upwzlz').text
                except:
                    railway_station='NA'
                    print('==railway NOT clicked==')
                try:
                    driver.find_element_by_xpath("//*[text()='Airport']").click()
                    time.sleep(ra.choice(tm2))
                    print('==airport clicked==')
                    airport=driver.find_element_by_css_selector('.css-1upwzlz').text
                except:
                    airport='NA'
                    print('==airport NOT clicked==')
                        
            except:
                print('===commute tab NOT clicked===')
                
                # Bank
            try:
                driver.find_element_by_css_selector('.css-114rjcj').click()
                time.sleep(ra.choice(tm2))
                print('==bank clicked==')
                bank=driver.find_element_by_css_selector('.css-1upwzlz').text
            except:
                bank='NA'
                print('==bank NOT clicked==')
                #cinema
            try:
                driver.find_element_by_css_selector('.css-12afihm').click()
                time.sleep(ra.choice(tm2))
                print('==cinema clicked==')
                cinema=driver.find_element_by_css_selector('.css-1upwzlz').text
            except:
                cinema='NA'
                print('==cinema NOT clicked')
                
                # restaurant and bar
            try:
                driver.find_element_by_css_selector('.css-v50rdr').click()
                time.sleep(ra.choice(tm2))
                print('===restaurant and food tab clicked===')
                    
                try:
                    driver.find_element_by_xpath("//*[text()='Restaurant']").click()
                    time.sleep(ra.choice(tm2))
                    print('==restaurant clicked==')
                    restaurant=driver.find_element_by_css_selector('.css-1upwzlz').text
                except:
                    restaurant='NA'
                    print('==restaurant NOT clicked==')
                try:
                    driver.find_element_by_xpath("//*[text()='Bar']").click()
                    time.sleep(ra.choice(tm2))
                    print('==bar clicked==')
                    bar=driver.find_element_by_css_selector('.css-1upwzlz').text
                except:
                    bar='NA'
                    print('==bar NOT clicked==')
                                               
            except:
                print('===restaurant and food tab NOT clicked==')
            #groceries
            try:
                driver.find_element_by_css_selector('.css-vgf4g3').click()
                time.sleep(ra.choice(tm2))
                print('==groceries clicked==')
                groceries=driver.find_element_by_css_selector('.css-1upwzlz').text
            except:
                groceries='NA'
                print('==groceries NOT clicked==')
            #healthcare    
            try:
                driver.find_element_by_css_selector('.css-hiwk2n').click()
                time.sleep(ra.choice(tm2))
                print('==healthcare clicked==')
                healthcare=driver.find_element_by_css_selector('.css-1upwzlz').text
            except:
                healthcare='NA'
                print('==healthcare NOT clicked==')
            #park
            try:
                driver.find_element_by_css_selector('.css-1p8xxr').click()
                time.sleep(ra.choice(tm2))
                print('===park clicked==')
                park=driver.find_element_by_css_selector('.css-1upwzlz').text
            except:
                park='NA'
                print('==park NOT clicked')
            #shopping mall
            try:
                driver.find_element_by_css_selector('.css-hth6yn').click()
                time.sleep(ra.choice(tm2))
                print('==shopping mall clicked==')
                mall=driver.find_element_by_css_selector('.css-1upwzlz').text
            except:
                mall='NA'
                print('==shopping mall NOT clicked==')
                    
                         
        except:
            print('===could not clicked lacality tab===')       
                
                
                
        housing_detail={'overview':overview,'amenity':amenities,'Brokerage_status':brokerage,'price_trend':price_trend,
                      'bus':Bus_station,'railway':railway_station,'airport':airport,'bank':bank,'cinema':cinema,
                       'restaurant':restaurant,'bar':bar,'grocery':groceries,'healthcare':healthcare,'park':park,'mall':mall,
                      'project_name':project_name }
        all_data.append(housing_detail)
        df=pd.DataFrame(all_data)
        print('data_scraped_upto_link_no_'+str(i))
        df.to_csv('wakad_ext_data.csv')
        print("==== Data Saved ====")
        driver.close()
        time.sleep(ra.choice(tm2))
        driver.switch_to.window(driver.window_handles[0])
    # else:
    #     print('==kuchhh to gadbad hai dayaaaa==')