import requests
from tqdm import tqdm
import zipfile
import os
import shutil

def _create_if_not_exists(path: str, remove=True) -> None:
    if path is None:
        return
        
    if os.path.exists(path):
        if not remove:
            return
        else:
            if os.path.isdir(path):
                shutil.rmtree(path)
            else:
                os.remove(path)

    # If is a file -> get parent. If no parent -> exit
    if os.path.split(path)[0] == '':
        return

    if '.' in os.path.split(path)[1]:
        path = os.path.split(path)[0]

    os.makedirs(path, exist_ok=True)

def download(url: str, filename: str, unzip=False, unzip_path: str = None, force_download=False, clean=False) -> None:
    """
    Download a file from a OneDrive url.

    Yes, this documentation was generated by copilot. Thank you copilot.
    :param url: The url to download from (should end with '?download=1').
    :param filename: The filename to save the file as.
    :param unzip: Whether to unzip the file.
    :param unzip_path: The path to unzip the file to. Default is current path.
    :param force_download: Whether to force download the file even if it already exists.
    :param clean: Whether to clean the unzipped files after unzipping.
    """

    if not url.endswith("?download=1"):
        # replace everithing after the last ? with ?download=1
        url = url.split("?")[0] + "?download=1"

    try:
        response = requests.get(url, stream=True)
        total_size_in_bytes = int(response.headers.get('content-length', 0))
        progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True) if total_size_in_bytes > 1024 else None
        block_size = 1024

        # parent if filename has a path else current path
        parent_path = os.path.split(filename)[0] if os.path.split(filename)[0] != '' else os.getcwd()

        if not os.path.exists(filename) or force_download:
            _create_if_not_exists(filename)

            with open(filename, 'wb') as f:
                for data in response.iter_content(block_size):
                    if progress_bar is not None:
                        progress_bar.update(len(data))
                    f.write(data)
            
            if progress_bar is not None:
                progress_bar.close()

                if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
                    raise Exception(
                        f"ERROR, something went wrong during download!\nExpected {total_size_in_bytes} Bytes, got {progress_bar.n} Bytes.")

        # unzip file if necessary
        if unzip:
            assert filename.endswith(".zip"), "ERROR: file is not a zip file!"

            clean_unzip_path = unzip_path is not None and os.path.realpath(unzip_path) not in os.path.realpath(filename)
    
            print("Extracting files...")

            _create_if_not_exists(unzip_path, remove=clean_unzip_path)
            with zipfile.ZipFile(filename, 'r') as zip_ref:
                zip_ref.extractall(unzip_path)

            if clean:
                os.remove(filename)

    except Exception as e:
        print(e)
        raise Exception("ERROR, something went wrong, see error above!")


if __name__ == "__main__":
    ln = "https://unimore365-my.sharepoint.com/:u:/g/personal/215580_unimore_it/EUmqgpzRz3tPlD2KiVNRqdABBJl7qQYcIeROtMc4g2UeIA?e=zZtkLr"
    print('Downloading dataset')
    download(ln, filename="files.zip", unzip=True)
