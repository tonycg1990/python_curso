#Estructuras de datos que permite almacenar valores diferentes tipo (enteros, cadenas de texto, decimales) e icluso listas y otros diccionarios
#clave : valor 

dicc={"Peru":"Lima", "Colombia":"Bogota", "Argentina": "Buenos Aires", "Bolivia": "La Paz"}
dicc["Ecuador"]="Quito"
print(dicc)
del dicc["Bolivia"]  #del = eliminar una clave y valor
print(dicc)

dicc={"Peru":"Lima", 7:"Cristiano Ronaldo", "Chiflados":3}
print(dicc)

#mitupla=["España", "Peru", "Bolivia", "Ecuador"]
#dicc={mitupla[0]:"Madrid",mitupla[1]:"Lima", mitupla[2]: "La Paz", mitupla[3]:"Quito"}
#print(dicc)


dicc={7:"Cristiano", "Nombre": "Ronaldo", "Equipo":"Real Madrid","Champions":{"Temporadas":[2007,2008,2009]}}
#print(dicc["Equipo"])
#print(dicc.keys())   #imprime las claves
#print(dicc.values())  #imprime los valores
print(len(dicc))       #imprime la cantidad
#print(dicc)