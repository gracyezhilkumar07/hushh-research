from dataset_profiles import DATASET_PROFILES
from ranking_engine import rank_datasets


def recommend_datasets(query):

    recommendations = rank_datasets(
        query,
        DATASET_PROFILES
    )

    return recommendations[:3]