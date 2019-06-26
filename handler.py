from senial import Senial

class Handler(object):

    def __init__(self):

        self._open_senials = list

        self.load_open_senials()
        
    
    def load_open_senials(self):

        f = open("open_senial.txt")
        rows = f.readlines()

        s = Senial()
        for row in rows:
            s.load_attributes(row)
            self._open_senials.append(s)
        
        f.close()

        # Print
        print("Leyendo archivo de cantidad de seniales abiertas")
        print("Cantidad de seniales abiertas -> " + str(len(self._open_senials)))


    def save_open_senials(self):
        """Guarda todas las seniales abiertas, escribiendolas en un fichero txt. Para una
        posible carga de ellas.
        """

        f = open("open_senial.txt", "w")
        f.writelines(self._open_senials)
        f.close()

        # Print
        print("Guardando seniales abiertas")
        print("Cantidad de seniales guardadas: " + str(len(self._open_senials)))

    
    def 