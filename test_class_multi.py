class Cliente(object):

    def __init__(self, text):
        print("Inicializado Cliente")
        print(text)

class Servidor(object):
    
    def __init__(self, text):
        print("Inicializado Servidor")
        print(text)

def run_Cliente(text):
    t = Cliente(text)

    print("Fin")
    

def run_Servidor(text):
    a = Servidor(text)

    print("Fin")