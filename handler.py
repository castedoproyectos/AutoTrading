from senial import Senial

class Handler(object):

    def __init__(self):

        self._open_senials = list()
        
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

    
    def new_msn(self, line):
        # Nuevo mensaje
        s = Senial()
        s.set_attributes(line)

        if s._real_senial is True:
            print("El nue_vo mensaje es una senial")
            if self.check_is_new(s):
                self._open_senials.append(s)
                self.create_senial_mt4(s)
        else:
            print("El nuevo mensaje no es una senial")


    def check_is_new(self, sen):
        """Comprueba que la nueva senial no se encuentra entre las 
        seniales abiertas.
        
        Arguments:
            sen {[Senial]} -- Senial a comprobar
        
        Returns:
            [boolean] -- Si la senial no se encuentra devuelve -> True
                         Si la senial si se encuentra devuelve -> False
        """
        for s in self._open_senials:
            if s._raw_info is sen._raw_info:
                return False
        
        return True

    def create_senial_mt4(self, Senial):
        pass


    def execute(self):

        # Esperando mensajes
        list_msn = list()
        
        for item in list_msn:
            self.new_msn(item)