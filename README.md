# News-keyword generator for news downloaded from g0v #

## Requirement ##

* python 3.6
* jieba package
* tqdm package

## How to use ##

### `DataFetcher.py` ###

#### Purpose ####

Download zipped news in `.gz` format form g0v's site.

#### Command ####

Directly execute it by command: `python DataFetcher` under source directory

#### Output ####

then sub-directory `/news` will be created and news from g0v will be downloaded there.

* Configure: Change `zipped_start_date` and `zipped_end_date` will change interval of news should be downloaded.

### `JsonAnalyzer.py` ###

#### Purpose ####
1. Convert original file from g0v to pure json format
2. Fetch keyword from each news

#### Command ####

Directly execute it by command: `python JsonAnalyzer.py` under source directory.

#### Output ####

1. sub-directory `/converted_news` will be created.

2. Then news in `/news` will be

      1. appended unique `article_id`
      2. converted to format of pure json
      3. used to fetch keywords

3. Finally, under `/converted_news`,

    1. json format news will be saved with name `{date}-article.json`
    2. json format keywords will be saved with name `{date}-keyword.json`.
    3. if any line of news in json string in original file invalid, they will be caught and write in `{date}-invalid.txt`
