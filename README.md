# <div align="center">Yolo en películas</div>
<p>
   <a align="left" href="https://ultralytics.com/yolov5" target="_blank">
   <img width="850" src="https://user-images.githubusercontent.com/65417448/101770908-2ff3ff00-3b0f-11eb-9c54-9c27f7a9ecd6.png"></a>
</p>
<p>

## <div>Desarrollado por:</div>

<ul>
   <li type="circle"> <a href=https://github.com/mererr20> Merelyn Rodríguez Rojas </a> </li>
   <li type="circle"> <a href=https://github.com/mendez-jfer> Fernando Méndez Hurtado </a> </li>
   <li type="circle"> <a href=https://github.com/LDVargas> Daniel Vargas Gómez </a> </li>
</ul>

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

    - Personas (Person).
    - Bebidas alcohólicas (Drink).
    - Armas (Weapon).
    - Cuchillos (knife).
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
   
En el [main.py](https://github.com/mererr20/Yolo-Project/main.py) se debe enviar por parámetros en el método main cuál será la carpeta a analizar (tomando en cuenta que se debe enviar la ruta de dicha carpeta, por ejemplo 'C:\User\...'), por defectos se indica la carpeta [videos](https://github.com/mererr20/Yolo-Project/videos) que se encuentra en la raíz de dicho proyecto.

</details>

<br><br>
# <div align="center">Explicación/Ejecución</div>

A continuación, explicamos cómo se implementó la solución realizada y su ejecución.

Para empezar, la función "main(routeDirectory)" es la función principal, la cual será la encargada de llamar las demás funciones para una ejecución correcta, y además, la encargada de recibir por parámetro la ruta de la carpeta a analizar, como se mencionó anteriormente.

Primeramente se hace la llamada de la función *getMoviesRoute*, esta nos permite extraer los nombres de las películas que se encuentren en la carpeta indicada. Luego de esto, se crean los directorios, donde se almaceneraon los resultados y frames obtenidos.

Teniendo ya las rutas y los directorios necesarios (FinalResults e Images) para control, se llama la función encarga de crear los 2 primeros procesos, encargos de obtener los frames de las películas con la función *getFrames*. De cada película se extrae un frame (image) por segundo.

Creando los directorios y obteniendo los frames, ya se puede proceder a hacer el análisis de los frames, para esto se llama la función encargada de crear 4 procesos, los cuales estarán encargados de ingresar a las carpetas donde se encuentran los frames.

Finalmente, se llama la función *yolo*, YOLO se encarga de detectar los objetos según lo entendido por el modelo anteriormente explicado. Aquí también se guarda la data que va obteniendo en txt y por último se generan unas gráficas en la carpeta *FinalResults* donde se muestran los resultados, además de una impresión en consola que muestra lo mismo.

=======
# <div align="center">Yolo en películas</div>
<p>
   <a align="left" href="https://ultralytics.com/yolov5" target="_blank">
   <img width="850" src="https://user-images.githubusercontent.com/65417448/101770908-2ff3ff00-3b0f-11eb-9c54-9c27f7a9ecd6.png"></a>
</p>
<p>

## <div>Desarrollado por:</div>

<ul>
   <li type="circle"> <a href=https://github.com/mererr20> Merelyn Rodríguez Rojas </a> </li>
   <li type="circle"> <a href=https://github.com/mendez-jfer> Fernando Méndez Hurtado </a> </li>
   <li type="circle"> <a href=https://github.com/LDVargas> Daniel Vargas Gómez </a> </li>
</ul>

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

    - Personas (Person).
    - Bebidas alcohólicas (Drink).
    - Armas (Weapon).
    - Cuchillos (knife).
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
   
En el [main.py](https://github.com/mererr20/Yolo-Project/main.py) se debe enviar por parámetros en el método main cuál será la carpeta a analizar (tomando en cuenta que se debe enviar la ruta de dicha carpeta, por ejemplo 'C:\User\...'), por defectos se indica la carpeta [videos](https://github.com/mererr20/Yolo-Project/videos) que se encuentra en la raíz de dicho proyecto.

</details>

<br><br>
# <div align="center">Explicación/Ejecución</div>

A continuación, explicamos cómo se implementó la solución realizada y su ejecución.

Para empezar, la función "main(routeDirectory)" es la función principal, la cual será la encargada de llamar las demás funciones para una ejecución correcta, y además, la encargada de recibir por parámetro la ruta de la carpeta a analizar, como se mencionó anteriormente.

Primeramente se hace la llamada de la función *getMoviesRoute*, esta nos permite extraer los nombres de las películas que se encuentren en la carpeta indicada. Luego de esto, se crean los directorios, donde se almaceneraon los resultados y frames obtenidos.

Teniendo ya las rutas y los directorios necesarios (FinalResults e Images) para control, se llama la función encarga de crear los 2 primeros procesos, encargos de obtener los frames de las películas con la función *getFrames*. De cada película se extrae un frame (image) por segundo.

Creando los directorios y obteniendo los frames, ya se puede proceder a hacer el análisis de los frames, para esto se llama la función encargada de crear 4 procesos, los cuales estarán encargados de ingresar a las carpetas donde se encuentran los frames.

Finalmente, se llama la función *yolo*, YOLO se encarga de detectar los objetos según lo entendido por el modelo anteriormente explicado. Aquí también se guarda la data que va obteniendo en txt y por último se generan unas gráficas en la carpeta *FinalResults* donde se muestran los resultados, además de una impresión en consola que muestra lo mismo.

<br><br>
# <div align="center">Resultados</div>
Para los resultados, se tomó una película llamada "Hombre lobo" con una duración de 1h, de la cuál se obtuvo lo siguiente:

<p>
   <img width="550" src="https://github.com/mererr20/Yolo-Project/blob/main/ResultadosReadme/hombrelobo.jpg"></a>
</p>

A nivel de consola se muestra así:

<p>
   <img width="550" src="https://github.com/mererr20/Yolo-Project/blob/main/ResultadosReadme/hombrelobo.png"></a>
</p>

