#!/usr/local/bin/python
# coding: latin-1


#hola mundo
from operator import le

#si a una variable greeting cuyo valor es 'hola' y luego colocamos greeting += ' mundo' se sumara el contenido de la variable cuyo resltado sera hola mundo
#hola mundo
greeting = 'hola'
greeting += ' mundo'
print(greeting)

#si a una variable number cuyo valor es 1 y luego colocamos number += 1 se sumara el contenido de la variable cuyo resltado 2
#2
number = 1
number += 1
print(number)

#si creamos una lista cuyo nombre de la variable es list y el contenido es ['item] y luego colocaos *= 3 lo que hace es que va a multiplicar el item de la lista por la cantidad que tu coloques que en el ejemplo es 3
#['item', 'item', 'item']
list = ['item']
list *= 3
print(list)

#al colocar 'palabra1' 'palabra2' las palabras se uniran
#dianadiana
print('diana' 'diana')

#si colocamos 'palabra' * n cantidade de veces lo que haces es que la palabra se repetira la cantidad de veces indicada
#dianadianadianadianadiana
print('diana' * 5)

#end se usa para determinar un signo que se usara al final de cada palabra
#id-nombre-apellidos-dni-
datos = ['id','nombre','apellidos','dni']
for table in datos:
    print(table, end='-')

#sep se una para asignar un signo que se usara entre cada item de una palabra por ejemplo '1','2'
#hola...como...estas
print('hola','como','estas', sep='...')

#contar la cantidad de letras de un string
#5
d = len('hello')
print(d)

#contar la cantidad de items de una lista
#3
D = len(['my','1','love'])
print(D)



