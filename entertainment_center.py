import fresh_tomatoes
import media

# Create Instances of class Movie

how_to_train_dragon = media.Movie("How to train a dragon",
                        "https://upload.wikimedia.org/wikipedia/en/f/fd/How_to_Train_Your_Dragon_3_poster.png",
                        "https://www.youtube.com/watch?v=_OJB3jrdTzQ")

the_grinch = media.Movie("The Grinch",
                        "https://upload.wikimedia.org/wikipedia/en/4/4f/The_Grinch%2C_final_poster.jpg",
                        "https://www.youtube.com/watch?v=_UOh0UX3alI")

smallfoot = media.Movie("Smallfoot",
                        "https://upload.wikimedia.org/wikipedia/en/e/e8/Smallfoot_%28film%29.png",
                        "https://www.youtube.com/watch?v=uBw6EvIxIS8")

incredibles_2 = media.Movie("Incredibles 2",
                        "https://upload.wikimedia.org/wikipedia/en/2/27/The_Incredibles_2.jpg",
                        "https://www.youtube.com/watch?v=i5qOzqD9Rms")

early_man = media.Movie("Early Man",
                        "https://upload.wikimedia.org/wikipedia/en/0/04/Early_Man_Poster.jpg",
                        "https://www.youtube.com/watch?v=ZRiPQ8YNrVs")

coco = media.Movie("Coco",
                        "https://upload.wikimedia.org/wikipedia/en/9/98/Coco_%282017_film%29_poster.jpg",
                        "https://www.youtube.com/watch?v=zNCz4mQzfEI")

# Create List containing the instances of class Movie 
movies = [how_to_train_dragon, the_grinch, smallfoot, incredibles_2, early_man, coco]
#Open the website featuring movies mentioned above
fresh_tomatoes.open_movies_page(movies)