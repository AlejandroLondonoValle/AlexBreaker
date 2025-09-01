import hashlib
import os
import pyfiglet
from colorama import Fore, Style, init
from time import time

# Inicializar colorama
init(autoreset=True)

# Carpeta de diccionarios por defecto
DEFAULT_DICT_FOLDER = "dictionaries"

# Tipos de hash disponibles
HASH_TYPES = {
    "MD5": hashlib.md5,
    "SHA1": hashlib.sha1,
    "SHA224": hashlib.sha224,
    "SHA256": hashlib.sha256,
    "SHA384": hashlib.sha384,
    "SHA512": hashlib.sha512
}


def print_banner():
    banner = pyfiglet.figlet_format("AlexBreacker")
    print(Fore.CYAN + banner)


def guess_hash_type(hash_str):
    length = len(hash_str)
    return {
        32: "MD5",
        40: "SHA1",
        56: "SHA224",
        64: "SHA256",
        96: "SHA384",
        128: "SHA512"
    }.get(length, "Unknown")


def get_hash_function(hash_type):
    return HASH_TYPES.get(hash_type)


def prompt_for_hash():
    while True:
        hash_input = input(Fore.BLUE + "[>] Ingresa el Hash completo: ").strip().lower()
        if all(c in '0123456789abcdef' for c in hash_input):
            return hash_input
        else:
            print(Fore.RED + "[!] Hash inválido. Debe ser hexadecimal.")


def prompt_for_custom_dictionary():
    use_custom = input(Fore.YELLOW + "[?] ¿Desea añadir un diccionario personalizado generado por ingeniería social? (s/n): ").strip().lower()
    if use_custom == "s":
        path = input(Fore.YELLOW + "[>] Ruta del diccionario personalizado: ").strip()
        if os.path.isfile(path):
            return path
        else:
            print(Fore.RED + f"[!] No se encontró el archivo: {path}")
    return None


def get_default_dictionaries():
    """Obtiene todos los .txt dentro de la carpeta dictionaries (incluyendo subcarpetas)."""
    dict_files = []
    for root, _, files in os.walk(DEFAULT_DICT_FOLDER):
        for file in files:
            if file.endswith(".txt"):
                dict_files.append(os.path.join(root, file))
    return sorted(dict_files)


def crack_with_dictionary(target_hash, dict_path, hash_func, guessed_type):
    print(Fore.CYAN + f"[+] Iniciando ataque con: {dict_path}\n")
    try:
        with open(dict_path, "r", encoding="latin-1", errors="ignore") as f:
            start_time = time()
            for i, line in enumerate(f, 1):
                password = line.strip()
                h = hash_func()
                h.update(password.encode('utf-8'))
                if h.hexdigest() == target_hash:
                    duration = time() - start_time
                    print(Fore.GREEN + f"\n[✓] ¡Contraseña encontrada!: '{password}' usando {guessed_type}")
                    print(Fore.CYAN + f"[⏱] Tiempo transcurrido: {duration:.2f} segundos")
                    return True
                if i % 500000 == 0:
                    print(Fore.YELLOW + f"[*] {i} contraseñas procesadas...")
        return False
    except Exception as e:
        print(Fore.RED + f"[!] Error en {dict_path}: {e}")
        return False


def crack_hash(target_hash, custom_dict=None):
    guessed_type = guess_hash_type(target_hash)
    hash_func = get_hash_function(guessed_type)

    print(f"{Fore.MAGENTA}[?] Hash detectado como: {guessed_type} ({len(target_hash)} caracteres)\n")

    if guessed_type == "Unknown" or not hash_func:
        print(Fore.RED + "[!] No se puede determinar el tipo de hash.")
        return

    # Si el usuario añadió diccionario personalizado, usarlo primero
    if custom_dict:
        if crack_with_dictionary(target_hash, custom_dict, hash_func, guessed_type):
            return

    # Luego probar con los diccionarios encontrados en la carpeta
    default_dicts = get_default_dictionaries()
    if not default_dicts:
        print(Fore.RED + f"[!] No se encontraron diccionarios en la carpeta '{DEFAULT_DICT_FOLDER}'")
        return

    for dict_path in default_dicts:
        if crack_with_dictionary(target_hash, dict_path, hash_func, guessed_type):
            return

    print(Fore.RED + "\n[✗] No se encontró coincidencia en ninguno de los diccionarios.")


if __name__ == "__main__":
    print_banner()
    target = prompt_for_hash()
    custom_dict = prompt_for_custom_dictionary()
    crack_hash(target, custom_dict)
