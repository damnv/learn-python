def serializeDict(entity) -> dict:
    return {**{item: str(entity[item]) for item in entity if item == '_id'},
            **{item: entity[item] for item in entity if item != '_id'}}


def serializeList(entities) -> list:
    return [serializeDict(entity) for entity in entities]
