d1 = {"1": {"2": "some", "3": {"4": "the"}}}


def recursive_search(dictionary, target_key):
    if target_key in dictionary:
        return dictionary[target_key]
    for value in dictionary.values():
        if isinstance(value, dict):
            result = recursive_search(value, target_key)
            if result is not None:
                return result


# Example usages
result_3 = recursive_search(d1, "3")
result_4 = recursive_search(d1, "4")
result_2 = recursive_search(d1, "2")

print(result_3)  # Output: {'4': 'the'}
print(result_4)  # Output: the
print(result_2)  # Output: some


tup1 = (2, 3, [1, 2, 3])
tup1[2].append(4)
print(tup1)


# Django serialization
# Converts Django model object in json, XML etc.
# Django routers
"""Routers are used with ViewSets in django rest framework to auto config the urls.
 Routers provides a simple, quick and consistent way of wiring ViewSet logic to a set of URLs. 
 Router automatically maps the incoming request to proper viewset action based on the request 
 method type(i.e GET, POST, etc)."""

# Django ORM


def flatten_dict(d, parent_key="", separator="_"):
    items = {}
    for key, value in d.items():
        new_key = parent_key + separator + key if parent_key else key
        if isinstance(value, dict):
            items.update(flatten_dict(value, new_key, separator))
        else:
            items[new_key] = value
    return items


# Example nested dictionary
nested_dict = {"a": 1, "b": {"c": 2, "d": {"e": 3}}, "f": 4}

# Flatten the dictionary
flattened_dict = flatten_dict(nested_dict)

print(flattened_dict)
