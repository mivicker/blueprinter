# blueprinter
This is one function that takes a nested dictionary, typically created from json.load and returns a graphqlish dictionary.

## example use

```python
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

output = blueprinter(input)
```
### Result
```python
# output
{
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
```
