# assignment04-github.py
# author: Céaman Collins
# a script to modify the contents of a file on github
# replacing instances of the word Andrew with Céaman


# imports
from github import Github
from github import Auth
from config import keys
import requests

# getting key from config file and setting auth
key = keys['github2']
auth = Auth.Token(f"{key}")

# opening connection to github
g = Github(auth=auth)

# setting repository and getting file info and url
repo = g.get_repo("CeamanCollins/pands-mywork")
file_info = repo.get_contents("test.txt")
url_of_file = file_info.download_url

# using stored url to download file contents
response = requests.get(url_of_file)
response_contents = response.text

# replacing instances of Andrew with Céaman
new_contents = response_contents.replace("Andrew","Céaman")

# updating file on github
repo.update_file(file_info.path, "updated by program", new_contents, file_info.sha, branch='main')

# closing connection
g.close()