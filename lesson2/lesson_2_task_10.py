def bank (x, y):
    for  l in range (1, y+1) :
        count = x + (x/10)
        x = count
        print (round (count, 4))  

bank (1000,10)