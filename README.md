# how to run the code?
```pip install -r requirements.txt
python .\script.py
python .\script2.py
```
# your results will be saved in result.csv and result2.csv


# The problem states that we need to get all the product name, price, url, description of different products on the Amazon page.

What is web scrapping?
- In web scrapping we read data from website and extract the useful data that we need, and put it in organized format like CSV, Excel, XML or JSON
- Unorganized and useless website data to organized and useful data in csv xl or json

Which Technology to use to solve this problem?

For opening and reading data from a website we have different web scrapping libraries in python:
- Beautiful soup
- Scrappy
- Requests
- Selenium
- and many many more

For putting the data into csv file we can use built in or external libraries:
- csv
- pandas
- file

For now we will use Selenium and pandas to solve this problem.