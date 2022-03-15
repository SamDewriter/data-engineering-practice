    

def main():
    # Create a directory to save the files
    directory = "downloads"
    parent_dir = "/home/mubarak/data-engineering-practice/Exercises/Exercise-1"

    # Join the directory and the path
    path = os.path.join(parent_dir, directory)
    os.mkdir(path)

    t1 = time.perf_counter()
    def download_file(download_uri):
        try:
            file = requests.get(download_uri).content
            with open(path, "wb") as f:
                f.write(file.content)
            print("Downloading...")
        except:
            print("Check the link, it seems it's not working properly")

    # Fetching files concurrently
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_file, download_uris)

if __name__ == '__main__':
    main()



try:
            file = requests.get(download_uri).content
            with open(path, "wb") as f:
                f.write(file.content)
            print("Downloading...")
        except:
            print("Check the link, it seems it's not working properly")
