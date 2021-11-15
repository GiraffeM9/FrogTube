import googleapiclient.discovery
import random
from os import path
import json

api_service_name, api_version, DEVELOPER_KEY = "youtube", "v3", "insert_api_key"
file_path = "website/templates/static/videos.json"

def api_response():
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    tags = ["frog", "frogs", "cute frog", "funny frog"]
    r = {}
    for tag in tags:
        request = youtube.search().list(
            part="snippet",
            maxResults=1000,
            q=tag,
            safeSearch="strict",
            type="video",
            videoEmbeddable="true"
        )
        response = request.execute()
        r.update(response)
    with open(file_path, "w") as file:
                json.dump(r, file)
    return response
    

def generate_video():
    if not path.exists(file_path):
        response = api_response()
    else:
        with open(file_path, "r") as file:
            response = json.load(file)
    videos = []
    for result in response.get("items", []):
        if result["id"]["kind"] == "youtube#video":
            videos.append('%s' % (result["id"]["videoId"]))
    random.shuffle(videos)
    # print(generate_video())
    return (random.choice(videos))


def get_videos(num):
    pass
