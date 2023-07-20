import cv2

# Create a simple window and display an image for testing
image = cv2.imread(r'C:\Users\Administrator\Desktop\Face-Recognition-Attendance-System-main (1)\Face-Recognition-Attendance-System-main (1)\Face-Recognition-Attendance-System-main\TrainingImage\arin.201666.1.jpg')
cv2.imshow('Test Window', image)

# Wait for a key press and close the window on key 'q' press
while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Close all OpenCV windows and release resources
cv2.destroyAllWindows()
