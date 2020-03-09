def fibo(n):
    if n <= 1:
        return n
    else:
        return(fibo(n-1) + fibo(n-2))


wartosc = int(input("Podaj liczbę większą od 0: "))

if wartosc <= 0:
    print("Zła wartość!")
else:
    print("Ciąg Fibonacciego:")
    for i in range(wartosc):
        print(fibo(i))
