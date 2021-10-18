from sys import executable
import cv2
import os
import time
import glob
import torch
from PIL import Image
import multiprocessing

listMovies = any
import json

listMovies = any
f = open ('D:\\Marvin Documentos\\Descargas\\Pruebas\\Pruebas\\detections.txt','w')

detections={} #JSON detection with the amount.

def cleanPath(route, movieDirectory):
    return str(movieDirectory).replace(route,'').replace('\\','').replace('.mp4','').replace(' ','').lower()

def getMoviesRoute(route):
    global listMovies
    listMovies = glob.glob(route + os.sep + '*.mp4')

def createDirectories(route):
    global listMovies
    for movieDirectory in listMovies:
        createMovieDirectories(cleanPath(route, movieDirectory))
        
def createMovieDirectories(nameMovie):
    try:
        if not os.path.exists('Images'): 
            os.makedirs('Images')
        if not os.path.exists('Images\\' + nameMovie): 
            os.makedirs('Images\\'+ nameMovie)
        if not os.path.exists('Images\\' + nameMovie + '\\first'): 
            os.makedirs('Images\\' + nameMovie + '\\first')
        if not os.path.exists('Images\\' + nameMovie + '\\second'): 
            os.makedirs('Images\\' + nameMovie + '\\second')    
    except OSError: 
        print ('Error: Creating directory of data')

def getFrames(route, list):
    print(list)
    for routeMovie in list:
        nameFolder = cleanPath(route, routeMovie)
        extractFrames(routeMovie, nameFolder)
        p3 = multiprocessing.Process(target=getResultYOLO, args= (nameFolder, 'first'))
        p4 = multiprocessing.Process(target=getResultYOLO, args= (nameFolder,'second'))
        p3.start()
        p4.start()
        p3.join()
        p4.join()

def extractFrames(path, nameMovie):
    video = cv2.VideoCapture(path)
    sizeFrame = video.get(cv2.CAP_PROP_FRAME_COUNT)
    currentframe = 1
    count = 0
    timeRate = 1 # El intervalo de tiempo para capturar fotogramas de video (aquí hay un fotograma cada 10 segundos)
    while(True): 
        ret,frame = video.read()
        FPS = video.get(5)
        if ret:
            frameRate = int (FPS) * timeRate # Debido a que la cantidad de fotogramas obtenidos por cap.get (5) no es un número entero, debe redondearse hacia arriba (int para redondear hacia abajo, round para redondear hacia arriba, ceil (del módulo matemático para redondear hacia arriba) ) Método)
            if(currentframe % frameRate == 0 and currentframe < int(sizeFrame/2)): 
                name = './Images/'+ nameMovie + '/first/frame' + str(count) + '.jpg'
                #print ('Creating...' + name) 
                cv2.imwrite(name, frame)
                count += 1
            if(currentframe % frameRate == 0 and currentframe > int(sizeFrame/2)):
                name = './Images/'+ nameMovie + '/second/frame' + str(count) + '.jpg'
                #print ('Creating...' + name) 
                cv2.imwrite(name, frame)
                count += 1
            currentframe += 1
            cv2.waitKey(0)
        else: 
            #print("Se han guardado todos los fotogramas")
            break
    video.release() 
    cv2.destroyAllWindows()

def yolo(route):
    model = torch.hub.load('ultralytics/yolov5', 'custom', path=r'.\best.pt') #('ultralytics/yolov5', 'yolov5s')
    img = Image.open(route)
    #model(img, size=640)
    results = model(img, size=640)
    results.save()

    className = results.pandas().xyxy[0].to_json()
    nameJSON = json.loads(className)["name"]

    for value in nameJSON.keys():
        if nameJSON[value] not in detections:
            detections[nameJSON[value]] = 1
        else:
            detections[nameJSON[value]] = detections[nameJSON[value]]+1


def getResultYOLO(nameFolder, folder):
    path = '.\\Images\\' + nameFolder + '\\' + folder
    listImage = glob.glob(path + os.sep + '*.jpg')
    for image in listImage:
        yolo(image)

def main():
    global listMovies
    routeDirectory = './videos' 
    
    getMoviesRoute(routeDirectory)

    createDirectories(routeDirectory)

    size = len(listMovies)
    mitad = int(size/2)

    inicio = time.time()

    p1 = multiprocessing.Process(target=getFrames, args= (routeDirectory,listMovies[0:mitad]))
    p2 = multiprocessing.Process(target=getFrames, args= (routeDirectory,listMovies[mitad:size]))
    p1.start()
    p2.start()
    p1.join()
    p2.join()


    fin = time.time()
    print("Tardo:" + str((fin - inicio)))
    

    fin = time.time()
    print("Tardo:" + str((fin - inicio)))
    
    # Save results
    print("\nDETECTIONS")
    print(detections)
    f.writelines("Hubo un total de " + str(len(listMovies)) + " imagenes. \nEn estas se detectaron los siguientes objetos peligrosos:\n")
    for value in detections.keys():
        f.writelines(str(value + ": " + str(detections[value]))+"\n")

if __name__ == "__main__":
    print(multiprocessing.cpu_count())
    main()