def singleton(class_):
    instance = {}

    def wrapper(*args, **kwargs):
        if class_ not in instance:
            object_ = class_(*args, **kwargs)
            instance[class_] = object_
        return instance[class_]
    return wrapper
