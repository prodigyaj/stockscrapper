from config import *
import bs4
import subprocess
import sys
from random import randint
import time

#filename = "cached/"+sys.argv[1]
log_file = open("log.txt","w")

def bePolite(should_i,random = 2):
    if should_i == True:
        randseed = randint(1,random)
        time.sleep(randseed)

def read_web(url):
    try:
        phantom_call = PHANTOM_JS_BIN+"phantomjs"
        jsengine = "jsengine.js"
        final_call = phantom_call+" "+jsengine+" "+url
        print final_call
        #subprocess.call(final_call,shell=True)
        p = subprocess.Popen(final_call,shell=True,stdout=subprocess.PIPE).communicate()[0]
        return p
    except:
        log_file.write("Error reading url: "+url.strip()+'\n')
        return "ERROR"

def parse_content(content):
    try:
        soup = bs4.BeautifulSoup(content)
        stock_name = soup.find("h1", { "class" : "srcompanynametext" })
        stock_current = soup.find("td", { "class" : "tbmainred" })
        return stock_name.text,stock_current.text
    except:
        log_file.write( "Error parsing url: "+url.strip() +'\n')
        return "",""


if __name__ == "__main__":
    url_list = open("url_list.txt","r")
    stockprice_file = open("StockPrice.txt","w")

    for url in url_list:
        print url.strip()
        content = read_web(url.strip())
        #content = read_web("http://www.bseindia.com/stock-share-price/stockreach_financials.aspx?scripcode=500002&expandable=0")
        name,price = parse_content(content)
        if not name or not price:
            stockprice_file.write(name+','+price+','+'error'+'\n')
            print name,price,"error"
        else:
            stockprice_file.write(name+','+price+'\n')
            print name,price
        bePolite(True,3)
