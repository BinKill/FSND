import media
import fresh_tomatoes

# Creates a new Movie instance with the following parameters
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life.",
                        "November 22, 1995",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",  # noqa
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "December 18, 2009",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",  # noqa
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")

the_social_network = media.Movie("The Social Network",
                                 "The story of Mark Zuckerburg.",
                                 "October 1, 2010",
                                 "https://upload.wikimedia.org/wikipedia/en/7/7a/Social_network_film_poster.jpg",  # noqa
                                 "https://www.youtube.com/watch?v=lB95KLmpLR4")

i_am_legend = media.Movie("I Am Legend",
                          "A sole survivor in post apocolyptic New York.",
                          "December 14, 2007",
                          "https://upload.wikimedia.org/wikipedia/en/d/df/I_am_legend_teaser.jpg",  # noqa
                          "https://www.youtube.com/watch?v=ewpYq9rgg3w")

life_of_pi = media.Movie("Life of Pi",
                         "A boy trapped on a boat with a tiger.",
                         "November 21, 2012",
                         "https://upload.wikimedia.org/wikipedia/en/5/57/Life_of_Pi_2012_Poster.jpg",  # noqa
                         "https://www.youtube.com/watch?v=mZEZ35Fhvuc")

catch_me_if_you_can = media.Movie("Catch me if you Can",
                                  "A true story of a con artist.",
                                  "December 25, 2002",
                                  "https://upload.wikimedia.org/wikipedia/en/4/4d/Catch_Me_If_You_Can_2002_movie.jpg",  # noqa
                                  "https://www.youtube.com/watch?v=xas1UyTiVUw")  # noqa


# Adds all movie's to the movies array
movies = [toy_story, avatar, the_social_network, i_am_legend, life_of_pi, catch_me_if_you_can]  # noqa

# passes the movies array too the open_movies_page() function
fresh_tomatoes.open_movies_page(movies)
