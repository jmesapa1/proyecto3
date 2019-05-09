-es inmportante al crear un cluster instalarle manualmente la libreria nltk

-El proyecto fue realizado sobre databricks community edition - python

-el proyecto esta ejecutandose sobre un texto prueba que cotiene aproximadamente 30 noticias para ambitos de prueba 

---------""" si se tuviese mas poder de computo se pudiera ejecutar el progrmaa sobre articles1,articles2,srticles3 sin que se superen los limites de computo"""---------------



1-Preparacion de datos

este programa se encarga de eliminar datos basura en los textos
procedimiento:
se determino leer cada archivo .csv linea a linea y dividir el string en dos partes
una parte que se contiene la informacion respecto a el y el otro contiene el contenido como tal de cada noticia
al primer substring no se le realiza algun procedemiento se deja igual con sus separadores por comas con el objetivo
de pensar en el proximo entregable del indice invertido,mientras que el segundo substring que contiene el contenido
de la noticia con ayuda de la libreria nltk se elimino stopwords y signos de puntuacion para que ejecucion del codigo
se haga mas rapidamente, como proceso final se concatenan los dos substring con el objetivo de almacernarlos y seguir con las 
noticias siguientes  
Toda la informacion es guardada en una lista 


2-Contador

una vez ejecutado el programa clearData.py y guardado los datos de cada noticia en una posicion se recorre esta lista posicion a posicion para asi crear una coleccion de palabras de cada noticia para generar un contador que aumente cada vez que encuentre una coincidencia 

https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/2270583156149495/2944819796898215/4851533722723077/latest.html