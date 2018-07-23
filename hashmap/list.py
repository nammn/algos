def a(b):
    if b > 100:
        print('fertig')
        
        return
    b = b + 1
    print('i got recursed, counter: ', b)
    a(b)


a(0)
