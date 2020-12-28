from datetime import datetime

def retorna_data():
    data_atual = datetime.now()

    data_completa = data_atual.strftime("%d/%m/%Y %H:%M")

    return data_completa