from senial import Senial
import queue

class Handler(object):

    def __init__(self):
        
        self._total_senials = list()
        self._open_senials = list()
        self._pair_accepted = list()

        self.load_open_senials()
        self.load_pair_accepted()
    

    def load_open_senials(self):

        f = open("open_senial.txt")
        rows = f.readlines()

        if len(rows) > 0:
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

    
    def load_pair_accepted(self):
        # Determina el par de la senial
        f = open("pairs_acept.txt", "r")
        rows = f.readlines()

        for item in rows:
            self._pair_accepted.append(item)

        # Print
        print("Cargados los pares con exito")


    def new_msn(self, line):
        # Nuevo mensaje
        s = Senial()
        s.set_attributes(line)

        if s._real_senial is True:
            print("El nuevo mensaje es una senial")
            if self.check_is_new(s):
                self._open_senials.append(s)
                self.create_senial_mt4(s)
        else:
            print("El nuevo mensaje no es una senial")


    def convert_msn_to_senial(self, line):
        """Obtención de todos los valores correspondientes con la clase de senial
        introduciendolos en un diccionario.
        
        Arguments:
            line {[str]} -- Información de la posible senial
        
        Returns:
            Varios -- None - Si no es senial
                      Dict - Valores de la senial
        """
        senial_dict = dict()

        # Asignación del par
        senial_dict['pair'] = "ERROR"
        for pair in self._pair_accepted:
            if line.find(pair) is not -1:
                senial_dict['pair'] = pair
                break

        # Comprobación de senial
        if senial_dict['pair'] is "ERROR":
            return None

        # Asignación del tipo
        if line.find('BUY') is not -1:
            senial_dict['type'] = 'BUY'
        elif line.find('SELL') is not -1:
            senial_dict['type'] = "SELL"
        else:
            senial_dict['type'] = "ERROR"
            
        # Asignación de la entrada
        pos = line.find("@") + 1
        pos_fin = line.find(" ",pos)

        if pos is not -1:
            entry_dict = dict()
            entry_dict['price'] = line[pos:pos_fin]
            entry_dict['time'] = None   # TODO: tiempo entrada
            entry_dict['reach'] = None  
            senial_dict['entry'] = entry_dict

        # Asignación del stoploss
        pos = line.find("SL") + 3
        pos_fin = line.find(" ",pos + 4)

        if pos is not -1:
            sl_dict = dict()
            sl_dict['price'] = line[pos:pos_fin]
            sl_dict['time'] = None
            sl_dict['reach'] = None
            senial_dict['sl'] = sl_dict

        # Asignación del takeprofit
        it = 1
        pos = 0
        last_pos = 0
        while pos is not -1:
            tp = "TP" + str(it)
            pos = line.find(tp) + len(tp) + 1
            pos_fin = line.find(" ",pos + 5)

            data = dict()
            if pos != last_pos:
                data['price'] = line[pos:pos_fin]
                data['time'] = None
                data['reach'] = None

                senial_dict[tp].append(data)
                it += 1
            else:
                break

            last_pos = pos
        
        # Resto de parametros
        senial_dict['raw_info'] = line
        senial_dict['id'] = 1       # TODO establecer el tiempo 
        
        s = Senial(senial_dict)
        return s


    def is_new_senial(self, s):
        for it in range(len(self._total_senials)-1):
            if self._total_senials[it]._id is s._id:
                return it
        
        return None
        

