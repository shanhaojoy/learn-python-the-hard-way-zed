print "you enter a dark room with two doors.do you go through a door #1 or #2?"

door=raw_input(">")

if door=="1":
    print "there's a giant bear eating a cheese cake. waht do you do?"
    print"1.take the cake "
    print"2.scream the bear."
    
    bear=raw_input(">")
    
    if bear=="1":
       print "the bear eats your face off."
    elif bear=="2":
        print"the bear eats your legs off"
    else:
        print"well,the bear runs away.%s is good"%bear
        
elif door=="2":
    print "you stare into the endless abyss at cthulhu's retina."
    
    print"1.blueberries\n 2.yellow jacket clothespins.\n 3.understanding revolvers yelling melodies."
    
    insanity=raw_input(">")
    
    if insanity=="1" or insanity=="2":
        print "your body survives"
    else:
        print "the insanity rots your eyes into a pool of muck."
else:
    print "fall on a knife and die."