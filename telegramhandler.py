from telethon import TelegramClient, events, sync
from telethon.tl.functions.messages import GetHistoryRequest

import time, queue

class TelegramHandler(object):

    def __init__(self):
        self._list_msn = list()

        self._sesion_name = "test"
        self._hash_id = "526632"
        self._hash_num = "eeb7b94dc683848287857f8bfa03aa58"

        self._client = TelegramClient(self._sesion_name,
                                self._hash_id,
                                self._hash_num)

        self._client.start()

        self._channel_entity = self._client.get_entity('https://t.me/joinchat/LbVznBRH92k0YavhYueMFg')


    def is_new_msn(self, list_msn):
        """Realizael filtro de los mensajes para poder identificar cuales de 
        ellos son nuevos para el sistema.
        
        Arguments:
            list_msn {[list]} -- Lista de mensajes recibidos para ser filtrados
        
        Returns:
            {[list]} -- Devuelve la lista de mensajes ya filtrada y sin los repetidos.
        """
        while len(list_msn) > 0: 
            if list_msn[0] in self._list_msn:
                list_msn.pop(0)        
            else:
                break
        
        self._list_msn.extend(list_msn)
        return list_msn


    def get_msn(self, num_msn):
        """Obtiene los mensajes de un canal de telegram, fijado como variable
        interna de la clase (self._channel_entity). Los mensajes estan colocados
        de forma que el primero es el que menos tiempo tiene desde su envio.
        
        Arguments:
            num_msn {[int]} -- Número de mensajes a obtener en el canal.
        
        Returns:
            [list] -- Devuelve una lista de mensajes, leidos y no leidos.
        """
        posts = self._client(GetHistoryRequest(
            peer=self._channel_entity,
            limit=100,
            offset_date=None,
            offset_id=0,
            max_id=0,
            min_id=0,
            add_offset=0,
            hash=0))
    
        # TODO Ordenarlo al contrario. 0 -> n-1
        return list(posts.messages[:].message)
        
        
    def main_loop(self, num_msn, q):
        """Bucle de ejecución principal donde se adquieren los mensajes,
        se filtran para identificar los buenos y se colocan en una cola.
        
        Arguments:
            num_msn {[int]} -- Número de mensajes a coger en cada iteración
            q {[queue]} -- Cola de mensajes donde situarlos
        """
        while True:
            msn = self.get_msn(num_msn)
            new_msn = self.is_new_msn(msn)
            q.put(new_msn)

            time.sleep(5)