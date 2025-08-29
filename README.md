# 🔓 AlexBreaker

**AlexBreaker** es una herramienta escrita en Python para **crackear hashes** mediante ataques de diccionario. Es ideal para pruebas de seguridad, recuperación de contraseñas y aprendizaje en criptografía. Utiliza el famoso diccionario `rockyou.txt` (u otros personalizados) para intentar descifrar hashes comunes como MD5, SHA1, SHA256, entre otros.

![alexbreaker-banner](https://img.shields.io/badge/status-active-success?style=flat-square)
![python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square)
![license](https://img.shields.io/badge/license-MIT-lightgrey?style=flat-square)

---

## 📌 Características

- ✅ Soporte para múltiples algoritmos de hash: `MD5`, `SHA1`, `SHA224`, `SHA256`, `SHA384`, `SHA512`
- 📁 Opción de usar diccionarios personalizados o por defecto (`rockyou.txt`)
- 🧠 Detección automática del tipo de hash según su longitud
- 🎨 Interfaz visual en consola con banner (usando `pyfiglet` y `colorama`)
- ⚡ Medición del tiempo total de ejecución
- 🛑 Manejo de errores e interrupciones limpias (Ctrl + C)
- 🔄 Código modular y fácilmente ampliable

---

## 🛠️ Requisitos

- Python 3.6 o superior
- Paquetes requeridos:
  - `pyfiglet`
  - `colorama`

Puedes instalarlos con:

```bash
pip install -r requirements.txt
```

## 🚀 Uso

Asegúrate de tener el diccionario rockyou.txt en la misma carpeta del script, o proporciona otro.

Ejecuta el script:

```bash
python hash_cracker.py
```

Introduce el hash objetivo cuando se te pida.

Puedes usar un diccionario personalizado cuando te lo solicite el programa (o presionar Enter para usar rockyou.txt).


## 💻 Ejemplo de uso
```bash
[>] Ingresa el Hash completo: 5f4dcc3b5aa765d61d8327deb882cf99
[?] ¿Usar diccionario personalizado? (Enter para usar por defecto): 

[?] Hash detectado como: MD5 (32 caracteres)

[+] Iniciando ataque de diccionario con: rockyou.txt

[*] 500000 contraseñas procesadas...
[✓] ¡Contraseña encontrada!: 'password' usando MD5
[⏱] Tiempo transcurrido: 12.54 segundos
```

## 📂 Estructura del Proyecto

```bash
alexbreaker/
│
├── hash_cracker.py         # Código principal
├── rockyou.txt             # Diccionario (no incluido por defecto)
├── requirements.txt        # Dependencias
└── README.md               # Este archivo
```

## ⚠️ Advertencia de Uso:

Esta herramienta está destinada exclusivamente a fines educativos y de auditoría ética.
El uso no autorizado contra sistemas ajenos es ilegal y va contra los principios de la comunidad.
Úsala bajo tu responsabilidad y siempre con permiso.


## 📄 Licencia

Este proyecto está bajo la licencia MIT.
Eres libre de usar, modificar y distribuir este código, siempre y cuando mantengas los créditos.


## ✍️ Autor

Creado por Alejandro Londoño & Alejandro Roque


