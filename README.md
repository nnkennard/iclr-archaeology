# iclr-archaeology

This repository contains an attempt to retrieve initial review text and scores for ICLR 2018-2023. Since reviewers are allowed to update their scores during the review process, the final score may reflect their interactions with other participants in the review process. Unfortunately, only the final score is available through the OpenReview API.

Fortunately, many members of the ICLR community have taken advantage of ICLR's openness to publish analyses of review scores immediately after the reviews are released (such analyses tend to be popular with researchers who have papers  under submission at ICLR).

This repository collates review information from the data sources of these analyses.

| Author        | Scraping method | Format | Rating format  | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 |
|---------------|-----------------|--------|----------------|------|------|------|------|------|------|
| Federico Botu | OpenReview      | CSV    | Lists          |      |      |      | Y    |      |      |
| Dong Zhou     | HTML            | TSV    | Lists          |      |      |      | Y    |      |      |
| Bastian Rieck | OpenReview API  |        | Review objects |      |      | Y    | Y    |      |      |
| Horace He     | HTML            | JSON   | Lists          | Y    | Y    | Y    |      |      |      |
| Guoqiang Wei  | HTML            | sqlite | Lists          |      |      |      |      | Y    | Y    |
