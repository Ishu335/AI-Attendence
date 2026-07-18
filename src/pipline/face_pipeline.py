import numpy as np
from sklearn.svm import SVC
import streamlit as st  #type:ignore
from src.database.db import get_all_students
from insightface.app import FaceAnalysis #type:ignore

@st.cache_resource
def load_dlib_detector_models():
    app = FaceAnalysis(
        name="buffalo_l",
        providers=["CPUExecutionProvider"]
    )
    app.prepare(
        ctx_id=-1,
        det_size=(640, 640)
    )
    return app


def check_face(img):
    detector = load_dlib_detector_models()
    faces = detector.get(img)
    return faces

def get_face_embeddings(image_np,faces):
    embeddings=[]
    for face in faces:
        embeddings.append(face.embedding)
    return embeddings


@st.cache_resource
def get_trained_model():
    x=[]
    y=[]
    student_db=get_all_students()
    if not student_db:
        return None
    for student in student_db:
        embedding =student.get('face_embedding')
        if embedding:
            x.append(np.array(embedding))
            y.append(student.get('student_id'))
    
    if len(x)==0:
        return 0
    
    model=SVC(kernel='linear',probability=True,class_weight='balanced')
    # | Parameter                 | Meaning                                                                                                           |
    # ----------------------------------------------------------------------------------------------------------------------------------------------- |
    # | `kernel='linear'`         | Uses a **linear decision boundary** (straight line/plane) to separate classes. Best for linearly separable data.                                |
    # | `probability=True`        | Enables `predict_proba()` to return the probability of each class. It makes training slightly slower.                                           |
    # | `class_weight='balanced'` | Automatically gives **more importance to the minority class** when the dataset is imbalanced. This helps reduce bias toward the majority class. |

    try: 
        model.fit(x,y)
    except ValueError:
        pass
    return {'model_clf':model,"x":x,"y":y}

def train_classifier():
    st.cache_resource.clear()
    model_data=get_trained_model()
    return bool(model_data)

def predict_attendance(class_image_np,faces):
    encodings = get_face_embeddings(class_image_np,faces)
    detected_student = {}

    model_data = get_trained_model()
    if not model_data:
        return detected_student, []

    clf = model_data['model_clf']
    x_train = model_data["x"]
    y_train = model_data["y"]

    all_students = sorted(list(set(y_train)))


    from sklearn.metrics.pairwise import cosine_similarity

    for encoding in encodings:
        if len(all_students) >= 2:
            predicted_id = int(clf.predict([encoding])[0])
        else:
            predicted_id = int(all_students[0])
        student_embedding = x_train[y_train.index(predicted_id)]

        similarity = cosine_similarity([student_embedding],[encoding])[0][0] # type: ignore


        if similarity >= 0.5:
            detected_student[predicted_id] = True
            predicted_id = int(clf.predict([encoding])[0])
    return detected_student, all_students