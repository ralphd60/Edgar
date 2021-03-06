from CreateDetailFile import detail_file as dfile

import requests
from bs4 import BeautifulSoup


def get_details(url, filename, count):
    """using the request module, this will retrieve a sudo html list of the files in the director
    it will then use the Beautiful soup module to format the returned data into better formed html
    thrn filter snd return the file  list."""

    # create response object
    r = requests.get(url + filename)

    # create beautiful-soup object
    soup = BeautifulSoup(r.content, "xml")

    count = dfile(soup, filename, count)
    return count
# used to test
# get_details('https://www.sec.gov/Archives/','edgar/data/702165/0001225208-18-006528.txt', 0)
# get_details('https://www.sec.gov/Archives/','edgar/data/702165/0001225208-18-000220.txt',0)