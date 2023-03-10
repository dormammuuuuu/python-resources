import cv2 as cv
import time
import mediapipe as mp
import os
import tensorflow as tf


mpFaceDetection = mp.solutions.face_detection
mpDraw = mp.solutions.drawing_utils
faceDetection = mpFaceDetection.FaceDetection(0.75)

# Load the model
model = tf.keras.models.load_model('model.h5')
labels = {0: 'up', 1: 'down', 2: 'left', 3: 'right', 4: 'front'}



class FaceDetector():
    def __init__(self, minDetectionCon=0.5):

        self.midDetectionCon = minDetectionCon

        self.mpFaceDetection = mp.solutions.face_detection
        self.mpDraw = mp.solutions.drawing_utils
        self.mpFaceDetection = self.mpFaceDetection.FaceDetection(
            minDetectionCon)

    def findFaces(self, img, draw=True):
        imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        self.results = faceDetection.process(imgRGB)
        print(self.results)

        bboxs = []
        if self.results.detections:
            for id, detection in enumerate(self.results.detections):
                # print(id, detection)
                # print(detection.score)
                # print(detection.location_data.relative_bounding_box)

                bboxC = detection.location_data.relative_bounding_box
                ih, iw, ic = img.shape
                bbox = int(bboxC.xmin * iw - 65), int(bboxC.ymin * ih - 100), \
                    int(bboxC.width * iw + 130), int(bboxC.height * ih + 130)
                print(bbox)
                bboxs.append([id, bbox, detection.score])
                img = self.fancyDraw(img, bbox)

                cv.putText(img, f'',
                           (bbox[0], bbox[1] - 20), cv.FONT_HERSHEY_PLAIN, 1, (255, 0, 255), 1)

        return img, bboxs

    def fancyDraw(self, img, bbox, l=15, t=3):
        x, y, w, h = bbox
        x1, y1 = x + w, y + h
        # print("bbox: ",bbox)
        # print(f"x: {x}, y: {y}, w: {w}, h: {h}")

        cv.rectangle(img, bbox, (255, 0, 255), 2)
        

        # Top Left x,y
        cv.line(img, (x, y), (x + l, y), (255, 0, 255), t)
        cv.line(img, (x, y), (x, y+l), (255, 0, 255), t)

        # Top Right x1,y
        cv.line(img, (x1, y), (x1 - l, y), (255, 0, 255), t)
        cv.line(img, (x1, y), (x1, y+l), (255, 0, 255), t)

        # Bottom Left x,y1
        cv.line(img, (x, y1), (x + l, y1), (255, 0, 255), t)
        cv.line(img, (x, y1), (x, y1-l), (255, 0, 255), t)

        # Bottom Right x1,y1
        cv.line(img, (x1, y1), (x1 - l, y1), (255, 0, 255), t)
        cv.line(img, (x1, y1), (x1, y1-l), (255, 0, 255), t)

        face = cv.getRectSubPix(img, (w, h), (x + w//2, y + h//2))
        face = cv.resize(face, (227, 227))
        # Make prediction
        prediction = model.predict(face[None, ...])
        class_index = tf.keras.backend.eval(tf.argmax(prediction, axis=-1))
        class_label = labels[class_index[0]]

        print(class_label)

        return face

    def saveFaces(self, user, img, bboxs, img_id, width=227, height=227):
        for bbox in bboxs:
            x, y, w, h = bbox[1]
            imgCrop = img[y:y+h, x:x+w]
            imgCrop = cv.resize(imgCrop, (width, height))
            dirname = f'dataset/{user}/'
            if not os.path.exists(dirname):
                os.makedirs(dirname)
            cv.imwrite(f'{dirname}{user}_{img_id}.jpeg', imgCrop)

        print('Faces saved')
        return img_id + 1


def main():
    cap = cv.VideoCapture(0)
    pTime = 0
    detector = FaceDetector()
    img_id = 0


    while True:
        success, img = cap.read()
        img, bboxs = detector.findFaces(img)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        # cv.putText(img, f'FPS: {int(fps)}', (20, 70),
        #            cv.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 3)

        # save image
        # img_id = detector.saveFaces("Test", img, bboxs, img_id)
        print(img.shape)
        # prediction = model.predict(img)
        # cv.putText(img, f'Prediction: {prediction}', (20, 70),
        #            cv.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 3)
        cv.imshow("Video", img)


        if cv.waitKey(1) == 13 or int(img_id) == 400:
            break

    cap.release()
    cv.destroyAllWindows()
    print("Collecting Samples Complete")


if __name__ == '__main__':
    main()