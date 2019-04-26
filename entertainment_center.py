import fresh_tomatoes
import media

# Create Instances of class Movie
# How to train dragon movie = movie title, poster image and movie trailer
how_to_train_dragon = media.Movie(
        "How to train a dragon",
        "https://upload.wikimedia.org/wikipedia/en/f/fd/How_to_Train_Your_Dragon_3_poster.png",  # NOQA
        "https://www.youtube.com/watch?v=_OJB3jrdTzQ"
        )

# The Grinch movie = movie title, poster image and movie trailer
the_grinch = media.Movie(
        "The Grinch",
        "https://upload.wikimedia.org/wikipedia/en/4/4f/The_Grinch%2C_final_poster.jpg",  # NOQA
        "https://www.youtube.com/watch?v=_UOh0UX3alI"
        )

# Smallfoot movie = movie title, poster image and movie trailer
smallfoot = media.Movie(
        "Smallfoot",
        "https://upload.wikimedia.org/wikipedia/en/e/e8/Smallfoot_%28film%29.png",  # NOQA
        "https://www.youtube.com/watch?v=uBw6EvIxIS8"
        )

# Incredibles 2 movie = movie title, poster image and movie trailer
incredibles_2 = media.Movie(
        "Incredibles 2",
        "https://upload.wikimedia.org/wikipedia/en/2/27/The_Incredibles_2.jpg",  # NOQA
        "https://www.youtube.com/watch?v=i5qOzqD9Rms"
        )

# Early man movie  = movie title, poster image and movie trailer
early_man = media.Movie(
        "Early Man",
        "https://upload.wikimedia.org/wikipedia/en/0/04/Early_Man_Poster.jpg",  # NOQA
        "https://www.youtube.com/watch?v=ZRiPQ8YNrVs"
        )

# Coco movie = movie title, poster image and movie trailer
coco = media.Movie(
        "Coco",
        "https://upload.wikimedia.org/wikipedia/en/9/98/Coco_%282017_film%29_poster.jpg",  # NOQA
        "https://www.youtube.com/watch?v=zNCz4mQzfEI"
        )

# Create List containing the instances of class Movie
movies = [
    how_to_train_dragon,
    the_grinch, smallfoot,
    incredibles_2,
    early_man,
    coco
    ]

# Open the HTML file in a webbrowser via fresh_tomatoes.py file
fresh_tomatoes.open_movies_page(movies)
