import json
import requests
import urllib.request
import random

url = "https://instagram-downloader-download-instagram-videos-stories1.p.rapidapi.com/"

def downloader(post):
    querystring = {"url": post}
    headers = {
        "X-RapidAPI-Key": "f5c031158amsh3e427efcf8451d8p151c85jsn9ff8191549bc",
        "X-RapidAPI-Host": "instagram-downloader.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)

    url_link = json.loads(response.text)
    video_link = url_link['result']['video_url']
    video_name = url_link['result']['username']
    urllib.request.urlretrieve(video_link, f'{video_name}.mp4')


def pinterest(url):
    url = "https://pinterest-downloader-download-pinterest-image-video-and-reels.p.rapidapi.com/api/data"
    # post = "https://pin.it/5dUupCPqq"
    querystring = {"url": url}

    headers = {
        "X-RapidAPI-Key": "f5c031158amsh3e427efcf8451d8p151c85jsn9ff8191549bc",
        "X-RapidAPI-Host": "pinterest-downloader-download-pinterest-image-video-and-reels.p.rapidapi.com"
    }
    a = "qwertaysjlf"
    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    img_url = data["data"]["images"]["564x"]["url"]
    img_name = ""
    for i in random.sample(a, 5):
        img_name += i

    img_name = data["data"]["images"]["564x"]["width"]
    urllib.request.urlretrieve(img_url, f'{img_name}.jpg')

pinterest("https://pin.it/5dUupCPqq")


