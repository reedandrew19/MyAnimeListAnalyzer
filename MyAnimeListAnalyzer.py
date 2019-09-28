from jikanpy import Jikan
import time
jikan = Jikan()

# json of all anime info specified by Jikan docs
#

seasons = ['winter', 'spring', 'summer', 'fall']


def isAdult(show):
    genres = show['genres']
    for genre in genres:
        if 'Hentai' in genre.values():
            return True
    return False

def isValidShow(show):
    if show['type'] != 'Special' and show['continuing'] == False and isAdult(show) == False and show['score'] is not None:
        return True
    return False


def printShowInfo():
    print(show['title'] + ' ' + str(show['score']) + ' ' + show['type'])


def getShows():
    season_shows = jikan.season(year=year, season=season)
    return season_shows['anime']


def rateLimitBatchRequests():
    # jikan api requires at least 4 seconds between batch requests
    time.sleep(4.1)


for year in range(2017, 2019):
    for season in seasons:
        show_count = 0

        print (str(year) + ' ' + str(season) + ': ')
        shows = getShows()
        for show in shows:
            if isValidShow(show):
                printShowInfo()

                show_count += 1

        print(show_count)

        rateLimitBatchRequests()