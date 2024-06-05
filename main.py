def ler_nivel_agua(index):
    nivel_agua = [15, 30, 85, 70, 55, 45, 20, 95, 50, 40]
    return nivel_agua[index]

def ler_ph(index):
    valor_do_ph = [6.5, 7.0, 8.5, 7.2, 6.8, 7.5, 6.0, 8.0, 7.1, 6.9]
    return valor_do_ph[index]

def conta_peixes(index):
    contagem_peixes = [2, 5, 8, 6, 4, 3, 1, 9, 7, 10]
    return contagem_peixes[index]

for i in range(10):
    nivel_agua = ler_nivel_agua(i)
    valor_do_ph = ler_ph(i)
    contagem_peixes = conta_peixes(i)

    if nivel_agua < 20:
        status_da_agua = "Baixo"
    elif 20 <= nivel_agua <= 80:
        status_da_agua = "Normal"
    else:
        status_da_agua = "Alto"

    if valor_do_ph < 7:
        status_do_ph = "Ácido"
    elif valor_do_ph == 7:
        status_do_ph = "Neutro"
    else:
        status_do_ph = "Alcalino"

    if contagem_peixes < 3:
        status_dos_peixes = "Poucos Peixes"
    elif 3 <= contagem_peixes <= 7:
        status_dos_peixes = "Quantidade Adequada"
    else:
        status_dos_peixes = "Muitos Peixes"

    print(f"Nível de Água: {nivel_agua:.2f}% - Status: {nivel_agua}")
    print(f"pH da Água: {valor_do_ph:.2f} - Status: {status_do_ph}")
    print(f"Quantidade de Peixes: {contagem_peixes} - Status: {status_dos_peixes}")
    print("-" * 40)
