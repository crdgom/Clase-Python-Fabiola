class DecimalJsonEncoder(json.JSONEncoder):
    """
    Custom JSON encoder.

    This class is needed because we store some data as a decimal (e.g. the
    individual weight entries in the workout log) and they need to be
    processed, json.dumps() doesn't work on them
    """

    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return str(obj)
        if isinstance(obj, datetime.date):
            return str(obj)
        return json.JSONEncoder.default(self, obj)
