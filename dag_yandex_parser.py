from airflow import DAG 
from airflow.operators.python_operator import PythonOperator 
from datetime import datetime
from time import sleep
import pickle
import re
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
# selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
# waits
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import sqlalchemy as sa 
from airflow.models import Variable



host = Variable.get("host_dm")
login = Variable.get("login_dm")
password = Variable.get("password_dm")

def main():
    postgres_con()
    baza=baza_sql()
    domen_list=parser(baza['сравним ру;256820;'])
    create_dataFrame(domen_list)
    


def baza_sql():
    con=postgres_con()
    query= "SELECT * FROM sravni.baza"
    baza=pd.read_sql(query, con)
    baza.drop('index', axis=1, inplace=True)
    return baza

def load_cookie(browser, path):
    with open(path, 'rb') as cookiesfile:
        cookies = pickle.load(cookiesfile)
        for cookie in cookies:
            print(cookie)
            try:
                browser.add_cookie(cookie) 
            except Exception as e:
                continue


def parser (search_list):
    options = Options()
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
    options.add_argument(f'user-agent={user_agent}')
    options.add_argument("--headless") 
    service=Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=options)
    browser.get('https://ya.ru/search/')
    load_cookie(browser, 'cookies_yan.dat')
    browser.refresh()
    
    queries_list=[]
    
    for d in search_list:    
        u = f'https://yandex.ru/search/?text={d}&rstr=-213&lr=213'
        print(u)
        browser.get(u)
    
        for i in browser.find_elements(By.CLASS_NAME, "serp-item"):
                
          organic__subtitle = i.find_elements(By.CLASS_NAME, 'organic__subtitle')
          serp_url__item = i.find_elements(By.CLASS_NAME, 'serp-url__item')
          
          if organic__subtitle:
            h = organic__subtitle[0].text
            t = 'Ads'

          elif serp_url__item:   
            h = serp_url__item[0].text
            t = 'Organic'
          else:
            continue
                    
          queries_list.append([d,h.split('›')[0],t])
          
    return queries_list


def postgres_con():
    engine = sa.create_engine(f'postgresql://{login}:{password}@{host}/postgres') 
    con=engine.connect()
    return con


def create_dataFrame(data):
    con=postgres_con()
    df = pd.DataFrame(data, columns = ['Request','Domen', "Type"])
    df['Date'] = str(datetime.now())
    df.to_sql(con=con, schema='sravni',if_exists='append', name='sravni_queries')
    con.close()



with DAG(
          dag_id='yandex_parser',
          start_date = datetime(2023, 12, 29),
          schedule_interval='0 20 * * *',
          catchup=False
) as dag:

          parser_yandex = PythonOperator(
                  task_id = 'parser_yandex',
                  python_callable=main
          )
          

parser_yandex