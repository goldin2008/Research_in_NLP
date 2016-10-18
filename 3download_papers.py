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
#    con = soup.find("main", {"id": "mainContent"})
    # Find and Get all div whose class = "acsBorder"
    mytitle = soup.findAll("a", { "class" : "title" })
    mydivs = soup.findAll("a", { "class" : "webtrekk-track pdf-link" })
    


    
    paper_links =  list()
    title_list = list()
    abstract_links = list()


    for title in mytitle:
#        print title.text
        title_list.append(title.text)
    
##        print 'before ', title
#        if not title.find_all('a'):
#            title = title.find_all('h3')[0].text
#            title_list.append(title) # Get title of the paper
#        
#        else:
#            title = title.find_all('a')[0].text
##            print 'after ', title
#            t = re.findall('SR[0-9]+[0-9](.*)$', title) # findAll() return lists
#            title_list.append(t[0]) # Get title of the paper



    
    for div in mydivs:
#        print div["href"]
        paper_links.append(div["href"])    # Get link of the paper

#        for link in div.find_all('a'):  # find_all() is a new name of the method, but it is exactly the same as findAll() method
#            for link in div.find_all('a'):
##                print link["href"]
#                if '/pdf' in link["href"]:
#                    href = link["href"]
##                    print href
##                    l = re.findall('(\S*full.pdf)', href)
#                    if href not in paper_links:
#                        paper_links.append(href)    # Get link of the paper




    print("%d Papers Found" % len(paper_links))


#    print len(title_list)
#    for t in title_list:
#        print t
#    print len(paper_links)
#    print paper_links
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

#    print len(paper_links)
#    print len(title_list)
#    exit()
    '''
    Find next page if it exists
    '''
    # Find and Get all div within div whose id = "searchResults"
    next_pages_con = soup.findAll("a", { "class" : "next" })
    
    if next_pages_con:
        next_page = next_pages_con[0]["href"]
#        print next_page
        return next_page
    else:
#        print
        return


    

    

def main():

    base_url  = "http://link.springer.com"
    url = "http://link.springer.com/search?search-within=Journal&facet-journal-id=10661&query=Soil+Quality%3B+Soil+Management%3B+Dynamic+Soil+Properties%3B+Soil+Health&showAll=false"

    
    start = time.time()

    next_page = down_paper(base_url, url)
    print next_page
#    exit()

    while next_page:
        new_url = base_url + next_page
        next_page = down_paper(base_url, new_url)
        print next_page


    end = time.time()
    cost = end - start
    hour = int(cost)/3600
    min = int(cost)%3600 / 60
    sec = int(cost)%3600 % 60
    print 'Environmental Monitoring & Assessment'
    print 'Cost Time = %d hour %d min %d sec'  % (hour, min, sec)

    return 0

if __name__ == "__main__":
    main()
