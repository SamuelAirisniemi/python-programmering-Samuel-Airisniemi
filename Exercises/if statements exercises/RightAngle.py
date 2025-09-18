vinkel1 = float(input("Ange den första vinkeln: "))
vinkel2 = float(input("Ange den andra vinkeln: "))
vinkel3 = float(input("Ange den tredje vinkeln: "))

if vinkel1 + vinkel2 + vinkel3 != 180:
    print("Vinklarna formar inte en triangel!")
elif vinkel1 == 90 or vinkel2 == 90 or vinkel3 == 90:
    print("Triangeln är rätvinklig")
else:
    print("Din triangel har ingen rät vinkel")