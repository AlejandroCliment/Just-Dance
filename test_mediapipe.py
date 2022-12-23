#DIBUJA EL ESQUELETO EN LAS FOTOS DEL TEST PARA MEDIAPIPE
import cv2
import mediapipe as mp
import os

entrada='/home/erika/Escritorio/Vision/just dance refachero/frames_mediapipe'
imagenes=os.listdir(entrada)

for i in imagenes:
    # utils for drawing on image
    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles
    mp_pose = mp.solutions.pose
    # mediapipe pose model
    with mp_pose.Pose(
            static_image_mode=False,#Imagen
            model_complexity=2,
            enable_segmentation=False,
            min_detection_confidence=0.3) as pose:#Sensibilidad
        
        image = cv2.imread(entrada+"/"+i)
        if image is None:#Comprobación
            print("Error al cargar la imagen", image)
            quit()
        #convert image to RGB (just for input to model)
        image_input = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # get results using mediapipe
        results = pose.process(image_input)

        if not results.pose_landmarks:
            print("no results found")
        else:
            mp_drawing.draw_landmarks(
                image,
                results.pose_landmarks,
                mp_pose.POSE_CONNECTIONS,
                landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())

        # write image to storage
        cv2.imwrite(i, image)
        print("Foto" ,i, "Guardada")