import cv2
import os
import json
import time
import glob
import torch
from PIL import Image
import multiprocessing
from matplotlib import pyplot

listMovies = any

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
        if not os.path.exists('FinalResults'): 
            os.makedirs('FinalResults')
        if not os.path.exists('Images\\' + nameMovie): 
            os.makedirs('Images\\'+ nameMovie)
        if not os.path.exists('Images\\' + nameMovie + '\\firstPortion'): 
            os.makedirs('Images\\' + nameMovie + '\\firstPortion')
        if not os.path.exists('Images\\' + nameMovie + '\\secondPortion'): 
            os.makedirs('Images\\' + nameMovie + '\\secondPortion')
        if not os.path.exists('Images\\' + nameMovie + '\\results'): 
            os.makedirs('Images\\' + nameMovie + '\\results')
        open('Images\\' + nameMovie + '\\results\\Person.txt',"w") 
        open('Images\\' + nameMovie + '\\results\\Drink.txt',"w") 
        open('Images\\' + nameMovie + '\\results\\Knife.txt',"w") 
        open('Images\\' + nameMovie + '\\results\\Weapon.txt',"w")
        open('Images\\' + nameMovie + '\\results\\Final.txt',"w")
    except OSError: 
        print ('Error: Creating directory of data')

def getFrames(route, list):
    print(list)
    for routeMovie in list:
        nameFolder = cleanPath(route, routeMovie)
        extractFrames(routeMovie, nameFolder)
  
def extractFrames(path, nameMovie):
    video = cv2.VideoCapture(path)
    sizeFrame = video.get(cv2.CAP_PROP_FRAME_COUNT)
    currentframe = 1
    count = 0
    timeRate = 1 # The time interval to capture video frames (here is a frame every 1 second)
    while(True): 
        ret,frame = video.read()
        FPS = video.get(5)
        if ret:
            frameRate = int (FPS) * timeRate
            if(currentframe % frameRate == 0 and currentframe < int(sizeFrame/2)): 
                name = './Images/'+ nameMovie + '/firstPortion/frame' + str(count) + '.jpg'
                cv2.imwrite(name, frame)
                count += 1
            if(currentframe % frameRate == 0 and currentframe >= int(sizeFrame/2)):
                name = './Images/'+ nameMovie + '/secondPortion/frame' + str(count) + '.jpg'
                cv2.imwrite(name, frame)
                count += 1
            currentframe += 1
            cv2.waitKey(0)
        else: 
            break
    video.release() 
    cv2.destroyAllWindows()

def getResultYOLO(route, list, folder):
    for movieDirectory in list:
        nameFolder = cleanPath(route, movieDirectory)
        root = '.\\Images\\' + nameFolder + '\\'
        path =  root + folder
        listImage = glob.glob(path + os.sep + '*.jpg')
        inicio = time.time()
        for image in listImage:
            yolo(root, image)
        fin = time.time()
        writeTxt(root, 'Final', str(fin - inicio))
        
def writeTxt(path, className, data):
    route = path + 'results\\' + className + '.txt'
    with open(route, 'a', 1) as file:
        file.write(data + '\n')

def yolo(path, image):
    model = torch.hub.load('ultralytics/yolov5', 'custom', path=r'.\best.pt')
    model.conf = 0.25
    img = Image.open(image)
    results = model(img, size=640)
    className = results.pandas().xyxy[0].to_json()
    nameJSON = json.loads(className)["name"]
    for value in nameJSON.keys():
        writeTxt(path, nameJSON[value], '1')

def readTxt(path, className):
    route = path + 'results\\' + className + '.txt'
    count = 0
    with open(route, 'r', 1) as file:
        for line in file:
            try:
                if line != '\n':
                    count += int(line)
            except:
                count += float(line)
    with open(route, 'w', 1) as file:
        file.write(str(count))

def countResults(route):
    global listMovies
    for movieDirectory in listMovies:
        nameFolder = cleanPath(route, movieDirectory)
        root = '.\\Images\\' + nameFolder + '\\'
        readTxt(root, 'Drink')
        readTxt(root, 'Final')
        readTxt(root, 'Knife')
        readTxt(root, 'Person')
        readTxt(root, 'Weapon')

