import cv2

# Caminho do vídeo
caminho_video = 'video_face_4.h264'  # Substitua pelo caminho do seu vídeo H.264

# Abre o vídeo
captura = cv2.VideoCapture(caminho_video)
cont = 0

# Verifica se o vídeo foi aberto corretamente
if not captura.isOpened():
    print("Erro ao abrir o vídeo.")
else:
    # Loop para ler e processar cada frame
    while True:
        # Lê um frame
        ret, frame = captura.read()
        
        # Verifica se conseguiu ler o frame
        if not ret:
            print("Fim do vídeo ou erro ao ler frame.")
            break
        
        # Processamento específico: neste caso, exibir o frame
        cv2.imshow('Frame', frame)
        cont = cont + 1
        
        # Aguarda uma tecla por 25 ms. Pressione 'q' para sair do loop
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

print(f'Frames capturados: {cont}')
# Libera o objeto de captura e fecha a janela
captura.release()
cv2.destroyAllWindows()
