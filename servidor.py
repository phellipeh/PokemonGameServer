from SimpleWebSocketServer import WebSocket, SimpleWebSocketServer
from controle import JogoRequisicao

class ServerController(WebSocket):
        def handleMessage(self): 
                try:
                        jogo = JogoRequisicao()
                        r = jogo.process(self.data)
                        self.sendMessage(r)
                except Exception as ex:
                        print "Exception: " + str(ex)
            
        def handleConnected(self):
            print self.address, ' Conectado'

        def handleClose(self):
            print self.address, ' Desconectado'


print "Iniciando..."
try:
        server = SimpleWebSocketServer('', 9999, ServerController)
        print "Servidor Iniciado na porta 9999"
        server.serveforever()
except Exception as ex:
        print "Exception: " + str(ex)
