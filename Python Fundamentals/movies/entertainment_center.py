import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", "A story of a boy and his toys.", "http://ia.media-imdb.com/images/M/MV5BNTE2Njk1NjcxMl5BMl5BanBnXkFtZTYwMDkyOTA5._V1_SX640_SY720_.jpg", "https://www.youtube.com/watch?v=KYz2wyBy3kc")

#print(toy_story.storyline)


avatar = media.Movie("Avatar", "Marine on planet", "http://www.goldposter.com/wp-content/uploads/2015/05/Avatar_poster_goldposter_com_56.jpg", "https://www.youtube.com/watch?v=KYz2wyBy3kc")

#print(avatar.storyline)
#avatar.show_trailer()

my_cousin_vinny = media.Movie("My Cousin Vinny", "NY Lawer Alabama", "http://ia.media-imdb.com/images/M/MV5BMTQxNDYzMTg1M15BMl5BanBnXkFtZTgwNzk4MDgxMTE@._V1_SX214_AL_.jpg", "https://www.youtube.com/watch?v=SL4HdaZXuOw")

movies = [toy_story, avatar, my_cousin_vinny]
fresh_tomatoes.open_movies_page(movies)
