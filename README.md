#  Sistema de Gestión de Biblioteca Digital

## Programación Avanzada – Trabajo Práctico Final

**Universidad Nacional Guillermo Brown**
**Licenciatura en Ciencia de Datos**

---

## Descripción del proyecto

Este proyecto consiste en el desarrollo de un **Sistema de Gestión de Biblioteca Digital** implementado en **Python** utilizando los principios de la **Programación Orientada a Objetos (POO)**.

El sistema permite administrar libros, usuarios y préstamos, aplicando conceptos avanzados de programación como herencia, polimorfismo, composición, agregación, decoradores, metaclases y el patrón de diseño Singleton.

---

## Funcionalidades

### Gestión de Libros

* Alta de libros.
* Listado de libros registrados.

### Gestión de Usuarios

* Alta de usuarios.
* Modificación de correo electrónico.
* Baja de usuarios.
* Listado de usuarios.

### Gestión de Préstamos

* Registro de préstamos.
* Registro de devoluciones.
* Validación para impedir prestar un libro que ya posee un préstamo activo.

---

## Conceptos de Programación Avanzada implementados

### Herencia

Se implementó una jerarquía donde la clase **Usuario** hereda de la clase **Persona**.

### Polimorfismo

La clase **Usuario** redefine el método `mostrar_perfil()` heredado de `Persona`, mostrando información específica del usuario.

### Agregación

La clase **Biblioteca** mantiene una colección de objetos **Libro**, cuyos ciclos de vida son independientes de la biblioteca.

También la clase **GestorUsuarios** administra una colección de objetos **Usuario**.

### Composición

La clase **Usuario** posee un objeto **Cuenta**, cuya existencia depende completamente del usuario.

Además, la clase **Biblioteca** contiene los registros de **Préstamo**, los cuales forman parte de su composición.

### Decorador propio

Se implementó el decorador `validar_disponibilidad`, encargado de impedir que un libro pueda prestarse cuando ya posee un préstamo activo.

### Metaclase

Se implementó la metaclase `MetaValidadora`, encargada de verificar que las clases derivadas implementen el método `mostrar_perfil()`.

### Patrón de Diseño

Se implementó el patrón **Singleton** mediante la metaclase `SingletonMeta`, garantizando que exista una única instancia de la clase **Biblioteca** durante toda la ejecución del sistema.

---

## Estructura principal del proyecto

```text
Proyecto/
│
├── main.py
├── README.md
├── uml.png (o uml.pdf)
└── demás archivos del proyecto
```

---

## Requisitos

* Python 3.10 o superior.

---

## Ejecución del proyecto

1. Clonar el repositorio.

```bash
git clone (https://github.com/romydelperal/Sistema-de-Gestion-de-Biblioteca-Digital)
```

2. Ingresar a la carpeta del proyecto.

```bash
cd nombre_del_proyecto
```

3. Ejecutar el programa principal.

```bash
python main.py
```

---

## Tecnologías utilizadas

* Python 3
* Programación Orientada a Objetos
* Git
* GitHub

---

## Grupo

Grupo 13 

## Integrantes

* del Peral Acevedo Paola Romina
* Dodero Leonel Ivan

---

## Docente

Repositorio compartido con el usuario **compudiego**, según los requisitos del trabajo práctico.
