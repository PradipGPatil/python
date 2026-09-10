welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the Lightning", "Metallica", 1984

print(metallica)

print(metallica[0])
print(metallica[1])
print(metallica[2])

# if we try to assing value it will give an error
#metallica[0]="master of puppet"

# so if need to can convert this into the list
metallica2=list(metallica)
print(metallica2)

metallica2[0]="master of puppet"
print(metallica2)