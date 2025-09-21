dict_test = {}

"""def mostrar_perritos(dogs: list) -> dict:
    global dict_test
    count_dogs = 0
    for element in dogs:
        # print(element)
        for key in element.keys():
            count_dogs += 1
            print(f'Perrito [{count_dogs}]->{key}')
            # dict_test["name"] = key
    return dict_test"""
def mostrar_perritos(dogs: list):
    count_dogs = 0
    if len(dogs) == 0:
        print('No hay perritos por el momento!!')
    else:
        for element in dogs:
            # print(element)
            for key in element.keys():
                count_dogs += 1
                print(f'Perrito [{count_dogs}]->{key}')
                # dict_test["name"] = key

def address_dogs(dogs: list):
    for element in dogs:
        name = input("Enter your dog name: ")
        color = input("Enter your dog color: ")
        disponibilidad = input("Enter your availability: ")
        atention_dis = True if disponibilidad == "SI" else False
        años = int(input("Enter your years: "))
        raza = input("Enter your race dog: ")

        element[name] = {
            "color": color,
            "disponibilidad": atention_dis,
            "años": años,
            "raza": raza
        }
        for key in element.keys():
            print(f'Nuevo perrito agregado {key}')

def show_dogs(dog: list):
    count_dogs = 0
    for element in dog:
        for key in element.keys():
            count_dogs += 1
            print(f'Perrito [{count_dogs}]->{key}')
            # dict_test["name"] = key
