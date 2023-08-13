from random import choice
import string

qtd_caracteres = int(
    input("Informe a quantidade de caracteres que você quer na sua senha: "))

caractereres = string.ascii_letters + string.digits + string.punctuation
senha = ''

for c in range(qtd_caracteres):
    senha += choice(caractereres)
print(f"Sua senha é: {senha}")
