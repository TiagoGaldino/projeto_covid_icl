from cov3_back import imp_cid, cad_user, cad_cidadaos, cad_saudacoes, cad_sintomas, list_user, list_cidadaos, list_sintomas, list_saudacoes
from cov3_back2 import diagnostico
from cov3_back3 import filtrox, consolida_cid, consolida_dig
import random

def login(usuarios):
    print("\nDigite seu Código de Usuário: ")
    cod = input()
    for chave in usuarios:
        subdic = usuarios.get(chave)
        for subchave in subdic:
            if cod == subdic.get(subchave):
                print("Digite sua Senha:")
                password = input()
                if password == subdic.get("Senha"):
                    perf = subdic.get("Perfil")
                    return perf
                else:
                    print("Senha Inválida")
                    return 0



def gerasaudacao(saudacoes):
    tam = len(saudacoes)
    x = random.randint(1, tam)
    for chave in saudacoes:
        if x == chave:
            print(f"\n - - - {saudacoes.get(chave)} - - - \n")


def menu(usuarios, cidadaos, saudacoes, sintomas, diagnosticos):
    tam = len(saudacoes)
    if tam < 1:
        print("\n\n --- Olá, Seja Bem Vind[x] ----")
    else:
        gerasaudacao(saudacoes)

# Implementando nova entrada de usuário
    print(" --- Digite [1] Login ou [2] Sair")
    entrar = int(input())
    while entrar < 1 or entrar > 2:
        print("\nEntrada inválida!")
        print(" --- Digite [1] Login ou [2] Sair")
        entrar = int(input())
    if entrar == 2:
        print("\nPrograma Finalizado")
        exit()
    else:
        y = 88
        while y == 88:
            acesso = login(usuarios)
            if acesso == "Admin":
                x = 99                          # código já implementando.
                while x == 99:
                    print("\n--- MENU ---")
                    rota = int(input("\n[1] Cadastrar | [2] Listar | [3] Diagnóstico | [4] Relatórios | [5] Sair "))
                    if rota == 1:
                        print("\n\n--- SUB MENU ---")
                        subrota = int(input("\n[1] Cadastrar Usuário | [2] Cadastrar Cidadãos | [3] Cadastrar Saudações | [4] Cadastrar Sintomas "))
                        if subrota == 1:
                            cad_user(usuarios)
                        elif subrota == 2:
                            subcadcid = int(input("\n ---- [1] Importar Cidadão | [2] Cadastro Manual ---- "))
                            if subcadcid == 1:
                                imp_cid(cidadaos)
                            if subcadcid == 2:
                                cad_cidadaos(cidadaos)
                        elif subrota == 3:
                            cad_saudacoes(saudacoes)
                        elif subrota == 4:
                            cad_sintomas(sintomas)
                    if rota == 2:
                        print("\n\n--- SUB MENU ---")
                        subrota = int(input("\n[1] Listar Usuários | [2] Listar Cidadãos | [3] Listar Saudações | [4] Listar Sintomas "))
                        if subrota == 1:
                            list_user(usuarios)
                        elif subrota == 2:
                            list_cidadaos(cidadaos)
                        elif subrota == 3:
                            list_saudacoes(saudacoes)
                        elif subrota == 4:
                            list_sintomas(sintomas)
                    if rota == 3:
                        diagnostico(cidadaos, sintomas, diagnosticos)
                    if rota == 4:
                        print("\n\n --- SUB MENU ---")
                        subrota = int(input("\n [1] Consolidados de Cidadãos | [2] Consolidado de Diagnósticos | [3] Filtros Cruzados"))
                        if subrota == 1:
                            consolida_cid(cidadaos)
                        elif subrota == 2:
                            consolida_dig(cidadaos, diagnosticos)
                        elif subrota == 3:
                            filtrox(cidadaos, sintomas, diagnosticos)
                    if rota == 5:
                        x = 5
                        print("\n\nPROGRAMA FINALIZADO \n\n")
                        exit()

            if acesso == "Gestor":
                print("\n\n --- MENU GESTOR ---")
                subrota = int(input("\n [1] Consolidados de Cidadãos | [2] Consolidado de Diagnósticos | [3] Filtros Cruzados | [4] Sair"))
                if subrota == 1:
                    consolida_cid(cidadaos)
                elif subrota == 2:
                    consolida_dig(cidadaos, diagnosticos)
                elif subrota == 3:
                    filtrox(cidadaos, sintomas, diagnosticos)
                elif subrota == 4:
                    x = 4
                    print("\n\nPROGRAMA FINALIZADO \n\n")
                    exit()