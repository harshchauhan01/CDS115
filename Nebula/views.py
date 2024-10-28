from django.shortcuts import render
import requests
import logging
from datetime import datetime, timedelta

# Create your views here.
def Home(request):
    return render(request,'home.html')


logger = logging.getLogger(__name__)

def News(request):
    apod_url = 'https://api.nasa.gov/planetary/apod?api_key=r2IimDgbSBNHqvpuIGZuB7rPh2Sdn6c9KwjD2Ipn'
    try:
        apod_response = requests.get(apod_url)
        apod_response.raise_for_status()
        apod_data = apod_response.json()
        logger.info(f"Fetched APOD data: {apod_data}")

        if apod_data.get('media_type') == 'image':
            apod_context = {
                'image_url': apod_data.get('url'),
                'hd_image_url': apod_data.get('hdurl'),
                'apod_text': apod_data.get('title'),
                'explanation': apod_data.get('explanation'),
            }
        else:
            apod_context = {'error': "No image available today."}

    except requests.exceptions.RequestException as e:
        logger.error(f"APOD request failed: {e}")
        apod_context = {'error': "An error occurred while fetching APOD data."}

    
    news_url = 'https://newsapi.org/v2/everything?q=ISRO&from=2024-09-27&sortBy=publishedAt&apiKey=712d87378da84afaaa9d693b757030a7'
    try:
        news_response = requests.get(news_url)
        news_response.raise_for_status()
        news_data = news_response.json()
        logger.info(f"Fetched news data: {news_data}")

        if news_data.get('status') == 'ok' and 'articles' in news_data:
            articles = []
            for article in news_data['articles']:
                articles.append({
                    'title': article.get('title'),
                    'image_url': article.get('urlToImage'),
                    'published_at': article.get('publishedAt'),
                    'description': article.get('description'),
                })

            articles = articles[:7]

        else:
            articles = []

    except requests.exceptions.RequestException as e:
        logger.error(f"News request failed: {e}")
        articles = []

    context = {
        'apod': apod_context,
        'articles': articles,
    }

    return render(request, 'news.html', context)


def Mission(request):
    return render(request,'mission.html')

def Explore(request):
    return render(request,'explore.html')

def Earth(request):
    return render(request,'earth.html')



