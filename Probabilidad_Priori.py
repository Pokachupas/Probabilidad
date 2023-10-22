
def probabilidad_a_priori(numero_dado):
    # Suponemos que hay 6 caras en un dado estándar.
    numero_posibilidades = 6

    # La probabilidad a priori de cada número es igual.
    probabilidad_individual = 1 / numero_posibilidades

    return probabilidad_individual

numero_deseado = 4  # Cambia esto al número de interés
prob_a_priori = probabilidad_a_priori(numero_deseado)

print(f"Probabilidad a priori de obtener el número {numero_deseado} en el próximo lanzamiento: {prob_a_priori}")