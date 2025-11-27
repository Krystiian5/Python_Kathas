# 📦 Importaciones globales para todo el proyecto
import statistics #Importamos el módulo estándar para operaciones estadísticas para el ejercicio 5 y 27
import math #Importamos el módulo de matemáticas para el ejercicio 6 y 39
from functools import reduce #Importamos el módulo reduce de functools para los ejercicios 17, 22, 23 y 24
import operator #Importamos el módulo operator para el ejercicio 24
from collections import Counter #Importamos el módulo Counter para el ejercicio 30

"""1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias
de cada letra en la cadena. Los espacios no deben ser considerados."""
def ejercicio1():
    def frecuencia_letras (cadena):
    #Para eliminar los espacios de mi cadena y que no haya distinción entre mayúsculas y minúsculas:
        cadena = cadena.replace(" ","").lower()
    #Creamos un diccionario vacío para guardar las frecuencias de cada letra
        frecuencias = {}
    #Bucle for para recorrer cada letra en la cadena
        for letra in cadena:
    #Usamos el método .get() del diccionario para que si existe devuelva su valor actual, si no devuelva 0 y luego sumamos 1
            frecuencias[letra] = frecuencias.get(letra, 0) + 1
        return frecuencias
    texto = "Primer Ejercicio"
    resultado = frecuencia_letras(texto)
    print (f'Resultado ejercicio 1: {resultado}')

"""2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()"""
def ejercicio2():
    def doblar_valores(lista):
    #Añadimos la función lambda para coger un valor y que nos devuelva el doble
        nueva_lista = list(map(lambda x: x*2,lista))
        return nueva_lista
    numeros = [3, 4, 7, 8, 13]
    resultado = doblar_valores(numeros)
    print (f'Resultado ejercicio 2: {resultado}')

"""3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe
devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo."""
def ejercicio3():    
    def filtrar_palabras(lista_palabras, palabra_objetivo):
        #Utilizamos filter() para que devuelva las palabras que contengan la palabra objetivo  
        resultado = list(filter(lambda palabra: palabra_objetivo in palabra, lista_palabras))
        return resultado
    palabras = ['gato', 'perro', 'gatito', 'ratón', 'gatuno']
    objetivo = 'gat'
    resultado = filtrar_palabras(palabras,objetivo)
    print (f'Resultado ejercicio 3: {resultado}')

"""4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()"""
def ejercicio4(): 
    def diferencia_listas (lista1, lista2):
        diferencias = list(map(lambda x, y: x-y, lista1, lista2))
        return diferencias
    lista_a = [10, 20, 30, 40]
    lista_b = [2, 4, 6, 9]
    resultado = diferencia_listas(lista_a, lista_b)
    print (f'Resultado ejercicio 4: {resultado}')

"""5. Ecribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por
defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual
que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver
una tupla que contenga la media y el estado."""
def ejercicio5():

    #Calculamos la media de una lista para evaluar si es aprobado o suspenso
    def evaluar_promedio(lista_numeros, nota_aprobado=5):
        media = statistics.mean(lista_numeros)

    #Evaluamos el estado en función de la media
        estado = 'aprobado' if media >= nota_aprobado else 'suspenso'
        return (media, estado)
    notas = [4, 6, 5, 7]
    resultado = evaluar_promedio(notas)
    print (f'Resultado ejercicio 5: {resultado}')

"""6. Escribe una función que calcule el factorial de un número de manera recursiva."""
def ejercicio6():
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n*factorial(n-1)
    numero = 5
    resultado = factorial(numero)
    print (f'Resultado ejercicio 6: {resultado}')

"""7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()"""
def ejercicio7():
    def tuplas_a_strings(lista_tuplas):
        return list(map(lambda t: ", ".join(map(str, t)), lista_tuplas))
    tuplas = [(1,2),(3,4),(5,6)]
    resultado = tuplas_a_strings(tuplas)
    print (f'Resultado ejercicio 7: {resultado}')
    print (f'Tipo de resultado: {type(resultado)}')
    print (f'Tipo del primer elemento:{type(resultado[0])}')

