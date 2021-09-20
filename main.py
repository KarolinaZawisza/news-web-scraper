from mail_manager import MailManager
from data_manager import DataManager

website_content = DataManager.scrape_website('https://news.ycombinator.com/news')
soup = DataManager.access_data_from_website(website_content)
titles = DataManager.get_titles_from_website(soup)
links = DataManager.get_links_from_website(soup)
scores = DataManager.get_scores_from_website(soup)
index = DataManager.get_highest_score_index_from_website(scores)
message = DataManager.create_message(titles, links, scores, index)
print(links[index])
MailManager.send_email(message)
