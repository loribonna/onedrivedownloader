# OneDrive downloader: python utility to download files from OneDrive

## Requires
- `tqdm`: for nice progress bar
- `requests`: fetch data from OneDrive

## Usage
```
from onedrivedownloader import download

...

download(url: str, filename: str, unzip=False, unzip_path: str = None, force_download=False, force_unzip=False, clean=False)
```

### Required parameters:
- `url`: The url to download from (should end with '?download=1').
- `filename`: The filename to save the file as.

### Optional parameters:
- `unzip`: want to unzip file or just download? Requires files to be `.zip` if True. (default: False)
- `unzip_path`: path to unzip files (default: current directory)
- `force_download`: force files download if exist? (default: False)
- `force_unzip`: force files unzip if `unzip_path` exists? (default: False)
- `clean`: clean source file after unzip?

## Example
`download("https://<stuff>.sharepoint.com/<path>?download=1", filename="files.zip", unzip=True, unzip_path="./data")`