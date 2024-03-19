import YT_Search as YT
import os
from dotenv import load_dotenv

load_dotenv()

def generate_songs():
    path = (os.getenv('TEMPPATH'))
    file = open('songs.txt', 'w+')
    for folder in os.listdir(path):
        file.write(folder + "\n")

if __name__ == "__main__":
    if not os.path.exists('./songs.txt'):
        generate_songs()