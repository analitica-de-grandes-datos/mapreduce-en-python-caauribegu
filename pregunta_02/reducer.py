#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    # Se crea una lista vacia para los tipo de atributos
    anteratributo = None
    maximo = 0

    # Se lee el archivo de entrada linea a linea
    for line in sys.stdin:

        # se obtiene el atribito de tipo de credito y el valor 1
        atributo, valor = line.split("\t")
        # Se convierte el valor a entero
        valor = int(valor)

        # se compara el atributo si son iguales se le suma 1 al valor
        if atributo == anteratributo:
            if valor > maximo:
                maximo = valor
        else:
            # se el anterior atributo no es vacio se inmprime la linea
            if anteratributo is not None:
                sys.stdout.write("{}\t{}\n".format(anteratributo, maximo))

            # se reinicia los valores de atributo y valor con el nuevo atributo
            anteratributo = atributo
            maximo = valor

    sys.stdout.write("{}\t{}\n".format(anteratributo, maximo))
