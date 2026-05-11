TRUSTED_SOURCES = [
    "healthcare_api",
    "research_portal",
    "verified_partner"
]


def verify_provenance(source):

    return source in TRUSTED_SOURCES