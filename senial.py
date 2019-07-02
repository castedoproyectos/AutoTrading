class Senial(object):

    def __init__(self):

        self._raw_info = None
        self._real_senial = None

        self._id = None
        self._id_mt4 = None
        
        self._pair = None
        self._type = None
     
        self._entry = dict()
        self._tp = list()
        self._sl = dict()

        self._text = list()

    
    def set_attributes(self, line):
        """Determina los valores de la clase correspondientes con la lectura de una cadena de 
        caracteres. 

        Argumentos:
            line {[str]} -- String correspondiente con un mensaje recibido por telegram
        """

        # Saber si es una senial
        self.__set_pair(line)
        
        if self._pair is None:
            self._real_senial = False
        else:
            self._real_senial = True
            self.__set_tipo(line)
            self.__set_entry(line)
            self.__set_sl(line)
            self.__set_tp(line)

            self.__set_raw_info()        


    def __set_pair(self, line):
        """Determina si una señal es valida, para ello comprueba que el par de la señal
        se encuentre en la lista de pares aceptados.

        Arguments:
            line [String] - Linea correspondiente con el texto leido desde Telegram
        
        Returns:
            ES una señal devuelve una lista:    [0] - Pair
            NO ES una señal devuelve:   None
        """

        # Determina el par de la senial
        f = open("pairs.txt", "r")
        rows = f.readlines()

        for it in range(len(rows)):
            rows[it] = rows[it][:6] 
            if line.find(rows[it]) is not -1:
                self._pair = rows[it]



    def __set_tipo(self, line):
        """Determina el tipo de senial, de compra o venta. Depende exclusivamente
        de encontrar la cadena de caracteres BUY o SELL.
        
        Arguments:
            line {[str]} -- Mensaje de telegram en forma de String
        """
        pos = line.find("BUY")
        if pos is not -1:
            self._type = line[pos:pos+3]

        else:
            pos = line.find("SELL")
            if pos is not -1:
                self._type = line[pos:pos+4] 


    def __set_entry(self, line):
        pos = line.find("@") + 1
        pos_fin = line.find(" ",pos)

        self._entry['price'] = line[pos:pos_fin]
        self._entry['time'] = None   # TODO: tiempo entrada
        
        # Se da por hecho que si se pone el precio de entrada ese 
        # es porque se ha alcanzado en algún momento.
        # TODO: Comprobación del valor del precio para saber si se alcanza.
        self._entry['reach'] = None  


    def __set_sl(self, line):
        pos = line.find("SL") + 3
        pos_fin = line.find(" ",pos + 4)

        if pos is not -1:
            self._sl['price'] = line[pos:pos_fin]
            self._sl['time'] = None
            self._sl['reach'] = None


    def __set_tp(self, line):

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

                self._tp.append(data)
                it += 1
            else:
                break

            last_pos = pos


    def __set_raw_info(self):
        self._raw_info = self._pair + self._type + str(self._entry['price']) + str(self._entry['time']) 

    def set_text(self, line):
        pass

   
    def load_attributes(self, line):
        pass