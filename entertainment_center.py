import media
import fresh_tomatoes

#instantiate movies
toy_story = media.Movie("Toy Story", #this one is from the instructor
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")
avatar = media.Movie("Avatar", #this one is from the instructor
                    "A marine on an alien planet",
                    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                    "https://www.youtube.com/watch?v=5PSNL1qE6VY")

for_s_marshall = media.Movie("Forgetting Sarah Marshall",
                            "Man has trouble getting over ex",
                            "https://upload.wikimedia.org/wikipedia/en/7/7c/Forgetting_sarah_marshall_ver2.jpg",
                            "https://www.youtube.com/watch?v=PyVEHIO6jZ0")
the_sting = media.Movie("The Sting",
                        "About a heist",
                        "https://upload.wikimedia.org/wikipedia/en/9/9c/Stingredfordnewman.jpg",
                        "https://www.youtube.com/watch?v=LN2hBOIXhBs")
oceans_eleven = media.Movie("Oceans Eleven",
                            "Daniel Ocean and his pals rob a casino",
                            "https://upload.wikimedia.org/wikipedia/en/a/ae/Ocean%27sEleven%281960%29Poster.jpeg",
                            "https://www.youtube.com/watch?v=ppVby97BNiw")
tommy_boy = media.Movie("Tommy Boy",
                        "The misfit boss's son has to save the factoryx",
                        "https://upload.wikimedia.org/wikipedia/en/f/f8/Tommy_Boy.jpg",
                        "https://www.youtube.com/watch?v=6nQ4K2bvVxY")

#organize movies as list, then pass into function from fresh tomatoes to open website
movies = [toy_story,avatar,for_s_marshall,the_sting,oceans_eleven,tommy_boy]
fresh_tomatoes.open_movies_page(movies)