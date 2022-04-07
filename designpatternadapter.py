import time
import random
class StockMarket:
    def getprice(self, symbol):
        print("StockMarket getprice")
        return {"symbol": symbol, "price": random.randint(0, 100), "time": time.time()}
class StockClient:
    def __init__(self, servicegetstockinformation):
        self.servicegetstockinformation = servicegetstockinformation
        self.history = []
        print("__init__ self.servicegetstockinformation", self.servicegetstockinformation)
    def getprice(self, symbol):
        print("StockClient getprice " + symbol)
        print(self.servicegetstockinformation)
        price = self.servicegetstockinformation.getprice(symbol)
        print("price", price)
        self.history.append(price)
        return price
    def getsymbolhistory(self, symbol):
        return [oneprice for oneprice in self.history if oneprice["symbol"] == symbol]


stockmarketclass = StockMarket() #get quotes or prices from a stock market
stockclientclass = StockClient(stockmarketclass) #retrieves data from the market.  Initialize with the servicegetstockinformation to read and set up a history attribute to keep track of the stock's history.  Invoke getprice at StockClient to retrieve a price for the symbol from StockMarket.  getsymbolhistory retrieves data from the history list for the symbol named.
for i in range(3):
    print(stockclientclass.getprice("PYTH"))
    print(stockclientclass.getprice("RUST"))
    print(stockclientclass.getprice("CPP"))
    '''
    __init__ self.servicegetstockinformation <__main__.StockMarket object at 0x7f7df007c0d0>
    StockClient getprice PYTH
    <__main__.StockMarket object at 0x7f7df007c0d0>
    StockMarket getprice
    price {'symbol': 'PYTH', 'price': 52, 'time': 1649317661.8737662}
    {'symbol': 'PYTH', 'price': 52, 'time': 1649317661.8737662}
    StockClient getprice RUST
    <__main__.StockMarket object at 0x7f7df007c0d0>
    StockMarket getprice
    price {'symbol': 'RUST', 'price': 20, 'time': 1649317661.8737898}
    {'symbol': 'RUST', 'price': 20, 'time': 1649317661.8737898}
    StockClient getprice CPP
    <__main__.StockMarket object at 0x7f7df007c0d0>
    StockMarket getprice
    price {'symbol': 'CPP', 'price': 58, 'time': 1649317661.873805}
    {'symbol': 'CPP', 'price': 58, 'time': 1649317661.873805}
    StockClient getprice PYTH
    <__main__.StockMarket object at 0x7f7df007c0d0>
    StockMarket getprice
    price {'symbol': 'PYTH', 'price': 15, 'time': 1649317661.8738227}
    {'symbol': 'PYTH', 'price': 15, 'time': 1649317661.8738227}
    StockClient getprice RUST
    <__main__.StockMarket object at 0x7f7df007c0d0>
    StockMarket getprice
    price {'symbol': 'RUST', 'price': 88, 'time': 1649317661.8738425}
    {'symbol': 'RUST', 'price': 88, 'time': 1649317661.8738425}
    StockClient getprice CPP
    <__main__.StockMarket object at 0x7f7df007c0d0>
    StockMarket getprice
    price {'symbol': 'CPP', 'price': 96, 'time': 1649317661.873863}
    {'symbol': 'CPP', 'price': 96, 'time': 1649317661.873863}
    StockClient getprice PYTH
    <__main__.StockMarket object at 0x7f7df007c0d0>
    StockMarket getprice
    price {'symbol': 'PYTH', 'price': 8, 'time': 1649317661.8738773}
    {'symbol': 'PYTH', 'price': 8, 'time': 1649317661.8738773}
    StockClient getprice RUST
    <__main__.StockMarket object at 0x7f7df007c0d0>
    StockMarket getprice
    price {'symbol': 'RUST', 'price': 86, 'time': 1649317661.8738914}
    {'symbol': 'RUST', 'price': 86, 'time': 1649317661.8738914}
    StockClient getprice CPP
    <__main__.StockMarket object at 0x7f7df007c0d0>
    StockMarket getprice
    price {'symbol': 'CPP', 'price': 42, 'time': 1649317661.8739083}
    {'symbol': 'CPP', 'price': 42, 'time': 1649317661.8739083}
    '''
#Connect to a second market.  The second market reeturns data in a different format using a named tuple instead of a dictionary, returns information we don't want, and uses a different method; in other words, a different function with a different name.
from collections import namedtuple
quote = namedtuple("quote", ["symbol", "price", "time", "delta"])
class NewMarketSecondMarket:
    def getlatestprice(self, symbol):
        print("NewMarketSecondMarket getlatestprice")
        return quote(symbol, random.randint(0, 100), time.time(), random.randint(0, 10) - 10)


