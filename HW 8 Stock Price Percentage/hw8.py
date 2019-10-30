"""
HW8
This program creates a Stock object and displays its previous closing price,
its new current price and calculates and displays the price-change percentage.
Author: Naveed Hussain
"""

# Create Stock class

class Stock():

    # Constructor for the Stock class

    def __init__(self, symbol, name, previousClosingPrice, currentPrice):
        self.__symbol = symbol
        self.__name = name
        self.__previousClosingPrice = previousClosingPrice
        self.__currentPrice = currentPrice

    # Get method that returns stock name
    
    def getStockName(self):
        return self.__name

    # Get method that returns stock symbol

    def getStockSymbol(self):
        return self.__symbol

    # Get method for stock's previous price

    def getPrevious(self):
        return self.__previousClosingPrice

    # Get method for stock's current price

    def getCurrent(self):
        return self.__currentPrice

    # Set method for stock's previous price

    def setPrevious(self, previousClosingPrice):
        self.__previousClosingPrice = previousClosingPrice

    # Set method for stock;s current price

    def setCurrent(self, currentPrice):
        self.__currentPrice = currentPrice

    # Method that returns percentage changed

    def getChangePercent(self):
        changePercent = ((self.__currentPrice - self.__previousClosingPrice)/(self.__previousClosingPrice))*100
        return changePercent


def main():

    # Calls stock method with values
    
    stock1 = Stock("INTC","Intel Corporation",20.5,20.35)

    # Outputs result
    
    print(stock1.getStockName())
    print(stock1.getStockSymbol())
    print("The stock's previous closing price was $%.2f" % stock1.getPrevious())
    print("The stock's new current price is $%.2f" % stock1.getCurrent())
    print("The price change percentage is %.2f" %(stock1.getChangePercent()))


main()




