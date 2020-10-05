#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 22:53:25 2020

@author: nutchapoldendumrongsup
"""

import sys
import argparse 
import os
import re
import urllib.request
import urllib
from lxml import etree
from lxml import html
import requests
from concurrent.futures import ThreadPoolExecutor as PoolExecutor


def call_arXiv_API(search_query, search_by, sort_by, max_results, folder_name):
    # Remove space in seach query
    search_query=search_query.strip().replace(" ", "+")
    # Call arXiv API
    arXiv_url='http://export.arxiv.org/api/query?search_query={search_by}:{search_query}&sortBy={sort_by}&start=0&max_results={max_results}'\
        .format(search_by=search_by,search_query=search_query, sort_by=sort_by, max_results=max_results)
    with urllib.request.urlopen(arXiv_url) as url:
        s = url.read()
    
    # Parse the xml data
    root = html.fromstring(s)
    # Fetch relevant pdf information
    pdf_titles=root.xpath("entry/title/text()")
    
    # parse title
    pdf_titles=[re.sub('[^a-zA-Z0-9]', ' ', t) for t in pdf_titles]
    pdf_urls=root.xpath("entry/link[@title='pdf']/@href")
    folder_names=[folder_name]*len(pdf_titles)
    pdf_info=list(zip(pdf_titles, pdf_urls, folder_names))
    
    
    # Check number of available files
    print('requesting {max_results} files'.format(max_results=max_results))
    if len(pdf_urls)<int(max_results):
        matching_pdf_num=len(pdf_urls)
        print('only {matching_pdf_num} files available'.format(matching_pdf_num=matching_pdf_num))
    
    return pdf_info

# Download a single pdf file given the relevant information
def download_pdf(pdf_info):
    pdf_title=pdf_info[0]
    pdf_url=pdf_info[1]
    folder_name=pdf_info[2]
    r = requests.get(pdf_url, allow_redirects=True)
    open(folder_name+'/'+pdf_title+'.pdf', 'wb').write(r.content)

# Download all avaiable requested pdf files in parallel 
def download_pdf_parallel(download_pdf, pdf_info):
    with PoolExecutor(max_workers=4) as executor:
        for _ in executor.map(download_pdf, pdf_info):
            pass     
        
# Wrapper function
def download_arXiv_pdf(search_query, search_by='all', sort_by='relevance', max_results=1, folder_name='fetched_pdf'):
    pdf_info=call_arXiv_API(search_query, search_by, sort_by, max_results, folder_name)
    
    try:
        # Create target Directory
        os.mkdir(folder_name)
        print("Directory " , folder_name ,  " Created ") 
    except FileExistsError:
        print("Directory " , folder_name ,  " already exists. Plese request a different folder name to prevent papers from mixing up")
    
    download_pdf_parallel(download_pdf, pdf_info)
  



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="""
    Use this script to download papers from argXiv. 
    """)
    parser.add_argument("--search", help="Search query")
    parser.add_argument("--search_by", default='all', choices=['ti', 'au', 'abs', 'co', 'jr', 'cat', 'rn', 'all'], help="Search by")
    parser.add_argument("--sort_by", default='relevance', choices=['relevance', 'lastUpdatedDate', 'submittedDate'], help="Sort by")
    parser.add_argument("--max_results", default=1, help="Number of requested papers")
    parser.add_argument("--folder_name", default='fetched_pdf', help="Name of the folder where papers will be stored")
    args=parser.parse_args()
    
    search_query=args.search
    search_by=args.search_by
    sort_by=args.sort_by
    max_results=args.max_results
    folder_name=args.folder_name
    
    try:
        download_arXiv_pdf(search_query, search_by, sort_by, max_results, folder_name)
    except:
        print('Invalid request')


