import requests
import json

def download_artwork(game: str):
    with open("secrets.json", "r") as file:
        data = json.load(file)


    base_url = "https://api.igdb.com/v4"
    client_id = data.get("client_id")
    access_token = data.get("response").get("access_token")
    header = {
        "Client-ID":client_id,
        "Authorization":f"Bearer {access_token}"
    }


    response = requests.post("https://api.igdb.com/v4/games/",headers=header,data='search "skul"; fields cover.*, artworks.*;')


    with open("result.json","w") as file:
        json.dump(response.json(),file,indent=4)


if __name__ == "__main__":
    with open("secrets.json", "r") as file:
        data = json.load(file)


    base_url = "https://api.igdb.com/v4"
    client_id = data.get("client_id")
    access_token = data.get("response").get("access_token")
    header = {
        "Client-ID":client_id,
        "Authorization":f"Bearer {access_token}"
    }


    response = requests.post("https://api.igdb.com/v4/games/",headers=header,data='search "skul"; fields cover.*, artworks.*;')


    with open("result.json","w") as file:
        json.dump(response.json(),file,indent=4)