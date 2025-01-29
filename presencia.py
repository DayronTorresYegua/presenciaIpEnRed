import sys
import subprocess
import platform

# 1. Validación de Datos de Entrada:

def validarIp(ip):
    octetos = ip.split('.')
    if len(octetos) != 4:
        return False
    for octeto in octetos:
        if not octeto.isdigit():
            return False
        if int(octeto) < 0 or int(octeto) > 255:
            return False
    return True

def determinarClase(ip):
    primerOcteto = int(ip.split('.')[0])
    if 0 <= primerOcteto <= 127:
        return 'A'
    elif 128 <= primerOcteto <= 191:
        return 'B'
    elif 192 <= primerOcteto <= 223:
        return 'C'
    elif 224 <= primerOcteto <= 239:
        return 'D'
    elif 240 <= primerOcteto <= 255:
        return 'E'

# 2. Implementación de la Funcionalidad:

def nombreSistemaOperativo():
    """
    Obtiene el nombre y la versión del sistema operativo.
    """
    sistema = platform.system()  # Ejemplo: "Windows", "Linux", "Darwin" (macOS)
    version = platform.version()  # Versión del sistema operativo
    return sistema, version

# 3. Comprobar si la IP está activa en la red usando ping:

def verificarIpConPing(ip, timeout=3):
    """
    Verifica si una IP está activa utilizando el comando ping.
    Compatible con Windows y Unix/Linux/macOS.
    """
    try:
        # Comando ping según el sistema operativo
        if platform.system().lower() == "windows":
            comando = ['ping', '-n', '1', '-w', str(timeout * 1000), ip]  # Windows usa -n y -w (en milisegundos)
        else:
            comando = ['ping', '-c', '1', '-W', str(timeout), ip]  # Unix/Linux/macOS usa -c y -W

        # Ejecuta el comando ping
        output = subprocess.run(comando, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Si el comando ping fue exitoso, la IP está activa
        return output.returncode == 0
    except Exception as e:
        print(f"Error al ejecutar ping: {e}")
        return False

def main():
    # 1. Validación de Datos de Entrada:
    if len(sys.argv) != 2:
        print("La ip no debe contener espacios en sus octetos")
        sys.exit(1)

    direccionIp = sys.argv[1]

    if validarIp(direccionIp):
        clase = determinarClase(direccionIp)
        print(f"La dirección IP {direccionIp} es de clase {clase}.")
    else:
        print("La dirección IP ingresada no es válida. Debe contener 4 octetos con números comprendidos entre 0 y 255.")
        sys.exit(1)

    # 2. Implementación de la Funcionalidad:
    sistemaOperativo = nombreSistemaOperativo()
    print(f"El sistema operativo es: {sistemaOperativo}")

    # Verificar si la IP está activa usando ping
    print(f"Comprobando si la dirección IP {direccionIp} está activa...")
    if verificarIpConPing(direccionIp):
        print(f"La dirección IP {direccionIp} está activa.")
    else:
        print(f"La dirección IP {direccionIp} no está activa o no responde.")

if __name__ == "__main__":
    main()
