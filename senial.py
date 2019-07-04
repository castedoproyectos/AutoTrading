class Senial(object):

    def __init__(self, dict_attr):

        self._raw_info = None
        self._id = None
        self._id_mt4 = None
        
        self._pair = None
        self._type = None
     
        self._entry = dict()
        self._tp = list()
        self._sl = dict()

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

    def _set_identificator(self):
        self._id = self._pair + self._type + str(self._entry['price']) + str(self._entry['time'])

    def set_new_text(self, list_text):
        self._text.extend(list_text)