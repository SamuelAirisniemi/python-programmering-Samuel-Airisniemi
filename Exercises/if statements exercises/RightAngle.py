vinkel1 = float(input("Ange den första vinkeln i grader: "))
vinkel2 = float(input("Ange den andra vinkeln i grader: "))
vinkel3 = float(input("Ange den tredje vinkeln i grader: "))

summa = vinkel1 + vinkel2 + vinkel3

if vinkel1 > 0 and vinkel2 > 0 and vinkel3 > 0 and summa == 180:
    if vinkel1 == 90 or vinkel2 == 90 or vinkel3 == 90:
        print("Triangeln är en rätvinklig triangel.")
    else:
        print("Triangeln är inte rätvinklig.")
else:
    print("Vinklarna är ogiltiga och bildar inte en triangel.")