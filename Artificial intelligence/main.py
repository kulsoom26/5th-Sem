import tensorflow as tf
from keras.preprocessing.image import ImageDataGenerator
# from keras.preprocessing import image
# from tensorflow.keras.optimizers import Adam
import cv2
# from tensorflow.keras.utils import img_to_array
import scipy
from keras.models import load_model

import tkinter as tk
from tkinter import filedialog, BOTH

filename = ''

def pdc(filename):
    model = load_model("trained.h5")
    eval_datagen = ImageDataGenerator(rescale = 1/255)

    test_generator = eval_datagen.flow_from_directory(
        'D:/University/Semester 5/chest_xray/test',
        target_size = (300, 300),
        batch_size = 128,
        class_mode = 'binary'
    )
    img= cv2.imread(filename);
    img = cv2.resize(img,(300,300))
    img = img/255.0
    img = img.reshape(1,300,300,3)


    prediction = model.predict(img) >= 0.5
    if prediction>=0.5:
        prediction = "Pneumonia"
    else:
        prediction = "Normal"

    root1 = tk.Tk()
    root1.geometry("250x250")
    root1.configure(bg="white")
    T = tk.Text(root1, height = 5, width = 52)

# Create label
    l = tk.Label(root1, text = prediction)
    l.config(font =("Courier", 14))

    T.pack()
    l.pack()

    root1.mainloop()


def UploadAction(event=None):
    filename = filedialog.askopenfilename()
    pdc(filename)

def main():
    print("Hello")
    root = tk.Tk()
    root.geometry("500x500")
    root.configure(bg="white")

    frame = tk.LabelFrame(
        root,
        text='Pnemonia Diagnostic Center',
        bg='#f0f0f0',
        font=(30)
    )
    frame.pack(expand=True, fill=BOTH)


    button = tk.Button(frame, text='Upload Xray Image', command=UploadAction, fg="white", bg="red")
    button.pack(
        ipadx=5,
        ipady=5,
        expand=True
    )

    root.mainloop()

main()



# train_datagen = ImageDataGenerator(rescale = 1./255,shear_range = 0.2,zoom_range = 0.2,horizontal_flip = True)
# train_images = "D:/University/Semester 5/chest_xray/train"
# train_generator = train_datagen.flow_from_directory(train_images,target_size = (300,300),batch_size = 128,class_mode = 'binary')
# print(train_generator.class_indices)
#
# test_datagen = ImageDataGenerator(rescale = 1./255)
#
# #Validation data generator and loading validation data
# validation_generator = test_datagen.flow_from_directory('D:/University/Semester 5/chest_xray/val',
#                                                         target_size= (300,300),
#                                                         batch_size = 128,
#                                                         class_mode = 'binary')
#
#
# model= tf.keras.models.Sequential([
#     tf.keras.layers.Conv2D(16, (3,3), activation= 'relu', input_shape= (300, 300, 3)),
#     tf.keras.layers.MaxPool2D(2,2),
#     tf.keras.layers.Conv2D(32, (3,3), activation= 'relu'),
#     tf.keras.layers.MaxPool2D(2,2),
#     tf.keras.layers.Conv2D(64, (3,3), activation= 'relu'),
#     tf.keras.layers.MaxPool2D(2,2),
#     tf.keras.layers.Conv2D(128, (3,3), activation= 'relu'),
#     tf.keras.layers.MaxPool2D(2,2),
#     tf.keras.layers.Conv2D(128, (3,3), activation= 'relu'),
#     tf.keras.layers.MaxPool2D(2,2),
#
#     tf.keras.layers.Flatten(),
#     tf.keras.layers.Dense(256, activation= 'relu'),
#     tf.keras.layers.Dense(512, activation= 'relu'),
#     tf.keras.layers.Dense(1, activation= 'sigmoid')
# ])
# model.summary()
# model.compile(optimizer= 'adam', loss= 'binary_crossentropy', metrics= ['accuracy'])
#
# Training_model = model.fit_generator(train_generator,  epochs = 50, validation_data = validation_generator)
#
# model.save("trained.h5")

