# Importing libraries
import cv2
from pyzbar.pyzbar import decode

# Make one method to decode the barcode 
def BarcodeReader(img):
    # Decode the barcode image
    detectedBarcodes = decode(img)

    # If not detected then print the message
    if not detectedBarcodes:
        #print("Barcode Not Detected or your barcode is blank/corrupted!")
        pass
    else:
        # Traverse through all the detected barcodes in the image
        for barcode in detectedBarcodes:
            # Locate the barcode position in the image
            (x, y, w, h) = barcode.rect
            # Put a rectangle in the image to highlight the barcode
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Changed color to green (0, 255, 0)
            if barcode.data != "":
                # Print the barcode data
                print(barcode.data)
                print(barcode.type)

    return img

# Function to capture images from the webcam
def web_cam():
    cap = cv2.VideoCapture(0)
    while True:
        success, img = cap.read()
        img = BarcodeReader(img)
        cv2.imshow('Barcode Scanner', img)
        if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' key to exit
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    web_cam()
