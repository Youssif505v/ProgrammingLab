# print("Hello world!")
# ------------------------------------ esercise 1
# time = 538
# minutes = time // 60
# seconds = time % 60
# print(f"{minutes} minutes and {seconds} seconds")
# ------------------------------------ esercise 2
# number = int(input("Enter a number: "))
# quadrato=number**2
# cubo=number**3
# print(f"quadrato: {quadrato}\n  cubo:{cubo}")
# ------------------------------------ esercise 3
# number = int(input("Enter a number: "))
# if (number % 2 == 0):
#     print("The number is even.")
# else:
#     print("The number is odd.")
# ------------------------------------ esercise 4
# parola = input("Enter a word: ")
# lettera = input("Enter a letter: ")
# def repeated_character(parola,lettera):
#     count=0
#     for i in range(len(parola)):
#         if lettera == parola[i]:
#             count += 1
#     return count
# print(repeated_character(parola, lettera))
# ------------------------------------ esercise 5
# n = int(input("Inserisci un numero: "))
# if n <= 1:
#     print("Non è primo")
# else:
#     is_prime = True
#     for i in range(2, n):
#         if n % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(f"{n} è un numero primo")
#     else:
#         print(f"{n} non è un numero primo")
# ------------------------------------ esercise 6
# n = 0
# total = 0
# n = int(input("Inserisci un numero: "))
# while n != 0:
#     total = total + n
#     n = int(input("Inserisci un numero: "))
# print(f"La somma totale è: {total}")
# ------------------------------------ esercise 7
# n = int(input("Inserisci un numero: "))
# def fattoriale_iterativo(n):
#     if n < 0:
#         return "Errore: il numero deve essere non negativo"
#     risultato = 1
#     for i in range(1, n+1):
#         risultato *= i
#     return risultato
# print(fattoriale_iterativo(n))
# # ------------------------------------ esercise 8
# def tipo_triangolo(a, b, c):
#     # Verifica validità (ogni lato deve essere minore della somma degli altri due)
#     if (a + b <= c) or (a + c <= b) or (b + c <= a):
#         return "Non è un triangolo"


#     # Classificazione
#     if a == b == c:
#         return "Equilatero"
#     elif a == b or b == c or a == c:
#         return "Isoscele"
#     else:
#         return "Scaleno"
# ------------------------------------- esercise 9
# def conta_vocali(stringa):
#     vocali = "aeiouAEIOU"
#     contatore = 0

#     for carattere in stringa:
#         if carattere in vocali:
#             contatore += 1

#     return contatore


# # Esempio: conta_vocali("Trieste") -> 3 (i, e, e)
