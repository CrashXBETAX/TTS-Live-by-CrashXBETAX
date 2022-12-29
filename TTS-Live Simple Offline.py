import pyttsx3
def TTS(text):
    pyttsx3.speak(text)
print("Bem-vindo ao programa TTS-Live Simple Offline")
print("Programa iniciado")
print("Frases prontas: ")
print("1 = Bom dia!")
print("2 = Boa tarde!")
print("3 = Boa noite!")
print("4 = Tudo bem")
print("5 = Sim tudo. Obrigado")
print("6 = Tchau tenha ótimo dia!")
print("7 = Tenho coisas para complementar.")
print("8 = Não tenho coisas para complementar.")
print("9 = Desculpe, não entendi.")
print("stop = Fechar o programa TTS-Live Simple Offline")
while True:
    type = str(input("Digite: "))
    if type == "1":
        text = "Bom dia!"
        TTS(text)
    elif type == "2":
        text = "Boa tarde!"
        TTS(text)
    elif type == "3":
        text = "Boa noite!"
        TTS(text)
    elif type == "4":
        text = "Tudo bem?"
        TTS(text)
    elif type == "5":
        text = "Sim tudo. Obrigado."
        TTS(text)
    elif type == "6":
        text = "Tchau. Tenha ótimo dia!"
        TTS(text)
    elif type == "7":
        text = "Tenho coisas para complementar."
        TTS(text)
    elif type == "8":
        text = "Não tenho coisas para complementar."
        TTS(text)
    elif type == "9":
        text = "Desculpe, não entendi."
        TTS(text)
    elif type == "stop":
        print("Encerrando o programa TTS-Live Simple Offline")
        break
    else:
        TTS(type)