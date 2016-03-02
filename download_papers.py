from bs4 import BeautifulSoup
import json
import os
import pandas as pd
import re
import requests
import subprocess


# base_url  = "http://papers.nips.cc"
# index_url = "http://papers.nips.cc/book/advances-in-neural-information-processing-systems-28-2015"

base_url  = "https://dl.sciencesocieties.org"
index_url =  "https://dl.sciencesocieties.org/publications/search?searchTab=&doi=&search%5B0%5D=soil+quality+conservation+management&searchType%5B0%5D=Manual&year=&volume=&issue=&first-page=&citation-year=&citation-volume=&citation-first-page=&num-results=100&sort=relevance&stem=false&open-access=false&searchTab=&start=101"

r = requests.get(index_url)

soup = BeautifulSoup(r.content)
# print 'soup = ', soup
# fout = open('output.txt', 'w')
# fout.write(str(soup))
# fout.close()

# Find and Get all div within div whose id = "searchResults"
con = soup.find("div", {"id": "searchResults"})
# Find and Get all div whose class = "acsBorder"
mydivs = con.findAll("div", { "class" : "acsBorder" })

# print mydivs

paper_links =  list()
title_list = list()
abstract_links = list()


# For each div, get pdf link
count = 1
fout = open('papers.txt', 'wb')

for div in mydivs:
    # print div.text[0]
    if div.text[0] != 'J':  # Check if it is Journal
        continue

    # print div.text[0]
    # print div.find_all('a')
    # title = div.findAll("search:title")
    # print div.findAll("search:title")[0].text
    title = div.find_all("search:title")[0].text.rstrip() # findAll() return lists
    title_list.append(title)    # Get title of the paper

    # # Output title of paper to a text file
    # fout.write('No. ' + str(count) + '  ' + title + '\n\n')
    # count = count + 1

    for link in div.find_all('a'):  # find_all() is a new name of the method, but it is exactly the same as findAll() method
        # print link.text
        # print type(link)
        if 'pdfs' in link["href"]:
            paper_links.append(link)    # Get link of the paper

        if 'abstracts' in link["href"]:
            abstract_links.append(link)

# fout.close()

# for div in mydivs:
#     # print div.find_all('a')
#     for link in div.find_all('a'):
#         # print link.text
#         # print type(link)
#         paper_links.append(link)

# paper_links = [link for link in soup.find_all('a') if link["href"][:7]=="/paper/"]

# print 'paper_links: ', paper_links
# print 'title_list: ', title_list
# print 'abstract_links:', abstract_links

print("%d Papers Found" % len(paper_links))

nips_authors = set()
papers = list()
paper_authors = list()

temp_path = os.path.join("output", "temp.txt")

def text_from_pdf(pdf_path, temp_path):
    if os.path.exists(temp_path):
        os.remove(temp_path)
    subprocess.call(["pdftotext", pdf_path, temp_path])
    f = open(temp_path)
    text = f.read()
    f.close()
    os.remove(temp_path)
    return text

#for link in paper_links[:5]:
for link in paper_links:
    # paper_title = link.contents[0]
    # info_link = base_url + link["href"]
    # pdf_link = info_link + ".pdf"
    # pdf_name = link["href"][7:] + ".pdf"
    # paper_id = re.findall(r"^(\d+)-", pdf_name)[0]

    index =  paper_links.index(link)
    paper_title = title_list[index]
    pdf_link = base_url + link["href"]
    pdf_name = paper_title[:35] + ".pdf"

    # Download papers
    pdf = requests.get(pdf_link)
    pdf_path = os.path.join("output", "pdfs", pdf_name)
    pdf_file = open(pdf_path, "wb")
    pdf_file.write(pdf.content)
    pdf_file.close()
    print paper_title + '\n'

    # Output title of paper to a text file
    # fout.write('No. ' + str(count) + '  ' + paper_title + '\n\n')
    # count = count + 1

    # paper_soup = BeautifulSoup(requests.get(info_link).content)
    # abstract = paper_soup.find('p', attrs={"class": "abstract"}).contents[0]
    # authors = [(re.findall(r"-(\d+)$", author.contents[0]["href"])[0],
    #             author.contents[0].contents[0])
    #            for author in paper_soup.find_all('li', attrs={"class": "author"})]
    # for author in authors:
    #     nips_authors.add(author)
    #     paper_authors.append([len(paper_authors)+1, paper_id, author[0]])
    # event_types = [h.contents[0][23:] for h in paper_soup.find_all('h3') if h.contents[0][:22]=="Conference Event Type:"]
    # if len(event_types) != 1:
    #     print(event_types)
    #     print([h.contents for h in paper_soup.find_all('h3')])
    #     raise Exception("Bad Event Data")
    # event_type = event_types[0]
    # paper_text = text_from_pdf(pdf_path, temp_path)
    # print(paper_title)
    # papers.append([paper_id, paper_title, event_type, pdf_name, abstract, paper_text])

# pd.DataFrame(list(nips_authors), columns=["Id","Name"]).to_csv("output/Authors.csv", index=False)
# pd.DataFrame(papers, columns=["Id", "Title", "EventType", "PdfName", "Abstract", "PaperText"]).to_csv("output/Papers.csv", index=False)
# pd.DataFrame(paper_authors, columns=["Id", "PaperId", "AuthorId"]).to_csv("output/PaperAuthors.csv", index=False)

# fout.close()
