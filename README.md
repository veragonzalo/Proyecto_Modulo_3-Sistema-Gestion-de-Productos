# 📦 Sistema de Gestión de Productos – Portafolio N°3

## 📌 Descripción del proyecto

Este proyecto corresponde al Portafolio N°3 del modulo **FUNDAMENTOS DE PROGRAMACIÓN EN PYTHON**, del curso **“Desarrollo de Aplicaciones Full Stack Python”**.

Consiste en el desarrollo de un **Sistema de Gestión de Productos en Python**, ejecutado en consola, cuyo objetivo es aplicar de forma práctica los contenidos vistos en el módulo, tales como estructuras de control, funciones, estructuras de datos y modularización del código.

El sistema permite administrar productos mediante un menú interactivo, incorporando validaciones, control de roles y un sistema de login básico.

---

## 🎯 Objetivos del proyecto

- Aplicar los fundamentos del lenguaje Python en un sistema funcional.
- Utilizar estructuras de control (`if`, `while`, `for`, `break`, `continue`).
- Implementar funciones con parámetros y valores de retorno.
- Manejar estructuras de datos como listas, diccionarios, tuplas y sets.
- Organizar el código de forma modular utilizando múltiples archivos `.py`.
- Simular un sistema real de gestión con control de acceso por roles.

---

## ⚙️ Funcionalidades principales

- 🔐 **Login con validación de usuario y contraseña**
- 👤 **Control de roles (Admin / Usuario)**
- 📋 **Listado de productos**
- 🔍 **Búsqueda de productos por código**
- ➕ **Registro de nuevos productos (solo Admin)**
- ✏️ **Modificación de productos (solo Admin)**
  - Nombre
  - Precio
  - Stock  
  *(el código del producto es inmutable)*
- 🗑️ **Eliminación de productos (solo Admin)**
- ❌ Validación de datos de entrada
- 📦 Gestión de productos mediante estructuras de datos en memoria

---

## 🧠 Estructuras de datos utilizadas

- **Listas (`list`)**: almacenamiento de productos.
- **Diccionarios (`dict`)**: representación de cada producto y usuarios del sistema.
- **Tuplas (`tuple`)**: definición de roles del sistema (datos inmutables).
- **Conjuntos (`set`)**: control de códigos únicos de productos.

---

## 🗂️ Estructura del proyecto
proyecto_gestion_productos/
│
├── main.py
├── README.md
│
└── modulos/
├── init.py
├── menu.py
├── gestion_datos.py
├── validaciones.py
└── funciones_utiles.py
