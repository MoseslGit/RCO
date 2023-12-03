import os
import requests

# Define the base URL and folder where you want to save the files
base_url = "https://web.evanchen.cc/exams/"
save_folder = "data/tex/"


def build_urls():
    urls = []

    urls += [f"USAMO-{year}-notes.tex" for year in range(1996, 2024)]
    urls += [f"JMO-{year}-notes.tex" for year in range(2010, 2024)]
    urls += [f"sols-TSTST-{year}.tex" for year in range(2011, 2024)]
    urls += [f"sols-TST-IMO-{year}.tex" for year in range(2014, 2024)]
    urls += [f"IMO-{year}-notes.tex" for year in range(1997, 2024)]
    urls += [f"ELMO-{year}-sols.tex" for year in [2010, 2011, 2013, 2014, 2016]]

    return urls

def download_store_url(filename):
    response = requests.get(base_url + filename)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Save the file to the specified folder
        with open(os.path.join(save_folder, filename), "wb") as file:
            file.write(response.content)
        print(f"Downloaded url {url}")
    else:
        print(f"Failed to download {url}")

if __name__ == '__main__':
    os.makedirs(save_folder, exist_ok=True)

    urls = build_urls()

    for url in urls:
        download_store_url(url)

    print("Download completed.")
