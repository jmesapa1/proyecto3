import operator
Buscar="house"
Buscar=Buscar.lower()
released = {
		0 : 0}
releasedTitulo = {
		0 : 0}
contadorLinea=0
for linea in LineFiltered:
  Id=""
  contador=0
  
  frecuencia=0
  coleccionPalabras=tokenizer.tokenize(linea)
  for palabra in coleccionPalabras:
    contador+=1
    if palabra==Buscar:
      frecuencia+=1
    if contador==2:
      Id=palabra

      
  releasedTitulo[tittle[contadorLinea]]=frecuencia    
  released[Id]=frecuencia
  contadorLinea+=1

ordenTitulo=sorted(releasedTitulo.items(),key=operator.itemgetter(1))  
  
sorted_x = sorted(released.items(), key=operator.itemgetter(1))
sorted_x.reverse()
ordenTitulo.reverse()

i=0
while i < 5:
  print( sorted_x[i])
  print(ordenTitulo[i])
  print("------------------------------------------------------------")
  i += 1   
