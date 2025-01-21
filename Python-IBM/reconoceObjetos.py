import cv2
import numpy as np
import tensorflow as tf

# Convertir el modelo a TensorFlow Lite
converter = tf.lite.TFLiteConverter.from_saved_model('C:\\Users\\09773491d\\Documents\\Modelos\\ssd_mobilenet_v2_coco_2018_03_29')
tflite_model = converter.convert()

# Guardar el modelo convertido
with open('model.tflite', 'wb') as f:
    f.write(tflite_model)

# Cargar el modelo TensorFlow Lite
interpreter = tf.lite.Interpreter(model_path='model.tflite')
interpreter.allocate_tensors()

# Obtener detalles de entrada y salida
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Función para realizar la detección de objetos
def detect_objects(image_np):
    input_data = np.expand_dims(image_np, axis=0).astype(np.uint8)
    interpreter.set_tensor(input_details[0]['index'], input_data)
    interpreter.invoke()
    boxes = interpreter.get_tensor(output_details[0]['index'])
    classes = interpreter.get_tensor(output_details[1]['index'])
    scores = interpreter.get_tensor(output_details[2]['index'])
    num = interpreter.get_tensor(output_details[3]['index'])
    return boxes, classes, scores, num

# Función para dibujar las etiquetas y marcos en la imagen
def draw_labels(image_np, boxes, classes, scores, category_index, threshold=0.5):
    for i in range(boxes.shape[1]):
        if scores[0, i] > threshold:
            class_name = category_index[int(classes[0, i])]
            if class_name == 'person':
                box = boxes[0, i]
                (startY, startX, endY, endX) = (box[0] * image_np.shape[0], box[1] * image_np.shape[1],
                                                box[2] * image_np.shape[0], box[3] * image_np.shape[1])
                cv2.rectangle(image_np, (int(startX), int(startY)), (int(endX), int(endY)), (0, 255, 0), 2)
                label = f"{class_name}: {scores[0, i]*100:.2f}%"
                cv2.putText(image_np, label, (int(startX), int(startY) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    return image_np

# Abrir una conexión con la cámara web
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    if not ret:
        break
    
    # Realizar la detección de objetos
    boxes, classes, scores, num = detect_objects(frame)
    
    # Dibujar etiquetas y marcos en el fotograma
    frame = draw_labels(frame, boxes, classes, scores, category_index)
    
    # Mostrar el fotograma
    cv2.imshow('Person Detection - Press Q to Quit!', frame)
    
    # Salir del bucle si se presiona Q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara web y cerrar todas las ventanas de OpenCV
cap.release()
cv2.destroyAllWindows()