def getLine(root):
    with open(root, 'r', 1) as file:
        for line in file:
            return line

def generateGraph(route):
    global listMovies
    classes = ('Person', 'Drink', 'Weapon', 'Knife')

    for movieDirectory in listMovies:
        nameFolder = cleanPath(route, movieDirectory)
        root = '.\\Images\\' + nameFolder + '\\results\\'
        list = []
        list.append(int(getLine((root + 'Person.txt'))))
        list.append(int(getLine((root + 'Drink.txt'))))
        list.append(int(getLine((root + 'Weapon.txt'))))
        list.append(int(getLine((root + 'Knife.txt'))))

        slices = tuple(list)
        colores = ('red','blue','green','#DD98AA','#18492D')
        pyplot.rcParams['toolbar']  = 'None'
        _,_,texto = pyplot.pie(slices, colors=colores, labels=classes, autopct='%1.1f%%')
        for tex in texto:
            tex.set_color('white')
        time = float(getLine((root + 'Final.txt')))

        pyplot.annotate(('Time: ' + str(time) + ' seg.'), xy=(10, 20), xycoords='figure pixels')
        pyplot.axis('equal')
        pyplot.title('Film: ' + nameFolder)
        #pyplot.show()
        pyplot.savefig('.\\FinalResults\\' + nameFolder + '.jpg')
        pyplot.close()

        print('In film ' + nameFolder + ', the following classes have been detected: ' +
                '\n\tPerson: ' + str(list[0]) +
                '\n\tDrink: ' + str(list[1]) +
                '\n\tWeapon: ' + str(list[2]) +
                '\n\tKnife: ' + str(list[3]) +
                '\nThis detection was carried out in ' + str(time) + ' seg.')

def firstProcesses(routeDirectory,mitad,size):
    #Processes to get the frames of the videos
    if (size > 1):
        p1 = multiprocessing.Process(target=getFrames, args= (routeDirectory,listMovies[0:mitad]))
        p2 = multiprocessing.Process(target=getFrames, args= (routeDirectory,listMovies[mitad:size]))
        p1.start()
        p2.start()
        p1.join()
        p2.join()
    else:
        p1 = multiprocessing.Process(target=getFrames, args= (routeDirectory,listMovies))
        p1.start()
        p1.join()

def secondProcesses(routeDirectory,mitad,size):
    #Process to send the images to YOLO
    if (size > 1):
        p3 = multiprocessing.Process(target=getResultYOLO, args= (routeDirectory, listMovies[0:mitad], 'firstPortion'))
        p4 = multiprocessing.Process(target=getResultYOLO, args= (routeDirectory, listMovies[mitad:size],'secondPortion'))
        p5 = multiprocessing.Process(target=getResultYOLO, args= (routeDirectory, listMovies[0:mitad], 'firstPortion'))
        p6 = multiprocessing.Process(target=getResultYOLO, args= (routeDirectory, listMovies[mitad:size],'secondPortion'))
        p3.start()
        p4.start()
        p5.start()
        p6.start()
        p3.join()
        p4.join()
        p5.join()
        p6.join()
    else:
        p3 = multiprocessing.Process(target=getResultYOLO, args= (routeDirectory, listMovies, 'firstPortion'))
        p4 = multiprocessing.Process(target=getResultYOLO, args= (routeDirectory, listMovies,'secondPortion'))
        p3.start()
        p4.start()
        p3.join()
        p4.join()

def main(routeDirectory):
    global listMovies
    getMoviesRoute(routeDirectory)
    createDirectories(routeDirectory)
    size = len(listMovies)
    mitad = int(size/2)

    firstProcesses(routeDirectory,mitad,size)
    secondProcesses(routeDirectory,mitad,size)

    countResults(routeDirectory)
    generateGraph(routeDirectory)

if __name__ == "__main__":
    cpuCount = multiprocessing.cpu_count()
    if (cpuCount >= 4):
        print('Welcome to the movie analyzer!')
        main('D:\Peliculas') #Address of the folder to analyze
    else:
        print("I'm really sorry, but your system doesn't meet the requirements...\n" +
        "You need at least 4 processors, and you have " + cpuCount)
