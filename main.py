from bs4 import BeautifulSoup

with open('website.html') as website_file:
    html = website_file.read()

soup = BeautifulSoup(html, features='html.parser')
print(type(soup.get_text()))
