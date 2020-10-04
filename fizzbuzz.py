# -*- coding: utf-8 -*-

fizzbuzz = 0
buzz = 0
fizz = 0

print("Brojevi od 1 do 100:")
for i in range (1, 16):
    if (i%3==0 and i%5==0):
        print("FizzBuzz")
        fizzbuzz=fizzbuzz+i
    elif (i%5==0):
        print("Buzz")
        buzz=buzz+i
    elif (i%3==0):
        print("Fizz")
        fizz=fizz+i
    else:
        print(i)

print("fizz "+str(fizz))
print("buzz "+str(buzz))
print("fizzbuzz "+str(fizzbuzz))
rezultat=fizz+buzz-fizzbuzz
print("Rezultat "+str(rezultat))

    

    

    
    
