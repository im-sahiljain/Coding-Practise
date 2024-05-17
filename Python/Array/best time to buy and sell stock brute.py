def stock(a):
    maxprofit = 0
    n= len(a)
    for i in range(0,n):
        for j in range(i+1, n):
            profit = a[j] - a[i]
            if profit > maxprofit:
                maxprofit = profit
                buy_amount = a[i]
                sell_amount = a[j]
    
                
    return maxprofit,buy_amount, sell_amount


if __name__ == "__main__":
    a = [7,1,5,3,6,4]
    r = stock(a)
    print(r)