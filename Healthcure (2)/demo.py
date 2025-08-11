import os

def list_top_level(path='.'):
    for item in os.listdir(path):
        if os.path.isdir(os.path.join(path, item)):
            print(f"{item}/")  # folder
        else:
            print(item)       # file

list_top_level('.')
