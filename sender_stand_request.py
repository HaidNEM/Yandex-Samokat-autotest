import requests
import data
import configuration

def post_new_order(body):
    url = configuration.URL_SERVICES + configuration.CREATE_ORDER_PATH
    print("POST URL:", url)
    response = requests.post(
        url,
        json=body,
        headers=data.headers
    )
    response.raise_for_status()
    return response.json().get("track")

def get_order_by_track(track):
    url = configuration.URL_SERVICES + configuration.GET_ORDER_PATH.format(track=track)
    return requests.get(url, headers=data.headers)