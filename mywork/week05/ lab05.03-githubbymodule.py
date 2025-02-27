from github import Github
from github import Auth
from config import keys
import requests

key = keys['github2']

auth = Auth.Token(f"{key}")

g = Github(auth=auth)

# for repo in g.get_user().get_repos():
#     print(repo.name)
# #     repo.edit(has_wiki=False)

# print(dir(repo))

repo = g.get_repo("CeamanCollins/pands-mywork")

# repo.create_file("test.txt", "test", "test")

contents = repo.get_contents("test.txt",)
# repo.update_file(contents.path, "more tests", "more tests", contents.sha)

# repo = g.get_repo("CeamanCollins/aprivateone")
# print(repo.clone_url)

fileInfo = repo.get_contents("test.txt")
# urlOfFile = fileInfo.download_url
# print (urlOfFile)

response = requests.get('https://raw.githubusercontent.com/CeamanCollins/pands-mywork/main/test.txt')
response_contents = response.text
# print(contents)

new_contents = response_contents + "\n \n additional test text in test file"

repo.update_file(fileInfo.path, "updated by program", new_contents, contents.sha, branch='main')



g.close()