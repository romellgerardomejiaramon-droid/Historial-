
import time

class Pila:
    def __init__(self):
        self.elementos = []

    def apilar(self, sitio):
        self.elementos.append(sitio)

    def desapilar(self):
        if self.esta_vacia():
            return None
        return self.elementos.pop()

    def cima(self):
        if self.esta_vacia():
            return None
        return self.elementos[-1]

    def esta_vacia(self):
        return len(self.elementos) == 0

    def mostrar(self):
        print("\n--- PILA DEL HISTORIAL ---")

        if self.esta_vacia():
            print("|       Vacia       |")
        else:
            for sitio in reversed(self.elementos):
                print("| " + sitio + " |")

        print("--------------------------")


def main():
    historial = Pila()
    tiempo_total = 0

    while True:
        print("\n===== HISTORIAL DEL NAVEGADOR =====")
        print("1. Visitar un sitio")
        print("2. Regresar al sitio anterior")
        print("3. Ver sitio actual")
        print("4. Mostrar historial completo")
        print("5. Salir")

        opcion = input("Elige una opcion: ").strip()

        if opcion == "5":
            print("\nPrograma finalizado")
            print("Tiempo total de ejecucion: {:.9f} segundos".format(tiempo_total))
            print("Fin del programa")
            break

        sitio = ""

        if opcion == "1":
            sitio = input("Ingresa la direccion del sitio: ")

        inicio = time.perf_counter()

        if opcion == "1":
            if sitio.strip() != "":
                historial.apilar(sitio.strip())
                print("\nSitio agregado al historial")
                historial.mostrar()
            else:
                print("La direccion no puede estar vacia")

        elif opcion == "2":
            sitio_anterior = historial.desapilar()

            if sitio_anterior is None:
                print("No hay sitios para regresar")
            else:
                print("Regresaste desde:", sitio_anterior)

                if historial.esta_vacia():
                    print("No hay un sitio anterior")
                else:
                    print("Sitio actual:", historial.cima())

                historial.mostrar()

        elif opcion == "3":
            sitio_actual = historial.cima()

            if sitio_actual is None:
                print("No hay ningun sitio abierto")
            else:
                print("Sitio actual:", sitio_actual)

        elif opcion == "4":
            historial.mostrar()

        else:
            print("Opcion invalida")

        fin = time.perf_counter()
        tiempo_operacion = fin - inicio
        tiempo_total += tiempo_operacion

        print("Tiempo de la operacion: {:.9f} segundos".format(tiempo_operacion))


if __name__ == "__main__":
    main()
