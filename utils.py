
import mediapipe as mp
import pandas as pd
import numpy as np
import cv2

mp_pose = mp.solutions.pose



def calculate_angle(a, b, c):
    a = np.array(a)  
    b = np.array(b)  
    c = np.array(c)  

    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) -\
              np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180.0 / np.pi)

    # check cord sys area
    if angle > 180.0:
        angle = 360 - angle

    return angle



def detection_body_part(landmarks, body_part_name):
    return [
        landmarks[mp_pose.PoseLandmark[body_part_name].value].x,
        landmarks[mp_pose.PoseLandmark[body_part_name].value].y,
        landmarks[mp_pose.PoseLandmark[body_part_name].value].visibility
    ]


def detection_body_parts(landmarks):
    body_parts = pd.DataFrame(columns=["body_part", "x", "y"])

    for i, lndmrk in enumerate(mp_pose.PoseLandmark):
        lndmrk = str(lndmrk).split(".")[1]
        cord = detection_body_part(landmarks, lndmrk)
        body_parts.loc[i] = lndmrk, cord[0], cord[1]

    return body_parts


def score_table(exercise, counter, status):
    score_table = cv2.imread("./images/score_table.png")
    cv2.putText(score_table, "Activity : " + exercise.replace("-", " "),
                (10, 65), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (182, 158, 128), 2,
                cv2.LINE_AA)
    cv2.putText(score_table, "Counter : " + str(counter), (10, 100),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (182, 158, 128), 2, cv2.LINE_AA)
    cv2.putText(score_table, "Status : " + str(status), (10, 135),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (182, 158, 128), 2, cv2.LINE_AA)
    cv2.imshow("Score Table", score_table)