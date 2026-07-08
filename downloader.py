import os 
import requests

from config import DOWNLOAD_FOLDER


def download_pdf(url):

    '''
    Download the pdf given the url.
    '''

    os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

    response = requests.get(url)

    response.raise_for_status()

    filename = os.path.basename(url)

    file_path = os.path.join(DOWNLOAD_FOLDER , filename)

    with open(file_path, "wb") as file:
        file.write(response.content)

    return file_path









