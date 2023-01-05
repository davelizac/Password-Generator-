#Password Generator Project
#En esta versión apliqué optimización del código aprendida en el curso de Python a la primera versión del Password Generator que yo creé. Ya no hay problema con el Index. 
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


password_list = [] #la lista vacia permite adicionar elementos con el 'for loop'
  
for letter in range(0, nr_letters): # la variable 'letter' toma un elemento a la vez de la lista 'letters' dentro del rango especificado.
  password_list += random.choice(letters) 
  
for symbol in range(0, nr_symbols):
  password_list += random.choice(symbols)
 
for number in range(0, nr_numbers):
  password_list += random.choice(numbers)
  
random_password = "".join(random.sample(password_list, len(password_list))) # para que la password se presente ordenada aleatoriamente utilicé la función 'random.sample()'. En este punto también se debe utilizar la función "".join(), de otro modo la password se imprimirá como una lista, es decir, dentro de corchetes y con los elementos que la componen separados por comas.

print(f"\nYour new password is: {random_password}")

  