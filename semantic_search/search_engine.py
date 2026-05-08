from embedding_engine import generate_embedding
from dataset_index import DATASETS


def semantic_search(query):

    query_embedding = generate_embedding(query)

    results = []

    for dataset in DATASETS:

        dataset_embedding = generate_embedding(dataset)

        similarity = len(
            query_embedding.intersection(
                dataset_embedding
            )
        )

        results.append(
            (dataset, similarity)
        )

    results.sort(
        key=lambda x: x[1],
        reverse=True
    )

    return results[:3]