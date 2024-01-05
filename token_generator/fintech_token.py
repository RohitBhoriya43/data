
from urllib.parse import urlencode

import requests


def main_token(url,client_id,client_secret):

    try:    
        data = {
            'client_id': client_id,
            'client_secret': client_secret,
            'grant_type': 'client_credentials'
        }
        encoded_data = urlencode(data)
        headers = {
         "Content-Type": "application/x-www-form-urlencoded"
        }       
        # res = requests.request("POST", url, headers=headers, data=encoded_data)
        res = requests.post(url, headers=headers, data=encoded_data)
        res = res.json()
        print(res,"ressssssss")
        return res.get("access_token")
    except Exception as e:        
        return {"error":str(e)}



