import wget
import zipfile

print("Download...")
wget.download('http://vectors.nlpl.eu/repository/20/180.zip')

print("Extract...")
archive = '180.zip'
with zipfile.ZipFile(archive, 'r') as zip_file:
    zip_file.extractall("")
