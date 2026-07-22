
import time
import numpy as np
from sklearn.svm import SVC
import streamlit as st  #type:ignore
from src.database.db import get_all_students
from insightface.app import FaceAnalysis #type:ignore
from sklearn.metrics.pairwise import cosine_similarity


@st.cache_resource
def load_dlib_detector_models():
    start = time.perf_counter()

    app = FaceAnalysis(
        name="buffalo_l", #large Model
        # name="buffalo_sc", #small Model
        providers=["CPUExecutionProvider"]
    )
    app.prepare(
        ctx_id=0,
        det_size=(512,512)
    )

    print(f"Model Loading Time: {time.perf_counter() - start:.3f} sec")
    return app


@st.cache_resource
def check_face(img):
    start = time.perf_counter()

    detector = load_dlib_detector_models()
    faces = detector.get(img)

    print(f"Face Detection Time: {time.perf_counter() - start:.3f} sec")
    return faces


@st.cache_resource
def get_face_embeddings(image_np, faces):
    start = time.perf_counter()

    embeddings = []
    for face in faces:
        embeddings.append(face.embedding)

    print(f"Embedding Time: {time.perf_counter() - start:.3f} sec")
    return embeddings


@st.cache_resource
def get_trained_model():
    start = time.perf_counter()

    x = []
    y = []

    student_db = get_all_students()

    if not student_db:
        return None

    for student in student_db:
        embedding = student.get('face_embedding')
        if embedding:
            x.append(np.array(embedding))
            y.append(student.get('student_id'))

    if len(x) == 0:
        return 0

    model = SVC(kernel='linear', probability=True, class_weight='balanced')

    try:
        model.fit(x, y)
    except ValueError:
        pass

    print(f"SVM Training Time: {time.perf_counter() - start:.3f} sec")
    return {'model_clf': model, "x": x, "y": y}


@st.cache_resource
def train_classifier():
    start = time.perf_counter()

    st.cache_resource.clear()
    model_data = get_trained_model()

    print(f"Train Classifier Time: {time.perf_counter() - start:.3f} sec")
    return bool(model_data)


@st.cache_resource
def predict_attendance(class_image_np, faces):
    total_start = time.perf_counter()

    start = time.perf_counter()
    encodings = get_face_embeddings(class_image_np, faces)
    print(f"Embedding Extraction: {time.perf_counter() - start:.3f} sec")

    start = time.perf_counter()
    model_data = get_trained_model()
    print(f"Load Trained Model: {time.perf_counter() - start:.3f} sec")

    detected_student = {}

    if not model_data:
        return detected_student, []

    clf = model_data['model_clf']
    x_train = model_data["x"]
    y_train = model_data["y"]

    all_students = sorted(list(set(y_train)))

    for encoding in encodings:

        svm_start = time.perf_counter()

        if len(all_students) >= 2:
            predicted_id = int(clf.predict([encoding])[0])
        else:
            predicted_id = int(all_students[0])

        print(f"SVM Prediction: {time.perf_counter() - svm_start:.6f} sec")

        sim_start = time.perf_counter()

        student_embedding = x_train[y_train.index(predicted_id)]

        similarity = cosine_similarity(
            [student_embedding],
            [encoding]
        )[0][0]

        print(f"Cosine Similarity: {time.perf_counter() - sim_start:.6f} sec")

        if similarity >= 0.5:
            detected_student[predicted_id] = True

    print(f"Total Prediction Time: {time.perf_counter() - total_start:.3f} sec")

    return detected_student, all_students