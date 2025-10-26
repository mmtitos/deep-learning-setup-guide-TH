## 🔹 Proyectos de nivel básico
Enfocados en comprender el flujo completo: adquisición → procesado → clasificación o síntesis.
### 1. Clasificador de sonidos del habla vs. ruido ambiental
  Entrenamiento de una red neuronal para distinguir voz humana de ruido.
  Dataset: UrbanSound8K o grabaciones propias.
  Objetivo: detección de actividad vocal (Voice Activity Detection).
### 2. Reconocimiento de emociones en el habla
  Clasificar emociones (alegría, enfado, tristeza, neutro) a partir del audio.
  Dataset: RAVDESS o CREMA-D.
  Aprender extracción de espectrogramas, MFCCs y uso de CNNs simples.
### 3. Reconocimiento de hablantes
  Identificar a la persona que habla entre un conjunto de 5–10 voces.
  Dataset: VoxCeleb mini subset o grabaciones de clase.
  Permite aplicar embeddings y métricas de distancia.
### 4. Detección automática de palabras clave (“OK UGR”)
  Sistema tipo keyword spotting para activar una acción cuando detecta una palabra específica.
  Dataset: Google Speech Commands.
  Permite experimentar con CNNs o RNNs ligeras.
## 🔹 Proyectos de nivel intermedio (grupos de 3–4 estudiantes)
Integran distintos módulos de procesamiento, reconocimiento o síntesis.
### 1. Sistema básico de reconocimiento automático del habla (ASR)
  Entrenar o adaptar un modelo speech-to-text con Wav2Vec2 o Whisper (Hugging Face).
  Aplicación: transcripción de grabaciones cortas o comandos simples.
  Conversor de voz a texto con análisis semántico
### 2. Transcribir y analizar sentimientos o intenciones en la voz.
  Combina ASR + modelo de lenguaje (transformer).
  Conversor texto-voz (TTS) personalizado
### 3. Generar voz sintética.
  Permite mostrar redes encoder–decoder y generación secuencial.
### 4. Detector de acentos o dialectos del español
   Clasificar el acento de una muestra de voz (andaluz, castellano, latinoamericano…).
  Dataset: Common Voice.
## 🔹 Proyectos de nivel avanzado o integrador (grupos de 4–5 estudiantes)
Combina varias tecnologías del habla y requiere diseño de sistema completo.
### 1. Asistente de voz local sin conexión
  Combina detección de palabra clave, reconocimiento de voz y síntesis de respuesta.
  Ejemplo: “Encender luz”, “¿Qué hora es?”.
  Requiere integrar varios modelos ligeros y una interfaz de usuario.
### 2. Evaluador de pronunciación para aprendizaje de idiomas
  Analiza cómo pronuncia el alumno comparando con una referencia.
  Usa forced alignment y embeddings acústicos.
  Aplicación práctica para e-learning.
### 3. Sistema de análisis de voz para detección temprana de fatiga o estrés
  Analiza parámetros prosódicos y espectrales de la voz.
