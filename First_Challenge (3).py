# This is a simple test to qualify you for the vacation!


name = input("What is your name? ")
age = int(input("How old are you? {0} ".format(name)))

if (age > 17) and (age < 31): #They are the correct age to attend
    print("You are welcome on the holiday, {}!".format(name))

elif (age > 32): #Too Old to attend
    print("Unfortunately {} you are too old to attend the vacation, get younger you old fuck!".format(name))

else:
    (age < 16) #They are too young to attend
    print("Im sorry {} unfortunately you cannot attend the vacation as you are too young!".format(name))