def diagnostico(cidadaos, sintomas, diagnosticos):
    cpfexiste = 0
    print("\nAgora vamos iniciar seu diagnostico.")
    print("Digite seu CPF:")
    cpf = int(input())
    for chave in cidadaos:
        if cpf == chave:
            cpfexiste = 1
            if len(sintomas) < 1:
                print("\nNão há sintomas cadastrados...\n")
            else:
                diagnosticos[cpf] = {}
                print("Responda as perguntas abaixo.")
                for chavsintomas in sintomas:
                    print(f"{sintomas.get(chavsintomas)}")
                    resp = input()
                    respup = resp.upper()
                    diagnosticos[cpf][sintomas.get(chavsintomas)] = respup
    if cpfexiste == 0:
        print("CPF nao cadastrado...\n")
