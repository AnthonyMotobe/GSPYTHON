opc_binario = ["S", "N"]
opc_pesquisas = [
  {
    "nome": "Fossa de Leviathan",
    "pH": 6.5,
    "movimento_peixes": 42,
    "temperatura": 25
  },
  {
    "nome": "Jardim de Poseidon",
    "pH": 7.2,
    "movimento_peixes": 38,
    "temperatura": 28
  },
  {
    "nome": "Caldeira de Vulcano",
    "pH": 5.8,
    "movimento_peixes": 23,
    "temperatura": 22
  },
  {
    "nome": "Ilha da Aurora",
    "pH": 6.7,
    "movimento_peixes": 56,
    "temperatura": 26
  },
  {
    "nome": "Mar de Sirenas",
    "pH": 8.0,
    "movimento_peixes": 64,
    "temperatura": 21
  },
  {
    "nome": "Baía dos Kraken",
    "pH": 5.5,
    "movimento_peixes": 31,
    "temperatura": 30
  },
  {
    "nome": "Triângulo das Bermudas",
    "pH": 6.1,
    "movimento_peixes": 45,
    "temperatura": 24
  },
  {
    "nome": "Mar de Netuno",
    "pH": 7.4,
    "movimento_peixes": 29,
    "temperatura": 27
  },
  {
    "nome": "Arquipélago dos Corais",
    "pH": 5.9,
    "movimento_peixes": 52,
    "temperatura": 23
  },
  {
    "nome": "Estreito de Andrômeda",
    "pH": 6.3,
    "movimento_peixes": 60,
    "temperatura": 25
  }
]

def validadorBinario(selecao, mensagem):
    validador = selecao
    while not validador.upper() in opc_binario:
        validador = input(mensagem)
    return validador.upper()

def entrar():
    selecao = input("Você deseja acessar o sistema? (S/N): ")
    binario = validadorBinario(selecao, "Opção inválida! Por favor, digite 'S' para sim ou 'N' para não: ")

    if binario in opc_binario:
        if binario == "S":
            print("Acessando o sistema...\n")
            inicializador()
        else:
            print("Obrigado por acessar a plataforma DMO!")

def validadorNumerico(selecao, mensagem):
    validador = selecao
    while not validador.isnumeric():
        validador = input(mensagem)
    validador = int(validador)
    return validador

def validadorSelecao(numero, mensagem):
    validador = numero
    while not 0 <= validador <= len(opc_pesquisas) - 1:
        validador = input(mensagem)
        validacao = validadorNumerico(validador, "Opção inválida! Por favor, digite um número: ")
        validador = validacao
    validador = int(validador)
    return validador

def status(ph, movimento_peixes, temperatura):
    if ph < 7:
        status_do_ph = "Ácida"
    elif ph == 7:
        status_do_ph = "Neutra"
    else:
        status_do_ph = "Alcalina"

    if movimento_peixes < 3:
        status_dos_peixes = "Poucos Peixes"
    elif 3 <= movimento_peixes <= 7:
        status_dos_peixes = "Quantidade Razóavel"
    else:
        status_dos_peixes = "Quantidade Saudável"

    if temperatura < 25:
        status_da_temperatura = "Baixa"
    elif 25 <= temperatura <= 28:
        status_da_temperatura = "Normal"
    else:
        status_da_temperatura = "Alta"

    return {"ph": status_do_ph, "peixes": status_dos_peixes, "temperatura": status_da_temperatura}

def inicializador():
    print("Que bom que está aqui. Vamos começar!\n")
    while True:
        contagem = -1
        string = "\nPara selecionar uma opção, digite o número correspondente:\n"
        for pesquisa in opc_pesquisas:
            contagem += 1
            string = string + f"{contagem}) {pesquisa['nome']} \n"
        string = string + "->"
        selecao = input(string)
        numeroSelec = validadorNumerico(selecao, "Opção inválida! Por favor, digite um número: ")
        numeroFinal = validadorSelecao(numeroSelec, f"Opção inválida! Por favor, digite um número de 0 a {len(opc_pesquisas) - 1}: ")

        statusPesquisa = status(opc_pesquisas[numeroFinal]['pH'], opc_pesquisas[numeroFinal]['movimento_peixes'], opc_pesquisas[numeroFinal]['temperatura'])

        print("\nSeleção realizada com sucesso!\n"
              "Aqui estão os dados da sua pesquisa:\n")

        print(f"Nome da Pesquisa: {opc_pesquisas[numeroFinal]['nome']}\n"
              f"pH da Água: {opc_pesquisas[numeroFinal]['pH']} - {statusPesquisa['ph']}\n"
              f"Movimentação dos Peixes: {opc_pesquisas[numeroFinal]['movimento_peixes']} - {statusPesquisa['peixes']}\n"
              f"Temperatura da Água: {opc_pesquisas[numeroFinal]['temperatura']}°C - {statusPesquisa['temperatura']}\n")

        continuar = input("Deseja pesquisar mais? (S/N): ")
        binario = validadorBinario(continuar, "Opção inválida! Por favor, digite 'S' para sim ou 'N' para não: ")

        if binario == "N":
            print("Obrigado por acessar a plataforma DMO!")
            break

print("Seja bem vindo à plataforma DMO!")
entrar()
