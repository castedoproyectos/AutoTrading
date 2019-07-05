from DWX_ZeroMQ_Connector_v2_0_2_RC1 import DWX_ZeroMQ_Connector
from senial import Senial

class Mt4Handler(object):

    def __init__(self):
        self._conn = DWX_ZeroMQ_Connector()

    '_action': 'OPEN',
                  '_type': 0,
                  '_symbol': 'EURUSD',
                  '_price': 0.0,
                  '_SL': 500, # SL/TP in POINTS, not pips.
                  '_TP': 500,
                  '_comment': 'DWX_Python_to_MT',
                  '_lots': 0.01,
                  '_magic': 123456,
                  '_ticket': 0})

    def new_operation(self, senial):


        self._conn._DWX_MTX_NEW_TRADE_()

