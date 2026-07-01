import requests

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


def download(url):
    try:
        r = requests.get(
            url,
            headers=HEADERS,
            timeout=20
        )

        if r.status_code == 200:
            return r.text

    except Exception as e:
        print(e)

    return None