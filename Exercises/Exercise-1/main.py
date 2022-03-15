import requests
import os
import concurrent.futures
from multiprocessing.pool import ThreadPool
from zipfile import ZipFile

download_uris = [
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip'
]

# Create a directory the zip files will be downloaded to
directory = "downloads"
parent_dir = "/home/mubarak/data-engineering-practice/Exercises/Exercise-1"
path = os.path.join(parent_dir, directory)
os.mkdir(path)

def download_file(download_uri):
    file = requests.get(download_uri)
    if download_uri.find("/"):
        dir_name = download_uri.rsplit("/", 1)[1]
        file_name = dir_name.rsplit(".", 1)[0]
        filename = f"{file_name}.csv"
        open(f"{path}/{dir_name}", "wb").write(file.content)

    # Extract the csv file and delete the zip file
    try:
        with ZipFile(f"{path}/{dir_name}", "r") as zip_file:
            zip_file.extract(filename, path)
        os.remove(f"{path}/{dir_name}")         
        print("Downloading and extracting")

    except:
        print("Not a zip file, continue")
        pass

def main():
    downloads = ThreadPool(5).imap_unordered(download_file, download_uris)
    for download in downloads:
        print("CSV file extracted")

if __name__ == "__main__":
    main()
    print("Program executed")