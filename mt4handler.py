from DWX_ZeroMQ_Connector_v2_0_2_RC1 import DWX_ZeroMQ_Connector
from senial import Senial

class Mt4Handler(object):

    def __init__(self):
        self._conn = DWX_ZeroMQ_Connector()

    def convert_senial_to_trade(self, s):
              
        _my_trade = self._conn._generate_default_order_dict()

        # Determinar tipo
        if s._type is "BUY":
            _my_trade['type'] = 0
        elif s._type is "SELL":
            _my_trade['type'] = 1

        _my_trade['_symbol'] = s._pair
        _my_trade['_price'] = 0.0
        _my_trade['_SL'] = s.get_points("SL")
        _my_trade['_TP'] = s.get_points("TP1")
        _my_trade['_comment'] = "AutoTrading-Python"
        _my_trade['_lots'] = 0.01
        _my_trade['_magic'] = 123456
        _my_trade['_ticket'] = s._id_mt4

        return _my_trade
                  

    def open_operation(self, trade):
        try:
            self._conn._DWX_MTX_NEW_TRADE_(trade)
        except:
            print("Error en el apertura de la orden")


    def close_operation(self, trade):
        self._conn._DWX_MTX_CLOSE_TRADE_BY_TICKET_()

    def send_action(self, senial):
        pass