"""8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico
o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje
indicando si la división fue exitosa o no."""
def ejercicio8():
    def dividir():
        try:
            #Solicitamos los valores al usuario
            num1 = float(input("Introduce el primer número"))
            num2 = float(input("Introduce el segundo número"))
            resultado = num1/num2
        except ValueError:
            #Se ejecutaría si el usuario introduce un valor no numérico
            print("Error: Debes introducir valores numéricos")
            return
        except ZeroDivisionError:
            #Se ejecutaría si el segundo número es cer
            print ("Error: No se puede dividir entre cero")
            return
        else: 
            #Si no hay errores
            print(f"División correcta. El resultado del ejercicio 8 es: {resultado}")

    dividir ()
    
"""9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista
excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre",
"Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter()"""
def ejercicio9():    
    def filtrar_mascotas_validas (lista_mascotas):
        prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
        prohibidas_lower = [p.lower() for p in prohibidas]
        mascotas_filtradas = list(filter(lambda m: m.lower() not in prohibidas_lower, lista_mascotas))
        return mascotas_filtradas
    mascotas = ["Perro", "gato", "MAPACHE", "Serpiente Pitón", "Conejo", "cocodrilo", "Loro"]
    resultado = filtrar_mascotas_validas(mascotas)
    print (f'Resultado ejercicio 9: {resultado}')

"""10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una
excepción personalizada y maneja el error adecuadamente."""
def ejercicio10():
    class ListaVaciaError(Exception):
        #Se laanza cuando la lista está vacía y no se puede calcular el promedio
        pass
    #Calculamos el promerio
    def calcular_promedio(lista):
        if not lista:
            raise ListaVaciaError ('Error: La lista está vacía. No se puede calcular el promedio')
        return sum (lista) / len(lista)
    try:
        numeros = [5,6,8]
        resultado = calcular_promedio(numeros)
        print (f'Resultado ejercicio 10, el promedio es: {resultado}')
    except ListaVaciaError as e:
        print (e)

"""11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un
valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones
adecuadamente."""
def ejercicio11():
    def solicitar_edad():
        while True:
            try:
                edad_str = input("Introduce tu edad: ").strip()
                edad = int(edad_str)
                if edad < 0 or edad > 120:
                    raise ValueError ("La edad debe estar entre 0 y 120")
            except ValueError as e:
                print (f"Error: {e}. Inténtalo de nuevo.")
            else:
                print (f"Edad válida: {edad}")
                break
    solicitar_edad()

"""12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()"""
def ejercicio12():
    def longitudes_palabras(frase):
        palabras = frase.split()
        longitudes = list(map(len,palabras))
        return longitudes
    frase = "Este Verano está siendo muy caluroso"
    resultado = longitudes_palabras(frase)
    print (f'Resultado ejercicio 12: {resultado}')

"""13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en
mayúsculas y minúsculas. Las letras no pueden estar repetidas. Usa la función map()"""

def ejercicio13():
    def mayus_minus_unicas(conjunto):
        # Filtrar sólo letras y pasar a minúscula para evitar duplicados
        letras_unicas = set(filter(str.isalpha, conjunto.lower()))
        
        # Usamos map para crear tuplas (mayúscula, minúscula)
        resultado = list(map(lambda c: (c.upper(), c), letras_unicas))
        
        # Ordenamos para que la salida sea consistente
        resultado.sort()
        return resultado

    conjunto = "aAbBcCdDeEfF123!!"
    resultado = mayus_minus_unicas(conjunto)
    print(f'Resultado ejercicio 13: {resultado}')

"""14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la
función filter()"""

def ejercicio14():
    def filtrar_por_letra(lista_palabbras, letra):
        letra = letra.lower()
        return list (filter(lambda palabra: palabra.lower().startswith(letra),lista_palabbras))
    palabras = ["Perro", "gato", "ratón", "caballo", "Ganso", "gallina"]
    letra_objetivo = "g"
    resultado = filtrar_por_letra(palabras, letra_objetivo)
    print (f'Resultado ejercicio 14: {resultado}')

"""15. Crea una función lambda que sume 3 a cada número de una lista dada."""

def ejercicio15():
    numeros = [1, 4, 7, 10]
    resultado = list(map(lambda x: x + 3, numeros))
    print (f'Resultado ejercicio 15: {resultado}')

"""16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de
todas las palabras que sean más largas que n. Usa la función filter()"""

