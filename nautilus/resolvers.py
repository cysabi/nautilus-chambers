from nautilus import query, greeting


@greeting.field("words")
def resolve_words(obj, info):
    return f"Hello, {obj['name']}!"


@greeting.field("person")
def resolve_person(obj, info):
    return "Some Other Dude"


@query.field("greet")
def resolve_greet(*_, **kwargs):
    return kwargs
