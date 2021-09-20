import numpy
import requests
from bs4 import BeautifulSoup


class DataManager:

    @staticmethod
    def scrape_website(link):
        return requests.get(link).text

    @staticmethod
    def access_data_from_website(website_content):
        soup = BeautifulSoup(website_content, 'html.parser')
        return soup

    @staticmethod
    def get_titles_from_website(soup):
        return [story.get_text() for story in soup.find_all(name='a', class_='storylink')]

    @staticmethod
    def get_links_from_website(soup):
        return [story.get('href') for story in soup.find_all(name='a', class_='storylink')]

    @staticmethod
    def get_scores_from_website(soup):
        return [score.getText() for score in soup.find_all(name='span', class_='score')]

    @staticmethod
    def get_highest_score_index_from_website(score):
        story_score_int = [int(story.split()[0]) for story in score]
        return story_score_int.index(numpy.max(story_score_int))

    @staticmethod
    def create_message(titles, links, scores, index):
        return (f'SUBJECT: Daily Hack News \n\n'
                f'Checkout today most popular news!\n'
                f'Title: {titles[index]}\n'
                f'Link: {links[index]}\n'
                f'This story received {scores[index]} votes today!')
