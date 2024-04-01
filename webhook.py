import requests



base_url = 'https://webexapis.com/v1'

bearer_token = 'ZTZhZmJi..d65305c2ce82'



headers = {

    "Accept": "application/json",

    "Content-Type": "application/json",

    "Authorization": f"Bearer {bearer_token}",

}



webhook = {

    "name": "My Awesome Webhook",

    "targetUrl": "http://377cf7274b2d.ngrok.io/webhook",

    "resource": "messages",

    "event": "created",

}



#read current webhooks and delete them as a cleanup

response = requests.get(f"{base_url}/webhooks", headers=headers, json=webhook)

response.raise_for_status()



#delete them one by one

for item in response.json()["items"]:

    print (f'Deleting webhook \"{item["name"]}\"...')

    del = requests.delete(f'{base_url}/webhooks/{item["id"]}', headers=headers)

    del.raise_for_status()

    print (del.status_code)



#create a new one

response = requests.post(f"{base_url}/webhooks", headers=headers, json=webhook)

response.raise_for_status()



webhook_id = response.json()["id"]

print(f"Webhook for {webhook['targetUrl']} added with ID\n{webhook_id}")