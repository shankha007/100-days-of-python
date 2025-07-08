import env
import requests

HEADER = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {env.SHEETY_TOKEN}"
}


class DataManager:
    def __init__(self):
        self.prices_endpoint = env.SHEETY_ENDPOINT
        self.users_endpoint = env.SHEETY_USERS_ENDPOINT
        self.destination_data = {}
        self.customer_data = {}

    def get_destination_data(self):
        response = requests.get(url=self.prices_endpoint, headers=HEADER)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }

            response = requests.put(
                url=f"{env.SHEETY_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=HEADER
            )
            print(response.text)

    def get_customer_emails(self):
        response = requests.get(url=self.users_endpoint, headers=HEADER)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
