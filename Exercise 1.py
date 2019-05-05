
journey = """Just a small tone girl
Leaving in a lonely whirl
She took the midnight tray going anywhere
Just a seedy boy
Bored and raised in South Detroit or something
He took the midnight tray going anywhere"""

journey = (journey
.replace("tone","town")
.replace("Leaving", "Livin'")
.replace("whirl", "world")
.replace("tray", "train", 2)
.replace("going","goin'")
.replace("seedy","city")
.replace("Bored", "Born")
.replace("or something","")
)
#newJourney = journey.replace("tone", "town")
#newJourney2 = newJourney.replace("Leaving", "Livin'")
#newJourney3 = newJourney2.replace("whirl", "world")
#newJourney4 = newJourney3.replace("tray","train", 2)
#newJourney5 = newJourney4.replace("going","goin'")
#newJourney6 = newJourney5.replace("seedy","city")
#newJourney7 = newJourney6.replace("Bored", "Born")
#newJourney8 = newJourney7.replace("or something","")
print(journey)
