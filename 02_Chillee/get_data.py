import collections
import csv
import json

import archeo_lib as al

CHILLEE = "Chillee"

CONF_FIELDS = "initial_date final_date initial_url final_url".split()
ConfTuple = collections.namedtuple("ConfTuple", CONF_FIELDS)

CONF_TUPLES = {
    al.iclr_2018: ConfTuple(
    '2017-12-03',
    '2018-02-14',
    "https://raw.githubusercontent.com/Chillee/OpenReviewExplorer/d84065792d0b5f527ae7ae0a11e496283dcf348d/public/data.json",
        "https://raw.githubusercontent.com/Chillee/OpenReviewExplorer/master/data/iclr2018.json"
    ),
    al.iclr_2019: ConfTuple(
    '2018-11-10',
    '2019-11-07',
    "https://github.com/Chillee/OpenReviewExplorer/raw/master/data/iclr2019_11_06.json",
    "https://github.com/Chillee/OpenReviewExplorer/raw/c419b5d459ad9292b7df045052a1f4b4966a0399/data/iclr2019.json"
    ),
    al.iclr_2020: ConfTuple(
 '2019-11-07',
    '2019-12-21',
    "https://github.com/Chillee/OpenReviewExplorer/raw/c419b5d459ad9292b7df045052a1f4b4966a0399/data/iclr2020.json",
    "https://github.com/Chillee/OpenReviewExplorer/raw/1a6b56ff491eb7f18dec17735ec68667f62d0dce/data/iclr2020.json"

    ),
}

def get_conference(conference, conf_tuple):

    urls = {
        al.INITIAL: conf_tuple.initial_url,
        al.FINAL: conf_tuple.final_url 
    }

    filenames = {}
    ratings = collections.defaultdict(dict)
    for version, link in urls.items():
        filenames[version] = f'{conference}_{version}.json'
        al.get_file(link, filenames[version])

        with open(filenames[version], 'r') as f:
            obj = json.load(f)
            for forum in obj:
                ratings[version][
                al.url_to_id(forum['url'])] = forum['ratings']

    return convert_rows(conference, ratings, conf_tuple.initial_date,
                        conf_tuple.final_date)



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
                    al.RatingPair(CHILLEE, conference, forum_id, i, None,
                                  initial, initial_date, final, final_date))
    return rows


def main():

    rows = []
    for conference, conf_tuple in CONF_TUPLES.items():
        rows += get_conference(conference, conf_tuple)

    al.write_csv(rows)


if __name__ == "__main__":
    main()
