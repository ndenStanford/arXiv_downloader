# ArXiv Paper Downloader

This code downloads papers in parellel from ArXiv given search parameters. The papers are saved in the pdf format. The script used the [ArXiv API](https://arxiv.org/help/api) to access the database. The code is written in Python3. 

## Disclaimer
Large number of papers downloading is prohibited. Please see [ArXiv API rules](https://arxiv.org/help/api/tou). In addition, using a third-party scaper (such as Scrapy library) to download papers from ArXiv is strictly prohibited. Please see the [ArXiv site rule](https://arxiv.org/help/robots)  


## Installation

1. Create a virtualenv -  [How to create virtualenv](https://docs.python.org/3/tutorial/venv.html)
2. Activate the virtualenv - 'source path/to/bin/activate'
3. Run 'pip install -r requirements.txt'

## Running 
After crating virtual environment, clone this repo and run: 

```
python arXiv_pdf_downloader.py --search <searchQuery> --search_by <searchBy> --sort_by <sortBy> --max_result <maxResult> --folder_name<folderName>
```

## Quary parameters
Query parameters are defined below

* searchQuery: Search query, could be any string
* searchBy: Seach by, choose one from 
    * 'ti': Title
	* 'au': Author
	* 'abs': Abstract
	* 'co': Comment
	* 'jr': Journal Reference
	* 'cat': Subject Category
	* 'rn': Report Number
	* 'all': All of the above 
* sortBy: Parameter to use for sorting, choose one from 
	* 'relevance'
	* 'lastUpdatedDate'
	* 'submittedDate'
* maxResult: Number of requested paper. It is possible to receive papers less than requested number is not enough papers matched with the query.
* folderName: Name of the folder where downloaded paper will be stored

Example of valid parameters and format:

* searchQuery: 'nlp transformer'
* searchBy: 'all'
* sortBy: 'relevance'
* maxResult: 5
* folderName: 'arXiv papers'







