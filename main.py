import sys

def hello_world(name):
    print(f"Hello, {name}!")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide your name as a command-line argument.")
    else:
        name = sys.argv[1]
        hello_world(name)
