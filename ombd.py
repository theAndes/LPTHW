import urllib.request
import json


def main():

    class OMDB:
        movie = "lego movie".replace(" ", "+")
        imdbID = None
        baseURL = "https://www.omdbapi.com/"
        key = "apikey=trilogy"

    def get_OMBD_data(imdbID):
        if imdbID == None:
            get_imbdID_of_movie()
        else:
            print(
                f'You seacrhed {OMDB.baseURL} for the Movie "{OMDB.movie}". The imdbID for this movie is {imdbID}.')
            webURL = urllib.request.urlopen(
                f"{OMDB.baseURL}?i={imdbID}&{OMDB.key}")
            for key, val in json.loads(webURL.read()).items():
                print(f'''{key}: {val}''')
            print('-'*100)

    def get_imbdID_of_movie():
        webURL = urllib.request.urlopen(
            f"{OMDB.baseURL}?s={OMDB.movie}&{OMDB.key}")
        data = webURL.read()
        movieData = json.loads(data)

        for movies in movieData["Search"]:
            OMDB.imdbID = movies['imdbID']
            OMDB.movie = movies['Title']
            get_OMBD_data(OMDB.imdbID)

    get_OMBD_data(OMDB.imdbID)


if __name__ == "__main__":

    main()