def ejercicio16():
    def palabras_mas_largas_que (texto, n):
        palabras = texto.split()
        return list(filter(lambda p: len(p) > n, palabras))
    texto = "El verano es mi estación de año preferida"
    n = 5
    resultado = palabras_mas_largas_que(texto, n)
    print (f'Resultado ejercicio 16: {resultado}')

"""17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2]
corresponde al número quinientos setenta y dos (572). Usa la función reduce()"""

def ejercicio17():
    def lista_a_numero(lista_digitos):
        return reduce(lambda acc, d: acc * 10 + d, lista_digitos)
    digitos = [5,7,2]
    resultado = lista_a_numero(digitos)
    print (f'Resultado ejercicio 17: {resultado}')

"""18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes
(nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a
90. Usa la función filter()"""

def ejercicio18():
    estudiantes = [
        {"nombre": "Ana", "edad": 20, "calificacion": 95},
        {"nombre": "Luis", "edad": 28, "calificacion": 85},
        {"nombre": "María", "edad": 36, "calificacion": 92},
        {"nombre": "Carlos", "edad": 18, "calificacion": 78},
        {"nombre": "Sofía", "edad": 45, "calificacion": 90},
    ]

    sobresalientes = list(filter(lambda e: e["calificacion"] >= 90, estudiantes))

    print ('Resultado ejercicio 18:')
    for estudiante in sobresalientes:
        print (estudiante)

"""19. Crea una función lambda que filtre los números impares de una lista dada."""

def ejercicio19():
    numeros = [1,2,3,4,5,6,7,8,9,10]
    impares = list(filter(lambda x: x % 2 != 0, numeros))
    print (f'Resultado ejercicio 19: {impares}')

"""20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función
filter()"""

def ejercicio20():
    elementos = [1, "hola", 3, "casa", 5, "gato", 7]
    solo_enteros = list(filter(lambda x: isinstance(x,int), elementos))
    print (f'Resultado ejercicio 20: {solo_enteros}')

"""21. Crea una función que calcule el cubo de un número dado mediante una función lambda"""

def ejercicio21():
    #Calculamos el cubo usando pow() con una función lambda
    cubo = lambda x: pow(x,3)
    numero = 4
    resultado = cubo(numero)
    print (f'Resultado ejercicio 21: {resultado}')

"""22. Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función reduce()."""

def ejercicio22():
    numeros = [2,3,4,5]
    producto = reduce(lambda x, y: x*y, numeros)
    print (f'Resultado ejercicio 22: {producto}')

"""23. Concatena una lista de palabras.Usa la función reduce()."""

def ejercicio23():
    palabras = ["Me", "encanta", "la", "playa"]
    resultado = reduce(lambda x, y: x + " " + y, palabras)
    print (f'Resultado ejercicio 23: {resultado}')

"""24. Calcula la diferencia total en los valores de una lista. Usa la función reduce()."""

def ejercicio24():
    lista = [10, 3, 5, 2]
    #Utilizamos el módulo operator.sub() para que el operador reste los valores
    diferencia_total = reduce(operator.sub, lista)
    print (f'Resultado ejercicio 24: {diferencia_total}')

"""25. Crea una función que cuente el número de caracteres en una cadena de texto dada."""

def ejercicio25():
    def contar_caracteres(cadena):
        return sum(1 for _ in cadena)
    texto = "Python es divertido"
    resultado = contar_caracteres(texto)
    print (f'Resultado ejercicio 25: {resultado}') #Incluye espacios y letras ya que el enunciado indica contar caracteres, no letras

"""26. Crea una función lambda que calcule el resto de la división entre dos números dados."""

def ejercicio26():
    resto = lambda x, y: x % y
    resultado = resto (17, 5)
    print (f'Resultado ejercicio 26: {resultado}')

    
"""27. Crea una función que calcule el promedio de una lista de números."""

def ejercicio27():
    def calcular_promedio(lista):
        return statistics.mean(lista)

    numeros = [4,7,9,10]
    resultado = calcular_promedio(numeros)
    print (f'Resultado ejercicio 27: {resultado}')

"""28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada."""

def ejercicio28():
    def primer_duplicado(lista):
        vistos = set()
        for elemento in lista:
            if elemento in vistos: #Si el elemento ya estaba en vistos, es el primer duplicado y lo devolvemos.
                return elemento
            vistos.add(elemento) #Si no, lo añadimos al set.
        return None #Si no hay duplicados

    datos = [3,1,4,2,5,1,6]
    resultado = primer_duplicado(datos)
    print (f'Resultado ejercicio 28: {resultado}')

