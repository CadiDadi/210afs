# For this project you will create a simple media player that will use Data structure(s) to store a playlist of songs with the functions outlined below. (Note: Your media player program WILL NOT actually play any songs)  For this project you can ONLY use the following data structures covered in this course: Linked List (Singly or Doubly), Stacks, Queues, Graphs and Trees.  You CAN NOT use a third party library or code written by someone else outside of this course.

#  Your task:

# 1. In your Week 7 folder, create a folder called ‘capstone_project’ for this assignment.
# 2. Download the file mediaplayer.py into the folder 'capstone_project'
# 3. Edit mediaplayer.py and complete the code for each of the menu choices.
# - Add songs to a playlist
# - Remove songs from a playlist
# - Play the current selected song, default is the first song on the playlist
# - Skip to the next song on the playlist. If at end of list, restart from the beginning
# - Go back to the previous song on the playlist.  If at the start, go back to the end of the list.
# - Randomly shuffle the song list - Create your own algorithm to randomly sort the data structure you have chosen to use.  This algorithm does not need to be efficient.
# - Show Currently Playing Song
# - Show Current Playlist Order
# 4. Preload your playlist with at least six songs of your choice
# 5. Test your code to ensure that all of the menu options are working as expected.


class Song:
    def __init__(self,title,artist):
        self.title = title
        self.artist = artist

    def getTitle(self):
        return self.title

    def getArtist(self):
        return self.artist
        
    def __str__(self):
        return self.title + " by " + self.artist 

    def __eq__(self, other):
        return ((self.title, self.artist) == (other.title, other.artist))
        
    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return ((self.title, self.artist) < (other.title, other.artist))
        
    def __gt__(self, other):
        return ((self.title, self.artist) < (other.title, other.artist))
        
class Controls:
    def __init__(self):




    def add(self, title, artist):
        
    def delete(self, ):

    def playFromStart(self, ):
    
    def skip(self, ):

    def prev():

    def shuffle():

    def current():
    
    def showList():

mediaPlayer = Controls()

# boring but using #s to ensure working correctly
mediaPlayer.add("song1","artist1")
mediaPlayer.add("song2","artist2")
mediaPlayer.add("song3","artist3")
mediaPlayer.add("song4","artist4")
mediaPlayer.add("song5","artist5")
mediaPlayer.add("song6","artist6")

def menu():
    print(20 * "-" , "MENU" , 20 * "-")
    print("1. Add Song to Playlist")
    print("2. Remove song from Playlist")
    print("3. Play")
    print("4. Skip")
    print("5. Go Back")
    print("6. Shuffle")
    print("7. Show Currently Playing Song")
    print("8. Show Current Playlist Order")
    print("0. Exit")
    print(47 * "-")

while True:
    menu()
    choice = int(input())

    if choice == 1:
        # Add code to prompt user for Song Title and Artist Name
        artist = input("A. Add song to playlist - please input the artist: ")
        title = input("B. Add song to playlist - Please input the song title: ")
        # Add song to playlist
        mediaPlayer.add(artist, title)
        print(title + " was added to the Playlist")
    elif choice == 2:   
        # Prompt user for Song Title 
        title = input("Delete song from playlist - please input the title of the song to be deleted: ")
        # remove song from playlist
        mediaPlayer.delete(title)
        print(title + " was removed from the Playlist")
    elif choice == 3:
        # Play the playlist from the beginning
        # Display song name that is currently playing
        print("Playing Playlist from start")  
        mediaPlayer.playFromStart()          
    elif choice == 4:
        # Skip to the next song on the playlist
        # Display song name that is now playing
        print("Skipping....") 
        mediaPlayer.skip()                    
    elif choice == 5:
        # Go back to the previous song on the playlist
        # Display song name that is now playing
        print("Replaying....")  
        mediaPlayer.prev()
        print()
    elif choice == 6:
        # Randomly shuffle the playlist and play the first song
        # Display song name that is now playing
        print("Shuffling....")    
        mediaPlayer.shuffle()
    elif choice == 7:
        # Display the song name and artist of the currently playing song
        print("Currently playing: ", end=" ")  
        mediaPlayer.current()  
    elif choice == 8:
        # Show the current song list order
        print("\nSong list:\n")
        print(mediaPlayer.showList)
    elif choice == 0:
        print("Goodbye.")
        break

            
