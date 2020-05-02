import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten, Dropout, MaxPool2D,TimeDistributed
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import load_model
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint


input_shape = (160, 320, 1)

model = Sequential([
        Conv2D(16, 3, padding='same', activation='relu', input_shape=input_shape),
        MaxPool2D(pool_size=(1,2)),
        Conv2D(32, 3, padding='same', activation='relu'),
        MaxPool2D(pool_size=(1,2)),
        Conv2D(128, 3, padding='same', activation='relu'),
        MaxPool2D(pool_size=(1,2)),
        Flatten(),
        Dense(256, activation='relu'),
        Dropout(0.1),
        Dense(3,activation='softmax')
        ])   

model.compile(optimizer='adam',loss='categorical_crossentropy', metrics=['accuracy'])

earlyStopping = EarlyStopping(monitor='val_accuracy', patience=10, verbose=0, mode='max')
mcp_save = ModelCheckpoint('.dino_326', save_best_only=True, monitor='val_accuracy', mode='max')
datagen = ImageDataGenerator( validation_split=0.1, rescale=1./255)
train_generator = datagen.flow_from_directory(
        'D:/Project/images',
        target_size=(160, 320),
        batch_size=1,
        subset='training',
        color_mode = 'grayscale',
        class_mode='categorical')
validation_generator = datagen.flow_from_directory(
        'D:/Project/images',
        target_size=(160, 320),
        batch_size=32,
        subset='validation',
        color_mode = 'grayscale',
        class_mode='categorical')
model.fit(train_generator,
        epochs=60,
        validation_data=validation_generator,callbacks=[earlyStopping, mcp_save])
model.save('.dino_326.h5')
