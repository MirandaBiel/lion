import serial
import time
import matplotlib.pyplot as plt

# Configuração da porta serial
serial_port = "COM3"  # Substitua pela sua porta
baud_rate = 9600
arduino = serial.Serial(serial_port, baud_rate)

# Variáveis para armazenar os dados
data = []  # Lista para guardar os valores do ECG
start_time = time.time()  # Marca o início da captura
duration = 30  # Duração da captura em segundos

print("Capturando dados por 30 segundos...")

try:
    while True:
        # Captura os dados enquanto o tempo não excede 30 segundos
        current_time = time.time()
        if current_time - start_time > duration:
            break

        # Lê os dados brutos da porta serial
        line = arduino.readline().strip()
        try:
            # Decodifica a linha para texto
            line = line.decode('utf-8')
            if line.isdigit():  # Certifica-se de que é um número
                ecg_value = int(line)
                data.append(ecg_value)
        except UnicodeDecodeError:
            print("Dado ignorado devido a erro de codificação.")

    print("Captura concluída! Plotando os dados...")

    # Plota os dados capturados
    plt.figure(figsize=(10, 5))
    plt.plot(data, label="ECG Signal")
    plt.title("ECG Capturado")
    plt.xlabel("Amostras")
    plt.ylabel("Amplitude")
    plt.grid()
    plt.legend()
    plt.show()

except Exception as e:
    print(f"Erro durante a execução: {e}")

finally:
    arduino.close()  # Fecha a conexão serial
