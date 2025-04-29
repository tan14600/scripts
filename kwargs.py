def print_user_details(**kwargs):
    print(kwargs)  # kwargs is a dictionary of key-value pairs
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_user_details(name="Alice", age=25, city="New York")