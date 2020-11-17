import requests

# ADD YOUR IMPORTS BEFORE THIS LINE

# Use this function to write information about ONE book
# to the result file
# It takes a string as input, this string should have the following format
# line = book_name,book_price,book_url

# Feel free to change this method, if needed


def write_line(line):
    with open('./books.csv', 'a') as file:
        file.write(line)
        file.write('\n')

# WRITE YOUR CODE BELOW THIS LINE

    URL = "http://books.toscrape.com/catalogue/page-1.html"

    r = requests.get(url=URL)

    data = r.json
    print(data)


write_line('skandert')
