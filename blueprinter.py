def blueprinter(structure):
    """
    Takes a json.load-created dictionary and returns a graphqlish 
    blueprint of the object.
    """
    match structure:
        case [*items]:
            return [blueprinter(items[0])]
        case {**items}:
            return {key: blueprinter(value) for key, value in items.items()}
        case _:
            return type(structure).__name__


if __name__ == "__main__":
    # A test
    input = {
        "integer": 0,
        "string": "harvey",
        "ball": {
            "diameter": 1000,
            "weight": 1000,
        },
        "providers": [
            {
                "name": "money",
                "address": "everywhere",
            },
            {
                "name": "food",
                "address": "melt",
            }
        ],
        "flat_list": [
            "apple",
            "orange",
            "banana",
        ],
    }
    output = {
        "integer": "int",
        "string": "str",
        "ball": {
            "diameter": "int",
            "weight": "int",
        },
        "providers": [
            {
                "name": "str",
                "address": "str",
            }
        ],
        "flat_list": ["str"]
    }

    assert blueprinter(input) == output
