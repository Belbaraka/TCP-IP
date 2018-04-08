import websocket

command0="CMD_short:0"
command1="CMD_short:1"
command_flood="CMD_floodme"
URL='ws://tcpip.epfl.ch:5006'

def on_open(ws):
    ws.send(command_flood) #modify command wa

def on_message(ws, message):
    print(message.decode())

ws= websocket.WebSocketApp(URL, on_open=on_open, on_message=on_message)
ws.run_forever()





