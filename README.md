# Curso: Matemática Discreta 1 - MM2015 - Proyecto 2

## Descripción
Este proyecto tiene como objetivo desarrollar un programa interactivo en Python que implemente el sistema de encriptación RSA desde cero. El programa permite a los usuarios generar llaves RSA (clave pública y privada), encriptar mensajes utilizando la clave pública y desencriptar mensajes mediante la clave privada. Este enfoque ofrece una experiencia educativa práctica, en la que los usuarios pueden explorar y entender los principios fundamentales de la criptografía asimétrica, como el uso de números primos, la exponenciación modular y el cálculo del inverso modular.

El programa está diseñado con una interfaz interactiva que incluye animaciones y mensajes en consola, mejorando la experiencia del usuario y facilitando la comprensión de los pasos involucrados en el proceso de cifrado y descifrado. La implementación se realizó de manera modular, incorporando validaciones y programación defensiva para gestionar entradas incorrectas y garantizar la robustez del sistema.

Para reforzar los objetivos educativos, se han implementado manualmente los algoritmos necesarios, evitando el uso de funciones predefinidas para que los usuarios y desarrolladores puedan profundizar en la lógica subyacente. Estas implementaciones incluyen la generación de números primos, el algoritmo de Euclides para calcular el máximo común divisor (MCD) y su versión extendida para determinar el inverso modular. El programa también cuenta con un generador pseudoaleatorio que simula la selección de valores iniciales, contribuyendo a una comprensión más amplia del funcionamiento interno de RSA.

Este proyecto busca ser una herramienta útil tanto en entornos educativos formales como en situaciones de autoaprendizaje, permitiendo a los usuarios experimentar y obtener resultados inmediatos que refuercen su comprensión teórica. Su diseño y desarrollo están orientados no solo a mostrar el poder de la criptografía RSA, sino también a ofrecer un recurso práctico y accesible para aprender los conceptos matemáticos y computacionales que la sustentan.

## Autores
- Nombre del integrante del grupo 5: PABLO DANIEL BARILLAS MORENO - Carné No. 22193
- Nombre del integrante del grupo 5: DIEGO JAVIER LOPEZ REINOSO - Carné No. 23747
- Nombre del integrante del grupo 5: HUGO DANIEL BARILLAS AJIN - Carné No. 23556

## Instalación de Librerias Adicionales

### Colorama
La libreria colorama permite agregar colores al output de codigo en la terminal
- Windows -> pip install colorama
- MacOs -> pip install colorama
- Linux (Arch) -> yay -S python-colorama 

### Time
Libreria que permite realizar delays en la ejecucion del programa.
- Windows -> Ya instalado por defecto
- MacOs -> Ya instalado por defecto
- Linux (Arch) -> Ya instalado por defecto

### os 
LIbreria para realizar animaciones por medio de la interaccion del sistema operativo.
- Windows -> Ya instalado por defecto
- MacOs -> Ya instalado por defecto
- Linux (Arch) -> Ya instalado por defecto
