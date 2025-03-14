import requests

r = requests.get('https://api.github.com/users/isomaribaba')
reponser = r.json()
#print(f"Login: {reponser['login']} \n followers { reponser['followers_url']} \n repos { reponser['repos_url']}")
avatar_req = requests.get(reponser['avatar_url'])

with open('avatar.jpg', 'wb') as f:
    f.write(avatar_req.content)

exit(1)
#Liste des repo de l'utilisateur
list_repos = requests.get(reponser['repos_url'])
list_repos = list_repos.json()

for repo in list_repos:
    line = (f"Nom repository : {repo['name']}\n Description : {repo['description']}\n  url : {repo['url']}\n")
    with open('list_repo.txt', 'a') as f:
        f.write(line)
