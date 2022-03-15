from csv import DictReader
from io import TextIOWrapper
import requests
import concurrent.futures
import os
from zipfile import ZipFile
import time

download_uris = [
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip',
]
# create a directory
def download_file(download_uris):

    # Create a directory the zip files will be downloaded to
    directory = "downloads"
    parent_dir = "/home/mubarak/data-engineering-practice/Exercises/Exercise-1"
    path = os.path.join(parent_dir, directory)
    os.mkdir(path)

    # Download the contents 
    for download_uri in download_uris:
        file = requests.get(download_uri)
        if download_uri.find("/"):
            dir_name = download_uri.rsplit("/", 1)[1]
            file_name = dir_name.rsplit(".", 1)[0]
            filename = f"{file_name}.csv"
            open(f"{path}/{dir_name}", "wb").write(file.content)

        # Extract the csv file and delete the zip file
        with ZipFile(f"{path}/{dir_name}", "r") as zip_file:
            zip_file.extract(filename, path)
        os.remove(f"{path}/{dir_name}")         
        print("Downloading and extracting")
    
   
download_file(download_uris=download_uris)