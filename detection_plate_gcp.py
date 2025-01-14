import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

import os
from io import BytesIO
import requests
import tempfile

from ultralytics import YOLO
import torch
import streamlit as st
# plt.switch_backend('Agg')  # Esto fuerza el uso de un backend no interactivo

# Cambiar fondo a negro y texto a blanco usando CSS
st.markdown(
    """
    <style>
    body {
        background-color: black;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

#Título de la app
st.title('PLATE DETECTION WEB APP')

# *********************************************************************
# *********************************************************************
###### DESCARGANDO EL MODELO .PT DESDE MI REPO PRIVADO DE GITHUB ######
# *********************************************************************
# *********************************************************************

# Leer el token desde una variable de entorno y el URL de github del modelo
token = os.getenv('GITHUB_TOKEN')
url = 'https://github.com/davidcarrillo10288/Hyperblog/raw/master/best.pt'

# Configurar las cabeceras para autenticación
headers = {
    'Authorization': f'token {token}'
}

# Descargar el archivo desde la URL
response = requests.get(url, headers=headers)

if response.status_code == 200:
    # Guardar el archivo en un archivo temporal
    with tempfile.NamedTemporaryFile(delete=False, suffix='.pt') as temp_file:
        temp_file.write(response.content)
        temp_file_path = temp_file.name

    # Cargar el modelo desde el archivo temporal
    model = YOLO(temp_file_path)
else:
    print(f"Error al descargar el archivo: {response.status_code}")
    model = None

# *********************************************************************
# *********************************************************************
# *********************************************************************
# *********************************************************************


# Widget para cargar una imagen
uploaded_file = st.file_uploader("Elige una imagen", type=["jpg", "jpeg", "png"])

# Botón para limpiar la pantalla
if st.button("Limpiar pantalla"):
    uploaded_file = None  # Restablecer el archivo carga

if uploaded_file is not None:

    # Abre la imagen
    image_path = Image.open(uploaded_file)
    # Convertir la imagen a RGB si tiene un canal alfa (RGBA a RGB)
    if image_path.mode == 'RGBA':
        image_path = image_path.convert('RGB')
    
    # Convertir la imagen a una matriz de píxeles (array de NumPy)
    image_array = np.array(image_path)

    # Realizar la predicción
    detections = model.predict(source=image_array)
    result_image = detections[0].plot()

    # Obtener las coordenadas de detección
    coordenadas = detections[0].boxes.xyxy  # .xyxy retorna [x_min, y_min, x_max, y_max]
    
    # Verificar si se detectaron coordenadas
    if len(coordenadas) > 0:
        # Convertir las coordenadas a enteros
        x_min, y_min, x_max, y_max = map(int, coordenadas[0])
        
        # Recortar la imagen usando las coordenadas obtenidas
        image_plate_array = image_array[y_min:y_max, x_min:x_max]
        
        # Convertir la imagen recortada de vuelta a un objeto PIL para mostrarla
        image_plate = Image.fromarray(image_plate_array).resize((image_array.shape[1], image_array.shape[0]))

    # Crear tres columnas para mostrar las imágenes
    col1, col2, col3 = st.columns(3)

    with col1:
        st.image(image_path, caption="ORIGINAL IMAGE", use_column_width=True)  # Imagen original

    with col2:
        st.image(result_image, caption="IMAGE WITH PLATE DETECTION", use_column_width=True)  # Imagen procesada

    with col3:
        st.image(image_plate, caption="PLATE IMAGE", use_column_width=True)  # Imagen de la placa detectada