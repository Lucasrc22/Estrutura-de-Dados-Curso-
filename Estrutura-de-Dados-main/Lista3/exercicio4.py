def tem_par_com_soma(arr, soma_objetivo):
    vistos = set()

    for num in arr:
        complemento = soma_objetivo - num
        if complemento in vistos:
            return True
        vistos.add(num)

    return False


arr = [10, 15, 3, 7]
soma_objetivo = 17
resultado = tem_par_com_soma(arr, soma_objetivo)
print("Par encontrado:", resultado)
