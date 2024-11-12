import matplotlib.pyplot as plt
import mediapipe as mp
import numpy as np
import math
import cv2
import rPPG_Methods as rppg

face_mesh = mp.solutions.face_mesh.FaceMesh(
    min_detection_confidence=0.5, 
    min_tracking_confidence=0.5, 
    max_num_faces=1
)

