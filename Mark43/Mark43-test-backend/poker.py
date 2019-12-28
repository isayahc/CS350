from collections.abc import Sequence
import copy
from itertools import groupby
import sys
from collections import Counter
class card(Sequence):
    def __init__(self,n):
        """This is creating a card object. based a string with 2 characters. 
        The first character will be the rank and the second character will be the suit
        """
        self.n = n
        super().__init__()
        self.rank = n[0]
        self.suit = n[1]

    def __getitem__(self, i):
        """ returns either the first or second character"""
        return self.n[i]
    
    def __len__(self):
        """Return the length of a card item"""
        return(self.L)

    def Keyval(self):
        return dict ({self.rank: self.suit})

    def getrank(self):
        """getrank returns the rank of a card object"""
        ranks =  dict = {"T":10,"J":11, "Q":12, "K":13, "A":14 }
        if str(self.rank)  in ranks:
            return ranks[self.rank]
        else:
            return int(self.rank)
    
    def getsuit(self):
        """return the suit of a card object"""
        return self.suit
    
    def getcard(self):
        """returns both the rank and suit in a tuple"""
        return tuple((self.getrank(),self.getsuit()))
    
class Hand():
    """A Hand consist of three card objects a,b,c"""
    def __init__(self, a, b, c):
        self.a = a.getcard() 
        self.b = b.getcard()
        self.c = c.getcard()

    def getcards(self):
        """return each card item in a list"""
        return list([self.a,self.b,self.c])

    def getdictionary(self):
        """returns a dictionary with suit being the key and rank being the value"""
        d = dict()
        for x,y in self.getcards():
            if y not in d:
                d[y]= list()
            if y in d:
                d[y].append(x)
        return d 
        
    def getranks(self):
        """returns all of the ranks in the cards objects in a sorted list"""
        l = list()
        for x,y in self.getcards():
            l.append(x)
        return sorted(l)

    def getsuits(self):
        """returns all of the suits in a list"""
        l = list()
        for x,y in self.getcards():
            l.append(y)
        return l

    def all_equal_ranks(self):
        """returns true if all of the ranks in an Hand object match"""
        iter = self.getranks()
        g = groupby(iter)
        return next(g, True) and not next(g, False)

    def all_equal_suits(self):
        """returns true if all of the suits in an Hand object match"""
        try:
            x = self.getsuits()
            g = groupby(self.getsuits()) #acting strangwe
        except TypeError:
            print("Hmm Issue Here")                 
        return next(g, True) and not next(g, False)

    def all_equal(self,iter):
        """This returns true if all items in an iterable object are true"""
        g = groupby(iter)
        return next(g, True) and not next(g, False)

    def ValidRun(self):
        """Returns true if the ranks in hand are n, n+1, n+2"""
        x = sorted(self.getranks().copy())
        max = x[len(x)-1]
        if max ==14 and x[-2] != 13:
            x[-1] = 1
            sorted(x)
        for i in reversed(range(len(x))):
            print(x[i] -i )
            x[i]= x[i]-i
            if x[i] - i != x[i-1]:
                return False               
        return True

    def cardtotal(self):
        """returns the summation of the ranks in Hand"""
        return sum(self.getranks())    
        
    def Ispairsrank(self):
        """If at least 2 card ranks match in hand, this method returns true"""
        x = sorted(self.getranks())
        fi = x[0]
        d = dict()
        for i in x:
            if fi-i not in d:
                d[fi-i] = i
            if fi-i in d:
                return True
        return False   

    def IspairSuit(self):
        """If at least 2 card suits match in hand, this method returns true"""
        return (len(self.getdictionary()) <=2)


    def Flush(self):
        """returns true if every suit in a Hand object is equal"""
        return (self.all_equal_suits())

    def StraightFlush(self):
        """ returns true if ValidRun() is true and all the suits are equal"""
        return (self.ValidRun() and self.all_equal_suits())
    def Straight(self):
        """return true if ValidRun is true"""
        return self.ValidRun()

    def ThreeOfKind(self):
        return self.all_equal_ranks()

    def Flush(self):
        return self.all_equal(self.getsuits())

    def Pair(self):
        return self.Ispairsrank()


    def Winrar(self):
        """loops through each win condition and returns the first winning conidition of Hand"""
        #return number
        d = dict()
        if self.StraightFlush():
            return 6
        elif self.ThreeOfKind():
            return 5
        elif self.Straight():
            return 4
        elif self.Flush():
            return 3
        elif self.Pair():
            return 2
        else:
            return 1

        def totalrank(self):
            return sum(self.getranks())


class Game(Hand):
    def __init__(self, n):
        self.n = n
        d = dict()
        #player 
        #rank
        #card total
        winner = 0
        
    

    # def Winrar(self,hand):
    #     """loops through each win condition and returns the first winning conidition of Hand"""
    #     #return number
    #     #d = dict()
    #     if hand.StraightFlush():
    #         return 6
    #     elif hand.ThreeOfKind():
    #         return 5
    #     elif hand.Straight():
    #         return 4
    #     elif hand.Flush():
    #         return 3
    #     elif hand.Pair():
    #         return 2
    #     else:
    #         return 1

    def calculation(self):
        """based on n. It returns the winner"""
        maxWin = 0
        maxHand = 0
        Winner = None
        d = dict()
        for i in range(n):
            x = input()
            xsplit = x.split(" ")
            #print(xsplit)
            player = xsplit[0]
            carda = card(xsplit[1])
            cardb = card(xsplit[2])
            cardc = card(xsplit[3])
            CurHand = Hand(carda,cardb, cardc)
            d[i] = {"player": i, "hand": CurHand, "Winrank": CurHand.Winrar(), "cardtotal" : CurHand.cardtotal()}
            if d[i].get("cardtotal") > maxHand:
                Winner = d[i].get("player")

        return Winner
            






            


        

if __name__ == '__main__':
    n = int(input())
    StartGame = Game(n)

    StartGame.calculation()


    
    