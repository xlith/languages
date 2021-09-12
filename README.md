# Languages list
[![Process Application](https://github.com/xlith/languages/actions/workflows/process.yml/badge.svg?branch=main)](https://github.com/xlith/languages/actions/workflows/process.yml)

This repo contains lists of languages with ISO codes. 
In the lists, you can find languages names in English, French, Chinese, Russian, and German along with their own native language. 
There is also the language family. 

These lists are created using Wikipedia pages https://en.wikipedia.org/wiki/Lists_of_languages. And repo pulls the data again every week using GitHub actions. 


## Current Formats
Current available formats: 
* csv [Latest version](https://github.com/xlith/languages/releases/latest/download/languages.csv)
* xml [Latest version](https://github.com/xlith/languages/releases/latest/download/languages.xml)
* json [Latest version](https://github.com/xlith/languages/releases/latest/download/languages.json)
* sqlite [Latest version](https://github.com/xlith/languages/releases/latest/download/languages.sqlite3.db)
* sql (insert statements) [Latest version](https://github.com/xlith/languages/releases/latest/download/languages.sql)

## How to access files

- You can always download the file you like. Just use the links below. They are the latest release. 
  
- You can clone this repo using terminal and use any of the file as you like. 

  > `git clone -b main --single-branch --depth 1 https://github.com/xlith/languages.git`

- You can use raw files directly from github
  * csv [Raw File](https://raw.githubusercontent.com/xlith/languages/main/languages.csv)
  * xml [Raw File](https://raw.githubusercontent.com/xlith/languages/main/languages.xml)
  * json [Raw File](https://raw.githubusercontent.com/xlith/languages/main/languages.json)
  * sqlite [Raw File](https://raw.githubusercontent.com/xlith/languages/main/languages.sqlite3.db)
  * sql (insert statements) [Raw File](https://raw.githubusercontent.com/xlith/languages/main/languages.sql)
  
- You can review versions and download from releases of this repo
  * https://github.com/xlith/languages/releases

## Additional information
  * If you look at the Wikipedia lists you will notice there are many more languages there but I filtered only the ones that have two-letter code. They are the ones that are used most.
  * Release tags are the dates that data is pulled from Wikipedia.
  * I use a very simple python script to pull and format the data. If you like want to have a look, you can find the script under the process folder. 
  * If you need additional format you can open an issue. I will try to add it as soon as I can. You can always get your hands dirty and contribute of course. Just clone the repo and open a pull request. 
