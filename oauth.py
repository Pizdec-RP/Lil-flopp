import requests, json

class Oauth:
    client_id="812950760399962123"
    client_secret="RTQ-7olvII1OPup03ek_nm1DdbnupCS9"
    redirect_uri="http://127.0.0.1:5000/login"
    scope="guilds%20identify%20email"
    discord_login_url=f"https://discord.com/api/oauth2/authorize?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code&scope={scope}"
    discord_token_url="https://discord.com/api/oauth2/token"
    discord_api_url="https://discord.com/"

    @staticmethod
    def get_access_token(code):
        payload = {
            "client_id": Oauth.client_id,
            "client_secret": Oauth.client_secret,
            "grant_type": "authorizaton_code",
            "code": code,
            "redirect_uri": Oauth.redirect_uri,
            "scope": Oauth.scope
        }
        access_token = requests.post(url= Oauth.discord_token_url,data=payload).json()
        return access_token.get("access_token")
        
    @staticmethod
    def get_user_json(access_token):
        url = f"{Oauth.discord_api_url}/users/@me"
        headers = {"Autorization": f"Bearer {access_token}"}
        user_object = requests.get(url = url,headers = headers).json()
        return user_object
