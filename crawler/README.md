# Crawler for Specific Subfields of Papers in arXiv
You can crawl papers' titles and abstracts in the subfields which you chosed.
## Requirements
Install these libraries in your local.\
```npm i puppeteer```\
```npm i -S fast-csv```

 

## How To Run
You have to run ```crawl_on_arXiv.js``` file with three command line arguments.
1. Which subfield do you want to crawl (You can find abbreviation of subfields [here](data/categories.json)) 
2. Which index do you want to start crawling
3. Which index do you want to stop

### Example
``` node .\crawl_on_arXiv.js cs.cl 0 1000 ``` this run will give you the first 1000 papers' titles and abstracts about Computer Language which is subfield of Computer Science.
