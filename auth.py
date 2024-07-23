import requests

def get_parameters():

    token_url = 'https://id.twitch.tv/oauth2/token'
    parameters = {
        'client_id': f'XXX',
        'client_secret':  f'XXX',
        'grant_type': 'client_credentials'
    }
    auth_response = requests.post(token_url, params = parameters).json()
    access_token = auth_response['access_token']
    
    return {
        'client_id': f'XXX',
        'authorization': f'Bearer {access_token}'
    }


    
