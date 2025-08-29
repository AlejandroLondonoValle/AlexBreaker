import hashlib
import os
import pyfiglet
from colorama import Fore, Style, init
from time import time

# Inicializar colorama
init(autoreset=True)

# Diccionario por defecto
DEFAULT_DICT_PATH = "rockyou.txt"

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


def prompt_for_dictionary():
    custom_path = input(Fore.YELLOW + "[?] ¿Usar diccionario personalizado? (Enter para usar por defecto): ").strip()
    return custom_path if custom_path else DEFAULT_DICT_PATH


def crack_hash(target_hash, dict_path):
    guessed_type = guess_hash_type(target_hash)
    hash_func = get_hash_function(guessed_type)

    print(f"{Fore.MAGENTA}[?] Hash detectado como: {guessed_type} ({len(target_hash)} caracteres)\n")

    if guessed_type == "Unknown" or not hash_func:
        print(Fore.RED + "[!] No se puede determinar el tipo de hash.")
        return

    if not os.path.isfile(dict_path):
        print(Fore.RED + f"[!] Archivo no encontrado: {dict_path}")
        return

    print(Fore.CYAN + f"[+] Iniciando ataque de diccionario con: {dict_path}\n")

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
                    return
                if i % 500000 == 0:
                    print(Fore.YELLOW + f"[*] {i} contraseñas procesadas...")

        print(Fore.RED + "\n[✗] No se encontró coincidencia en el diccionario.")
    except KeyboardInterrupt:
        print(Fore.RED + "\n[!] Proceso interrumpido por el usuario.")
    except Exception as e:
        print(Fore.RED + f"[!] Error inesperado: {e}")


if __name__ == "__main__":
    print_banner()
    target = prompt_for_hash()
    dictionary_path = prompt_for_dictionary()
    crack_hash(target, dictionary_path)