"""29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el
carácter '#', excepto los últimos cuatro."""

def ejercicio29():
    def enmascarar(variable):
        texto = str(variable)
        if len(texto) <=4:
            return texto
        return '#' * (len(texto) - 4) + texto[-4:]
    secreto = 123456789
    resultado = enmascarar(secreto)
    print (f'Resultado ejercicio 29: {resultado}')

"""30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras
pero en diferente orden."""

def ejercicio30():
    def son_anagramas(palabra1, palabra2):
        p1 = palabra1.replace(" ", "").lower()
        p2 = palabra2.replace(" ", "").lower()
        return Counter(p1) == Counter(p2)
    resultado = son_anagramas("Roma", "amor")
    print (f'Resultado ejercicio 30: {resultado}')

"""31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en
esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se
lanza una excepción."""

def ejercicio31():
    class NombreNoEncontrado(Exception):
        pass
    try: 
        entrada = input ("Introduce una lista de nombres separados por comas:").strip()
        lista_nombres = [nombre.strip().lower() for nombre in entrada.split(",") if nombre.strip()]
        if not lista_nombres:
            raise ValueError("La lista está vacía. Debes introducir al menos un nombre.")
        nombre_a_buscar = input("Introduce el nombre que quieres buscar: ").strip().lower()
        if nombre_a_buscar in lista_nombres:
            print(f"✅ El nombre '{nombre_a_buscar}' fue encontrado en la lista.")
        else: 
            raise NombreNoEncontrado (f"❌ El nombre '{nombre_a_buscar}' no se encuentra en la lista.")
    except NombreNoEncontrado as e:
        print(e)
    except Exception as e:
        print(f"⚠️ Error: {e}")

"""32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y
devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona
no trabaja aquí."""

def ejercicio32():
    def obtener_puesto(nombre_completo, empleados_dict):
        puesto = empleados_dict.get(nombre_completo.lower())
        if puesto:
            return f"📌 Puesto de {nombre_completo}: {puesto}"
        else:
            return f"❌ {nombre_completo} no trabaja aquí."
    empleados_dict = {
        "ana garcía": "Analista",
        "luis pérez": "Desarrollador",
        "marta ruiz": "Project Manager",
    }
    nombre = input("Introduce el nombre completo del empleado: ").strip()
    print ('Resultado ejercicio 32:', obtener_puesto(nombre,empleados_dict))

"""33. Crea una función lambda que sume elementos correspondientes de dos listas dadas."""

def ejercicio33():
    lista1 = [1, 2, 3, 4]
    lista2= [10, 20, 30, 40]

    resultado = list(map(lambda x, y: x+y, lista1, lista2))
    print (f'Resultado ejercicio 33: {resultado}')

"""34. Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son:
crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . El objetivo es implementar estos métodos para
manipular la estructura del árbol.
Código a seguir:
1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
2. Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
3. Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
4. Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
5. Implementar el método quitar_rama para eliminar una rama en una posición específica.
6. Implementar el método
info_arbol para devolver información sobre la longitud del tronco, el número de ramas y las longitudes de las
mismas.
Caso de uso:
1. Crear un árbol.
2. Hacer crecer el tronco del árbol una unidad.
3. Añadir una nueva rama al árbol.
4. Hacer crecer todas las ramas del árbol una unidad.
5. Añadir dos nuevas ramas al árbol.
6. Retirar la rama situada en la posición 2.
7. Obtener información sobre el árbol."""
def ejercicio34():
    class Arbol:
        def __init__(self):
            #Inicializamos el tronco en longitud 1 y lista de ramas vacía
            self.tronco = 1
            self.ramas = []
        def crecer_tronco(self):
            #Aumenta en 1 la longitud del tronco
            self.tronco += 1
        def nueva_rama(self):
            #Agrega una nueva rama de longitud 1
            self.ramas.append(1)
        def crecer_ramas(self):
            #Aumenta en 1 la longitud de toddas las ramas existentes
            self.ramas = [rama + 1 for rama in self.ramas]
        def quitar_rama(self, posicion):
            #Elimina la rama en una posición específica
            if 1 <= posicion <= len(self.ramas):
                self.ramas.pop(posicion - 1)
            else:
                print ("Aviso: Posición inválida. No existe esa rama.")
        def info_arbol(self):
            #Devuelve la información general del árbol
            return {
                "longitud_tronco": self.tronco,
                "numero_ramas": len(self.ramas),
                "longitudes_ramas": self.ramas
            }
        def __str__(self):
            return (
                f'Arbol → Tronco: {self.tronco}|'
                f'Ramas ({len(self.ramas)}): {self.ramas}'
            )
        # Caso de uso
    arbol = Arbol()                   # 1. Crear un árbol
    arbol.crecer_tronco()             # 2. Crece el tronco
    arbol.nueva_rama()                # 3. Añade una nueva rama
    arbol.crecer_ramas()              # 4. Crece todas las ramas
    arbol.nueva_rama()                # 5. Añade dos ramas más
    arbol.nueva_rama()
    arbol.quitar_rama(2)              # 6. Quita la rama en la posición 2
    resultado = arbol.info_arbol()    # 7. Obtén la info
    
    print (f'Resultado ejercicio 34: {resultado}')
    print(arbol)

