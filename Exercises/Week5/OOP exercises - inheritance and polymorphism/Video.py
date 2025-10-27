class Video:
    def __init__(self, title: str, genre: str, rating: float):
        self.title = title
        self.genre = genre 
        self.rating = rating
    def info(self) -> str:
        return (f"Video with title {self.title}, genre {self.genre} and rating {self.rating}")

class TV_serie(Video):
    def __init__(self, title: str, genre: str, rating: float, num_episodes: int):
        super().__init__(title, genre, rating)
        self.num_episodes = num_episodes
    def info(self) -> str:
        return (f"TV series with title {self.title}, genre {self.genre}, "
                f"rating {self.rating} and episodes {self.num_episodes}")

class Movie(Video):
    def __init__(self, title: str, genre: str, rating: float, duration: float):
        super().__init__(title, genre, rating)
        self.duration = duration
    def info(self) -> str:
        return (f"Movie with title {self.title}, genre {self.genre}, "
                f"rating {self.rating}, duration {self.duration} minutes")

class Documentary(Video):
    def __init__(self, title: str, genre: str, rating: float):
        super().__init__(title, genre, rating)
    def info(self) -> str:
        return (f"Documentary - {super().info()}")
    
pokemon = TV_serie("Pokemon", "Cartoon", 4.5, 550)
titanic = Movie("Titanic", "Romance", 4.7, 194)
code = Documentary("The Code", "Math", 4)

for video in tuple((pokemon, titanic, code)):
    print(video.info())