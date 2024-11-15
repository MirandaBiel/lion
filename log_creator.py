from datetime import datetime

def log(objeto, nome_arquivo):
    with open(f"{nome_arquivo}.txt", "w") as arquivo:
        data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        arquivo.write(f"Data e Hora de Criação: {data_hora}\n\n")
        
        for nome, valor in vars(objeto).items():
            if isinstance(valor, list):
                format_valor = ', '.join(map(str, valor))
                arquivo.write(f"{nome}: {format_valor}\n")
            else:
                arquivo.write(f"{nome}: {valor}\n")