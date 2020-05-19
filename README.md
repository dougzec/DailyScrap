# DailyScrap
- Python script to create daily and customized reports.
- This app uses Selenium and Google Chrome.

# Functions implemented
- Amazon product prices (list of URLs)
- Investing.com currencies to BRL (list of currencies)
- Investing.com stocks to BRL (list of stocks)
- Climatempo weather (list cities in the format 'city_number/city_name' as in the city's page URL)

## dailyscrap.py:
- Main code.
- Reads <i>ds_functions.py</i> and <i>ds_personal_functions.py</i> to get the functions and <i>searches.json</i> to get the inputs.

## ds_functions.py:
- All the functions provided by us.
- Function names have to be equal to keys in searches.json eventually used.
- The argument <i>driver</i> has to be used.
- The argument <i>inputs</i> is read from searches.json, so if multiple values (links in Amazon, for example) are expected, make sure to use iterate over this variable, like `for inputs in inputs: do stuff`
- The structure is: `def function_name(inputs, driver): ... a lot of prints and stuff...`

## ds_personal_functions.py:
- All the functions provided by yourself.

## searches.json:
- json where the data that the functions use are provided.
- The structure is:
 ```{'function_name':['list','of','inputs','function_name','uses'], 'function_name2': ...}```
- You may mention only the functions you want to be activated to generate your DailyScrap.
