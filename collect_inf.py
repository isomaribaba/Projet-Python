import requests

r = requests.get('https://api.github.com/users/isomaribaba')
reponser = r.json()
#print(f"Login: {reponser['login']} \n followers { reponser['followers_url']} \n repos { reponser['repos_url']}")
list_repos = requests.get(reponser['repos_url'])
list_repos = list_repos.json()

for repo in list_repos:
    print(repo)
