import torch
import cv2
from flask import Flask, request
import time
import numpy
import detect

app = Flask(__name__)

class_name = ['RicolaLemonMint', 'PringlesButterCaramel110G', 'AceCracker121G', 'ChocoHeim142G', 'CouqueDasseCake154G',
        'CushCush2P65G', 'mentosmixgrape37G', 'HoneyButterChips38G', 'ChamCracker56G', 'PocachipOriginal66G',
        'ShrimpChips68G', 'KkokkalcornSavorytaste72G', 'CaramelCornMaple74G', 'BananaKick75G', 'Gosomi80G',
        'CuttlefishSnack83G', 'MargaretOriginal88G', 'ShrimpCrackersSpicyFlavor90G', 'RITZCheeseSandwichCracker96G',
        'ABCChocoCookie152G', 'KinderChocolateT4_50G', 'PetitzelWaterjellyOrange130ML']

print(len(class_name))

@app.route("/product" , methods=['post'])
def getImage():
    if 'image' not in request.files:
        print("Not Image")
        return "Fail - Not Image"
    image_file = request.files['image']
    image = cv2.imdecode(numpy.frombuffer(image_file.read(), numpy.uint8), cv2.IMREAD_COLOR)
    cv2.imwrite("./images/output.jpeg" , image)
    
    result = detect.run(weights="../yolov5_weights/240208_weight.pt", source="./images/output.jpeg")
    
    print(result)

    return "Success"


@app.route("/clothes" , methods=['post'])
def getClothesImage():
    if 'image' not in request.files:
        print("Not Image")
        return "Fail - Not Image"
    image_file = request.files['image']
    image = cv2.imdecode(numpy.frombuffer(image_file.read(), numpy.uint8) , cv2.IMREAD_COLOR)
    cv2.imwrite("./images/output_clothes.jpeg" , image)

    return "Success"


if(__name__) == '__main__':
    app.run(host='0.0.0.0')
