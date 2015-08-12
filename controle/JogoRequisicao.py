import json

class JogoRequisicao:
    def process(self, entrada):
        data = json.load(entrada)
        key = data['key']
        action = data['action']
        parameters = data['parameter']

        if key is not None:
            if action == "compra":
                pass
            if action == "batalha":
                pass
            if action == "chat":
                pass
        else:
            if action == "login":
                pass
            if action == "singup":
                pass
        
    

        
        
