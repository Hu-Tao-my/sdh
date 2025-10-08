a = " "
while True:
    n = int ( input( ))
    if n != 0 :
        for i in range ( 1 , n ):
            if i % 7 == 0:
                continue
            a += str ( i )
            a += " "
        a += "\n"
    else:
        print (a)
        break