# Argumentos de clave-valor variable (**kwargs):
def mostrar_informacion_de(**kwargs):
  for clave, valor in kwargs.items():

    if clave == "nombre":
        print(f"El {clave} en español es: {valor}")
    elif clave == "name":
       print(f"El {clave} en inglés es: {valor}")
    else:
       print(f"Esto es para cualquier otra clave")
    
    


mostrar_informacion_de(nombre="midudev", edad=25, sexo="gato")
print("\n")
mostrar_informacion_de(name="madeval", edad=21, country="Uruguay")
print("\n")
mostrar_informacion_de(nick="pheralb", es_sub=True, is_rich=True)
print("\n")
mostrar_informacion_de(super_name="felixicaza", es_modo=True, gatos=40)