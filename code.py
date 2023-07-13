import cv2 
import mediapipe as mp
camara=cv2.VideoCapture(0)
mp_hands=mp.solutions.hands
mp_drawing=mp.solutions.drawing_utils
hands=mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5)
tipid=[8,12,16,20]
def countfingers(image,hand_landmarks,handnumber=0):
    if( hand_landmarks):
        landmarks=hand_landmarks[handnumber].landmark
        fingers=[]
        for id in tipid:
            fingertipy=landmarks[id].y
            fingerbottomy=landmarks[id-2].y
            if(fingertipy<fingerbottomy):
                fingers.append(1)
            if(fingertipy>fingerbottomy):
                fingers.append(0)
        totalfingers=fingers.count(1)
        text=f'FINGERS:{totalfingers}'
        cv2.putText(image,text,(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)            
def drawlandmark(image,hand_landmark):
    if hand_landmark:
        for l in hand_landmark:
            mp_drawing.draw_landmarks(image,l,mp_hands.HAND_CONNECTIONS)

while True:
    succes,image=camara.read()
    image=cv2.flip(image,1)
    results=hands.process(image)
    hand_landmark=results.multi_hand_landmarks
    drawlandmark(image,hand_landmark)
    countfingers(image,hand_landmark)
    cv2.imshow('output',image)
    if cv2.waitKey(1)==32:
        break