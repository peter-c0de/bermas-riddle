def berma_eggs():
    # From 7 to 3493:
    for i in range(1, 500):
        c = 7 * i # N7 Multiplications
        if (c%4==1) and (c%5==1) and (c%6==1) and (c%7==0):
            print(c)

berma_eggs()