import cv2 as cv
import numpy as np

# OpenCV DNN
net = cv.dnn.readNet(r"dnn_model//yolov4-tiny.weights", r"dnn_model//yolov4-tiny.cfg")
model = cv.dnn_DetectionModel(net)
model.setInputParams(size=(320, 320), scale=1 / 255)

# load Camera

classes = []
with open(r"dnn_model/classes.txt") as file_object:
    for class_name in file_object.readlines():
        class_name = class_name.strip()
        classes.append(class_name)

print(classes)

# Inizialize Camera
cap = cv.VideoCapture("rtsp://admin:Drixter22.@192.168.1.64") # ip camera id address

# improve resolution
# cap.set(cv.CAP_PROP_FRAME_WIDTH, 640)
# cap.set(cv.CAP_PROP_FRAME_HEIGHT, 480)


# Full HD (1920 x 1080)

button_person = False


# Click Function
# def click_button(event, x, y, flags, params):
#     global button_person
#
#     if event == cv.EVENT_LBUTTONDOWN:
#         print(x, y)
#         polygon = np.array([[(20, 20), (220, 20), (220, 70), (20, 70)]])
#
#         is_inside = cv.pointPolygonTest(polygon, (x, y), False)
#
#         if is_inside > 0:
#             print("inside in the polygon", x, y)
#             if button_person is False:
#                 button_person = True
#             else:
#                 button_person = False
#
#             print("now button person : ", button_person)


# Create Window
cv.namedWindow("Frame")
# cv.setMouseCallback("Frame", click_button)

while True:
    # Get frames
    ret, frame = cap.read()

    if ret == True:
        b = cv.resize(frame, (640, 480))
    else:
        break

    # # Object Detection
    # (class_ids, scores, bboxes) = model.detect(frame)
    #
    # # Bounding box
    # for class_id, score, bbox in zip(class_ids, scores, bboxes):
    #     x, y, w, h = bbox
    #
    #     class_name = classes[class_id]
    #
    #     if class_name == "person" and button_person is True:
    #         cv.putText(frame, str(class_name), (x, y - 5), cv.FONT_HERSHEY_PLAIN, 2, (200, 0, 50), 2)
    #         cv.rectangle(frame, (x, y), (x + w, y + h), (200, 0, 50), 3)
    #
    # # Create button
    #
    # # cv.rectangle(frame, (20,20),(220,70), (0,0,200), -1 )
    # polygon = np.array([[(20, 20), (220, 20), (220, 70), (20, 70)]])
    # cv.fillPoly(frame, polygon, (0, 0, 200))
    #
    # cv.putText(frame, "Person", (30, 60), cv.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 3)

    # print(f"class ids: {class_ids} score: {scores} bboxes:{bboxes}" )
    cv.imshow("Frame", frame)

    cv.waitKey(1)

    if cv.getWindowProperty("Frame", cv.WND_PROP_VISIBLE) < 1:
        break

cap.release()
cv.destroyAllWindows()
