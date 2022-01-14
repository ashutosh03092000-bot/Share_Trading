def MaxProfit(price, k):
    n = len(price)
    # base case
    if n <= 1:
        return 0

    # Profit[i][j] stores the maximum profit gained by doing atmost i transactions till j'th
    profit = [[0 for x in range(n)] for y in range(k + 1)]

    for i in range(k + 1):
        for j in range(n):
            # profit is 0 when
            # i = 0, i.e., for 0th
            # j = 0, i.e., no transaction is being performed
            if i == 0 or j == 0:
                profit[i][j] = 0
            else:
                max_so_far = 0
                for x in range(j):
                    curr_price = price[j] - price[x] + profit[i - 1][x]
                    if max_so_far < curr_price:
                        max_so_far = curr_price
                profit[i][j] = max(profit[i][j - 1], max_so_far)

    return profit[k][n - 1]

#Driver Code
if __name__ == '__main__':
    print("\t\t\tMaximum Profit Calculator\n")
    #Getting empty list to store prices of the shares
    price = []
    # Asking for the size of pricelist
    size=int(input("Enter the size of list: "))
    print("Enter the prices\n")
    for i in range(0,size):
            # Getting prices
            p=int(input())
            # Appending prices
            price.append(p)
    print(f"pricelist:{price} ")
    # Asking for maximum number of transactions
    k = int(input("Enter the maximum number of transaction: "))
    if k<len(price):
    # Calling function
        print('The maximum possible profit is', MaxProfit(price, k))
    # Case when k>length of price list
    else:
        print("Not possible to earn.")
