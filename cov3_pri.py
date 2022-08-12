from cov3_front import menu

usuarios = {
    1: {
    "Nome": "Silva",
    "Código": "131313",
    "Senha": "L13",
    "Perfil": "Admin"},
    2: {
    "Nome": "Ana",
    "Código": "141414",
    "Senha": "L14",
    "Perfil": "Gestor"},
    }
cidadaos = {}
saudacoes = {}
sintomas = {}
diagnosticos = {}

menu(usuarios, cidadaos, saudacoes, sintomas, diagnosticos)
