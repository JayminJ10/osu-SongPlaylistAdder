import YT_Search as YT
import os
import json
from dotenv import load_dotenv

load_dotenv()
song_dict = {}

def get_osu_path(*args)->str:
    path = (os.getenv('LOCALAPPDATA'))
    path = os.path.join(path, 'osu!')
    if len(args) != 0:
        for s in args:
            path = os.path.join(path, s)
    return path

def check_size() -> int:
    return (len(next(os.walk(os.path.join(get_osu_path("Songs"))))[1]))

def generate_songs():
    path = get_osu_path('Songs')
    file = open('songs.txt', 'w+')
    for song in os.listdir(path):
        song = os.path.splitext(song)
        file.write(song[0] + "\n")
        #print(song[0])
        #splitsong = str(song).split(" ")

def map_songs():
    file = open('songs.txt', 'r+')
    songs = {}
    s = " "
    json_file = get_osu_path("SongBot")
    json_file = os.path.join(json_file, "songs.json")
    for song in file:
        songsplit = str(song).split(" ")
        song_id = songsplit[0]
        song_name = songsplit[1:]
        songs.update({str(song_id) : s.join(song_name).strip("\n")})
    with open(json_file, 'w') as output:
        json.dump(songs, output)
    
# Return the songs loaded from the json as a dictionary
def get_song_dict() -> dict:
    global song_dict
    if (not bool(song_dict)):
        print("Dict empty\n")
        with open(get_osu_path("SongBot", "songs.json")) as jf:
            song_dict = json.load(jf)
    return song_dict

if __name__ == "__main__":
    ## This is for initial setup -- If folders/files don't exist then create them using the osu! installation.
    if not os.path.exists(get_osu_path('SongBot')):
        dir = "SongBot"
        parent = get_osu_path()
        path = os.path.join(parent, dir)
        os.makedirs(path)
    if not os.path.exists(get_osu_path("SongBot", "songs.json")):
        generate_songs()
        map_songs()
        os.remove("songs.txt")
    if len(get_song_dict().keys()) != check_size():
        generate_songs()
        map_songs()
        os.remove("songs.txt")