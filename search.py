# -*- coding: utf-8 -*-

import os
import json

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def by_keyword(keyword):
 # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "../oauthkey.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_local_server()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    request = youtube.search().list(
        part="snippet",
        maxResults=5,
        order="viewCount",
        q=keyword,
        type="video",
        #videoDefinition="high"
    )
    response = request.execute()
    return response
    '''
    #f = open('result.json', 'w')
    #print(response, file = f)
    #f.close()
    for key in response['items']:
        print(key['snippet']['title'])
        print('https://www.youtube.com/watch?v=' + key['id']['videoId'])
        #print(response['items'][0]['snippet']['title'])
        #print(response['items'][0]['id']['videoId'])
    '''
