'''
Python What.CD Album Bio generator,

(c) 2016 Joshua Butt.
Made for twitter user @Mabbupuku
'''

# Import required modules
from get_attributes import Song_Attributes, time_str
from glob import glob

# Run loop if main program
if __name__ == '__main__':
	file_type = "MP3"

	audio_files = glob("*.{type}".format(type=file_type.lower()))

	if len(audio_files) == 0:
		file_type = "FLAC"
		audio_files = glob("*.{type}".format(type=file_type.lower()))
		
	if len(audio_files) == 0:
		print "Error: No Media files detected"

	else:
		for file in range(len(audio_files)):	
			audio_files[file] = Song_Attributes(audio_files[file], file_type)
		
		# Itterate through multiple audio files
		if len(audio_files) > 1:	
			# Sort the audio files by track number
			audio_files.sort(key=lambda x: int(x.track[0].split('/')[0]))

			# Generate the album bio
			album_bio = ""
			album_bio += "[size=5][b][artist]{artist}[/artist] - {album}[/b][/size]\n".format(artist=audio_files[0].artist[0], album=audio_files[0].album[0])
			album_bio += "\n"
			album_bio += "[b]Year:[/b]{year}\n".format(year=audio_files[0].year[0])	
			album_bio += "[b]Format:[/b](INSERT FORMAT HERE)\n"
			album_bio += "\n"
			album_bio += "[size=4][b]Tracklist[/b][/size]\n"
			
			total_length = 0
			for file in audio_files:
				total_length += file.length
				album_bio += "[b]{track}.[/b] {title} [i]{length}[/i]\n".format(track=file.track[0], title=file.title[0], length=time_str(file.length))
			
			album_bio += "\n"
			album_bio += "[b]Total length:[/b] {length}\n".format(length=time_str(total_length))
			album_bio += "\n"
			album_bio += "More Information: [url](INSERT URL HERE)[/url]"
			
			output_file = open("album_bio.txt", "w+")
			output_file.write(album_bio)
			output_file.close()

			print "Successfully generated text File"

		else:
			print "Support for single files coming soon "
			
raw_input('Press Enter to exit')