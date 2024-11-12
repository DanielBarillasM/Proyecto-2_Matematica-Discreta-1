from colorama import Fore, Style, init
import time

# Inicializa colorama para manejar los colores en la consola
init(autoreset=True)

# Variable global para almacenar el mensaje encriptado
mensaje_encriptado_global = []
mensaje_original = ""  # Variable para almacenar el mensaje original

# Función para mostrar texto animado
def animacion_texto(texto, delay=0.05, color=Fore.WHITE):
    """
    Muestra texto con un efecto de animación en la consola.
    
    :param texto: El texto a mostrar.
    :param delay: El retraso entre cada carácter (en segundos).
    :param color: El color del texto.
    """
    for char in texto:
        print(f"{color}{char}", end='', flush=True)
        time.sleep(delay)
    print(Style.RESET_ALL)

# Función para mostrar barra de progreso en consola
def barra_progreso(cantidad=5, delay=0.2, color=Fore.YELLOW):
    """
    Muestra una barra de progreso en la consola.
    
    :param cantidad: La cantidad de bloques en la barra de progreso.
    :param delay: El retraso entre cada bloque (en segundos).
    :param color: El color de la barra de progreso.
    """
    print(f"{color}Procesando", end='', flush=True)
    for _ in range(cantidad):
        print(f'{color} █', end='', flush=True)
        time.sleep(delay)
    print(f"{color}...completado", flush=True)
    print(Style.RESET_ALL)

# Generador pseudoaleatorio (para evitar el uso de random)
def generador_pseudoaleatorio(seed, modulo, a=1664525, c=1013904223):
    """
    Genera un número pseudoaleatorio basado en una semilla.
    
    :param seed: La semilla inicial.
    :param modulo: El valor del módulo.
    :param a: El multiplicador (por defecto 1664525).
    :param c: El incremento (por defecto 1013904223).
    :return: Un número pseudoaleatorio.
    """
    seed = (a * seed + c) % modulo
    return seed

# Función para encontrar el MCD usando el algoritmo de Euclides
def mcd(a, b):
    """
    Calcula el Máximo Común Divisor (MCD) de dos números usando el algoritmo de Euclides.
    
    :param a: El primer número.
    :param b: El segundo número.
    :return: El MCD de a y b.
    """
    while b != 0:
        a, b = b, a % b
    return abs(a)  # Asegura que el resultado es positivo

# Función para encontrar el inverso modular
def inverso_modular(e: int, n: int):
    """
    Calcula el inverso modular de e módulo n usando el algoritmo extendido de Euclides.
    
    :param e: El número cuyo inverso modular se desea encontrar.
    :param n: El módulo.
    :return: El inverso modular de e módulo n.
    """
    # Validación de input
    if not isinstance(e, int) or not isinstance(n, int):
        raise ValueError("Los valores de e y n deben ser enteros.")
    if e <= 0 or n <= 1:
        raise ValueError("e debe ser positivo y n debe ser mayor que 1.")
    if mcd(e, n) != 1:
        raise ValueError("No existe un inverso modular porque e y n no son coprimos.")
    
    t, new_t = 0, 1
    r, new_r = n, e
    while new_r != 0:
        quotient = r // new_r
        t, new_t = new_t, t - quotient * new_t
        r, new_r = new_r, r - quotient * new_r
    if r != 1:
        print(Fore.RED + "No existe un inverso modular para los valores proporcionados.")
        return None
    if t < 0:
        t += n
    return t

# Función para verificar si un número es primo
def es_primo(num):
    """
    Verifica si un número es primo.
    
    :param num: El número a verificar.
    :return: True si el número es primo, False en caso contrario.
    """
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Función para generar un número primo en un rango dado
def generar_primo(rango_inferior, rango_superior, seed=1):
    """
    Genera un número primo dentro de un rango dado.
    
    :param rango_inferior: El límite inferior del rango.
    :param rango_superior: El límite superior del rango.
    :param seed: La semilla para el generador pseudoaleatorio.
    :return: Un número primo dentro del rango.
    """
    primos = [num for num in range(rango_inferior, rango_superior + 1) if es_primo(num)]
    if not primos:
        print(Fore.RED + "No se encontró un número primo en el rango proporcionado.")
        return None

    # Selección de un primo usando el generador de números pseudoaleatorios
    index =( generador_pseudoaleatorio(seed, len(primos) * 50) + generador_pseudoaleatorio(seed, 10000)) % len(primos)
    return primos[index]

