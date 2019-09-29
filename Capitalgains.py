"""
This program implements an queue that takes in inputs such as:

in1 = buy x shares at $ y each"
in2 = sell x shares at $ y each"

where x is the number of shares and y is the price for the shares.

When a sell is called, sell x shares at $ y each, the most oldest stocks are sold off first
to calculate the capital gains tax. 

 For example, suppose we buy 100 shares at $20 each on day 1, 20 shares at
$24 on day 2, 200 shares at $36 on day 3, and then sell 150 shares on day
4 at $30 each. Then applying the FIFO protocol means that of the 150
shares sold, 100 were bought on day 1, 20 were bought on day 2, and 30
were bought on day 3. The capital gain in this case would therefore be
100 · 10+20 · 6+30 ·(−6), or $940. 

Alan 09-28-19
"""

from ArrayQueue import ArrayQueueClass

def menu():
    in1 = "1. buy x shares at $ y each"
    in2 = "2. sell x shares at $ y each"
    print(in1)
    print(in2)
    

def evaluateCapitalGains(queue, selloption):
    
    #access the queue array
    calls = queue._data
    
    #store the num stocks and price in tuple form
    tempList = []
    
    #output - stores the running capital gains tax
    runningTax = 0
    
    #access the sell # shares and price in tuple form
    (numSharesSell, priceSell) = int(selloption.split(" ")[1]), int(selloption.split(" ")[5])
    
    #make a copy so we don't overwrite raw data
    numSold = numSharesSell
    
    
    #extract the number of shares and share price from the list
    for index in range(0,queue.__len__()):
        (numSharesBuy, priceBuy) = int(calls[index].split(" ")[1]), int(calls[index].split(" ")[5])
        tempList.append((numSharesBuy,priceBuy))
        
    
    #calculate running total. 
    for item in tempList:
        
        #calculate tax rate, when the differece is positive
        if (numSold - item[0]) > 0:
            runningTax += (priceSell - item[1])* item[0] 
        else:
            #since the difference between the number of stocks held in day N and numSold is negative,
            #calculate the rest of the stocks sold, numSold, at the current price rate.
            runningTax += (priceSell - item[1])* numSold
            break
            
        
        #decrement num stocks bought from number of stocks sold
        numSold -= item[0]
    
    return runningTax
    
if __name__ == "__main__":

    queue = ArrayQueueClass()
    
    menu()

    testStr1 = "buy %d shares at $ %d each" %(100,20)
    testStr2 = "buy %d shares at $ %d each" %(20,24)
    testStr3 = "buy %d shares at $ %d each" %(200,36)
    testStr4 = "sell %d shares at $ %d each" %(150,30)

    queue.enqueue(testStr1)
    queue.enqueue(testStr2)
    queue.enqueue(testStr3)
    print(evaluateCapitalGains(queue,testStr4))
    

