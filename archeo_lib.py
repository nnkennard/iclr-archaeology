import collections
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
