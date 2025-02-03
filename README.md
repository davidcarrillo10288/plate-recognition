# Plate Detection Web App 🚗📸
Este proyecto consiste en detectar placas de vehículos en imágenes, combinando herramientas de etiquetado, entrenamiento de modelos de detección de objetos y un frontend interactivo desarrollado con Streamlit.
![image](https://github.com/user-attachments/assets/bb609b0a-416e-40b5-a9de-442aa4dfd686)


## Características del proyecto 🌟

### Etiquetado del dataset
* Utilicé la plataforma Roboflow para etiquetar imágenes de vehículos, marcando la ubicación de las placas. Esto permitió generar un conjunto de datos estructurado con anotaciones precisas.

  ![image](https://github.com/user-attachments/assets/155644c6-d627-46e3-aab1-24a738d4bb75)

### Entrenamiento del modelo

* Descargué el dataset etiquetado en formatos compatibles con YOLOv8.
* Entrené el modelo utilizando la librería Ultralytics YOLO en un notebook, optimizando el rendimiento para detectar placas en imágenes.

### Desarrollo del frontend

* Implementé una aplicación interactiva con Streamlit que permite:
* Subir imágenes de vehículos.
* Mostrar la detección de la placa en la imagen.
* Extraer y visualizar únicamente la placa detectada.

## Capturas de pantalla 📸
### Interfaz principal:

* Imagen original: Se muestra la imagen cargada.
* Detección de la placa: Visualización del área detectada con un marcador.
* Recorte de la placa: Imagen de la placa extraída.

![image](https://github.com/user-attachments/assets/9d26d74c-8036-4c18-b20a-76071e1baa64)

## Tecnologías utilizadas 🛠️
* Roboflow: Para etiquetar las imágenes.
* YOLOv8 (Ultralytics): Para entrenar el modelo de detección de objetos.
* Streamlit: Para desarrollar el frontend interactivo.
* Google colab: Desarrollo de código para entrenar modelo.
* Python: Lenguaje de programación utilizado.
* VS code: IDE para Desarrollar el script y prueba.
* CMDER: consola.

## Próximos pasos 🚀
* Mejorar la precisión del modelo con más datos.
* Extender el soporte a videos para detección en tiempo real.
* Integrar una funcionalidad OCR para extraer el texto de las placas detectadas.

## Cómo usar este proyecto 🚀

### Clonar el repositorio
```bash
git clone https://github.com/davidcarrillo10288/plate-recognition.git
cd plate-detection-web-app
```

## Asegúrate de tener Python 3.8+ instalado y ejecuta
```bash
pip install -r requirements.txt
```

## Ejecuta la app.
```bash
streamlit run app.py
```
