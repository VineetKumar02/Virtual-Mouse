import cv2
import mediapipe as mp
import pyautogui

cam = cv2.VideoCapture(0)   # capture 1st video source
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks = True)
screen_width, screen_height = pyautogui.size()  # get screen dimensions

while True: # run forever
    _, frame = cam.read()   # read watever is captued by cam
    frame = cv2.flip(frame,1)   # flip frame vertically
    frame_height, frame_width, _ = frame.shape   # get frame dimensions

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # change color of frame from Grayscale to RGB
    output = face_mesh.process(rgb_frame)   # process the rgb frame

    landmark_points = output.multi_face_landmarks

    if landmark_points:  # if the face exists
        landmarks = landmark_points[0].landmark   # choose the 1st face

        for id, landmark in enumerate(landmarks[474:478]):  # divide eye into 4 landmarks
            x = int(landmark.x * frame_width )   # get position of face in width
            y = int(landmark.y * frame_height )   # get position of face in height
            cv2.circle(frame, (x,y), 3, (0, 255, 0))  # draw circles on frame with centre as(x,y) with radius as 3 and color as green(in rgb)

            if id == 1:
                screen_x = landmark.x * screen_width   # get position of cursor along width
                screen_y = landmark.y * screen_height   # get position of cursor along height
                pyautogui.moveTo(screen_x, screen_y)   # move cursor to given location

        left = [landmarks[145], landmarks[159]]  # landmarks of top and bottom lids of left eye

        for landmark in left:
            x = int(landmark.x * frame_width )  # get position of face in width
            y = int(landmark.y * frame_height )  # get position of face in height
            cv2.circle(frame, (x,y), 3, (0, 255, 255))  # draw circles on frame with centre as(x,y) with radius as 3 and color as yellow(in rgb)

            if(left[0].y - left[1].y < 0.004):  # get vertical postions of both landmarks(<0.004 means eyes r closed)
                pyautogui.click()  # click
                pyautogui.sleep(0.5)  # wait for 0.5 sec

    cv2.imshow('Eye Controlled Mouse', frame)  # show frame with the window name 'Eye Controlled Mouse'
    cv2.waitKey(1)   # wait for 1 sec