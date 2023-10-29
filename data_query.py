# external / builtin library imports
import os
import googleapiclient.discovery
from googleapiclient.discovery import HttpError
import pandas as pd
from pathlib import Path
from os import listdir, getcwd

# local imported files
from channel_ids import *
import api_keys


# /////////////////////////////////////////////////////////////////
def authenticate_credentials():
    """Run this at the start of a session to obtain"""
    developer_key = api_keys.developer_key
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    api_service_name = "youtube"
    api_version = "v3"
    return googleapiclient.discovery.build(api_service_name, api_version, developerKey=developer_key)


# /////////////////////////////////////////////////////////////////

def get_channel_details(channel_ids) -> pd.DataFrame | None:
    """retrieves various details about the provided channel(s), like channel name, id, sub count, video count, view count, etc."""
    all_data = []

    request = youtube.channels().list(part="snippet,contentDetails,statistics", id=",".join(channel_ids))
    response = request.execute()

    for item in response['items']:
        data = {"channelId": item['id'],
                "channelName": item['snippet']['title'],
                "viewCount": item['statistics']['viewCount'],
                "subscriberCount": item['statistics']['subscriberCount'],
                "videoCount": item['statistics']['videoCount'],
                "uploads": item['contentDetails']['relatedPlaylists']['uploads']
                }
        all_data.append(data)
    return pd.DataFrame(all_data)


def last_n_video_ids(playlist_id, n: int = 50):
    """retrieve the video ids for the creator's last n uploads, provided the channel's 'uploads' playlist ID"""
    ids = []

    request = youtube.playlistItems().list(
        part="snippet,contentDetails",
        playlistId=playlist_id,
        maxResults=n
    )

    response = request.execute()

    for item in response['items']:
        ids.append(item['contentDetails']['videoId'])

    return ids


def get_video_details(video_ids):
    """retrieves information about each video provided, as a list of dicts"""
    all_data = []
    if isinstance(video_ids, list):
        request = youtube.videos().list(
            part="snippet,contentDetails,statistics",
            id=",".join(video_ids)
        )
    elif isinstance(video_ids, str):
        request = youtube.videos().list(
            part="snippet,contentDetails,statistics",
            id=video_ids
        )
    response = request.execute()

    for item in response['items']:
        video_info = {
            'videoId': item['id'],
            'channelName': item['snippet']['channelTitle'],
            'description': item['snippet']['description'],
            'videoTitle': item['snippet']['title'],
            'postDate': item['snippet']['publishedAt'],
            'duration': item['contentDetails']['duration'],
            'views': item['statistics']['viewCount'],
            'commentCount': None,
            'thumbnail': item['snippet']['thumbnails']['default']['url']}
        all_data.append(video_info)
    return all_data


def get_n_comments(video_id, n=50):
    comments = []
    try:
        results = youtube.commentThreads().list(
            part='snippet',
            videoId=video_id,
            textFormat='plainText',
            maxResults=n
        ).execute()
    except HttpError:
        # comments are disabled on video
        # return list of None to match expected return format
        return [None]
    else:
        for item in results['items']:
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            comments.append(comment)
        return comments