newmarketclass = NewMarketSecondMarket()
newmarketclass.getlatestprice("RUBY")
#I want to use StockClient to retrieve from NewMarketSecondMarket.  I don't want to rewrite.  I don't want to rewrite either StockMarket or NewMarketSecondMarket.  The solution is an Adapter.  StockClient connects to the adapter which connects to NewMarketSecondMarket.  The adapter class makes the appropriate translations.  There are two approaches.  One is using inheritance.  Second is using composition.
class StockMarketAdapterComposition:
    def __init__(self, servicegetstockinformation):
        self.servicegetstockinformation = servicegetstockinformation
        print("__init__ self.servicegetstockinformation", self.servicegetstockinformation)
    def getprice(self, symbol):
        print("boo getprice " + symbol)
        print(self.servicegetstockinformation)
        nt = self.servicegetstockinformation.getlatestprice(symbol)
        print("nt", nt)
        return{"symbol": nt.symbol, "price": nt.price, "time": nt.time}


#Use StockClient to read from NewMarketSecondMarket.  Initialize StockClient with an instance of StockMarketAdapterComposition.  The adapter must be given an instance of NewMarketSecondMarket to read from.
stockclientclass2 = StockClient(StockMarketAdapterComposition(NewMarketSecondMarket()))
for i in range(5):
    stockclientclass2.getprice("RUBY")
    '''
    NewMarketSecondMarket getlatestprice
    __init__ self.servicegetstockinformation <__main__.NewMarketSecondMarket object at 0x7f36316477c0>
    __init__ self.servicegetstockinformation <__main__.StockMarketAdapterComposition object at 0x7f363166a040>
    StockClient getprice RUBY
    <__main__.StockMarketAdapterComposition object at 0x7f363166a040>
    boo getprice RUBY
    <__main__.NewMarketSecondMarket object at 0x7f36316477c0>
    NewMarketSecondMarket getlatestprice
    nt quote(symbol='RUBY', price=76, time=1649318159.1059077, delta=0)
    price {'symbol': 'RUBY', 'price': 76, 'time': 1649318159.1059077}
    StockClient getprice RUBY
    <__main__.StockMarketAdapterComposition object at 0x7f363166a040>
    boo getprice RUBY
    <__main__.NewMarketSecondMarket object at 0x7f36316477c0>
    NewMarketSecondMarket getlatestprice
    nt quote(symbol='RUBY', price=14, time=1649318159.1059382, delta=-7)
    price {'symbol': 'RUBY', 'price': 14, 'time': 1649318159.1059382}
    StockClient getprice RUBY
    <__main__.StockMarketAdapterComposition object at 0x7f363166a040>
    boo getprice RUBY
    <__main__.NewMarketSecondMarket object at 0x7f36316477c0>
    NewMarketSecondMarket getlatestprice
    nt quote(symbol='RUBY', price=56, time=1649318159.1059616, delta=-4)
    price {'symbol': 'RUBY', 'price': 56, 'time': 1649318159.1059616}
    StockClient getprice RUBY
    <__main__.StockMarketAdapterComposition object at 0x7f363166a040>
    boo getprice RUBY
    <__main__.NewMarketSecondMarket object at 0x7f36316477c0>
    NewMarketSecondMarket getlatestprice
    nt quote(symbol='RUBY', price=79, time=1649318159.1059911, delta=0)
    price {'symbol': 'RUBY', 'price': 79, 'time': 1649318159.1059911}
    StockClient getprice RUBY
    <__main__.StockMarketAdapterComposition object at 0x7f363166a040>
    boo getprice RUBY
    <__main__.NewMarketSecondMarket object at 0x7f36316477c0>
    NewMarketSecondMarket getlatestprice
    nt quote(symbol='RUBY', price=76, time=1649318159.1060205, delta=-7)
    price {'symbol': 'RUBY', 'price': 76, 'time': 1649318159.1060205}
    '''
print(stockclientclass2.history) #print [{'symbol': 'RUBY', 'price': 43, 'time': 1649317979.9856422}, {'symbol': 'RUBY', 'price': 1, 'time': 1649317979.9856613}, {'symbol': 'RUBY', 'price': 46, 'time': 1649317979.985679}, {'symbol': 'RUBY', 'price': 75, 'time': 1649317979.9856958}, {'symbol': 'RUBY', 'price': 65, 'time': 1649317979.9857123}]

print(stockclientclass.history) #print [{'symbol': 'PYTH', 'price': 52, 'time': 1649317661.8737662}, {'symbol': 'RUST', 'price': 20, 'time': 1649317661.8737898}, {'symbol': 'CPP', 'price': 58, 'time': 1649317661.873805}, {'symbol': 'PYTH', 'price': 15, 'time': 1649317661.8738227}, {'symbol': 'RUST', 'price': 88, 'time': 1649317661.8738425}, {'symbol': 'CPP', 'price': 96, 'time': 1649317661.873863}, {'symbol': 'PYTH', 'price': 8, 'time': 1649317661.8738773}, {'symbol': 'RUST', 'price': 86, 'time': 1649317661.8738914}, {'symbol': 'CPP', 'price': 42, 'time': 1649317661.8739083}]
