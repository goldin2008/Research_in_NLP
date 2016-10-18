from bs4 import BeautifulSoup
import json
import os
import pandas as pd
import re
import requests
import subprocess
import time


def down_paper(base_url ,index_url):
    r = requests.get(index_url)

    soup = BeautifulSoup(r.content)

    # Find and Get all div within div whose id = "searchResults"
    con = soup.find("div", {"id": "normal-search-results"})
    # Find and Get all div whose class = "acsBorder"
    mydivs = con.findAll("div", { "class" : "cit-extra" })
    mytitle = con.findAll("div", { "class" : "cit-metadata" })
    
    
    paper_links =  list()
    title_list = list()
    abstract_links = list()


    for title in mytitle:
        t = title.findAll("span", { "class" : "cit-title" }) # findAll() return lists
        title_list.append(t[0].text) # Get title of the paper
    
    for div in mydivs:

        for link in div.find_all('a'):  # find_all() is a new name of the method, but it is exactly the same as findAll() method
            for link in div.find_all('a'):
                if '.pdf' in link["href"]:
                    href = link["href"]
                    l = re.findall('(\S*full.pdf)', href)
                    if l[0] not in paper_links:
                        paper_links.append(l[0])    # Get link of the paper




    print("%d Papers Found" % len(paper_links))


    '''
    Download Papers in the paper_links
    '''
    for link in paper_links:
        index =  paper_links.index(link)
        paper_title = title_list[index]
        pdf_link = base_url + link
        
        if len(paper_title)>140:
            paper_title = paper_title[:140]
        
        pdf_name = paper_title + ".pdf"
        
#        print pdf_name
        
        # skip if the pdf_name has / which means subfolder
        if '/' in pdf_name:
            print '############'
            continue
        
        # Download papers
        pdf = requests.get(pdf_link)
        pdf_path = os.path.join("output", "pdfs", pdf_name)
        pdf_file = open(pdf_path, "wb")
        pdf_file.write(pdf.content)
        pdf_file.close()
        # print paper_title + '\n'

    '''
    Find next page if it exists
    '''
    # Find and Get all div within div whose id = "searchResults"
    next_pages_con = soup.findAll("a", { "class" : "next-results-link" })
    
    if next_pages_con:
        next_page = next_pages_con[0]["href"]
        print next_page
        return next_page
    else:
        print
        return


    

    

def main():

    base_url  = "http://www.jswconline.org"
    url = "http://www.jswconline.org/search?hits=80&submit=yes&submit=Go&submit=Go&sortspec=relevance&format=standard&y=11&fulltext=Soil%20Quality%3B%20Soil%20Management%3B%20Dynamic%20Soil%20Properties%3B%20Soil%20Health&x=16&FIRSTINDEX=160"
    
    
    start = time.time()

    next_page = down_paper(base_url, url)
    # print next_page

    while next_page:
        new_url = base_url + next_page
        next_page = down_paper(base_url, new_url)
        # print next_page


    end = time.time()
    cost = end - start
    hour = int(cost)/3600
    min = int(cost)%3600 / 60
    sec = int(cost)%3600 % 60
    print 'Journal of Soil and Water Conservation'
    print 'Cost Time = %d hour %d min %d sec'  % (hour, min, sec)

    return 0

if __name__ == "__main__":
    main()
