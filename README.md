# 🧩 Proyecto Lógica: Katas de Python
## 📘 Descripción del proyecto
Este proyecto forma parte del módulo **Python** y tiene como objetivo poner en práctica todo lo aprendido hasta ahora.
Aquí se aplican los conceptos vistos durante la formación, como son: tipos de datos, estructuras, funciones, clases, condicionales, iteraciones, y el uso de librerías y módulos.

En este proyecto se irán resolviendo **40 ejercicios de lógica (Katas)** cada uno centrado en un tema diferente de Python. Por ejemplo: manejo de cadenas, listas, funciones lambda, excepciones, programación funcional, y ejercicios con clases y objetos.
Para organizar todos los ejercicios de forma práctica, se ha implementado un **menú interactivo**.

---

## ⚙️ Requisitos del Proyecto

Para realizar este proyecto se deben cumplir los siguientes puntos del módulo:

- **Manejo de tipos de datos básicos:** uso de funciones incorporadas (`len()`, `sum()`, `map()`,etc.)
- **Uso de estructura de datos:** como listas, diccionarios, tuplas y conjuntos, junto con sus métodos.
- **Uso de condicionales e iteraciones:** (`if()`, `for()`, `while()`).
- **Creación y uso de funciones** en Python.
- **Manejo de clases y conceptos básicos de programaciónn orientada a objetos**.
- **Importación y uso de módulos y librerías estándar** vistas en el temario (`math()`,`functools()`, `collections()`,etc.)
- **Buenas prácticas de código:** nombres claros, funciones independientes y comentarios explicativos.

---

## 📂 Estructura del proyecto

📂 Python_Katas/
│
├── Python_Katas.py # Archivo principal con los 40 ejercicios y el menú interactivo
└── README.md # Archivo con la descripción y guía del proyecto

Cada ejercicio se define dentro de una función (`def ejercicioX():`) y se puede ejecutar individualmente gracias al **menú interactivo** integrado.

---

## 🧭 Menú Interactivo

Para no tener que ejecutar todo el código de golpe, implementé un menú que permite elegir el número de cada ejercicio que se quiere probar.
Este sistema me ha permitido **probar, depurar y revisar** cada kata por separado sin tener que comentar o desactivar líneas de código.

### 💡 Ventajas del menú: 
- 🔢 Permite ejecutar cualquier ejercicio individualmente (del 1 al 40).
- 🚪 Se puede salir del programa escribiendo `0`o `salir`. 
- ⛔ Evita bloqueos por funciones con `input()` en ejercicios que no quieres probar.
- ⚙️ Mejora la organización y la legibilidad del código.

Ejemplo de como se ve el menú:

📘 MENÚ DE EJERCICIOS

Ejercicio 1

Ejercicio 2
...

Ejercicio 40

Salir
Selecciona un ejercicio (1-40) o 0 para salir:

--- 

## 🧠 Contenidos y conceptos aplicados

Cada grupo de ejercicios se centra en un conjunto de temas o herramientas concretas en Python:

| Bloque | Conceptos principales | Ejercicios aproximados |
|:--|:--|:--:|
| **Datos básicos y funciones integradas** | Cadenas, listas, diccionarios, `map()`, `filter()`, `reduce()` | 1–10 |
| **Condicionales e iteraciones** | Uso de `if`, `for`, `while`, control de errores con `try/except` | 11–20 |
| **Funciones y lambdas** | Parámetros, valores por defecto, funciones anidadas, lambdas | 21–30 |
| **Programación Orientada a Objetos (POO)** | Clases, atributos, métodos, encapsulación | 31–35 |
| **Aplicaciones lógicas y procesamiento de texto** | Condicionales avanzados, entradas de usuario, manipulación de strings | 36–40 |

---

## 🧰 Herramientas utilizadas

- 🖥️ **Visual Studio Code** → editor principal del proyecto.  
- 🐍 **Python 3.10+** → lenguaje base del módulo.  
- 🧮 **Módulos estándar:**  
  - `functools` → para el uso de `reduce()`.  
  - `math` y `statistics` → operaciones matemáticas y promedios.  
  - `collections.Counter` → conteo de elementos y palabras.

---

## 💡 Buenas prácticas aplicadas  

- Código comentado de forma clara y precisa.  
- Uso de nombres descriptivos con `snake_case`.  
- Separación lógica de cada ejercicio dentro de su propia función.  
- Control de errores mediante `try / except`.  
- Implementación de `if __name__ == "__main__":` como punto de entrada.  
- Estructura modular y limpia para facilitar la lectura.  

---
## 🧭 Reflexión personal  

Este proyecto me ha servido para **consolidar la base de Python** y entender mejor cómo pensar de forma lógica y estructurada al resolver problemas.  
Durante el desarrollo, he aprendido a escribir código más ordenado, a reutilizar funciones y a manejar errores con mayor naturalidad.  
Además, el menú interactivo me ha ayudado muchísimo a probar los ejercicios de forma más cómoda y a resolver esos errores, ya que a raíz de esto se me ocurrió la idea de implementar este menú. Esto fue porque al ejecutar los ejercicios salían todos los resultados a la vez, o por ejemplo, al añadir la función `input()`se bloqueaba sin dar la opción de resolver los ejercicios siguientes.

---
