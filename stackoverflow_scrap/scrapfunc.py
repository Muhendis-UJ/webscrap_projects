from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as bs

# Functions for getting URL data
#--------------------------------------------------------------------#
# url is website link 
# ftype is lxml or html.parser
def get_urldata(url, ftype):
    req = Request(url)
    webpage = urlopen(req).read()
    webpage_data = bs(webpage, ftype)
    return webpage_data

def get_urldata_wh(url, ftype):
    req = Request(url , headers={'User-Agent': \
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A'})
    webpage = urlopen(req).read()
    webpage_data = bs(webpage, ftype)
    return webpage_data
#--------------------------------------------------------------------#

# Functions for getting searched tag data in text form
#--------------------------------------------------------------------#
#urldata is BeautifulSoup object
#mytag is tag you want to search in webpage
#myclass is class you want to search in webpage
def get_tagdata(urldata, mytag, myclass):
    a = []
    for a_tag in urldata.find_all(mytag, { 'class' : myclass}):
        a.append(a_tag.text.strip())
    return a
#--------------------------------------------------------------------#