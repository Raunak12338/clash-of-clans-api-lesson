import requests

headers = {
    'Accept' : 'application/json',
    'Authorization' : 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImI4ODJiOTYzLTkzNmItNGFhNS05ZDExLTgzZTY5ZTYyMzRiZSIsImlhdCI6MTYwODM1NDM0NSwic3ViIjoiZGV2ZWxvcGVyLzViNWZjMWE1LTY2MjYtMjc2NS1kMmViLWVkMTYyMWY2YmFiOCIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjEwMy45Mi4xMTUuMzUiXSwidHlwZSI6ImNsaWVudCJ9XX0.SoqHBhvxHMfnhDVj1CQwNJfQR0XUaUOdU1Hs-FqF7dZI8UhNLctt68V58Qws4vPCrR6A5ypF5mbpdyQQRvIFyg'
    
}

def get_user():
    # return user profile information
    response = requests.get(
    'https://api.clashofclans.com/v1/players/%23LRVGL2PLR', headers=headers)
    user_json = response.json()
    print(user_json)

 
def search_clan():
        #submit a clan search
        response = requests.get(
            'https://api.clashofclans.com/v1/clans?name=Silent%20Darkfall', headers=headers)
        clan_json = response.json()
        for clan in clan_json['items'] :
                print(clan['name'] + ': is level ' + str(clan['clanLevel']))


search_clan()
