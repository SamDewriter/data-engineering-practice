from http.client import responses
import requests
import os
from zipfile import ZipFile

download_uris = ['https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip',
                'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip'
                ]

def download_file(download_uris):
    responses = {download_uri: requests.get(download_uri, stream=True) 
                    for download_uri in download_uris}
    streams = {download_uri: responses[download_uri].iter_content(chunk_size=1024)
                for download_uri in download_uris}
    handles = {download_uri: open(os.path.basename(download_uri), "wb")
                for download_uri in download_uris}

    while streams:
        for download_uri in list(streams.keys()):
            try:
                chunk = next(streams[download_uri])
                print("Received {} bytes for {}".format(len(chunk), url))
                handles[download_uri].write(chunk)
            except StopIteration: # no more contenet
                handles[download_uri].close()
                streams.pop(download_uri)
