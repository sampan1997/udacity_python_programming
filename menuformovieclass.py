import media
import fresh_tomatoes
toy_story=media.Movie("toy story","sam toystory very good","","www.google.com")
print(toy_story.title)
avatar=media.Movie("avatar","kaniska jungle avatar","","www.youtube.com/patiala_peg")
print(avatar.storyline)
#avatar.showtrailer()
fresh_tomatoes.open_movies_page([ toy_story,avatar])
#avatar.storyline="sam"
#print(avatar.storyline)
print(media.Movie.__doc__)
print(media.Movie.__module__)
