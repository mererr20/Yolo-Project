# <div align="center">Yolo en películas</div>
<p>
   <a align="left" href="https://ultralytics.com/yolov5" target="_blank">
   <img width="850" src="https://user-images.githubusercontent.com/65417448/101770908-2ff3ff00-3b0f-11eb-9c54-9c27f7a9ecd6.png"></a>
</p>
<p>

## <div>Desarrollado por:</div>

Merelyn Rodríguez Rojas

Fernando Méndez Hurtado

Daniel Vargas Gómez
</p>

# <div align="center">Introducción</div>
<p>
YOLO es un sistema de código para la detección de objetos. Para su funcionamiento, la red neuronal divide la imagen en regiones de diferentes tamaños, prediciendo cuadros de identificación y probabilidades por cada región. 

En este proyecto, nos interesa la detección de objetos considerados como peligrosos dentro de una película. Esto para determinar si esta película es, por ejemplo, apta para menores de edad, o contiene material sensible.
</p>
<br><br>


# <div align="center">Modelo usado</div>

<p>
Para llevar a cabo la detección de los objetos, es necesario contar con un modelo entrenado para encontrar los objetos. En este caso, utilizamos y brindamos para su uso, un modelo entrenado con 5000 imágenes de cada una de las siguientes categorías:

    - Personas.
    - Bebidas alcohólicas.
    - Armas.
    - Cuchillos.
</p>
<br><br>
</div>

# <div align="center">Cómo iniciar</div>

<details open>
<summary>Instalación</summary>

Se requiere [**Python>=3.6.0**](https://www.python.org/) y los requerimientos especificados en
[requirements.txt](https://github.com/mererr20/Yolo-Project.git/requirements.txt) instalados, incluyendo
[**PyTorch>=1.7**](https://pytorch.org/get-started/locally/):

```bash
$ git clone https://github.com/mererr20/Yolo-Project.git
$ cd Yolo-Project
$ pip install -r requirements.txt
```

Una vez tenemos todo lo necesario, debemos ejecutar el [main.py](https://github.com/mererr20/Yolo-Project.git/main.py)
</details>

<br><br>

## <div align="center">Environments</div>

Get started in seconds with our verified environments. Click each icon below for details.

<div align="center">
    <a href="https://colab.research.google.com/github/ultralytics/yolov5/blob/master/tutorial.ipynb">
        <img src="https://github.com/ultralytics/yolov5/releases/download/v1.0/logo-colab-small.png" width="15%"/>
    </a>
    <a href="https://www.kaggle.com/ultralytics/yolov5">
        <img src="https://github.com/ultralytics/yolov5/releases/download/v1.0/logo-kaggle-small.png" width="15%"/>
    </a>
    <a href="https://hub.docker.com/r/ultralytics/yolov5">
        <img src="https://github.com/ultralytics/yolov5/releases/download/v1.0/logo-docker-small.png" width="15%"/>
    </a>
    <a href="https://github.com/ultralytics/yolov5/wiki/AWS-Quickstart">
        <img src="https://github.com/ultralytics/yolov5/releases/download/v1.0/logo-aws-small.png" width="15%"/>
    </a>
    <a href="https://github.com/ultralytics/yolov5/wiki/GCP-Quickstart">
        <img src="https://github.com/ultralytics/yolov5/releases/download/v1.0/logo-gcp-small.png" width="15%"/>
    </a>
</div>  

## <div align="center">Integrations</div>

<div align="center">
    <a href="https://wandb.ai/site?utm_campaign=repo_yolo_readme">
        <img src="https://github.com/ultralytics/yolov5/releases/download/v1.0/logo-wb-long.png" width="49%"/>
    </a>
    <a href="https://roboflow.com/?ref=ultralytics">
        <img src="https://github.com/ultralytics/yolov5/releases/download/v1.0/logo-roboflow-long.png" width="49%"/>
    </a>
</div>

|Weights and Biases|Roboflow ⭐ NEW|
|:-:|:-:|
|Automatically track and visualize all your YOLOv5 training runs in the cloud with [Weights & Biases](https://wandb.ai/site?utm_campaign=repo_yolo_readme)|Label and automatically export your custom datasets directly to YOLOv5 for training with [Roboflow](https://roboflow.com/?ref=ultralytics) |

