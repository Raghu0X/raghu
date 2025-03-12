def print_keyword_args(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_keyword_args(name="raghu", age=19, city="belagavi")
