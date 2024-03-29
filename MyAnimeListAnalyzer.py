from jikanpy import Jikan
import time

jikan = Jikan()

# json of all anime info specified by Jikan docs
#

seasons = ['winter', 'spring', 'summer', 'fall']


def main():
    for year in range(1970, 2019):
        yearly_show_count = 0
        yearly_show_total = 0

        for season in seasons:
            seasonal_show_count = 0
            seasonal_show_total = 0

            #print(str(year) + ' ' + str(season) + ': ')
            shows = getShows(year, season)
            for show in shows:
                if isValidShow(show):
                    #printShowInfo(show)

                    seasonal_show_count += 1
                    seasonal_show_total += show['score']

            yearly_show_count += seasonal_show_count
            yearly_show_total += seasonal_show_total

            rateLimitBatchRequests()
            print(season + ' ' + str(year) + ': ' + str(seasonal_show_total / seasonal_show_count))


        print(str(year) + ': ' + str(yearly_show_total / yearly_show_count))


def getShows(year, season):
    season_shows = jikan.season(year=year, season=season)
    return season_shows['anime']


def isValidShow(show):
    if show['type'] != 'Special' and show['continuing'] == False and isAdult(show) == False and show['score'] is not None:
        return True
    return False


def isAdult(show):
    genres = show['genres']
    for genre in genres:
        if 'Hentai' in genre.values():
            return True
    return False


def printShowInfo(show):
    print(show['title'] + ' ' + str(show['score']) + ' ' + show['type'])


def rateLimitBatchRequests():
    # jikan api requires at least 4 seconds between batch requests
    time.sleep(4.1)


main()
