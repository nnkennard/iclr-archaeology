import glob
import json

def main():

    rows = []
    for filename in glob.glob('iclr-analysis/Data/2020/*/*.json'):
        path = filename.split("/")
        forum_id = path[-2]
        review_id = path[-1][:-5]
        with open(filename, 'r') as f:
            obj = json.load(f)
            rows.append({
                "forum_id": forum_id,
                "review_id": review_id,
                "rating": obj['rating'],
                "review": obj['review']
            })

    with open('iclr_2020_reviews_2019-11-08.jsonl', 'w') as f:
        for row in rows:
            f.write(json.dumps(row)+"\n")


if __name__ == "__main__":
    main()

