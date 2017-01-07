from bs4 import BeautifulSoup
import requests
import time
from multiprocessing import Pool
from 分级A import chanel_list
from page_parsing import get_links_from

def get_all_link_from(channel):
    for num in range (1,5):
        get_links_from(channel,num)
if __name__== '__main__':
    pool = Pool()
    pool.map(get_all_link_from,chanel_list.split())
