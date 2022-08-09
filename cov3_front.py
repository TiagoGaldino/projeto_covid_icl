from cov3_back import imp_cid, cad_cidadaos, cad_saudacoes, cad_sintomas, list_cidadaos, list_sintomas, list_saudacoes
from cov3_back2 import diagnostico
from cov3_back3 import filtrox, consolida_cid, consolida_dig
import random


def gerasaudacao(saudacoes):
    tam = len(saudacoes)
    x = random.randint(1, tam)
    for chave in saudacoes:
        if x == chave:
            print(f"\n - - - {saudacoes.get(chave)} - - - \n")


def menu(cidadaos, saudacoes, sintomas, diagnosticos):
    x = 99
    while x == 99:
        tam = len(saudacoes)
        if tam < 1:
            print("\n\n - - - Olá, Seja Bem Vind[x] - - - ")
        else:
            gerasaudacao(saudacoes)

        print("\n--- MENU ---")
        rota = int(input("\n[1] Cadastrar | [2] Listar | [3] Diagnóstico | [4] Relatórios | [5] Sair "))
        if rota == 1:
            print("\n\n--- SUB MENU ---")
            subrota = int(input("\n[1] Cadastrar Cidadãos | [2] Cadastrar Saudações | [3] Cadastrar Sintomas "))
            if subrota == 1:
                subcadcid = int(input("\n ---- [1] Importar Cidadão | [2] Cadastro Manual ---- "))
                if subcadcid == 1:
                    imp_cid(cidadaos)
                if subcadcid == 2:
                    cad_cidadaos(cidadaos)
            elif subrota == 2:
                cad_saudacoes(saudacoes)
            elif subrota == 3:
                cad_sintomas(sintomas)
        if rota == 2:
            print("\n\n--- SUB MENU ---")
            subrota = int(input("\n[1] Listar Cidadãos | [2] Listar Saudações | [3] Listar Sintomas "))
            if subrota == 1:
                list_cidadaos(cidadaos)
            elif subrota == 2:
                list_saudacoes(saudacoes)
            elif subrota == 3:
                list_sintomas(sintomas)
        if rota == 3:
            diagnostico(cidadaos, sintomas, diagnosticos)
        if rota == 4:
            print("\n\n --- SUB MENU ---")
            subrota = int(input("\n [1] Consolidados de Cidadãos | [2] Consolidado de Diagnósticos | [3] Filtros Cruzados"))
            if subrota == 1:
                consolida_cid(cidadaos)
            if subrota == 2:
                consolida_dig(cidadaos, diagnosticos)
            if subrota == 3:
                filtrox(cidadaos, sintomas, diagnosticos)
        if rota == 5:
            x = 5
            print("\n\nPROGRAMA FINALIZADO \n\n")
            exit()
