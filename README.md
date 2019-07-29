# DL-Dataset-Useful-Script

When you want to make a dataset for deep learning, it may help you

## 1 Cat Face Detection

- Prerequisite: `opencv-python` and [`opencv files`](https://github.com/zhaoyuzhi/opencv/tree/master/data/haarcascades): [haarcascade_frontalcatface.xml](https://github.com/zhaoyuzhi/opencv/blob/master/data/haarcascades/haarcascade_frontalcatface_extended.xml), [haarcascade_frontalcatface.xml](https://github.com/zhaoyuzhi/opencv/blob/master/data/haarcascades/haarcascade_frontalcatface_extended.xml);

- Usage (catface_detection.py): All in one, the image based detection algorithm and folder based detection algorithm;

- Results: It is based on opencv cat detection. There are two choices of the given APIs: bigger and smaller rectangles. The results are not very perfect;

- Images: We plot the raw image and the result image.

![cat1](https://github.com/zhaoyuzhi/DL-Dataset-Useful-Script/blob/master/catface_detection/cat1.jpg)
![cat1result](https://github.com/zhaoyuzhi/DL-Dataset-Useful-Script/blob/master/catface_detection/cat1_result.jpg)

## 2 Face Detection by Dlib

- Prerequisite: `Dlib` and [`Dilb files`](http://dlib.net/files/): shape_predictor_5_face_landmarks.dat, shape_predictor_68_face_landmarks.dat;

- Usage (detection.py): Detect all the faces in a given image;

- Usage (landmark.py): Detect all the faces in a given image and predict the landmarks;

- Usage (alignment.py): Detect all the faces in a given image, then predict the landmarks, finally align all the faces based on the landmarks;

- Usage (alignment_save_by_image.py): Save all the aligned faces in a given image;

- Usage (alignment_save_by_image.py): Save all the aligned faces in a given folder, and name them according to the input file names;

- Results: It is based on dlib detection. The aligned faces will be influenced by border effect. Save to 'results' folder.

- Images: We plot the raw image and the result image.

![dlibsrc](https://github.com/zhaoyuzhi/DL-Dataset-Useful-Script/blob/master/face_detection_dlib/results/src.jpg)
The aligned sub-faces are (there is border effect in the sub-faces):
![dlibsub1](https://github.com/zhaoyuzhi/DL-Dataset-Useful-Script/blob/master/face_detection_dlib/results/det_0.jpg)
![dlibsub2](https://github.com/zhaoyuzhi/DL-Dataset-Useful-Script/blob/master/face_detection_dlib/results/det_1.jpg)
![dlibsub3](https://github.com/zhaoyuzhi/DL-Dataset-Useful-Script/blob/master/face_detection_dlib/results/det_2.jpg)

## 3 Face Detection by face_recognition

- Prerequisite: `face_recognition`;

- Usage (illustration.py): Illustrate the aligned faces in a given image;

- Usage (alignment_save_by_image_size.py): Save all the aligned faces in a given image, in a specified size (default: 128);

- Usage (alignment_save_by_folder_size.py): Save all the aligned faces in a given folder, and name them according to the input file names, in a specified size (default: 128);

- Usage (alignment_save_by_image_nosize.py): Save all the aligned faces in a given image, in an adaptive size, which can be added by 'addsize' parameter;

- Usage (alignment_save_by_folder_nosize.py): Save all the aligned faces in a given folder, and name them according to the input file names, in an adaptive size, which can be added by 'addsize' parameter;

- Usage (alignment_save_by_folder_nosize_general.py): Save all the aligned faces in a given folder, and name them according to the input file names (0, 1, 2, ...), in an adaptive size, which can be added by 'addsize' parameter;

- Usage (alignment_save_by_image_modified.py): Save all the aligned faces in a given folder, and name them according to the input file names (0, 1, 2, ...), in an adaptive size, which can be added by 'addsize' parameter; Besides, there is no border effect but need manual screening.

- Results: It is based on face_recognition lib. The aligned faces will not be influenced by border effect but need manual screening (alignment_save_by_image_modified.py) .Save to 'results' folder.

- Images: We plot the raw image and the result image (for alignment_save_by_image_modified.py). `Suppose there are 4 sub-faces in a given image, there are 4 * 4 = 16 output images, in 4 groups`. `The face order is not fixed for each group`.

The first output group:
![face_recognition0_0](https://github.com/zhaoyuzhi/DL-Dataset-Useful-Script/blob/master/face_detection_face_recognition/results/0_0.jpg)
![face_recognition0_1](https://github.com/zhaoyuzhi/DL-Dataset-Useful-Script/blob/master/face_detection_face_recognition/results/0_1.jpg)
![face_recognition0_2](https://github.com/zhaoyuzhi/DL-Dataset-Useful-Script/blob/master/face_detection_face_recognition/results/0_2.jpg)
![face_recognition0_3](https://github.com/zhaoyuzhi/DL-Dataset-Useful-Script/blob/master/face_detection_face_recognition/results/0_3.jpg)

The second output group:
![face_recognition1_0](https://github.com/zhaoyuzhi/DL-Dataset-Useful-Script/blob/master/face_detection_face_recognition/results/1_0.jpg)
![face_recognition1_1](https://github.com/zhaoyuzhi/DL-Dataset-Useful-Script/blob/master/face_detection_face_recognition/results/1_1.jpg)
![face_recognition1_2](https://github.com/zhaoyuzhi/DL-Dataset-Useful-Script/blob/master/face_detection_face_recognition/results/1_2.jpg)
![face_recognition1_3](https://github.com/zhaoyuzhi/DL-Dataset-Useful-Script/blob/master/face_detection_face_recognition/results/1_3.jpg)


The third output group:
![face_recognition2_0](https://github.com/zhaoyuzhi/DL-Dataset-Useful-Script/blob/master/face_detection_face_recognition/results/2_0.jpg)
![face_recognition2_1](https://github.com/zhaoyuzhi/DL-Dataset-Useful-Script/blob/master/face_detection_face_recognition/results/2_1.jpg)
![face_recognition2_2](https://github.com/zhaoyuzhi/DL-Dataset-Useful-Script/blob/master/face_detection_face_recognition/results/2_2.jpg)
![face_recognition2_3](https://github.com/zhaoyuzhi/DL-Dataset-Useful-Script/blob/master/face_detection_face_recognition/results/2_3.jpg)


The fourth output group:
![face_recognition3_0](https://github.com/zhaoyuzhi/DL-Dataset-Useful-Script/blob/master/face_detection_face_recognition/results/3_0.jpg)
![face_recognition3_1](https://github.com/zhaoyuzhi/DL-Dataset-Useful-Script/blob/master/face_detection_face_recognition/results/3_1.jpg)
![face_recognition3_2](https://github.com/zhaoyuzhi/DL-Dataset-Useful-Script/blob/master/face_detection_face_recognition/results/3_2.jpg)
![face_recognition3_3](https://github.com/zhaoyuzhi/DL-Dataset-Useful-Script/blob/master/face_detection_face_recognition/results/3_3.jpg)

## 4 Edge Detection

We provide 3 kinds of edge detection algorithms by OpenCV lib.

For the result of Lab color space (order: L -> a -> b):

![l](https://github.com/zhaoyuzhi/DL-Dataset-Useful-Script/blob/master/edge_detection/l.jpg)
![a](https://github.com/zhaoyuzhi/DL-Dataset-Useful-Script/blob/master/edge_detection/a.jpg)
![b](https://github.com/zhaoyuzhi/DL-Dataset-Useful-Script/blob/master/edge_detection/b.jpg)
![lresult](https://github.com/zhaoyuzhi/DL-Dataset-Useful-Script/blob/master/edge_detection/lresult.jpg)
![aresult](https://github.com/zhaoyuzhi/DL-Dataset-Useful-Script/blob/master/edge_detection/aresult.jpg)
![bresult](https://github.com/zhaoyuzhi/DL-Dataset-Useful-Script/blob/master/edge_detection/bresult.jpg)
