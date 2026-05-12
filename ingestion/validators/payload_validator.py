def validate_payload(records):

    if not isinstance(records, dict):
        raise Exception("Payload must be a dict")

    if len(records) == 0:
        raise Exception("Payload is empty")

    return True
