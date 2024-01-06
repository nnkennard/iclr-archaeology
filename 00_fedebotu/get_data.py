import collections
import csv

import archeo_lib as al

FEDEBOTU = "fedebotu"

TSV_URLS = {
    al.iclr_2022: {
        al.INITIAL:
        "https://raw.githubusercontent.com/fedebotu/ICLR2022-OpenReviewData/bd51a36c6b225df1a3e5426584ff5eee14963554/ratings.tsv",
        al.FINAL:
        "https://raw.githubusercontent.com/fedebotu/ICLR2022-OpenReviewData/master/ratings.tsv"
    },
    al.iclr_2023: {
        al.INITIAL:
        "https://raw.githubusercontent.com/fedebotu/ICLR2023-OpenReviewData/main/data/iclr2023_20221105.csv",
        al.FINAL:
        "https://raw.githubusercontent.com/fedebotu/ICLR2023-OpenReviewData/main/data/iclr2023_20230210.csv"
    }
}

def get_2022():

    initial_date = '2021-11-10'
    final_date = '2022-01-29'
    conference = al.iclr_2022
    urls = { al.INITIAL:
        "https://raw.githubusercontent.com/fedebotu/ICLR2022-OpenReviewData/bd51a36c6b225df1a3e5426584ff5eee14963554/ratings.tsv",
        al.FINAL:
        "https://raw.githubusercontent.com/fedebotu/ICLR2022-OpenReviewData/master/ratings.tsv"
    }

    filenames = {}
    ratings = collections.defaultdict(dict)
    for version, link in urls.items():
        filenames[version] = f'{conference}_{version}.tsv'
        al.get_file(link, filenames[version])
        with open(filenames[version], 'r') as f:
            reader = csv.DictReader(f, delimiter='\t')
            for row in reader:
                ratings[version][row['paper_id']] = [
                    row[str(x)] for x in range(1,7)]
    
    return convert_rows(conference, ratings, initial_date, final_date, True)


def get_2023():

    initial_date = '2022-11-05'
    final_date = '2023-02-10'
    conference = al.iclr_2023
    urls = { al.INITIAL:
        "https://raw.githubusercontent.com/fedebotu/ICLR2023-OpenReviewData/main/data/iclr2023_20221105.csv",
        al.FINAL:
        "https://raw.githubusercontent.com/fedebotu/ICLR2023-OpenReviewData/main/data/iclr2023_20230210.csv"
    }


    filenames = {}
    ratings = collections.defaultdict(dict)
    for version, link in urls.items():
        filenames[version] = f'{conference}_{version}.tsv'
        al.get_file(link, filenames[version])
        with open(filenames[version], 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                ratings[version][row['id']] = eval(row['ratings'])

    return convert_rows(conference, ratings, initial_date, final_date, False)


def convert_rows(conference, ratings, initial_date, final_date, add_one):
    rows = []
    for forum_id, initial_ratings in ratings[al.INITIAL].items():
        if forum_id not in ratings[al.FINAL]:
            continue
        final_ratings = ratings[al.FINAL][forum_id]
        for i, (initial, final) in enumerate(zip(initial_ratings,
        final_ratings)):
            index = i
            if add_one:
                index += 1
            if initial or final:
                rows.append(
                    al.RatingPair(
                        FEDEBOTU,
                        conference,
                        forum_id,
                        index,
                        None,
                        initial,
                        initial_date,
                        final,
                        final_date

                    )
                )
    return rows



def main():

    k = get_2022()
    k = get_2023()

if __name__ == "__main__":
    main()
