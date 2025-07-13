from bs4 import BeautifulSoup
import requests

# with open('website.html') as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, 'html.parser')
# print(soup.title)
# print(soup.title.name) # title
# print(soup.title.string) # Angela's Personal Site
# print(soup.a) # First anchor tag
# print(soup.p) # First paragraph tag
# all_annchor_tags = soup.find_all(name="a")
# print(all_annchor_tags)

# all_paragraph_tags = soup.find_all(name="p")
# print(all_paragraph_tags)

# for tag in all_annchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))

# heading = soup.find(name="h1", id="name")
# print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.getText())

# company_url = soup.select_one(selector="p a")
# print(company_url)
#
# name = soup.select_one(selector="#name")
# print(name)

# headings = soup.select(selector=".heading")
# print(headings)

response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
articles = soup.find_all(name="a", class_="storylink")
article_texts = [article_tag.getText() for article_tag in articles]
article_links = [article_tag.get("href") for article_tag in articles]
article_upvotes = [int(str(score.getText()).split(" ")[0]) for score in soup.find_all(name="span", class_="score")]
# print(article_texts)
# print(article_links)
# print(article_upvotes)

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)
print(article_texts[largest_index])
print(article_links[largest_index])
