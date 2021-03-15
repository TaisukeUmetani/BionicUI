def hand_tracker():
    import cv2
    import mediapipe as mp

    mp_drawing = mp.solutions.drawing_utils
    mp_hands = mp.solutions.hands
    cap = cv2.VideoCapture(0)

    with mp_hands.Hands(
            max_num_hands=4,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5) as hands:
        while cap.isOpened():
            tick = cv2.getTickCount()
            success, image = cap.read()
            if not success:
                print("Ignoring empty camera frame.")
                # If loading a video, use 'break' instead of 'continue'.
                continue

            # Flip the image horizontally for a later selfie-view display, and convert
            # the BGR image to RGB.
            image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
            # To improve performance, optionally mark the image as not writeable to
            # pass by reference.
            image.flags.writeable = False
            results = hands.process(image)

            print(results.multi_hand_landmarks)

            # Draw the hand annotations on the image.
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(
                        image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            resize_frame = cv2.resize(image, dsize=None, fx=3., fy=3.)
            fps = cv2.getTickFrequency() / (cv2.getTickCount() - tick)
            cv2.putText(
                resize_frame,
                "FPS: " + str(int(fps)),
                (image.shape[1] - 150, 40),
                cv2.FONT_HERSHEY_PLAIN,
                3,
                (0, 255, 0),
                3,
                cv2.LINE_AA)

            delay = 1
            cv2.imshow('hand_tracker (demo)', resize_frame)
            key = cv2.waitKey(delay) & 0xFF
            if key == ord('q'):
                break

        cap.release()


if __name__ == "__main__":
    hand_tracker()
