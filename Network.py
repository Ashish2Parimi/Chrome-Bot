import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten, Dropout, MaxPool2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import load_model
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
import matplotlib.pyplot as plt 


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
mcp_save = ModelCheckpoint('D:\Project\dino_4', save_best_only=True, monitor='val_accuracy', mode='max')
datagen = ImageDataGenerator(validation_split=0.1, rescale=1./255)
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
        batch_size=1,
        subset='validation',
        color_mode = 'grayscale',
        class_mode='categorical')
history = model.fit(train_generator,
        epochs=60,
        validation_data=validation_generator,callbacks=[earlyStopping, mcp_save])
acc = history.history[ 'accuracy' ] 
val_acc  = history.history[ 'val_accuracy' ] 
loss     = history.history[    'loss' ] 
val_loss = history.history['val_loss' ]  
epochs   = range(len(acc))


plt.plot  ( epochs, acc,'y', label='Training acc' )
plt.plot  ( epochs, val_acc,'r', label='validation acc' )
plt.title ('Training and validation accuracy')
plt.legend()
plt.figure() 
 
  # Plot training and validation loss per epoch 
plt.plot  ( epochs,     loss,'y', label='Training loss' ) 
plt.plot  ( epochs, val_loss,'r', label='Validation loss' ) 
plt.title ('Training and validation loss'   )
plt.legend()

plt.figure() 

model.save('D:\Project\dino-t.h5')
