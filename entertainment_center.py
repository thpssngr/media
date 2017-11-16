import fresh_tomatoes
import media

snatch = media.Movie("Snatch",
                    "a movie about diamonds",
                    "2000",
                    "https://upload.wikimedia.org/wikipedia/en/a/a7/Snatch_ver4.jpg",
                    "https://www.youtube.com/watch?v=9Jar2XkBboo")

revolver = media.Movie("Revolver",
                    "a movie about gambling",
                    "2005",
                    "https://upload.wikimedia.org/wikipedia/en/b/b6/Revolver2005.jpg",
                    "https://www.youtube.com/watch?v=M9JAYfZOHms")

lockstock = media.Movie("Lock Stock and two smoking Barrels",
                    "a movie about old guns",
                    "1998",
                    "https://upload.wikimedia.org/wikipedia/en/e/e9/Lock%2C_Stock_and_Two_Smoking_Barrels_2.jpg",
                    "https://www.youtube.com/watch?v=KZh33gGK3Y8")

rocknrolla = media.Movie("RocknRolla",
                    "a movie about diamonds",
                    "2008",
                    "https://upload.wikimedia.org/wikipedia/en/9/98/Rocknrolla_ver3.jpg",
                    "https://www.youtube.com/watch?v=TdpR8VuvbCM")

sherlock = media.Movie("Sherlock Holmes",
                    "a movie about a detective",
                    "2009",
                    "https://upload.wikimedia.org/wikipedia/en/e/e0/Sherlock_holmes_ver5.jpg",
                    "http://www.youtube.com/watch?v=Egcx63-FfTE")

sherlock_gos = media.Movie("Sherlock Holmes - Game of Shadows",
                    "another movie about a detective",
                    "2011",
                    "https://upload.wikimedia.org/wikipedia/en/5/53/Sherlock_Holmes2Poster.jpg",
                    "https://www.youtube.com/watch?v=V1OYiPa-eLg")

# kingarthur = media.Movie("Sherlock Holmes - Game of Shadows",
#                     "a movie about a sword",
#                     "https://upload.wikimedia.org/wikipedia/en/a/a4/King_Arthur_LotS_poster.jpg",
#                     "http://www.youtube.com/watch?v=4luDtkC3Oy0")

movies = [snatch, revolver, lockstock, rocknrolla, sherlock, sherlock_gos]
fresh_tomatoes.open_movies_page(movies)
#print (media.Movie.VALID_RATINGS)
