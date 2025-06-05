
def dubug(func):
    def wrapper(*args,**kwargs):
        args_value = ', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join(str(f"{key} = {value}") for key, value in kwargs.items())
        print(f"debug name: {func.__name__} and args: {args_value} and kwargs: {kwargs_value}")
        func(*args,**kwargs)
    return wrapper


@dubug
def user(name, greeting="hello"):
    print(f"{greeting}, {name}")

user("dev",greeting="hi")