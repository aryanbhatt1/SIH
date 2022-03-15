import json

from django.shortcuts import render, redirect
from .models import *
from .forms import *
import cv2
import numpy as np
import tensorflow as tf
from .models import Form, info_team
gpus= tf.config.experimental.list_physical_devices('GPU')
tf.config.experimental.set_memory_growth(gpus[0], True)
from mtcnn.mtcnn import MTCNN
from tensorflow.python.saved_model import tag_constants

from django.http import HttpResponse
class Coordinates:
    def __init__(self):
        self.photoCOOR = []
        self.signCOOR = []


Coor = Coordinates()

detector = MTCNN()
from django.views import View

def crop_img(img,coor = [],):
    #coor = [x1,y1,x2,y2]
    image = img
    return image

def compress_img(img):
    image = img
    return image


def check_photo(img):
    res = detector.detect_faces(img)
    print(len(res))
    if(len(res) == 1):
        Coor.photoCOOR = []
        return True
    return False

@tf.autograph.experimental.do_not_convert
def check_sign(img):
    saved_model_loaded = tf.saved_model.load("./checkpoints/yolov4-tiny-416", tags=[tag_constants.SERVING])
    original_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    image_data = cv2.resize(original_image, (416, 416))
    image_data = image_data / 255.
    images_data = []
    for i in range(1):
        images_data.append(image_data)

    images_data = np.asarray(images_data).astype(np.float32)
    infer = saved_model_loaded.signatures['serving_default']
    batch_data = tf.constant(images_data)
    pred_bbox = infer(batch_data)
    for key, value in pred_bbox.items():
        boxes = value[:, :, 0:4]
        pred_conf = value[:, :, 4:]

    boxes, scores, classes, valid_detections = tf.image.combined_non_max_suppression(
        boxes=tf.reshape(boxes, (tf.shape(boxes)[0], -1, 1, 4)),
        scores=tf.reshape(
            pred_conf, (tf.shape(pred_conf)[0], -1, tf.shape(pred_conf)[-1])),
        max_output_size_per_class=50,
        max_total_size=50,
        iou_threshold=0.40,
        score_threshold=0.5
    )
    pred_bbox = [boxes.numpy(), scores.numpy(), classes.numpy(), valid_detections.numpy()]

    _, __, ___, num = pred_bbox
    if(num[0] >= 1 and num[0] < 4):

        return True
    else:
        return False

def apply(request):
    context = {}
    # form = AdmissionForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        #form.photo = request.FILES['photo']
        #form.signature = request.FILES['signature']
        Pimg = cv2.imdecode(np.fromstring(request.FILES['photo'].read(),np.uint8),cv2.IMREAD_UNCHANGED)
        Simg = cv2.imdecode(np.fromstring(request.FILES['sign'].read(),np.uint8),cv2.IMREAD_UNCHANGED)

        name = str(request.POST.get('first_name')) + str(request.POST.get('last_name'," "))
        email = request.POST.get('email'," ")
        phone1 = request.POST.get('phone_number',0000000000)
        phone2 = request.POST.get('a_phone_number',0000000000)
        address = str(request.POST.get('add1',"")) + str(request.POST.get('add2',"")) + str(request.POST.get('city',"")) + str(request.POST.get('state',"")) + str(request.POST.get('pincode',""))
        father_name = str(request.POST.get('ffname','')) + str(request.POST.get('flname',''))
        mother_name = str(request.POST.get('mfname','')) + str(request.POST.get('mlname',''))

        college = request.POST.get('college')
        registerNo = request.POST.get('regno')
        course = request.POST.get('course')
        department = request.POST.get('department')
        year = request.POST.get('year')


        if(check_photo(Pimg) and check_sign(Simg)):
            print("Passed ALLED")
            signature = request.FILES['sign']
            photo = request.FILES['photo']
            #form = Form(photo = photo, signature = signature)
            form = Form(name = name,
                      email = email,
                      phone1 = phone1,
                      phone2 = phone2,
                      address = address,
                      father_name = father_name,
                      mother_name = mother_name,
                      college = college,
                      registerNo = registerNo,
                      course = course,
                      department = department,
                      year = year,
                      photo = photo,
                      signature = signature
                      )
            form.save()

        elif (check_photo(Simg) and check_sign(Pimg)):
            print("Passed EXCHANGED")
            # request.FILES['photo'],request.FILES['signature'] = request.FILES['signature'],request.FILES['photo']

            #form = Form(photo = signature, signature = photo)
            signature = request.FILES['photo']
            photo= request.FILES['sign']
            form = Form(name=name,
                      email=email,
                      phone1=phone1,
                      phone2=phone2,
                      address=address,
                      father_name=father_name,
                      mother_name=mother_name,
                      college=college,
                      registerNo=registerNo,
                      course=course,
                      department=department,
                      year=year,
                      photo=photo,
                      signature=signature
                      )
            form.save()
        else:
            return render(request,'error.html',context = context)
    # context['form'] = form
    return render(request, 'pages/apply.html')#, context=context)

def home(request):
    info_teams = info_team.objects.all()
    context = {
        'info_teams':info_teams,
    }
    return render(request,'pages/home.html', context=context)

def application(request):
    table = Form.objects.all()
    context = {
        'table': table,
    }
    return render(request,'pages/application.html',context=context)

#UI
#DISPLA
#CRPPING
#CHECKING