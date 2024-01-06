# iclr-archaeology

This repository contains an attempt to retrieve initial review text and scores for ICLR 2018-2023. Since reviewers are allowed to update their scores during the review process, the final score may reflect their interactions with other participants in the review process. Unfortunately, only the final score is available through the OpenReview API.

Fortunately, many members of the ICLR community have taken advantage of ICLR's openness to publish analyses of review scores immediately after the reviews are released (such analyses tend to be popular with researchers who have papers  under submission at ICLR).

This repository collates review information from the data sources of these analyses.

| Source                                                                                                   | Scraping method | Format | Rating format  | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 |
|----------------------------------------------------------------------------------------------------------|-----------------|--------|----------------|------|------|------|------|------|------|
| [Federico Botu](https://github.com/fedebotu/ICLR2023-OpenReviewData/tree/main)                           | OpenReview      | CSV    | Lists          |      |      |      |      | Y    | Y    |
| [Dong Zhou](https://github.com/evanzd/ICLR2021-OpenReviewData/tree/master)                               | HTML            | TSV    | Lists          |      |      |      | Y    |      |      |
| [Bastian Rieck](https://github.com/Pseudomanifold/iclr-analysis/)                                        | OpenReview API  |        | Review objects |      |      | Y    | Y    |      |      |
| [Horace He](https://github.com/Chillee/OpenReviewExplorer/tree/c419b5d459ad9292b7df045052a1f4b4966a0399) | HTML            | JSON   | Lists          | Y    | Y    | Y    |      |      |      |
| [Guoqiang Wei](https://github.com/weigq/iclr2022_stats)                                                  | HTML            | sqlite | Lists          |      |      |      |      | Y    | Y    |

## fedebotu

Unfortunately there seem to be some errors in this data. The ratings for ICLR 2023 seem to be off by one:

| forum_id    | csv_ratings  | actual_ratings  |
|-------------|--------------|-----------------|
| [RUzSobdYy0V](https://openreview.net/forum?id=RUzSobdYy0V) | **[1, 1, 1, 1]** | [5, 6, 8]       |
| [N3kGYG3ZcTi](https://openreview.net/forum?id=N3kGYG3ZcTi) | [5, 6, 8]    | [3, 6, 3, 1]    |
| [tmIiMPl4IPa](https://openreview.net/forum?id=tmIiMPl4IPa) | [3, 6, 3, 1] | [8, 6, 5, 8, 6] |
