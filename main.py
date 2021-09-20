from bs4 import BeautifulSoup
import requests
import numpy

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

print(stories_texts[index])
print(stories_links[index])
print(story_score_int[index])
print(index)
