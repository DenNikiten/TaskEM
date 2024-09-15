import os
import requests
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env

username = os.getenv("USER_NAME")
access_token = os.getenv("ACCESSES_TOKEN")
repo_name = os.getenv("REPO_NAME")
base_url = os.getenv("BASE_URL")
# base_url = "https://api.github.com"


def create_new_public_repos(access_token, repo_name):
    url = f"{base_url}/user/repos"
    headers = {
        "Authorization": f"token {access_token}",
    }
    data = {
        "name": repo_name,
        "visibility": 'public'
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 201:
        new_repos = response.json()
        print(f"New public repository '{repo_name}' created. Status code: {response.status_code}")
        return new_repos['name']
    else:
        print(f"Failed to create a new repo.")


def get_user_repos(username):
    url = f"{base_url}/users/{username}/repos"
    response = requests.get(url)
    if response.status_code == 200:
        repos_data = response.json()
        print(f"Repositories of {username} received. Status code: {response.status_code}")
        data = [repo['name'] for repo in repos_data]
        return data
    else:
        print(f"Failed to retrieve repositories.")
        # return None


def delete_repos(access_token, repo_name, username):
    url = f"{base_url}/repos/{username}/{repo_name}"
    headers = {
        "Authorization": f"token {access_token}",
    }
    response = requests.delete(url, headers=headers)
    if response.status_code == 204:
        print(f"Repository '{repo_name}' has been deleted successfully. Status code: {response.status_code}")
    elif response.status_code == 404:
        print(f"Repository not found or already deleted. Status code: {response.status_code}")
    else:
        print(f"Failed to delete repository. Status code: {response.status_code}")


def test_api_github():
    new_repo = create_new_public_repos(access_token, repo_name)
    repositories_data = get_user_repos(username)
    assert new_repo in repositories_data, f"There is no repository {new_repo}"
    delete_repos(access_token, repo_name, username)
