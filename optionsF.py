dict_test = {}

def mostrar_perritos(dogs: list) -> dict:
    global dict_test
    for element in dogs:
        # print(element)
        for key, value in element.items():
            dict_test["name"] = key
    return dict_test