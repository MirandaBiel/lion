from picamera2 import Picamera2
from collections import deque
import io

fs = 30 # Hz
ts = 5 # s
n_frames = fs * ts + 10

queue = deque(maxlen=n_frames)

picam2 = Picamera2()
video_config = picam2.create_video_configuration(controls={"FrameDurationLimits": (33333, 33333)}, main={"size": (800, 600)})
picam2.configure(video_config)
picam2.start()

for _ in range(2):
    main, metadata = picam2.capture_arrays()
    print(metadata)
    print(main)

picam2.stop()