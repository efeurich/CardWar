# Card Class
# Contains: Suit, Rank , Value

values = {'Twee':2,'Drie':3,'Vier':4,'Vijf':5,'Zes':6,'Zeven':7,'Acht':8,'Negen':9,'Tien':10,'Boer':11,'Vrouw':12,'Koning':13,'Aas':14,}
class Card:


    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return self.rank + " of  " + self.suit