import cv2
import mediapipe as mp
import numpy as np
import pyautogui
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands



cap = cv2.VideoCapture(0)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
with mp_hands.Hands(
    max_num_hands=1,
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      
      continue

    
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image)
    
    
    

    #image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:
        mp_drawing.draw_landmarks(
            image,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style())
        
        index_finger_tip_x = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * width
        index_finger_tip_y = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * height
        thumb_finger_tip_x = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x * width
        thumb_finger_tip_y = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y * height
        thumb_index_distance=((index_finger_tip_x - thumb_finger_tip_x)**2 + (index_finger_tip_y - thumb_finger_tip_y)**2)**0.5       
        if (thumb_index_distance<30):
                  
            pyautogui.press("space")
        
        
    
    cv2.imshow('Chrome Dinosaur', cv2.flip(image, 1))
    if cv2.waitKey(5) & 0xFF == 27:
      break
    
    
    
cap.release()