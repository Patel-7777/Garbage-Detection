from django.shortcuts import render
from .models import Pictures
import os
from tensorflow import keras
# Create your views here.
def home(request):
    model = keras.models.load_model('vgg16_smote.h5')
    if request.method == "POST" :
        img=request.FILES['img']
        form=Pictures()
        form.imgs=img
        form.save()
        import cv2
        path="images//"+str(img)
        print(path)
        classes=[ 'glass','cardboard', 'metal', 'plastic','paper', 'trash']
        def prepare(filepath):
            image = cv2.imread(filepath)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image = cv2.resize(image, (224, 224))
            return image.reshape(-1,224,224,3)

        prediction=model.predict(prepare(path))
        prediction_index=prediction.argmax()
        print(prediction_index)
        print(float(prediction[0][prediction_index])*100)
        per=str(float("{:.2f}".format(prediction[0][prediction_index]))*100 )+ " %"
        print(classes[prediction_index])
        label=classes[prediction_index].capitalize()
        return render(request,'home.html',{'form':form,"label":label,"acc":per})
    else:
        print(1)
        return render(request,'home.html')
