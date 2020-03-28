'''
@ TITLE:    roman_converter.py
@ DATE:     28-03-2020
@ AUTHOR:   Fernanda Guzman Gomez
@ PROBLEM:  Exercise 09
'''

def convertor_romano(numero):
    simbolo_decimal = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    simbolo_romano = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
    posicion_lista_decimal = 12


    while numero: 
        decimal_cupo_en_numero = numero // simbolo_decimal[posicion_lista_decimal]
        numero = numero % simbolo_decimal[posicion_lista_decimal]
  
        while decimal_cupo_en_numero:
            print(simbolo_romano[posicion_lista_decimal], end="")
            decimal_cupo_en_numero = decimal_cupo_en_numero - 1
        
        posicion_lista_decimal = posicion_lista_decimal - 1
  

if __name__ == "__main__": 
    num = 25
    print(f"The number: {num} in Roman is: ", end="")
    convertor_romano(num)
