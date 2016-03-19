import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", # Creates a new Movie instance with the following parameters
                        "A story of a boy and his toys that come to life.",
                        "November 22, 1995",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar",                     
                     "A paraplegic marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.",
                     "December 18, 2009",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")

the_social_network = media.Movie("The Social Network",
                                 "The story of Mark Zuckerburg and his creation of popular online Social Network Facebook.",
                                 "October 1, 2010",
                                 "https://upload.wikimedia.org/wikipedia/en/7/7a/Social_network_film_poster.jpg",
                                 "https://www.youtube.com/watch?v=lB95KLmpLR4")

i_am_legend = media.Movie("I Am Legend",
                          "Years after a plague kills most of humanity and transforms the rest into monsters, the sole survivor in New York City struggles valiantly to find a cure.",
                          "December 14, 2007",
                          "https://upload.wikimedia.org/wikipedia/en/d/df/I_am_legend_teaser.jpg",
                          "https://www.youtube.com/watch?v=ewpYq9rgg3w")

life_of_pi = media.Movie("Life of Pi",
                         "A young man who survives a disaster at sea is hurtled into an epic journey of adventure and discovery. While cast away, he forms an unexpected connection with another survivor: a fearsome Bengal tiger.",
                         "November 21, 2012",
                         "https://upload.wikimedia.org/wikipedia/en/5/57/Life_of_Pi_2012_Poster.jpg",
                         "https://www.youtube.com/watch?v=mZEZ35Fhvuc")

catch_me_if_you_can = media.Movie("Catch me if you Can",
                                  "A true story about Frank Abagnale Jr., who, before his 19th birthday, successfully conned millions of dollars' worth of checks as a Pan Am pilot, doctor, and legal prosecutor.",
                                  "December 25, 2002",
                                  "https://upload.wikimedia.org/wikipedia/en/4/4d/Catch_Me_If_You_Can_2002_movie.jpg",
                                  "https://www.youtube.com/watch?v=xas1UyTiVUw")


movies = [toy_story, avatar, the_social_network, i_am_legend, life_of_pi, catch_me_if_you_can]

fresh_tomatoes.open_movies_page(movies)	
