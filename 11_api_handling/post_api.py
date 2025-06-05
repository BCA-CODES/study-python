import requests

def fetch_post_api():
    url = "https://api.freeapi.app/api/v1/social-media/posts/get/t/dolore?page=1&limit=3"

    response = requests.get(url)
    real_data = response.json()

    if real_data["success"] and "data" in real_data:
        postData = real_data["data"]
        print(postData)
        firstname = postData["posts"][0]["author"]["firstname"]
        username = postData["posts"][0]["author"]["account"]["username"]
        email = postData["posts"][0]["author"]["account"]["email"]
        return firstname, username, email 
    else:
        raise Exception("Failed to fetch data")

def main():
    try:
        firstname, username, email = fetch_post_api()
        print(f"First name: {firstname} \nUsername: {username} \nEmail: {email}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()
