welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the Lightning", "Metallica", 1984


title, artist, year=metallica
print(title)
print(artist)
print(year)

# in table , their coder need to rememver the index . chances of being mistake
table = ("Coffee table", 200, 100, 75, 34.50)
print(table[1] * table[2])

#so better approch is unpack the tupple
name, length, width, height, price = table
print(length * width)