"""35. Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta
corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y
agregar dinero al saldo.
Código a seguir:
1. Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante True y False .
2. Implementar el método retirar_dinero para retirar dinero del saldo del usuario. Lanzará un error en caso de no
poder hacerse.
3. Implementar el método transferir_dinero para realizar una transferencia desde otro usuario al usuario actual.
Lanzará un error en caso de no poder hacerse.
4. Implementar el método agregar_dinero para agregar dinero al saldo del usuario.
Caso de uso:
1. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
PROYECTO LÓGICA: Katas de Python 3
2. Agregar 20 unidades de saldo de "Bob".
3. Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".
4. Retirar 50 unidades de saldo a "Alicia"."""

def ejercicio35():
    class UsuarioBanco:
        def __init__(self, nombre, saldo, cuenta_corriente=True):
            self.nombre = nombre
            self.saldo = saldo
            self.cuenta_corriente = cuenta_corriente

        def retirar_dinero(self, cantidad):
            """Resta dinero del saldo si es posible"""
            if not self.cuenta_corriente:
                raise Exception(f"{self.nombre} no tiene cuenta corriente activa.")
            if cantidad <= 0:
                raise ValueError("La cantidad a retirar debe ser positiva.")
            if cantidad > self.saldo:
                raise Exception(f"Fondos insuficientes en la cuenta de {self.nombre}.")
            self.saldo -= cantidad
            print(f"💸 {self.nombre} retiró {cantidad}. Saldo actual: {self.saldo}")

        def transferir_dinero(self, otro_usuario, cantidad):
            """Transfiere dinero desde otro usuario hacia este usuario"""
            if not otro_usuario.cuenta_corriente or not self.cuenta_corriente:
                raise Exception("Ambos usuarios deben tener cuenta corriente activa.")
            if cantidad <= 0:
                raise ValueError("La cantidad a transferir debe ser positiva.")
            if cantidad > otro_usuario.saldo:
                raise Exception(f"{otro_usuario.nombre} no tiene fondos suficientes para transferir.")
            
            otro_usuario.saldo -= cantidad
            self.saldo += cantidad
            print(f"🔄 Transferidos {cantidad} de {otro_usuario.nombre} a {self.nombre}.")

        def agregar_dinero(self, cantidad):
            """Agrega dinero al saldo"""
            if cantidad <= 0:
                raise ValueError("La cantidad a agregar debe ser positiva.")
            self.saldo += cantidad
            print(f"💰 {self.nombre} agregó {cantidad}. Saldo actual: {self.saldo}")

        def __str__(self):
            return f"👤 {self.nombre} | Saldo: {self.saldo} | Cuenta corriente: {self.cuenta_corriente}"

    # Caso de uso
    alicia = UsuarioBanco("Alicia", 100, True)
    bob = UsuarioBanco("Bob", 50, True)

    print(alicia)
    print(bob)

    # 1. Bob agrega 20
    bob.agregar_dinero(20)

    # 2. Transferencia de 80 desde Bob hacia Alicia con manejo de error
    try:
        alicia.transferir_dinero(bob, 80)
    except Exception as e:
        print(f"⚠️ Error en la transferencia: {e}")

    # 3. Alicia retira 50
    try:
        alicia.retirar_dinero(50)
    except Exception as e:
        print(f"⚠️ Error en el retiro: {e}")

    # Estado final
    print("\n📊 Estado final:")
    print(alicia)
    print(bob)

