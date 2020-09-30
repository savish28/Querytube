from apiclient.discovery import build 
from background_task import background
import datetime
from .models import Video, Query
DEVELOPER_KEYS = ["AIzaSyBamY361zKxtzXLW0LjAGXgbkjbdaNH4no"]
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

@background(schedule=10)
def youtube_search_keyword(query, max_results=50): 
    print('Its Query time', query)
    results = []
    print("Current date and time : ",datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    for developerKey in DEVELOPER_KEYS:
        try:
            youtube_object = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey = developerKey)
            search_keyword = youtube_object.search().list(q = query, part = "id, snippet", maxResults = max_results,type="video", order="date").execute()
            results = search_keyword.get("items", [])
            break
        except:
            print('Retry')
    videos = [] 
    for result in results: 
        if result['id']['kind'] == "youtube#video": 
            obj = {}
            obj['title'] = result["snippet"]["title"]
            obj['desc'] = result['snippet']['description']
            obj['videoId'] = result["id"]["videoId"]
            obj['thumbnail'] = result['snippet']['thumbnails']['default']['url']
            obj['publish_date'] = result['snippet']['publishedAt']
            obj['channelId'] = result['snippet']['channelId']
            obj['channelTitle'] = result['snippet']['channelTitle']
            videos.append(obj)

    query_obj = Query.objects.filter(query=query)[0]
    for video in videos:
        if(Video.objects.filter(videoId=video['videoId']).count()!=0):
            #already stored
            return
        Video(title=video['title'],desc = video['desc'],videoId=video['videoId'],thumbnail=video['thumbnail'],publish_date=video['publish_date'],channelId = video['channelId'],channelTitle = video['channelTitle'],query=query_obj).save()
