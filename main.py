from bs4 import BeautifulSoup
import requests
import numpy
import mail_manager

yc_web_page = requests.get('https://news.ycombinator.com/news').text

soup = BeautifulSoup(yc_web_page, 'html.parser')
stories = soup.find_all(name='a', class_='storylink')
stories_texts = []
stories_links = []
for story in stories:
    stories_texts.append(story.get_text())
    stories_links.append(story.get('href'))

story_score = [score.getText() for score in soup.find_all(name='span', class_='score')]
story_score_int = [int(story.split()[0]) for story in story_score]
index = story_score_int.index(numpy.max(story_score_int))

message = (f'SUBJECT: Daily Hack News \n\n'
           f'Checkout today most popular news!\n'
           f'Title: {stories_texts[index]}\n'
           f'Link: {stories_links[index]}\n'
           f'This story received {story_score_int[index]} votes today!')

mail_manager.send_email(message)
