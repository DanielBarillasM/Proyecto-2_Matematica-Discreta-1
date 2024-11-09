from colorama import Fore, Style, init
import time

# Inicializa colorama para manejar los colores en la consola
init(autoreset=True)

# Variable global para almacenar el mensaje encriptado
mensaje_encriptado_global = []

# Función para mostrar texto animado
def animacion_texto(texto, delay=0.05, color=Fore.WHITE):
    for char in texto:
        print(f"{color}{char}", end='', flush=True)
        time.sleep(delay)
    print(Style.RESET_ALL)

# Función para mostrar barra de progreso en consola
def barra_progreso(cantidad=5, delay=0.2, color=Fore.YELLOW):
    print(f"{color}Procesando", end='', flush=True)
    for _ in range(cantidad):
        print(f'{color} █', end='', flush=True)
        time.sleep(delay)
    print(f"{color}...completado", flush=True)
    print(Style.RESET_ALL)

# Generador pseudoaleatorio (para evitar el uso de random)
def generador_pseudoaleatorio(seed, modulo, a=1664525, c=1013904223):
    seed = (a * seed + c) % modulo
    return seed

# Función para encontrar el MCD usando el algoritmo de Euclides
def mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)  # Asegura que el resultado es positivo

# Función para encontrar el inverso modular usando el algoritmo extendido de Euclides
def inverso_modular(e, n):
    t, new_t = 0, 1
    r, new_r = n, e
    while new_r != 0:
        quotient = r // new_r
        t, new_t = new_t, t - quotient * new_t
        r, new_r = new_r, r - quotient * new_r
    if r > 1:
        print(Fore.RED + "No existe un inverso modular para los valores proporcionados.")
        return None
    if t < 0:
        t = t + n
    return t

# Función para verificar si un número es primo
def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Función para generar un número primo en un rango dado
def generar_primo(rango_inferior, rango_superior, seed=1):
    primos = [num for num in range(rango_inferior, rango_superior + 1) if es_primo(num)]
    if not primos:
        print(Fore.RED + "No se encontró un número primo en el rango proporcionado.")
        return None

    # Selección de un primo usando el generador de números pseudoaleatorios
    index = generador_pseudoaleatorio(seed, len(primos)) % len(primos)
    return primos[index]

# Función para generar las llaves pública y privada de RSA
def generar_llaves(rango_inferior, rango_superior, seed=1):
    animacion_texto("Generando llaves RSA...", color=Fore.CYAN)
    barra_progreso()
    
    p = generar_primo(rango_inferior, rango_superior, seed)
    q = generar_primo(rango_inferior, rango_superior, seed + 1)
    while p == q:
        q = generar_primo(rango_inferior, rango_superior, seed + 2)
        
    n = p * q
    phi = (p - 1) * (q - 1)
    
    e = 3
    while e < phi:
        if mcd(e, phi) == 1:
            break
        e += 2
    
    d = inverso_modular(e, phi)
    if d is None:
        print(Fore.RED + "Error generando las llaves, intenta de nuevo.")
        return None, None
    
    print(Fore.GREEN + f"Claves generadas exitosamente:\nClave pública: (e={e}, n={n})\nClave privada: (d={d}, n={n})")
    return (e, n), (d, n)

# Función para encriptar un caracter usando la clave pública
def encriptar(mensaje, llave_publica):
    global mensaje_encriptado_global
    e, n = llave_publica
    mensaje_encriptado_global = [pow(ord(char), e, n) for char in mensaje]
    print(Fore.BLUE + f"Mensaje encriptado: {mensaje_encriptado_global}")
    return mensaje_encriptado_global

# Función para desencriptar un caracter encriptado usando la clave privada
def desencriptar(mensaje_encriptado, llave_privada):
    d, n = llave_privada
    mensaje_desencriptado = ''.join([chr(pow(char, d, n)) for char in mensaje_encriptado])
    print(Fore.GREEN + f"Mensaje desencriptado: {mensaje_desencriptado}")
    return mensaje_desencriptado

# Función principal para ejecutar el programa con un menú interactivo
def main():
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
                encriptar(mensaje, llave_publica)

        elif opcion == "3":
            if not llave_privada:
                animacion_texto("Primero debes generar las llaves.", color=Fore.RED)
            elif not mensaje_encriptado_global:
                animacion_texto("Primero debes encriptar un mensaje.", color=Fore.RED)
            else:
                desencriptar(mensaje_encriptado_global, llave_privada)

        elif opcion == "4":
            animacion_texto("Gracias por utilizar el sistema RSA. Hasta pronto.", color=Fore.CYAN)
            break

        else:
            animacion_texto("Opción no válida. Por favor, selecciona una opción del menú.", color=Fore.RED)

# Ejecuta el programa
if __name__ == "__main__":
    main()