def Chorus(p1):     
    print("You put your", p1, "in") 
    print("You put your", p1, "out")     
    print("You put your", p1, "in") 
    print("And you shake it all about,") 
    print("You do the hokey pokey") 
    print("and you turn yourself around") 
    print("That’s what it's all about.") 
fingers = ["right hand", "left hand", "right foot"] 
printt = lambda x: Chorus(x)
for fing in fingers:
    printt(fing)