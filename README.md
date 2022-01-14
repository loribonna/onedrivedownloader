# OneDrive downloader: python utility to download files from OneDrive

## Requires
- `tqdm`: for nice progress bar
- `requests`: fetch data from OneDrive

## Usage
`from onedrivedownloader import download`

and

`download(url: str, path: str = None, unzip=False, unzip_path: str = None, force_download=False, force_unzip=False, clean=False)`

Defaults are:
- `path`: current path
- `unzip`: don't unzip, just download
- `unzip_path`: `path` + `_unzipped`
- `force_download`: DON'T download if file already exists
- `force_unzip`: DON'T unzip if file already exists
- `clean`: DON'T delete unzipped files after unzipped

## Example
`download("https://<stuff>.sharepoint.com/<path>?download=1", dest_path="files.zip", unzip=True, unzip_path="./data")`