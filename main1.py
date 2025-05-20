import cv2
import face_recognition

#load face encodings 

known_face_encodings = []
known_face_names = []

# load known faces  and their name here
known_persona1_image = face_recognition.load_image_file("C:/Users/prita/OneDrive/Pictures/Saved Pictures/profile.jpg")
known_person2_image = face_recognition.load_image_file("C:/Users/prita/OneDrive/Pictures/Saved Pictures/OIP (1).jpg")


known_person1_encoding = face_recognition.face_encodings(known_persona1_image)[0]      
known_person2_encoding = face_recognition.face_encodings(known_person2_image)[0]   

known_face_encodings.append(known_person1_encoding)
known_face_encodings.append(known_person2_encoding)

known_face_names.append("Pritam Som")
known_face_names.append("Virat Kohli")

# initialize webcam
video_capture = cv2.VideoCapture(0)
while True:
    # Capture frame by frame
    ret, frame= video_capture.read()

    # Find all face location in the current frame
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame,face_locations)


    # Loop Through each face found in the frame
    for(top,right,bottom,left), face_encoding in zip(face_locations,face_encodings):

        #check if the face matches any known faces
        matches = face_recognition.compare_faces(known_face_encodings,face_encoding)
        name = "unknown"

        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

         # draw a box  around the face and label with the name
        cv2.rectangle(frame, (left,top),(right,bottom), (0,0,255),2)   
        cv2.putText(frame , name, (left,top-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,0,255),2)

    # display the resulting frame
    cv2.imshow("Video",frame)    
    #break the loop when the 'a'  is pressed
    if cv2.waitKey(10) == ord("a"):
        break

    #release the webcam and close opencv windows
video_capture.release()
cv2.destroyAllWindows()    


