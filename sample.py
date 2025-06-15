def greet(name):
    """Function to greet a person."""
    return f"Hello, {name}!"

if __name__ == "__main__":
    name = input("Enter your name: ")
    print(greet(name))
    print("Script execution completed.")