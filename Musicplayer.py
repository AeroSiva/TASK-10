#Visit https://github.com/rvsp/typescript-oops/blob/master/Practice/music-player.md 
#and convert the UML diagram into Python Class and Methods.


'''Create a music player web app using html, oops, typescript and bootstrap with the following features.

Users can create audio using URLs available online.
Users can create multiple Playlists based on the genre of the song.
Users can add multiple audio files into each playlist created.
Users can search audio by name.
Users can search the playlist by name.
Users can give ratings to playlist and audio. Rating displayed is the average rating calculated after each submission.
For displaying Average rating:
Create 3 users and randomly generate ratings from 1 to 5.
find the average rating from the random number generated and display it in the front end.'''




class Music_player:
    def __init__(self) -> None:
        self.playlist = {"Melody": ["ms1","ms2","ms3"],
                        "Motivation": ["Mos1","Mos2","Mos3"],
                        "Folk":["Fs1","Fs2","Fs3"],
                        "Lastest":["ls1","ls2","ls3"],
                        }
        self.personalised_playlist = {}
        self.ratings = 0
        self.ratings_lst = []

# To create personalised playlist- can choose sings from either inbuilt playlist or from url
        
    def create_playlist (self):
        genre = input('''Enter the genre to create your playlist or 
        select one from the options: Melody Motivation Folk Lastest URL or enter new genre : ''')
        if genre in self.playlist.keys():
            self.personalised_playlist[genre] = []
            self.select_songs(genre)
        else:
            self.personalised_playlist[genre] = []
            self.create_audio_url(genre)
        print("Songs are added to the ",genre)
        
# To select songs inbuilt playlist or enter song url from internet  
    def select_songs(self,genre):
        print (f"Select songs from the list {self.playlist[genre]}")
        songs = input("Enter name of songs (seperated by comma): ")
        songs = [song.strip() for song in songs.split(',')]
        for song in songs:
            self.add_song_to_genre(song,genre)
        self.create_audio_url(genre)

# To add songs from inbuilt playlist/ url to personalised playlist 
    def add_song_to_genre (self,song,genre):
        if song not in self.personalised_playlist[genre]:
            self.personalised_playlist[genre].append(song)
            return "The audio song", self.personalised_playlist[genre]," added to the",genre," playlist"
        else:
            return "The audio song",song," already in the",genre," Playlist"
    
# To provide options to add song url  
    def create_audio_url (self,genre):
        url = input("Enter the song url: ")
        if url:
            song = url
            self.add_song_to_genre (song,genre)
     
# To show playlist and personalised playlist
    def print_plst (self):
        print(self.playlist)
        print(self.personalised_playlist)

# To search songs or genres from inbulit playlist and personalised playlist
    def search_songs (self,search_item):
        if search_item in self.playlist:
            print (self.playlist[search_item])
        elif  search_item in self.personalised_playlist:
            print (self.personalised_playlist[search_item])
        for genre in self.playlist.keys():
            if search_item in self.playlist[genre]:
                print (search_item,"is found in the playlist",genre)
        for genre in self.personalised_playlist.keys():
            if search_item in self.personalised_playlist[genre]:
                print (search_item,"is found in the playlist",genre)
        else:
            print( search_item ,"is not found in the music player")
    
# To get ratings from 3 users   
    def rating(self): # default value is 3
        for user in range (3):
            while True:
                rate = int(input("Enter your ratings for songs and playlist in the range from 1 to 5: "))
                if 1<= rate <=5: 
                    self.ratings_lst.append(rate)
                    break
                else:
                    print("Warning only from 1to 5: ")
        self.ratings = sum(self.ratings_lst) / len(self.ratings_lst)
        return ("Ovrall rating is: ",self.ratings)
        
# To generate random ratings for 3 users     
    def random_ratings(self,user_count=3):
        import random
        for user in range (user_count):
            rate = random.randint(1,5) # create random ratings
            self.ratings_lst.append(rate)
        self.ratings = sum(self.ratings_lst) / len(self.ratings_lst)
        return ("Ovrall rating is: ",self.ratings)




mp = Music_player()
# Creating playlist
print("Creating playlist by selecting songs already in playlist")
re = mp.create_playlist()   # Select Melody / motivation. if playlist already presents it shows the songs from it
print("Creating playlist by creating Hit list ( song url = Arjunaru villu)")
re = mp.create_playlist()   # create playlist name hit_songs  and add "Arjunaru villu" as url
re = mp.print_plst()
print("searching for melody songs")
re = mp.search_songs("Melody")
print("Searching for ms1 song")
re = mp.search_songs("ms1")
print("searching for Arjunaru villu song added using create playlist and linked url ")
re = mp.search_songs("Arjunaru villu")   #
print("user input rating")
re = print(mp.rating())
print("random ratings:")
re = print(mp.random_ratings())

