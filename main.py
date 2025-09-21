# Examples from today
# Brindar un programa que permita verificar el ingreso de un usuario y su contraseña
# para acceder al sistema. Además, crear un menú para agregar nuevos animales al Albergue
# "Patittas unidas con un menú de opciones" --> Los perritos dentro del albergue, añadir un
# perrito, mostrar actuales y salida del sistema.
from idlelib.sidebar import EndLineDelegator

from optionsF import mostrar_perritos, address_dogs, show_dogs

USER, PASSWORD = "alex", "alex123"
count = 0
exit_system = False

def verify_user(user, password):
    global count
    while count < 3:
        if (user == "" or user != USER) or (password == "" or password != PASSWORD):
            print(f'The user or password is incorrect!! :(')
            user = input("Enter your user: ")
            password = input("Enter your password: ")
            count += 1
            if count >= 3:
                print("Fallaste los 3 intentos")
                return False
        else:
            break
            # return False
    print('Bienvenido al sistema')
    return True

if __name__ == "__main__":
    username_system = input("Enter your user: ")
    password_system = input("Enter your password: ")
    access_system = verify_user(username_system, password_system)
    print(access_system)

    # List of the Dogs in the Hostel PATITAS UNIDAS
    dogs_list = [
        {
            "Leonardo": {
                "color": "marrón",
                "disponibilidad": True,
                "años": 5,
                "raza": "Pequines"
            },
            "Lina": {
                "color": "blanco",
                "disponibilidad": True,
                "años": 3,
                "raza": "Salchicha"
            }
        }
    ]

    while not exit_system:
        option_system = input("""------- PATITAS UNIDAS -------
        [A]-Mostrar perritos
        [B]-Añadir un perrito nuevo rescatado
        [C]-Lista actual de perritos
        [D]-Salir
        Selecciona tu opción --> """)

        if option_system.upper() == "A":
            print('------ Perritos dentro del albergue (today) ------')
            # show = mostrar_perritos(dogs_list)
            mostrar_perritos(dogs_list)
            """for i in show.values():
                print(i)"""
        elif option_system.upper() == "B":
            print('------ AÑADIR UN PERRITO NUEVO -----')
            address_dogs(dogs_list)
            # print(new_list)
        elif option_system.upper() == "C":
            print('------ LISTA ACTUAL DE PERRITOS --------')
            show_dogs(dogs_list)
        elif option_system.upper().split() == "D":
            print(f'Saliendo del sistema')
            exit_system = False
            break
        else:
            print("Error al ingresar letra")