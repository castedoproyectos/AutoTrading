import datetime
class Senial(object):

    def __init__(self, dict_attr):

        self._raw_info = None
        self._id = None
        self._ticket_mt4 = None
        
        self._pair = None
        self._type = None
     
        self._entry = dict()
        self._tp = list()
        self._sl = dict()

        self._action = list()
        self._text = list()

        if dict_attr is not None:
            self.set_attributes(dict_attr)

    
    def set_attributes(self, attrib):
        """Determina los valores de la clase correspondientes con la lectura de una cadena de 
        caracteres. 

        Argumentos:
            line {[str]} -- String correspondiente con un mensaje recibido por telegram
        """

        self._pair = attrib['pair']
        self._type = attrib['type']
        
        self._entry = attrib['entry']
        self._sl = attrib['Sl']

        self._tp.append(attrib['TP1'])
        self._tp.append(attrib['TP2'])
        self._tp.append(attrib['TP3'])

        self._set_identificator()
        self._set_ticket_mt4()


    def _set_identificator(self):
        """Crea el identificador propio de la senial, utilizado para comprobar si la senial
        es nueva o ya ha sido tratada por el sistema, siendo la única novedad el texto.
        """
        self._id = self._pair + self._type + str(self._entry['price']) + str(self._entry['time'])


    def _set_ticket_mt4(self):
        """Creación del ticket para mt4. Creado a partir de la fecha de entrada a la que se le
        añade un cero o un uno en función del tipo de orden. 
        """
        opc = "0"
        if self._type is "SELL":
            opc = "1"

        t = self._entry['time']
        self._ticket_mt4 = str(t.hour) + str(t.minute) + str(t.second) + str(t.day) + str(t.month) + str(t.year) + opc
        

    def set_new_text(self, list_text):
        """Añade un texto a la lista de textos de la senial. Esto se realizara en aquellas
        seniales que tengasn mas de un comentario y ya hayan sido tratadas.
        
        Arguments:
            list_text {[str]} -- Texto
        """
        self._text.extend(list_text)


    def get_points(self, opc):
        """Obtiene la distancia en puntos, existente entre la entrada y cualquiera de los 
        takeprofit o stoploss. Si la opcion no se encuentra entre las posibles se devolvera 
        un error.
        
        Arguments:
            opc {[str]} -- Las distintas opciones son: TP1, TP2, TP3 y SL.
        
        Returns:
            [int] -- Distancia en puntos desde la entrada a la opción elegida
        """

        # Determina la cantidad de decimales
        tam = 100000
        if self._entry['price'] > 10:
            tam  = 1000

        if opc is "TP1":
            return abs(self._entry['price'] - self._tp[0]['price']) * tam
        
        if opc is "TP2":
            return abs(self._entry['price'] - self._tp[1]['price']) * tam

        if opc is "TP3":
            return abs(self._entry['price'] - self._tp[2]['price']) * tam

        if opc is "SL":
            return abs(self._entry['price'] - self._sl['price']) * tam
        
        return None
    