import googleapiclient.discovery
import random

api_service_name, api_version, DEVELOPER_KEY = "youtube", "v3", "insert developer key"

def generate_video():
    videos = []

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.search().list(
        part="snippet",
        maxResults=300,
        q="frog",
        safeSearch="strict",
        type="video",
        videoEmbeddable="true"
    )
    response = request.execute()

    for result in response.get('items', []):
        if result['id']['kind'] == 'youtube#video':
            videos.append('%s' % (result['id']['videoId']))
    # print(generate_video())
    return (random.choice(videos))
