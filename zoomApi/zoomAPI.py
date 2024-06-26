import base64
import json
import logging
import time

import requests


base_url = 'https://zoom.us'
Account_id = "4h9jZgnETeC1jeCttAqewA"
client_id = "uWxvDYmLRBGf6uW2HUWgA"
client_secret = "B8Xg5H6UJbjppdTptwa2IOjn6mQaFsBs"

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s - %(message)s')

ch.setFormatter(formatter)

logger.addHandler(ch)


class ZoomClient:
    __client_id = None
    __client_secret = None
    __access_token = None
    expiry = None

    def __init__(self, account_id, client_id, client_secret) -> None:
        ZoomClient.__client_id = client_id
        ZoomClient.__client_secret = client_secret

    @property
    def access_token(cls):
        return cls.__access_token

    @access_token.setter
    def access_token(cls, token):
        cls.__access_token = token

    def __get_access_token(self):
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": f'Basic {base64.b64encode(f"{ZoomClient.__client_id}:{ZoomClient.__client_secret}".encode("utf-8")).decode("utf-8")}',
        }

        data = {
            "grant_type": "account_credentials",
            "account_id": Account_id,
        }

        try:
            response = requests.post(f'{base_url}/oauth/token', headers=headers, data=data)
            return response.json()

        except Exception as e:
            raise Exception(f"Error getting access token: {e}")

    def __save_token(self):
        logger.info("Getting the access token.")
        token = self.__get_access_token()
        logger.info("Token received.")
        token_data = {
            "access_token": token["access_token"],
            "expiry": (expiry_time:= time.time() + int(token["expires_in"])),
        }
        with open(".zoom_token", "w") as f:
            json.dump(token_data, f)

        ZoomClient.access_token = token["access_token"]
        ZoomClient.expiry = expiry_time
        return self
    
    def validate(self):
        try:
            with open(".zoom_token", "r") as f:
                token_data = json.load(f)
                if time.time() >= token_data["expiry"]:
                    logger.info('Token is expired. Setting up a new token.')
                    self.__save_token()
                else:
                    ZoomClient.access_token = token_data["access_token"]
        except FileNotFoundError:
            logger.info('File not found. Setting up new token.')
            self.__save_token()
        except Exception as e:
            logger.error(e)
            raise Exception(f"Error checking token expiry: {e}")
        return self
        
    def check_and_set_token(self):
        self.validate()
        return self
        
    def create_meeting(self,data:dict):
        self.validate()
        url = f'{base_url}/v2/users/me/meetings'
        header = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type':'application/json',
        }
        json_data = json.dumps(data, indent=2)
        
        response = requests.post(url, headers=header, data=json_data)
        logger.info('Response when creating the zoom meeting.')
        logger.info(response.text)
        response.raise_for_status()
        return response.json()
