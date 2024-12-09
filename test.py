import matplotlib.pyplot as plt
import process_functions as pf
import Signal_Quality as sqi
import rPPG_Methods as rppg
import mediapipe as mp
import extract as ex
import numpy as np
import cv2

def sqi_window_control(signal, fs, window_size):
    D = sqi.PPG_analysis(signal, fs, window_size)
    if (D['LSQI'] > 0.293) and (D['KSQI'] > 0.221):
        print("Unfitted signal")
        return 
    else:
        if len(D['exc_window']) == 0:
            return D['acc_window'], D['LSQI'], D['KSQI']
        else:
            return D['exc_window'], D['LSQI'], D['KSQI']


# Parâmetros
patches = [151, 101, 330]  # Regiões de interesse (números de landmarks)
face_mesh = mp.solutions.face_mesh.FaceMesh(
    min_detection_confidence=0.5, 
    min_tracking_confidence=0.5, 
    max_num_faces=1
)
fs = 30  # Frequência de amostragem (Hz)

# Caminho do vídeo
caminho_video = 'LioN\\cache\\video_face_1.h264'

# Lista para armazenar os valores RGB
rppg_channels = []
rppg_channels_ssr = []

# Abre o vídeo
captura = cv2.VideoCapture(caminho_video)

if not captura.isOpened():
    print("Erro ao abrir o vídeo.")
else:
    while True:
        ret, frame = captura.read()
        if not ret:
            print("Fim do vídeo ou erro ao ler frame.")
            break
        
        # Processa o frame e armazena o resultado
        rgb_values = ex.processa_um_frame(frame)  # Agora retorna [num_patches, 3]
        rppg_channels.append(rgb_values)

        # Processa o frame e extrai o patch 151 com tamanho fixo
        patch_crop = ex.processa_um_frame_ssr(frame, target_size=(32, 32))
        rppg_channels_ssr.append(patch_crop)
        
        # Exibe o frame
        cv2.imshow('Frame', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

# Libera o objeto de captura e fecha a janela
captura.release()
cv2.destroyAllWindows()

# Converte a lista para um ndarray com shape [num_patches, 3, num_frames]
rppg_channels = np.array(rppg_channels, dtype=np.float32)
rppg_channels = rppg_channels.transpose(1, 2, 0)

# Converte a lista para um ndarray com o formato necessário [num_frames, rows, columns, rgb_channels]
rppg_channels_ssr = np.array(rppg_channels_ssr, dtype=np.float32)

# Aplicar métodos rPPG
bvp_chrom = rppg.CHROM(rppg_channels)
bvp_green = rppg.GREEN(rppg_channels)
bvp_lgi = rppg.LGI(rppg_channels)
bvp_pos = rppg.POS(rppg_channels, fps=fs)
bvp_gbgr = rppg.GBGR(rppg_channels)
bvp_ica = rppg.ICA(rppg_channels, component='second_comp')
bvp_omit = rppg.OMIT(rppg_channels)
bvp_pbv = rppg.PBV(rppg_channels)
bvp_pca = rppg.PCA(rppg_channels, component='second_comp')
bvp_ssr = rppg.SSR(rppg_channels_ssr, fps=fs)

# Lista de sinais e seus rótulos
bvp_signals = [bvp_chrom, bvp_green, bvp_lgi, bvp_pos, bvp_gbgr, bvp_ica, bvp_omit, bvp_pbv, bvp_pca, bvp_ssr]

# Analisa os formatos de retorno
for i in bvp_signals:
    print(f'Shape: {i.shape}')

labels = ['CHROM', 'GREEN', 'LGI', 'POS', 'GBGR', 'ICA', 'OMIT', 'PBV', 'PCA', 'SSR']

# Plotar os sinais BVP extraídos
#ex.plot_bvp_signals_separately(bvp_signals, labels, fs)

# Testa os sinais BVP extraídos
for bvp, label in zip(bvp_signals, labels):
        n_patches, num_frames = bvp.shape

        for patch_idx in range(n_patches):
            # Filtra o sinal 
            filt_bvp = pf.filter_z_butterworth(bvp[patch_idx, :], 30)

            # Seleciona a melhor janela para analise
            window, LSQI, KSQI = sqi_window_control(filt_bvp, 30, 5)
            time = np.linspace(0, len(window) / fs, len(window))

            # Calcula BPM e iRPM do sinal
            spectrum, freqs = pf.calculate_fft(window, 30)
            bpm = pf.find_peak_in_range(spectrum, freqs)
            irpm = pf.calc_frequencia_respiratoria(window, 30)

            plt.figure(figsize=(10, 6))
            plt.plot(time, window, label=f'Patch {patch_idx+1}')
            plt.title(f'Sinal BVP - Método: {label} (Patch {patch_idx+1}, NSQI: {LSQI}, KSQI: {KSQI}, BPM: {round(bpm, 3)}, iRPM: {round(irpm, 3)})')
            plt.xlabel('Tempo (s)')
            plt.ylabel('Amplitude')
            plt.legend()
            plt.grid(True)
            plt.show()

            