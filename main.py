from flask import Flask, request
import os

app = Flask(__name__)


call_participants = [] 
DEFAULT_CALL = {"name": "Solita", "emote": "nolleyClap"}  



@app.route("/addcall", methods=['GET'])
def add_call():
    entries = request.args.get("entries", "").split()  
    if len(entries) % 2 != 0:
        return "Numero incorrecto de elementos, recuerda enviar siempre un Nombre sin espacios y un Emote por participante nephuDerp"

    for i in range(0, len(entries), 2):
        name = entries[i]
        emote = entries[i + 1]
        call_participants.append({"name": name , "emote": emote})
    
    return f"Participantes añadidos: {' , '.join([f'{name} {emote}' for name, emote in zip(entries[::2], entries[1::2])])}"


@app.route("/removecall", methods=['GET'])
def remove_call():
    names = request.args.get("entries", "").split() 
    removed = []
   
    names = [name.lower() for name in names]
    
    for name in names:
        for participant in call_participants[:]:
            if participant['name'].lower() == name:
                call_participants.remove(participant)
                removed.append(f"{name} {participant['emote']}")
    
    if not call_participants:
        return f"{DEFAULT_CALL['name']} {DEFAULT_CALL['emote']} " 
    
    if removed:
        return f"Participantes removidos: {' , ' .join(removed)} "
    else:
        return "No se encontraron participantes para remover."






@app.route("/resetcall", methods=['GET'])
def reset_call():
    call_participants.clear()
    return f"!call reiniciado nolleyClap"

@app.route("/call", methods=['GET'])
def get_call():
    if not call_participants:
        return f"{DEFAULT_CALL['name']} {DEFAULT_CALL['emote']}"
    
    call_info = " ".join([f"{p['name']} {p['emote']}" for p in call_participants])
    return call_info



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
