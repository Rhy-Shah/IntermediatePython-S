import requests
url = "https://www.codewithharry.com/videos/python-web-scraping-tutorial-in-hindi/"
r = requests.get(url)
htmlcontent = r.content
print(htmlcontent)
# print(htmlcontent)