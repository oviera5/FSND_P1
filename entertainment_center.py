import fresh_tomatoes
import media

""" Instantiates six instances of the Movie class from the media module.

    All six instances are placed in a movies list.

    The movies list is used as argument within the open_movies_page method
    from the imported fresh_tomatoes module.
"""

the_martian = media.Movie(
    "The Martin",
    "Astronaut gets stranded on Mars",
    "https://upload.wikimedia.org/wikipedia/en/c/c3/The_Martian_2014.jpg",
    "http://youtu.be/Ue4PCI0NamI",
    "2015",
    "Matt Damon")

prometheus = media.Movie(
    "Prometheus",
    "Space explorers in search of mankind's orgins",
    "https://upload.wikimedia.org/wikipedia/en/a/a3/Prometheusposterfixed.jpg",
    "http://www.youtube.com/watch?v=sftuxbvGwiU",
    "2012",
    "Charlize Theron")

interstellar = media.Movie(
    "Interstellar",
    "Astronauts sent across the galaxy in search of mankind's new home",
    ("https://upload.wikimedia.org/wikipedia/en/b/bc/"
     "Interstellar_film_poster.jpg"),
    "http://youtu.be/0vxOhd4qlnA",
    "2014",
    "Matthew Mcconaughey")

space_odyssey = media.Movie(
    "2001: A Space Odyssey",
    "Astronauts are sent on a mysterious mission",
    ("https://upload.wikimedia.org/wikipedia/en/e/ef/"
     "2001_A_Space_Odyssey_Style_B.jpg"),
    "http://youtu.be/E8TABIFAN4o",
    "1968",
    "Keir Dullea")

gravity = media.Movie(
    "Gravity",
    ("A medical engineer and astronauts are stranded in deep space "
     "with no link to Earth"),
    "https://upload.wikimedia.org/wikipedia/en/f/f6/Gravity_Poster.jpg",
    "http://youtu.be/OiTiKOy59o4",
    "2013",
    "Sandra Bullock")

moon = media.Movie(
    "Moon",
    ("A man experiences a personal crisis as he nears the end of a three-year "
     "solitary stint mining on the far side of the Moon"),
    ("https://upload.wikimedia.org/wikipedia/en/b/b0/"
     "Moon_%282008%29_film_poster.jpg"),
    "http://youtu.be/twuScTcDP_Q",
    "2009",
    "Sam Rockwell")

movies = [the_martian, prometheus, interstellar, space_odyssey, gravity, moon]

fresh_tomatoes.open_movies_page(movies)
