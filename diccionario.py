meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "BOT": "Se le dice a lguien muy malo jugando",
            "GATO":"Mamífero de la familia de los félidos, digitígrado, doméstico, de unos 50 centímetro(s) de largo "}
word = input("Escribe la palabra que no entiendas:").upper()

if word in meme_dict.keys():
    print("El significado es", meme_dict[word])
else:
    print ("sintaxiz error")

