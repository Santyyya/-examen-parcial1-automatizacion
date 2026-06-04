# -*- coding: utf-8 -*-

def main():
    nombre = "Santiago Alejandro Ortega Yañez"
    comandos_favoritos = [
        "git status - Muestra el estado del directorio de trabajo y del área de preparación.",
        "git log - Despliega el historial completo de commits realizados en la rama actual.",
        "git branch - Permite listar, crear o eliminar ramas dentro del repositorio."
    ]
    
    print(f"Nombre del estudiante: {nombre}")
    print("\nMis 3 comandos de Git favoritos:")
    for i, comando in enumerate(comandos_favoritos, 1):
        print(f"{i}. {comando}")

if __name__ == "__main__":
    main()