"""36. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras ,
reemplazar_palabras , eliminar_palabra . Estas opciones son otras funciones que tenemos que definir primero y llamar dentro
de la función procesar_texto .
Código a seguir:
1. Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto. Tiene
que devolver un diccionario.
2. Crear una función reemplazar_palabras para remplazar una palabra_original del texto por una palabra_nueva . Tiene
que devolver el texto con el remplazo de palabras.
3. Crear una función eliminar_palabra para eliminar una palabra del texto. Tiene que devolver el texto con la palabra
eliminada.
4. Crear la función procesar_texto que tome un texto, una opción(entre "contar", "reemplazar", "eliminar") y un
número de argumentos variable según la opción indicada."""
def ejercicio36():
    # 1. Función para contar palabras
    def contar_palabras(texto):
        palabras = texto.split()
        conteo = {}
        for palabra in palabras:
            conteo[palabra] = conteo.get(palabra, 0) + 1
        return conteo

    # 2. Función para reemplazar palabras
    def reemplazar_palabras(texto, palabra_original, palabra_nueva):
        return texto.replace(palabra_original, palabra_nueva)

    # 3. Función para eliminar una palabra
    def eliminar_palabra(texto, palabra):
        palabras = texto.split()
        palabras_filtradas = [p for p in palabras if p != palabra]
        return " ".join(palabras_filtradas)

    # 4. Función procesadora
    def procesar_texto(texto, opcion, *args):
        if opcion == "contar":
            return contar_palabras(texto)
        elif opcion == "reemplazar":
            if len(args) != 2:
                raise ValueError("Debes proporcionar palabra_original y palabra_nueva")
            return reemplazar_palabras(texto, args[0], args[1])
        elif opcion == "eliminar":
            if len(args) != 1:
                raise ValueError("Debes proporcionar la palabra a eliminar")
            return eliminar_palabra(texto, args[0])
        else:
            raise ValueError("Opción no válida. Usa: 'contar', 'reemplazar' o 'eliminar'.")

    # --------------------------
    # Caso de uso
    # --------------------------
    texto = "el gato y el perro juegan con el gato"

    print("📘 Texto original:", texto)

    # 1. Contar palabras
    resultado1 = procesar_texto(texto, "contar")
    print("🔹 Contar palabras:", resultado1)

    # 2. Reemplazar palabras
    resultado2 = procesar_texto(texto, "reemplazar", "gato", "conejo")
    print("🔹 Reemplazar palabras:", resultado2)

    # 3. Eliminar palabra
    resultado3 = procesar_texto(texto, "eliminar", "perro")
    print("🔹 Eliminar palabra:", resultado3)

"""37. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario"""
def ejercicio37():
    try:
        hora_str = input("⏰ ¿Qué hora es? (formato HH:MM): ").strip()

        # Validar formato HH:MM
        if ":" not in hora_str:
            print("❌ Formato incorrecto. Usa HH:MM (ejemplo: 09:45).")
            return

        partes = hora_str.split(":")
        if len(partes) != 2:
            print("❌ Formato incorrecto. Usa HH:MM (ejemplo: 09:45).")
            return

        horas, minutos = partes

        # Convertir a enteros
        horas = int(horas)
        minutos = int(minutos)

        # Validaciones de rango
        if not (0 <= horas <= 23 and 0 <= minutos <= 59):
            print("❌ Error: La hora debe estar entre 00:00 y 23:59.")
            return

        # Clasificación
        if 6 <= horas < 12:
            print(f"🌅 Es por la mañana ({hora_str}).")
        elif 12 <= horas < 20:
            print(f"🌇 Es por la tarde ({hora_str}).")
        else:
            print(f"🌙 Es por la noche ({hora_str}).")

    except ValueError:
        print("❌ Error: Debes introducir la hora en formato HH:MM con números válidos.")

