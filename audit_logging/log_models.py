class AuditLog:

    def __init__(
        self,
        user_id,
        dataset_id,
        access_type,
        approved
    ):

        self.user_id = user_id
        self.dataset_id = dataset_id
        self.access_type = access_type
        self.approved = approved