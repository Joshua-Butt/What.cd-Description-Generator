'''
Python What.CD Album Bio generator,

(c) 2016 Joshua Butt.
Made for twitter user @Mabbupuku
'''

# Import required modules
import time

from glob import glob
from mutagen.mp3 import MP3



class Song_Attributes:
    def __init__(self, filename):
        self.mp3_file = MP3(filename)

        tags = [
            ['title', u'TIT2'], ['album', u'TALB'],
            ['artist', u'TPE1'], ['year', u'TDRC'],
            ['track_number', u'TRCK'],
        ]

        # Strip MP3 metadata
        for var, tag in tags:
            try:
                setattr(self, var, self.mp3_file.tags[tag][0])
            except KeyError:
                print(f"Warning: Failed to find {var} for {filename} perhaps you have no ID3 tags populated")
                if var == 'title':
                    setattr(self, var, filename.rsplit('/',1)[1][:4])
                else:
                    setattr(self, var, "???")

            except TypeError:
                print(f"Error: Failed to load track {filename}")

        self.length = self.mp3_file.info.length


def time_str(seconds):
    return time.strftime("%M:%S", time.gmtime(seconds))

if __name__ == '__main__':

    audio_files = glob("*.mp3")

    if not audio_files:
        print("Error: No Media Detected")

    elif len(audio_files) > 1:
        for index, audio_file in enumerate(audio_files):
            audio_files[index] = Song_Attributes(audio_file)

        audio_files.sort(key=lambda x: int(x.track_number[0].split('/')[0]))

        album_bio = \
f'''[size=5][b][artist]{audio_files[0].artist}[/artist] - {audio_files[0].album}[/b][/size]

[b]Year:[/b] {audio_files[0].year}
[b]Format:[/b](INSERT FORMAT HERE)

[size=4][b]Tracklist[/b][/size]
'''

        total_length = 0
        for mp3_file in audio_files:
            total_length += mp3_file.length
            album_bio += f'\n[b]{mp3_file.track_number}.[/b] {mp3_file.title} [i]{time_str(mp3_file.length)}[/i]'

        album_bio += \
f'''
[b]Total Length:[/b] {time_str(total_length)}

More Information: [url](INSERT URL HERE)[/url]
'''

        with open('album_bio.txt', 'w', encoding="utf-8") as f:
            f.write(album_bio)

        print("Successfully generated text File")

    else:
        print("Support for single files coming soon...")

input('\nPress Enter to exit...')