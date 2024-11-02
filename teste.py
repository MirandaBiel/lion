from picamera2.outputs import FileOutput
from picamera2.encoders import Encoder
import io
import time


picam2 = Picamera2()
video_config = self.ui.picam2.create_video_configuration(
            controls={"FrameDurationLimits": (33333, 33333)},  # Limita para 30 fps
            main={"size": (800, 600)}
        )
picam2.configure(video_config)

encoder = Encoder()
buffer = io.Bytes()
output = FileOutput(buffer)

picam2.start_recording(encoder, output)
time.sleep(5)
picam2.stop_recording()

print("PROCESSO FINALIZADO")