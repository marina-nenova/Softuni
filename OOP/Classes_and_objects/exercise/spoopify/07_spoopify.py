from Classes_and_objects.exercise.spoopify.project.album import Album
from Classes_and_objects.exercise.spoopify.project.band import Band
from Classes_and_objects.exercise.spoopify.project.song import Song

song = Song("Running in the 90s", 3.45, False)
print(song.get_info())
album = Album("Initial D", song)
second_song = Song("Around the World", 2.34, False)
print(album.add_song(second_song))
print(album.details())
print(album.publish())
band = Band("Manuel")
print(band.add_album(album))
print(band.remove_album("Initial D"))
print(band.details())