# Función para generar las llaves pública y privada de RSA
def generar_llaves(rango_inferior: int, rango_superior: int, seed: int=1):
    """
    Genera las llaves pública y privada para el cifrado RSA.
    
    :param rango_inferior: El límite inferior del rango para generar números primos.
    :param rango_superior: El límite superior del rango para generar números primos.
    :param seed: La semilla para el generador pseudoaleatorio.
    :return: Una tupla con la llave pública y la llave privada.
    """
    # Validar input
    if not isinstance(rango_inferior, int) or not isinstance(rango_superior, int):
        raise ValueError("Los límites del rango deben ser números enteros.")
    if rango_inferior <= 0 or rango_superior <= 0:
        raise ValueError("Los límites del rango deben ser positivos.")
    if rango_inferior >= rango_superior:
        raise ValueError("El rango inferior debe ser menor que el rango superior.")
        
    animacion_texto("Generando llaves RSA...", color=Fore.CYAN)
    barra_progreso()
    
    try:
        # Generación de primos p y q
        p = generar_primo(rango_inferior, rango_superior, seed)
        q = generar_primo(rango_inferior, rango_superior, seed + 1)
        k = 2
        while p == q:
            q = generar_primo(rango_inferior + k, rango_superior, seed * k)
            k = k + 1
        
        # Cálculo de n y phi
        n = p * q
        phi = (p - 1) * (q - 1)
        
        # Generación de e (coprimo con phi)
        e = generar_e(phi)
        
        # Generación de d (inverso modular)
        d = inverso_modular(e, phi)
        if d is None:
            print(Fore.RED + "Error generando las llaves, intenta de nuevo.")
            return None, None
        
        # Éxito
        print(Fore.GREEN + f"Claves generadas exitosamente:\nClave pública: (e={e}, n={n})\nClave privada: (d={d}, n={n})")
        return (e, n), (d, n)
    
    except Exception as ex:
        print(Fore.RED + f"Error: {str(ex)}")
        return None, None

def generar_e(phi: int) -> int:
    """
    Encuentra un valor de e coprimo con phi.
    
    :param phi: Valor de phi (producto de (p-1) * (q-1)).
    :return: Un entero e tal que 1 < e < phi y gcd(e, phi) == 1.
    """
    for e in range(3, phi, 2):  # Empieza en 3, solo números impares
        if mcd(e, phi) == 1:
            return e
    raise ValueError("No se pudo encontrar un valor de e coprimo con phi.")

# Función para encriptar un caracter usando la clave pública
def encriptar(mensaje, llave_publica):
    """
    Encripta un mensaje usando la clave pública.
    
    :param mensaje: El mensaje a encriptar.
    :param llave_publica: La llave pública (e, n).
    :return: El mensaje encriptado.
    """
    global mensaje_encriptado_global
    e, n = llave_publica
    mensaje_encriptado_global = [pow(ord(char), e, n) for char in mensaje]
    print(Fore.BLUE + f"Mensaje encriptado: {mensaje_encriptado_global}")
    return mensaje_encriptado_global

# Función para desencriptar un caracter encriptado usando la clave privada
def desencriptar(mensaje_encriptado, llave_privada):
    """
    Desencripta un mensaje encriptado usando la clave privada.
    
    :param mensaje_encriptado: El mensaje encriptado.
    :param llave_privada: La llave privada (d, n).
    :return: El mensaje desencriptado.
    """
    d, n = llave_privada
    mensaje_desencriptado = ''.join([chr(pow(char, d, n)) for char in mensaje_encriptado])
    print(Fore.GREEN + f"Mensaje desencriptado: {mensaje_desencriptado}")
    return mensaje_desencriptado

# Función principal para ejecutar el programa con un menú interactivo
def main():
    """
    Función principal que ejecuta el programa con un menú interactivo.
    """
    animacion_texto("Bienvenido al sistema de encriptación RSA", color=Fore.YELLOW)
    llave_publica, llave_privada = None, None

    while True:
        print(Fore.GREEN + "\nMenú:")
        animacion_texto("1. Generar llaves RSA", color=Fore.YELLOW)
        animacion_texto("2. Encriptar mensaje", color=Fore.YELLOW)
        animacion_texto("3. Desencriptar mensaje", color=Fore.YELLOW)
        animacion_texto("4. Salir", color=Fore.YELLOW)
        opcion = input(Fore.CYAN + "Selecciona una opción: ")

        if opcion == "1":
            try:
                rango_inferior = int(input(Fore.CYAN + "Ingresa el rango inferior para generar números primos: "))
                rango_superior = int(input(Fore.CYAN + "Ingresa el rango superior para generar números primos: "))
                llave_publica, llave_privada = generar_llaves(rango_inferior, rango_superior)
            except ValueError:
                animacion_texto("Entrada no válida. Por favor, ingresa números enteros.", color=Fore.RED)

        elif opcion == "2":
            if not llave_publica:
                animacion_texto("Primero debes generar las llaves.", color=Fore.RED)
            else:
                mensaje = input(Fore.CYAN + "Ingresa el mensaje a encriptar: ")
                global mensaje_original
                mensaje_original = mensaje  # Almacena el mensaje original
                encriptar(mensaje, llave_publica)

        elif opcion == "3":
            if not llave_privada:
                animacion_texto("Primero debes generar las llaves.", color=Fore.RED)
            else:
                # Solicita ingresar el mensaje encriptado manualmente
                mensaje_encriptado_input = input(Fore.CYAN + "Ingresa el mensaje encriptado (separado por comas): ")
                # Convierte la entrada en una lista de enteros
                mensaje_encriptado = [int(x) for x in mensaje_encriptado_input.split(",")]
                desencriptar(mensaje_encriptado, llave_privada)

        elif opcion == "4":
            animacion_texto("Gracias por utilizar el sistema RSA. Hasta pronto.", color=Fore.CYAN)
            break

        else:
            animacion_texto("Opción no válida. Por favor, selecciona una opción del menú.", color=Fore.RED)

# Ejecuta el programa
if __name__ == "__main__":
    main()