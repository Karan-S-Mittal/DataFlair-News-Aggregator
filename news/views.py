from pprint import pprint
import requests
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup as BSoup
from news.models import Headline

requests.packages.urllib3.disable_warnings()

def news_list(request):
	headlines = Headline.objects.all()[::-1]
	context = {
		'object_list': headlines,
	}
	return render(request, "news/home.html", context)

def scrape(request):
	session = requests.Session()
	session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
	url = "https://www.theonion.com/"

	content = session.get(url, verify=False).content
	soup = BSoup(content, "html.parser")
	News = soup.find_all('article', {"class":"js_post_item"})
	for article in News:
		title = article.find_all('a', {"class":"js_link"})[-1].text
		link = article.find("a", {"class":"js_link"}).attrs["href"]
		image_src = article.find("a", {"class":"js_link"}).find("img")
		if image_src:
			try:
				image_src = image_src.attrs["srcset"]
				image_src = image_src.split(" ")[-4]
			except:
				try:
					image_src = image_src.attrs["data-expanded-srcset"]
					image_src = image_src.split(" ")[-4]
				except:
					continue
		else:
			continue
		new_headline = Headline()
		new_headline.title = title
		new_headline.url = link
		new_headline.image = image_src
		new_headline.save()
	return redirect("../")

