import sys

def stock(a):
    maxprofit = 0
    minprice = sys.maxsize
    for i in range(len(a)):
       if a[i] < minprice:
           minprice = a[i]
           buy_day = i
           
       current_profit = a[i] - minprice 
       if current_profit > maxprofit:
           maxprofit = current_profit
           sell_day = i

    return maxprofit, a[buy_day], a[sell_day]

if __name__ == "__main__":
    a = [7,1,5,3,6,4]
    r = stock(a)
    print(r)