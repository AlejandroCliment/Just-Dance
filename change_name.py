
# Importamos las librerias necesarias
import cv2
import os

#pwd ->  ver el directorio de la ruta actual

# Directorio donde estan las imagenes de entrada
input_images_path = "/home/usuario/Escritorio/Vision/Proyecto/FotosPrueba2/Poses/Pose16"
# Directorio donde se guardan las imagenes de salida
output_images_path = "/home/usuario/Escritorio/Vision/Proyecto/FotosPrueba2/Poses"


files_names = os.listdir(input_images_path)
#print(files_names)
print("Numero de imagenes: " + str(len(files_names)))


# Si el directorio no existe, se crea
if not os.path.exists(output_images_path):
    os.makedirs(output_images_path)
    print("Directorio creado: ", output_images_path)

count = 197

for file_name in files_names:
    print(file_name)
    
    # Si la extencion de la imagen NO esta dentro de los de la 
    # lista salta a la siguiente imagen
    #if file_name.split(".")[-1] not in ["jpeg", "png", ".jpg"]:
    #    continue
    
    image_path = input_images_path + "/" + file_name
    print(image_path)
    image = cv2.imread(image_path)
    if image is None:
        continue

    # Para redimencionar la imagen
    #image = cv2.resize(image, (100, 100), interpolation=cv2.INTER_CUBIC)

    cv2.imwrite("Pose16_Muestra" + str(count) + ".png", image)
    count += 1
    
# Comentar las tres ultimas lineas para que sea todo automatico
'''
    cv2.imshow("Image", image)
    cv2.waitKey(0)
cv2.destroyAllWindows()
'''
