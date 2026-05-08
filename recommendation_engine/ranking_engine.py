def rank_datasets(query, datasets):

    query_words = set(
        query.lower().split()
    )

    ranked = []

    for dataset in datasets:

        dataset_words = set(
            dataset.lower().split()
        )

        score = len(
            query_words.intersection(
                dataset_words
            )
        )

        ranked.append(
            (dataset, score)
        )

    ranked.sort(
        key=lambda x: x[1],
        reverse=True
    )

    return ranked