import collections
import csv
import requests

FIELDS = "source conference forum review_index review_id first_rating first_timestamp last_rating last_timestamp".split(
)
RatingPair = collections.namedtuple("RatingPair", FIELDS)

INITIAL, FINAL = "initial final".split()

iclr_2018 = "iclr_2018"
iclr_2019 = "iclr_2019"
iclr_2020 = "iclr_2020"
iclr_2021 = "iclr_2021"
iclr_2022 = "iclr_2022"
iclr_2023 = "iclr_2023"


def get_file(url, filename):
    r = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(r.content)

def url_to_id(url):
    pre_forum_id = url.split("?")[-1]
    assert pre_forum_id.startswith("id=")
    return pre_forum_id[3:]

def write_csv(rows):
    with open('ratings.csv', 'w') as f:
        writer = csv.DictWriter(f, FIELDS)
        writer.writeheader()
        for row in rows:
            writer.writerow(row._asdict())

