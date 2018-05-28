# array with a stock price changes
# with n^2 solution
def max_sub_array(a):
    abs_sum = 0
    low = 0
    end = 0
    for i in range(len(a) - 1):
        sum = a[i]
        for b in range(i + 1, len(a) - 1):
            sum += a[b]
            if sum > abs_sum:
                abs_sum = sum
                low = i
                end = b
    print('abs value: ', abs_sum, " Low: ", low, "end: ", end)


# recursive solution, using divide and conquer


stocks = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
max_sub_array(stocks)
