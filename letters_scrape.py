import requests
import bs4
import csv

# collect the web page
url = 'https://www.irishtimes.com/opinion/letters/'
req = requests.get(url)

# make the soup
soup = bs4.BeautifulSoup(req.text, 'html.parser')

# parse the soup
letters = soup.find_all('h2', class_ = 'c-heading')

# make the csv and append to existing file
HEADERS = ['heading']
with open('letter_headings.csv', "a") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for l in letters[:-2]:
            writer.writerow([l.text])