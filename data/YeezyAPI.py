import json

import requests


class YeezyAPI:
    def __init__(self):
        self._BASE_API_URL = "https://yeezypay.io/api/v1/google"
        self._HEADERS = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }

    def generate_auth(self, mcc_id, mcc_secret_token):
        url = self._BASE_API_URL + "/auth"

        payload = json.dumps({
            "account_id": mcc_id,
            "secret": mcc_secret_token,
            "timeout": 600
        })

        response = requests.request("POST", url, headers=self._HEADERS, data=payload)
        if not response or bool(response.json().get('state', False)) is False:
            print(f"generate_auth error: {response.text}")
            return

        return response.json()

    def get_master_balance(self, auth_token):
        url = self._BASE_API_URL + "/get-master-balance"

        auth = {'Authorization': f'Bearer {auth_token}'}

        response = requests.request("GET", url, headers=self._HEADERS | auth)
        if not response or bool(response.json().get('state', False)) is False:
            print(f"get_master_balanc error: {response.text}")
            return

        return response.json()

    def get_verify_account(self, auth_token, account_uid):
        url = self._BASE_API_URL + f"/accounts?uid={account_uid}"

        auth = {'Authorization': f'Bearer {auth_token}'}

        response = requests.request("GET", url, headers=self._HEADERS | auth)
        if not response or bool(response.json().get('state', False)) is False:
            print(f"get_verify_accounts error: {response.text}")
            return

        return response.json()

    def get_unverify_account(self, auth_token, account_uid):
        url = self._BASE_API_URL + f"/veryfying_accounts?uid={account_uid}"

        auth = {'Authorization': f'Bearer {auth_token}'}

        response = requests.request("GET", url, headers=self._HEADERS | auth)
        if not response or bool(response.json().get('state', False)) is False:
            print(f"get_verify_accounts error: {response.text}")
            return

        return response.json()

    # def get_verify_accounts(self, auth_token):
    #     url = self._BASE_API_URL + "/accounts"
    #
    #     auth = {'Authorization': f'Bearer {auth_token}'}
    #
    #     response = requests.request("GET", url, headers=self._HEADERS | auth)
    #     if not response or bool(response.json().get('state', False)) is False:
    #         print(f"get_verify_accounts error: {response.text}")
    #         return
    #
    #     return response.json()
    #
    # def get_unverify_accounts(self, auth_token):
    #     url = self._BASE_API_URL + "/veryfying_accounts"
    #
    #     auth = {'Authorization': f'Bearer {auth_token}'}
    #
    #     response = requests.request("GET", url, headers=self._HEADERS | auth)
    #     if not response or bool(response.json().get('state', False)) is False:
    #         print(f"get_unverify_accounts error: {response.text}")
    #         return
    #
    #     return response.json()


