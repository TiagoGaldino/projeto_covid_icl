def cad_user(usuarios):
    cont = 1
    print("\nQuantos usuários deseja cadastrar?")
    qtde = int(input())
    while cont <= qtde:
        usuarios[cont] = {}

        print("\nDigite o nome do usuário: ", cont)
        username = input()
        usuarios[cont]["Nome"] = username

        print("\nDigite o código do usuário: ", cont)
        usercode = int(input())
        usuarios[cont]["Código"] = usercode

        print("\nDigite a senha do usuário: ", cont)
        password = int(input())
        usuarios[cont]["Senha"] = password

        print(f"\nDigite o nome do usuário {cont}? [A] Admin ou [G] Gestor")
        usertype = input()
        if usertype == "A":
            usuarios[cont]["Perfil"] = "Admin"
        if usertype == "G":
            usuarios[cont]["Perfil"] = "Gestor"

        cont = cont + 1

#    print(usuarios)


def imp_cid(cidadaos):
    arquivo = open("Base_Cidadaos_Aula45.txt", "r")
    for linha in arquivo:
        linhabase = linha.split(",")
        cpf = linhabase[0]
        nome = linhabase[1]
        idade = linhabase[2]
        sex1 = linhabase[3]
        sexo = sex1.rstrip()
        cidadaos[cpf] = {}
        cidadaos[cpf]["Nome"] = nome
        cidadaos[cpf]["Idade"] = idade
        cidadaos[cpf]["Sexo"] = sexo
        if '0' < idade < '12':
            cidadaos[cpf]["Fx_Etária"] = 'CRI'
        if '11' < idade < '18':
            cidadaos[cpf]["Fx_Etária"] = 'ADO'
        if '17' < idade < '60':
            cidadaos[cpf]["Fx_Etária"] = 'ADU'
        if idade > '59':
            cidadaos[cpf]["Fx_Etária"] = 'IDO'
    arquivo.close()
    print(f"Dado Bruto: {cidadaos}")


def cad_cidadaos(cidadaos):
    qtde = int(input("\nDigite quantos cidadãos serão cadastrados: "))
    i = 1
    while i <= qtde:
        cpf = int(input("\nDigite CPF do cidadão: "))
        # cpf = validacpf(cpf)
        cidadaos[cpf] = {}
        nome = input("Digite Nome: ").upper()
        cidadaos[cpf]["Nome"] = nome
        idade = int(input("Digite Idade: "))
        cidadaos[cpf]["Idade"] = idade
        sexo = input("Digite Sexo [F] Feminino - [M] Masculino - [X] LGBTQIA+: ").upper()
        cidadaos[cpf]["Sexo"] = sexo
        if 0 < idade < 12:
            cidadaos[cpf]["Fx_Etária"] = 'CRI'
        if 11 < idade < 18:
            cidadaos[cpf]["Fx_Etária"] = 'ADO'
        if 17 < idade < 60:
            cidadaos[cpf]["Fx_Etária"] = 'ADU'
        if idade > 59:
            cidadaos[cpf]["Fx_Etária"] = 'IDO'
        i += 1
    print("\n\nCadastro de cidadãos realizado com sucesso!!\n\n")


def cad_saudacoes(saudacoes):
    qtde = int(input("\nQuantas saudações deseja cadastrar? "))
    id_saud = 1
    while id_saud <= qtde:
        saud = input(f"\nDigite a {id_saud}a a ser cadastrada: ")
        saudacoes[id_saud] = saud
        id_saud += 1


def cad_sintomas(sintomas):
    qtde = int(input("\nQuantos sintomas deseja cadastrar? "))
    id_sint = 1
    while id_sint <= qtde:
        saud = input(f"\nDigite o {id_sint}o a ser cadastrado: ")
        sintomas[id_sint] = saud
        id_sint += 1


def list_user(usuarios):
    print("Entrou na lista de usuários...")
    tam = len(usuarios)
    if tam < 1:
        print("\nNão há usuários cadastrados")
    else:
        for chave in usuarios:
            print(f"\n{chave}:")
            subdic = usuarios.get(chave)
            for subchave in subdic:
                print(f"{subchave} - {subdic.get(subchave)}")

def list_cidadaos(cidadaos):
    tam = len(cidadaos)
    if tam < 1:
        print("Não há cidadãos cadastrados...\n")
    else:
        for chave in cidadaos:
            print("\nCPF:", chave)
            subdic = cidadaos.get(chave)
            for subchave in subdic:
                print(f"{subchave} - {subdic.get(subchave)}")


def list_saudacoes(saudacoes):
    tam = len(saudacoes)
    if tam < 1:
        print("\nNão há saudações cadastradas...")
    else:
        print(f"\nSaudações Cadastradas: {tam}\n")
        for chave in saudacoes:
            print(f"{chave}a saudação: {saudacoes[chave]}")


def list_sintomas(sintomas):
    tam = len(sintomas)
    if tam < 1:
        print("\nNão há sintomas cadastrados...")
    else:
        for chave in sintomas:
            print(f"{chave}o sintoma: {sintomas[chave]}")
