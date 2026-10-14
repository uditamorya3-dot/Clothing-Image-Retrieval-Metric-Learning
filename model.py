# model.py - DAVV Module 3: Deep Metric Learning
import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import GlobalAveragePooling2D
from tensorflow.keras.models import Model
import numpy as np
from PIL import Image

print("Model load ho raha hai...")

# Pre-trained CNN 
base_model = MobileNetV2(weights='imagenet', include_top=False, input_shape=(224,224,3))
x = GlobalAveragePooling2D()(base_model.output)
embedding_model = Model(inputs=base_model.input, outputs=x)

def get_embedding(image_path):
    img = Image.open(image_path).resize((224,224))
    img = np.array(img) / 255.0
    if img.shape[-1] == 4:
        img = img[:,:,:3]
    if len(img.shape) == 2:
        img = np.stack([img]*3, axis=-1)
    img = np.expand_dims(img, axis=0)
    embedding = embedding_model.predict(img, verbose=0)
    return embedding[0]

def find_similar(query_embedding, all_embeddings, top_k=3):
    # Cosine similarity 
    scores = []
    for emb in all_embeddings:
        sim = np.dot(query_embedding, emb) / (np.linalg.norm(query_embedding) * np.linalg.norm(emb))
        scores.append(sim)
    sorted_idx = np.argsort(scores)[::-1][:top_k]
    return sorted_idx, [scores[i] for i in sorted_idx]

print("Model Ready! ✅")