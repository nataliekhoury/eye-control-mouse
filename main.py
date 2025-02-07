import cv2
import mediapipe as mp
import pyautogui
cam =cv2.VideoCapture(0) #detect the first webcam in the index 0
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True) # detect the eye
screen_width, screen_height = pyautogui.size()


while True:
    _, frame = cam.read() # capture every frame from the camera
    frame =cv2.flip(frame,1) # vertical flip
    rgb_frame =cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    result = face_mesh.process(rgb_frame)
    landmark_point = result.multi_face_landmarks

    frame_h, frame_w, _ = frame.shape

    # loop and draw the points face
    if landmark_point:
        landmarks = landmark_point[0].landmark
        for id,landmark in enumerate(landmarks[474:478]):
            x= int (landmark.x * frame_w) # the frame's width
            y= int (landmark.y * frame_h)  # the frame's high
            cv2.circle(frame,(x,y),3,(0,255,0)) # draw small circles all over the user eye
            if id==1:
                screen_x=screen_width/frame_w * x
                screen_y=screen_height/frame_h * y
                pyautogui.moveTo(screen_x,screen_y)

        left=[landmarks[145],landmarks[159]]
        for landmark in left:
            x = int(landmark.x * frame_w)  # the frame's width
            y = int(landmark.y * frame_h)  # the frame's high
            cv2.circle(frame, (x, y), 3, (0, 255, 255))  # draw small circles all over the user eye

            #check if the left eye is blinking
        if (left[0].y-left[1].y) < 0.005:
            print("click")
            pyautogui.click()

            pyautogui.sleep(1)

    cv2.imshow('control eye', frame)
    cv2.waitKey(1)




