import requests

def get_parameters():

    token_url = 'https://id.twitch.tv/oauth2/token'

    # these parameters help authenticate that I am a valid user to get an access token to use the api
    parameters = {
        'client_id': f'XXX',
        'client_secret':  f'XXX',
        'grant_type': 'client_credentials'
    }

    # this is a post response that uses that url and takes in these parameters and sends a request to the api
    auth_response = requests.post(token_url, params = parameters).json()

    # if all my parameters are valid, it'll give me an access token, which i can use to use the rest of the api through urls
    access_token = auth_response['access_token']
    

    return {
        'client_id': f'XXX',
        'authorization': f'Bearer {access_token}'
    }


    
