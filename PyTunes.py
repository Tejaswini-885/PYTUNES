from pygame import mixer


class Node:
    def __init__(self, data1, next1=None, prev1=None):
        self.data = data1
        self.next = next1
        self.prev = prev1


song1 = Node("./audiofile/Chaleya.mp3")
song2 = Node("./audiofile/Heeriye.mp3")
song3 = Node("./audiofile/GulabiSadi.mp3")
song1.prev = song3
song1.next = song2
song2.prev = song1
song2.next = song3
song3.prev = song2
song3.next = song1

songs = song1

# Starting the mixer
mixer.init()

# Loading the song
mixer.music.load(songs.data)

# Setting the volume
mixer.music.set_volume(0.7)

# Start playing the song
mixer.music.play()

# infinite loop
while True:
    print("press 'b' to go to prev song, 'n' to go to next song")
    print("Press 'p' to pause, 'r' to resume")
    print("Press 'e' to exit the program")
    query = input("  ")

    # For moving to next song
    if query == 'n':
        mixer.music.stop()
        songs = songs.next
        mixer.music.load(songs.data)
        mixer.music.play()
    # For moving to before song
    elif query == 'b':

        mixer.music.stop()
        songs = songs.prev
        mixer.music.load(songs.data)
        mixer.music.play()
    # To pause a song
    elif query == 'p':

        # Pausing the music
        mixer.music.pause()
    # To resume a song
    elif query == 'r':

        # Resuming the music
        mixer.music.unpause()
    # To stop the music player
    elif query == 'e':

        # Stop the mixer
        mixer.music.stop()
        break
