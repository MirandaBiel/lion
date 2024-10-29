from picamera2 import Picamera2
from collections import deque
import cv2

# ParÃ¢metros da captura
fs = 30  # Taxa de quadros em Hz
ts = 5   # DuraÃ§Ã£o da captura em segundos
n_frames = fs * ts + 10  # NÃºmero total de quadros a capturar

# Cria a fila com tamanho mÃ¡ximo
queue = deque(maxlen=n_frames)
tempos_de_captura = []

# Configura a cÃ¢mera
picam2 = Picamera2()
video_config = picam2.create_video_configuration(
    controls={"FrameDurationLimits": (33333, 33333)},  # Limita para 30 fps
    main={"format": 'RGB888', "size": (800, 600)}
)
picam2.configure(video_config)
picam2.start()

# Captura e armazena os quadros na fila
for _ in range(n_frames):
    [main], metadata = picam2.capture_arrays()
    tempos_de_captura.append(metadata["SensorTimestamp"])
    queue.append(main)  # Adiciona o quadro Ã  fila

# Calcula os intervalos entre os tempos de captura
intervalos = [(((tempos_de_captura[i+1] - tempos_de_captura[i]) * 0.000001) - 33.333)
              for i in range(len(tempos_de_captura) - 1)]
print("Intervalos entre capturas:", intervalos)

picam2.stop()

# Exibe os quadros capturados a 30 fps
print("\nExibindo os quadros capturados a 30 fps:")

for frame in queue:

    cv2.imshow("Frame", frame)

    # Define um delay de 33 ms para simular 30 fps e fecha a janela ao pressionar 'q'
    if cv2.waitKey(33) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
