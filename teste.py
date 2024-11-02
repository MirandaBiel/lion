from picamera2.outputs import FileOutput
from picamera2.encoders import Encoder
from picamera2 import Picamera2
from PyQt5 import QtCore, QtGui, QtWidgets
import io
import time


picam2 = Picamera2()
video_config = picam2.create_video_configuration(
            controls={"FrameDurationLimits": (33333, 33333)},  # Limita para 30 fps
            main={'format': 'XBGR8888', "size": (800, 600)}
        )
picam2.configure(video_config)

encoder = Encoder()
buffer = io.BytesIO()
output = FileOutput(buffer)

picam2.start_recording(encoder, output)
time.sleep(5)
picam2.stop_recording()

print("PROCESSO FINALIZADO")