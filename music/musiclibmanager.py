import argparse
import os
from tinytag import TinyTag

def trav_dir(dir):
    for root, dirs, files in os.walk(dir):       #recursive
        for file in files:
            yield os.path.join(root, file)

def exists_file(file_path):
    music_extensions = ['.mp3']
    return any(file_path.endswith(ext) for ext in music_extensions)


def show_metadata(file_path):
        t = TinyTag.get(file_path)
        print("____________________")
        print(f"File: {file_path}")
        print(f"Song: {t.title}")
        print(f"Artist: {t.artist}")
        print(f"Album: {t.album}")

def get_metadata(file_path):
        tag = TinyTag.get(file_path)
        return {
            'artist': tag.artist,
            'album': tag.album,
            'title': tag.title,
        }

def group_by_artist(files):
    artists = {}
    for file_path in files:
        metadata = get_metadata(file_path)
        if metadata:
            artist = metadata['artist']
            if artist not in artists:
                artists[artist] = []
            artists[artist].append(file_path)
    return artists

def group_by_album(files):
    albums = {}
    for file_path in files:
        metadata = get_metadata(file_path)
        if metadata:
            album = metadata['album']
            if album not in albums:
                albums[album] = []
            albums[album].append(file_path)
    return albums

def group_by_artist_album(files):
    artists = {}
    for file_path in files:
        metadata = get_metadata(file_path)
        if metadata:
            artist = metadata['artist']
            album = metadata['album']
            if artist not in artists:
                artists[artist] = {}
            if album not in artists[artist]:
                artists[artist][album] = []
            artists[artist][album].append(file_path)
    return artists


def print_grouped_files(grouped_files, indent=0):
    for key, value in grouped_files.items():
        print('  ' * indent + key)
        if isinstance(value, dict):
            print_grouped_files(value, indent + 1)
        else:
            for file_path in value:
                print('  ' * (indent + 1) + os.path.basename(file_path))

    

def main():
    p = argparse.ArgumentParser(description='MLM cli tool .')
    p.add_argument('--input', help='input syntax.')
    p.add_argument('--list-files', action='store_true', help='List songs in the directory')
    p.add_argument("--show-metadata", action="store_true", help="show metadata")
    p.add_argument("--group-by", choices=['ARTIST', 'ALBUM', 'ARTIST_ALBUM'], help="Group files")
    p.add_argument("--reorganize-by", choices=['ARTIST','ALBUM','ARTIST_ALBUM'],help="Group files")
    args = p.parse_args()

    dir = args.input

    if not os.path.isdir(dir):
         #check for valid direcotry, if not executes
        print(f"Error: '{dir}' is not a valid directory")
        return

    if args.list_files:
        for file_path in trav_dir(dir):
            if exists_file(file_path):
                print(os.path.basename(file_path))

    if args.input and args.show_metadata:
        for file_path in trav_dir(args.input):
            if file_path.endswith(('.mp3')): 
                show_metadata(file_path)

    if args.input and args.group_by:
        files = list(trav_dir(args.input))
        if args.group_by == 'ARTIST':
            grouped_files = group_by_artist(files)
        elif args.group_by == 'ALBUM':
            grouped_files = group_by_album(files)
        elif args.group_by == 'ARTIST_ALBUM':
            grouped_files = group_by_artist_album(files)
        print_grouped_files(grouped_files)

if __name__ == '__main__':
    main()