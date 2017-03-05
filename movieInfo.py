import mediaInfo
import fresh_tomatoes

theSoundOfMusic = mediaInfo.Movie("The Sound of Music",
                                  "Musical abt true love, friendship, bravery, sacrifice",
                                  #"https://placeholdit.imgix.net/~text?txtsize=28&txt=300%C3%97600&w=300&h=600",
                                  "https://image.tmdb.org/t/p/w1280/459fPVvI4lkEV0piSfcq0irKHi8.jpg",
                                  "https://www.youtube.com/watch?v=jITsImZdlMQ")
#theSoundOfMusic.showTrailer()

                                   
loveAffair = mediaInfo.Movie("Love Affair",
                             "A remake of the classic love story An Affair to Remember",
                             "https://image.tmdb.org/t/p/w1280/kdaPkR5QMFMxwtN80gqLwuOgCMY.jpg",
                             "https://www.youtube.com/watch?v=qvHxbZBlwZ0")
#loveAffair.showTrailer()

anAffairToRemember = mediaInfo.Movie("An Affair to Remember",
                                     "A couple falls in love and agrees to meet in six months at the Empire State Building - but will it happen?",
                                     "https://image.tmdb.org/t/p/w1280/6pTbj6YujsjcGZaDbEanAKCE1Zs.jpg",
                                     "https://www.youtube.com/watch?v=2aNbwUxqgp8")
#anAffairToRemember.showTrailer()

sabrina = mediaInfo.Movie("Sabrina",
                          "An ugly duckling having undergone a remarkable change, still harbors feelings for her crush",
                          "https://image.tmdb.org/t/p/w1280/jQh15y5YB7bWz1NtffNZmRw0s9D.jpg",
                          "https://www.youtube.com/watch?v=twTksx_lWB4")
#sabrina.showTrailer()

sleeplessInSeattle = mediaInfo.Movie("Sleepless in Seattle",
                                     "A recently widowed man's son calls a radio talk-show in an attempt to find his father a partner.",
                                     "https://image.tmdb.org/t/p/w1280/afkYP15OeUOD0tFEmj6VvejuOcz.jpg",
                                     "https://www.youtube.com/watch?v=-Lj2U-cmyek")
#sleeplessInSeattle.showTrailer()

theAmericanPresident = mediaInfo.Movie("The American President",
                                       "A widowed U.S. president and a lobbyist fall in love.",
                                       "https://image.tmdb.org/t/p/w1280/lvAvpWDySHra0ZK39wFy7No4h3A.jpg",
                                       "https://youtu.be/UrC75wUKoFM")
#theAmericanPresident.showTrailer()

movies = [theSoundOfMusic, loveAffair, anAffairToRemember, sabrina, sleeplessInSeattle, theAmericanPresident]
fresh_tomatoes.open_movies_page(movies)

