nterms = int(input("enter number of terms :"))
n1 , n2 = 0, 1
count=0
if nterms<=0:
    print("enter +ve value")
elif nterms == 1:
    print(n1)
else:
    while count<nterms:
        print(n1)
        nth = n1 +n2
        n1= n2
        n2=nth
        count = count +1