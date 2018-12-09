from django.db.backends.base.features import BaseDatabaseFeatures


class AdaptorDatabaseFeatures(BaseDatabaseFeatures):
    supports_transactions = False
    uses_savepoints = False
