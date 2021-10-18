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
[requirements.txt](https://github.com/mererr20/Yolo-Project/requirements.txt) instalados, incluyendo
[**PyTorch>=1.7**](https://pytorch.org/get-started/locally/):

```bash
$ git clone https://github.com/mererr20/Yolo-Project.git
$ cd Yolo-Project
$ pip install -r requirements.txt
```

Una vez tenemos todo lo necesario, debemos ejecutar el [main.py](https://github.com/mererr20/Yolo-Project/main.py)

</details>

<br><br>
# <div align="center">Explicación/Ejecución</div>

A continuación, explicamos cómo se implementó la solución realizada y su ejecución.

Para empezar, la función "main()" es la función principal y donde se crean el primer par de hilos. Aquí también es donde se indica la carpeta donde están los video o películas (específicamente en *routeDirectory*). Aquí se llama a las funciones que obtienen todos los videos que hay en la carpeta especificada y crear los directorios donde se guardarán las imágenes.

*getFrames* es la que se encarga de obtener las imágenes de los videos. Específicamente se extrae un frame (image) por segundo. En esta función es donde se hacen también los otros pares de hilos ya que se divide el video en 2 carpetas de imágenes.

Finalmente, se llama a Yolo que se encarga de detectar los objetos según lo entendido por el modelo anteriormente explicado. Aquí también se guarda la data que va obteniendo en json y por último en un .txt 

