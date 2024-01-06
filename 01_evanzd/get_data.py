import collections
import csv

import archeo_lib as al

EVANZD = "evanzd"


def get_2021():

    initial_date = '2020-11-11'
    final_date = '2021-01-13'
    conference = al.iclr_2021
    urls = { al.INITIAL:
        "https://raw.githubusercontent.com/evanzd/ICLR2021-OpenReviewData/39038e1ae9e73b6cb7bf1116505c199ef452a8cd/ratings.tsv",
        al.FINAL:
        "https://raw.githubusercontent.com/evanzd/ICLR2021-OpenReviewData/4aed86cd1729694a41ff57119af458b9187cce49/ratings.tsv"
    }

    filenames = {}
    ratings = collections.defaultdict(dict)
    for version, link in urls.items():
        filenames[version] = f'{conference}_{version}.tsv'
        al.get_file(link, filenames[version])
        with open(filenames[version], 'r') as f:
            reader = csv.DictReader(f, delimiter='\t')
            for row in reader:
                if 'paper_id' in row:
                    paper_id = row['paper_id']
                else:
                    paper_id = row['']
                ratings[version][paper_id] = [
                    row[str(x)] for x in range(6)]

    rows = []
    for forum_id, initial_ratings in ratings[al.INITIAL].items():
        if forum_id not in ratings[al.FINAL]:
            continue
        final_ratings = ratings[al.FINAL][forum_id]
        for i, (initial, final) in enumerate(zip(initial_ratings,
        final_ratings)):
            index = i
            if initial or final:
                rows.append(
                    al.RatingPair(
                        EVANZD,
                        conference,
                        forum_id,
                        i,
                        None,
                        initial,
                        initial_date,
                        final,
                        final_date

                    )
                )
    return rows



def main():

    k = get_2021()
    for x in k[:10]:
        print(x)

if __name__ == "__main__":
    main()
