from picamera2.outputs import FileOutput
from picamera2.encoders import Encoder
from picamera2 import Picamera2
from PyQt5 import QtCore, QtGui, QtWidgets
import io
import time
import numpy as np
import cv2  # Usado para manipular os dados de imagem

# ConfiguraÃ§Ã£o da cÃ¢mera
picam2 = Picamera2()
video_config = picam2.create_video_configuration(
    controls={"FrameDurationLimits": (33333, 33333)},  # Limita para 30 fps
    main={'format': 'XBGR8888', "size": (800, 600)}
)
picam2.configure(video_config)

# InicializaÃ§Ã£o do encoder e buffer
encoder = Encoder()
buffer = io.BytesIO()
output = FileOutput(buffer)

# Inicia a gravaÃ§Ã£o
picam2.start_recording(encoder, output)
time.sleep(5)  # Grava por 5 segundos
picam2.stop_recording()

# Converte o buffer em uma lista de quadros em formato BGR
frames = []
buffer.seek(0)  # Retorna ao inÃ­cio do buffer

# Carrega cada quadro do buffer e remove o canal alfa
while buffer.tell() < len(buffer.getvalue()):
    # Supondo que cada quadro Ã© um array com 800x600 de resoluÃ§Ã£o e canal extra (4 bytes por pixel para XBGR8888)
    frame_data = buffer.read(800 * 600 * 4)  # LÃª cada quadro com os 4 canais (XBGR)
    if not frame_data:
        break
    
    # Converte o quadro em um array numpy e remove o canal alfa
    frame = np.frombuffer(frame_data, dtype=np.uint8).reshape((600, 800, 4))  # Formato (H, W, 4)
    frame_bgr = frame[:, :, :3]  # Remove o canal alfa 'X'
    
    frames.append(frame_bgr)  # Armazena o quadro BGR na lista

print("PROCESSO FINALIZADO")
print(f"Total de quadros capturados: {len(frames)}")

# Mostra cada quadro extraÃ­do
for i, frame_bgr in enumerate(frames):
    cv2.imshow("Frame", frame_bgr)
    if cv2.waitKey(30) & 0xFF == ord('q'):  # Pressione 'q' para sair
        break

cv2.destroyAllWindows()
