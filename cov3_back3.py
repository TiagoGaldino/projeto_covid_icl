def filtrox(cidadaos, sintomas, diagnosticos):
    contsin = {}
    contsex = {}
    contfxe = {}
    contfiltro = {}
    tamcid = len(cidadaos)
    tamsin = len(sintomas)
    if tamcid < 1:
        print("Não há base de dados para gerar relatórios")
    else:
        for chave in cidadaos:
            subdic = cidadaos.get(chave)
            for subchave in subdic:
                if subchave == "Sexo":
                    contsex[subdic.get(subchave)] = {}
                if subchave == "Fx_Etária":
                    contfxe[subdic.get(subchave)] = {}

        for chave in cidadaos:
            subdic = cidadaos.get(chave)
            for subchave in subdic:
                if subchave == "Sexo":
                    contsex[subdic.get(subchave)][chave] = subdic.get("Nome")
                if subchave == "Fx_Etária":
                    contfxe[subdic.get(subchave)][chave] = subdic.get("Nome")

        for chave4 in contsex:
            subdic4 = contsex.get(chave4)
            print(f"\nFiltro: {chave4}")
            for subchave4 in subdic4:
                print(subchave4)

        for chave6 in contfxe:
            subdic6 = contfxe.get(chave6)
            print(f"\nFiltro: {chave6}")
            for subchave6 in subdic6:
                print(subchave6)

        for chave1 in contsex:
            subdic1 = contsex.get(chave1)
            for subchave1 in subdic1:
                for chave2 in contfxe:
                    subdic2 = contfxe.get(chave2)
                    for subchave2 in subdic2:
                        if subchave1 == subchave2:
                            contfiltro[chave1+"-"+chave2] = {}

        for chave1 in contsex:
            subdic1 = contsex.get(chave1)
            for subchave1 in subdic1:
                for chave2 in contfxe:
                    subdic2 = contfxe.get(chave2)
                    for subchave2 in subdic2:
                        if subchave1 == subchave2:
                            contfiltro[chave1+"-"+chave2][subchave1] = "OK"

        for chave in contfiltro:
            subdic = contfiltro.get(chave)
            print(f"\nFiltro Cruzado:{chave}")
            for subchave in subdic:
                print(subchave)


def consolida_cid(cidadaos):
    contsexo = {}
    contfxet = {}
    tamcid = len(cidadaos)
    if tamcid < 1:
        print("\nNão há Cidadãos Cadastrados...\n")
    else:
        for chave in cidadaos:
            subdic = cidadaos.get(chave)
            for subchave in subdic:
                if subchave == "Sexo":
                    contsexo[subdic.get(subchave)] = {}
                if subchave == "Fx_Etária":
                    contfxet[subdic.get(subchave)] = {}

        for chave in cidadaos:
            subdic = cidadaos.get(chave)
            for subchave in subdic:
                if subchave == "Sexo":
                    contsexo[subdic.get(subchave)][chave] = subdic.get("Nome")
                if subchave == "Fx_Etária":
                    contfxet[subdic.get(subchave)][chave] = subdic.get("Nome")

        print("\n Consolidado Sexos")
        for chave in contsexo:
            subdic = contsexo.get(chave)
            contador = len(subdic)
            print(f"{chave} -", contador)
        print(contsexo)

        print("\n Consolidado Faixas-Etárias")
        for chave in contfxet:
            subdic = contfxet.get(chave)
            contador = len(subdic)
            print(f"{chave} -", contador)
        print(contfxet)


def consolida_dig(cidadaos, diagnosticos):
    contsint = {}
    tamcid = len(cidadaos)
    tamdig = len(diagnosticos)
    if tamcid < 1:
        print("\nNão há cidadãos cadastrados...\n")
    else:
        if tamdig < 1:
            print("\nNão há diagnósticos realizados...\n")
        else:
            for chave in diagnosticos:
                subdic = diagnosticos.get(chave)
                for subchave in subdic:
                    contsint[subchave] = {}

            # contsint["Perda(Paladar+Olfato)"] = {}

            for chave in diagnosticos:
                subdic = diagnosticos.get(chave)
                for subchave in subdic:
                    valor = subdic.get(subchave)
                    if valor == "SIM":
                        contsint[subchave][chave] = "SIM"

        #                   if subdic.get("Sem Paladar?")=="SIM" and subdic.get("Sem Olfato?")=="SIM":
        #                       contsint["Perda(Paladar+Olfato)"][chave] = "SIM"

            print("\n Consolidado Sintomas")
            for chave in contsint:
                subdic = contsint.get(chave)
                for subchave in subdic:
                    contador = len(subdic)
                    print(f"{chave} -", contador)

            print("\nDiagnosticos:", contsint)
