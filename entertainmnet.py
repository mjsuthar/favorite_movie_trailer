import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A boy and their Toys stories",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

Avengers = media.Movie("The Avengers (2012)",
                       "Action Movie there superhumens which are protact to earth",
                       "https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg",
                       "https://www.youtube.com/watch?v=eOrNdBpGMv8")

pyar_ka_punchnama = media.Movie("Pyar ka Punchnama 2",
                               "Indian movie based on golddigers girls",
                               "https://upload.wikimedia.org/wikipedia/en/0/06/Pyaar-Ka-Punch.jpg",
                               "https://www.youtube.com/watch?v=tC-HGUhxyyc")

gangs_of_washepur = media.Movie("Gangs of washepur I",
                                "some bihari alternatively each other to show their power",
                                "https://upload.wikimedia.org/wikipedia/en/6/6a/Gangs_of_Wasseypur_poster.jpg",
                                "https://www.youtube.com/watch?v=j-AkWDkXcMY")
ghost_rider = media.Movie("Ghost Rider",
                         "A person who take punishment people sins",
                         "https://upload.wikimedia.org/wikipedia/en/7/71/GhostRiderBigPoster.jpg",
                         "https://www.youtube.com/watch?v=XE4PPJBazyw")
mission_impossible_3 = media.Movie("Mission Impossible III",
                                 "Action movie, American secret Agent group call M.I.",
                                 "https://upload.wikimedia.org/wikipedia/en/b/bc/Mission_Impossible_III.jpg",
                                 "https://www.youtube.com/watch?v=ssWbGKTgXFc")
movies = [toy_story,Avengers,pyar_ka_punchnama,gangs_of_washepur,ghost_rider,mission_impossible_3]
fresh_tomatoes.open_movies_page(movies)
