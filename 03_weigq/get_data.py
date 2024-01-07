import collections
import csv
import sqlite3

import archeo_lib as al

WEIGQ = "weigq"

DB_URLS = {
    al.iclr_2022:
    "https://github.com/weigq/iclr2022_stats/raw/master/assets/iclr2022.db",
    al.iclr_2023:
    "https://github.com/weigq/iclr2023_stats/raw/main/assets/iclr2023.db"
}

def get_2022():

    conference = al.iclr_2022
    filename = f'{conference}.db'
    al.get_file(DB_URLS[conference], filename)

    con = sqlite3.connect(filename)
    cur = con.cursor()

    cur.execute("SELECT url, ratings_0, ratings_3 FROM submissions")

    ratings = collections.defaultdict(dict)
    for url, initial_list, final_list in cur.fetchall():
        forum_id = al.url_to_id(url)
        ratings[al.INITIAL][forum_id] = eval(initial_list)
        ratings[al.FINAL][forum_id] = eval(final_list)

    return convert_rows(conference, ratings, "2021-11-09", "2022-01-30")

def get_2023():

    conference = al.iclr_2023
    filename = f'{conference}.db'
    al.get_file(DB_URLS[conference], filename)

    con = sqlite3.connect(filename)
    cur = con.cursor()

    cur.execute("SELECT url_id, s_0_list, s_6_list FROM submissions")

    ratings = collections.defaultdict(dict)
    for forum_id, initial_list, final_list in cur.fetchall():
        ratings[al.INITIAL][forum_id] = eval(initial_list)
        ratings[al.FINAL][forum_id] = eval(final_list)

    return convert_rows(conference, ratings, "2022-11-05", "2022-12-17")


def convert_rows(conference, ratings, initial_date, final_date):
    rows = []
    for forum_id, initial_ratings in ratings[al.INITIAL].items():
        if forum_id not in ratings[al.FINAL]:
            continue
        final_ratings = ratings[al.FINAL][forum_id]
        for i, (initial,
                final) in enumerate(zip(initial_ratings, final_ratings)):
            if initial or final:
                rows.append(
                    al.RatingPair(WEIGQ, conference, forum_id, i, None,
                                  initial, initial_date, final, final_date))
    return rows


def main():

    k = get_2022()
    k = get_2023()


if __name__ == "__main__":
    main()
