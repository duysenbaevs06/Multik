import requests


API_TOKEN = "836740af-5817-476a-8689-ec6f1898fbe1"



async def api_request(image_url):
    r = requests.post(
    "https://api.deepai.org/api/toonify",

    data={
        'image': image_url,
    },

    headers={'api-key': API_TOKEN}
    )



    data = r.json()

    if data:
        return data["output_url"]

    return None