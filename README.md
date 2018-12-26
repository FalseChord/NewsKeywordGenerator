# News-keyword generator for news downloaded from g0v #

## Requirement ##

* python3.6
* jieba package

## How to use ##

1. `DataFetcher.py`

   Directly execute it by command: `python DataFetcher` under source directory, then sub-directory `/news` will be created and news from g0v will be downloaded there.

   * Configure: Change `zipped_start_date` and `zipped_end_date` will change interval of news should be downloaded.

2. `JsonAnalyzer.py`

   Directly execute it by command: `python JsonAnalyzer.py` under source directory, then sub-directory `/converted_news` will be created.

   Then news in `/news` will be

   1. append unique `article_id`
   2. converted to format of pure json
   3. fetched keywords

   Finally, json format news and keywords will be saved under `/converted_news` with name `{date}-article.json` and `{date}-keyword.json`.
