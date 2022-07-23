#Faça um programa que leia um nome de usuário e a sua senha e
#não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

print("Wellcome to Lígia's code!")
Login=(str(input("Type your login: ")))
Password=(str(input("Type your password: ")))

while Login == Password:
    print("Repeat your password. Login and password cannot be equal!")
    Login=(str(input("Type your login: ")))
    Password=(str(input("Type your password: ")))

else:
    print("Registration Sucessful")



#input("Digite sua senha")
#nota=float(input("informe um numero de 0 a 10: "))
#while (nota>10) or (nota<0):
#	nota=float(input("informe um numero de 0 a 10: "))