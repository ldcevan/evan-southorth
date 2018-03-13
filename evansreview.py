"""
this is a program that will ask a user to reveiw some sort of media. 
this will store this in a python listcthis will also be able to then move data into a new list based on what the user input.
"""

media_type = input("what is your media type?")
media_title = input("what is the title of your media?")

print "wow, i like that media too!"

year_created = input("when was your media created?")
media_genre = input("what is your media's genre?")

print "on a sacale of 1 to 10 I would rate that a 10!"

hip_hop = [media_type, media_title, year_created, media_genre]

print str(hip_hop)

country = []

if media_type == "music" and media_genre == "country":
    country.append('wagon wheel')
else:
    hip_hop.append('gods plan')

print (country)
