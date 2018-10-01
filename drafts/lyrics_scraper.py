
import requests

CLIENT_ACCESS_TOKEN = "lTv0ZCyw1mkXQ7_9bZ9GmEdc9vPh2_VQzhFCpERSOYiFA1fXjEVrI8BY-D9_k6E2"

BASE_URI = "https://api.genius.com"

DREXLER_ARTIST_ID = 344463

def _get(path, params=None, headers=None):

    url = '/'.join([BASE_URI, path])

    token = "Bearer {}".format(CLIENT_ACCESS_TOKEN)

    if headers:
        headers['Authorization'] = token
    else:
        headers = {"Authorization": token}

    response = requests.get(url=url, params=params, headers=headers)
    response.raise_for_status()

    return response.json()

def get_artist_songs(artist_id):

    current_page = 1
    next_page = True
    songs = []

    while next_page:

        path = "artists/{}/songs/".format(artist_id)
        params = {'page': current_page}
        data = _get(path=path, params=params)

        page_songs = data['response']['songs']

        if page_songs:
            songs += page_songs
            current_page += 1
        else:
            next_page = False

    return songs


songs = get_artist_songs(DREXLER_ARTIST_ID)
songs = [song for song in songs if song['primary_artist']['id'] == DREXLER_ARTIST_ID]

thefile = open('test.txt', 'w')
for item in songs:
  thefile.write("%s\n" % item)