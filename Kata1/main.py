precio =3.49
descuento = 60
precio_con_descuento = precio - (precio * descuento / 100)

print(precio_con_descuento)
numero_de_barras = input("introduce el numero de barras vendidas: ")
numero_de_barras = int(numero_de_barras)
print("precio habitual:"+str(precio))
print("precio con descuento:"+ str(precio_con_descuento) )
print("coste final:" + str(numero_de_barras*precio_con_descuento))


