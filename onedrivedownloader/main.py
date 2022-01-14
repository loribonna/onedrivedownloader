import requests
from tqdm import tqdm
import zipfile
import os
import shutil


def download(url: str, path: str = None, unzip=False, unzip_path: str = None, force_download=False, force_unzip=False, clean=False) -> None:
    """
    Download a file from a OneDrive url.

    :param url: The url to download from (should end with '?download=1').
    :param path: The path to save the file to. Default: download to the current directory.
    :param unzip: Whether to unzip the file.
    :param unzip_path: The path to unzip the file to. Default is `path` + '_unzipped'.
    :param force_download: Whether to force download the file even if it already exists.
    :param force_unzip: Whether to force unzip the file even if it already exists.
    :param clean: Whether to clean the unzipped files after unzipping.
    """

    def _create_if_not_exists(path: str, remove=True) -> None:
        if os.path.exists(path):
            if not remove:
                return
            else:
                shutil.rmtree(path)

        if len(os.path.split(path)[1].split(".")) > 1:
            path = os.path.split(path)

        os.makedirs(path, exist_ok=True)

    if not url.endswith("?download=1"):
        # replace everithing after the last ? with ?download=1
        url = url.split("?")[0] + "?download=1"

    try:
        response = requests.get(url, stream=True)
        total_size_in_bytes = int(response.headers.get('content-length', 0))
        progress_bar = tqdm(total=total_size_in_bytes,
                            unit='iB', unit_scale=True)
        block_size = 1024

        if path is None:
            # get current working directory
            path = os.getcwd()

        if not os.path.exists(path) or force_download:
            _create_if_not_exists(path)

            with open(path, 'wb') as f:
                for data in response.iter_content(block_size):
                    progress_bar.update(len(data))
                    f.write(data)
            progress_bar.close()

            if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
                raise Exception(
                    f"ERROR, something went wrong during download!\nExpected {total_size_in_bytes} Bytes, got {progress_bar.n} Bytes.")

        # unzip file if necessary
        if unzip:
            if unzip_path is None:
                unzip_path = path + '_unzipped'

            if not os.path.exists(unzip_path) or force_unzip:
                print("Extracting files...")

                _create_if_not_exists(path, remove=True)
                with zipfile.ZipFile(path, 'r') as zip_ref:
                    zip_ref.extractall(unzip_path)

                if clean:
                    os.remove(path)

    except Exception as e:
        print(e)
        raise Exception("ERROR, something went wrong, see error above!")


if __name__ == "__main__":
    ln = "https://unimore365-my.sharepoint.com/<path>?download=1"
    print('Downloading dataset')
    download(ln, dest_path="files.zip", unzip=True, unzip_path="./data")