"""38. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica.
Las reglas de calificación son:
- 0 - 69 insuficiente
- 70 - 79 bien
- 80 - 89 muy bien
- 90 - 100 excelente"""
def ejercicio38():
    try:
        nota = int(input("📊 Introduce la calificación numérica (0-100): ").strip())

        if not (0 <= nota <= 100):
            print("❌ Error: La calificación debe estar entre 0 y 100.")
            return

        reglas = {
            "insuficiente": range(0, 70),
            "bien": range(70, 80),
            "muy bien": range(80, 90),
            "excelente": range(90, 101)
        }

        for texto, rango in reglas.items():
            if nota in rango:
                print(f"Resultado: {texto}")
                break
    except ValueError:
        print("❌ Error: Debes introducir un número entero válido.")
"""39. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo" , "circulo" o
"triangulo" ) y datos (una tupla con los datos necesarios para calcular el área de la figura)."""

def ejercicio39():
    def calcular_area(figura, datos):
        figura = figura.lower()

        if figura == "rectangulo":
            base, altura = datos
            return base * altura
        elif figura == "circulo":
            (radio,) = datos
            return math.pi * radio ** 2
        elif figura == "triangulo":
            base, altura = datos
            return (base * altura) / 2
        else:
            raise ValueError("Figura no reconocida. Usa rectangulo, circulo o triangulo.")

    # Casos de uso
    print("Área rectángulo:", calcular_area("rectangulo", (10, 5)))
    print("Área círculo:", calcular_area("circulo", (7,)))
    print("Área triángulo:", calcular_area("triangulo", (6, 4)))

"""40. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el
monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo
siguiente:
1. Solicita al usuario que ingrese el precio original de un artículo.
2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor
a cero). Por ejemplo, descuento de 15€.
5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él.
6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu
programa de Python."""

def ejercicio40():
    try:
        # 1️⃣ Solicitar precio original
        precio_original = float(input("💰 Introduce el precio original del artículo (€): ").strip())

        # Validación de precio
        if precio_original <= 0:
            print("❌ El precio debe ser mayor que 0.")
            return

        # 2️⃣ Preguntar si tiene cupón
        tiene_cupon = input("🎟️ ¿Tienes un cupón de descuento? (sí/no): ").strip().lower()

        # 3️⃣ Si responde 'sí', solicitar valor del cupón
        if tiene_cupon in ["sí", "si", "s"]:
            try:
                valor_cupon = float(input("🏷️ Introduce el valor del cupón (€): ").strip())
                if valor_cupon <= 0:
                    print("⚠️ El cupón no es válido. No se aplicará descuento.")
                    precio_final = precio_original
                elif valor_cupon >= precio_original:
                    print("⚠️ El cupón no puede ser mayor o igual al precio original.")
                    precio_final = precio_original
                else:
                    precio_final = precio_original - valor_cupon
                    print(f"✅ Descuento aplicado: {valor_cupon:.2f}€")
            except ValueError:
                print("❌ Valor del cupón no válido. No se aplicará descuento.")
                precio_final = precio_original

        # 4️⃣ Si responde 'no'
        elif tiene_cupon in ["no", "n"]:
            precio_final = precio_original
            print("ℹ️ No se aplicó ningún descuento.")

        # 5️⃣ Si responde algo distinto
        else:
            print("❌ Respuesta no válida. Se asume que no hay cupón.")
            precio_final = precio_original

        # 6️⃣ Mostrar resultado final
        print(f"💳 Precio final de la compra: {precio_final:.2f}€")

    except ValueError:
        print("❌ Error: Debes introducir un número válido para el precio.")

ejercicios = { 
    str(i): globals()[f"ejercicio{i}"]
    for i in range(1, 41)  # del 1 al 40 incluido
    if f"ejercicio{i}" in globals()
}


#Menu Interactivo
def main():
    while True:
        print("\n📘 MENÚ DE EJERCICIOS")
        for k in sorted(ejercicios, key=int):
            print(f"{k}. Ejercicio {k}")
        print("0. Salir")

        opcion = input("Selecciona un ejercicio (1-40) o 0 para salir: ").strip()

        if opcion in ("0", "salir", "SALIR"):
            print("👋 ¡Hasta pronto!")
            break
        elif opcion in ejercicios:
            print()
            ejercicios[opcion]()  # Ejecuta el ejercicio correspondiente
        else:
            print("❌ Opción no válida. Intenta con un número del 1 al 40.")

# Punto de entrada
if __name__ == "__main__":
    main()

