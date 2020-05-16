pasword = "contraseña"
pasword_del_usuario = input("introduzca la  contraseña:")
pasword_del_usuario = pasword_del_usuario.lower()
if pasword == pasword_del_usuario:
    print("El pasword es correcto")
else:
    print("el pasword no coincide")
    