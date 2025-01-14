# Plate Detection Web App 🚗📸
Este proyecto consiste en detectar placas de vehículos en imágenes, combinando herramientas de etiquetado, entrenamiento de modelos de detección de objetos y un frontend interactivo desarrollado con Streamlit.
![image](https://github.com/user-attachments/assets/bb609b0a-416e-40b5-a9de-442aa4dfd686)


## Características del proyecto 🌟
* Etiquetado del dataset
  Utilicé la plataforma Roboflow para etiquetar imágenes de vehículos, marcando la ubicación de las placas. Esto permitió generar un conjunto de datos estructurado con anotaciones precisas.

  ![image](https://github.com/user-attachments/assets/155644c6-d627-46e3-aab1-24a738d4bb75)

* Entrenamiento del modelo

Descargué el dataset etiquetado en formatos compatibles con YOLOv8.
Entrené el modelo utilizando la librería Ultralytics YOLO en un notebook, optimizando el rendimiento para detectar placas en imágenes.

* Desarrollo del frontend

Implementé una aplicación interactiva con Streamlit que permite:
Subir imágenes de vehículos.
Mostrar la detección de la placa en la imagen.
Extraer y visualizar únicamente la placa detectada.
