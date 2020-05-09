from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import socket
import sqlite3
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
from flask import Flask
from flask import request

app = Flask(__name__)

#conn.execute('''CREATE TABLE details (id int ,name text);''')


i=1
@app.route('/getInfo')
def getInfo():
    driver = webdriver.Chrome(executable_path=r'C:\Users\jaideep_shinde\Downloads\chromedriver_win32\chromedriver.exe')

    uname=request.args.get('username')
    driver.get("https://github.com/"+uname)
    
    content = driver.page_source
    
    driver.close()

    soup = BeautifulSoup(content)
    s=(soup.title.text).encode('ascii','ignore')


    conn = sqlite3.connect('test.db')
    print "Opened database successfully";

    q="INSERT INTO details values(1,'"+s.split(' ')[0]+"');"
    print q
    conn.execute(q)
    conn.commit()
    cursor = conn.execute("SELECT * from details;")
    for row in cursor:
        print "ID = ", row[0]
        print "NAME = ", row[1]
    return s
if __name__ == '__main__':
    app.run(host=IPAddr)



