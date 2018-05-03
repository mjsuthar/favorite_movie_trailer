import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A boy and their Toys stories",
                        "https://sco.wikipedia.org/wiki/File:Toy_Story_3_poster.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

movies = [toy_story]
fresh_tomatoes.open_movies_page(movies)
