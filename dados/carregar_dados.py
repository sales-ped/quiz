from collections import defaultdict

def carregar_usuarios():
    usuarios = defaultdict(dict)
    try :    
        with open("usuarios.txt" , "r" , encoding="utf-8") as arquivo :
            for linha in arquivo :
                nome_usuario , senha , status = linha.strip().split(",")      
                usuarios[nome_usuario]["senha"] = senha 
                usuarios[nome_usuario]["status"] = status
    except FileNotFoundError :
        pass
    return usuarios

def carregar_questoes(caminho="questoes.txt"):
    # retorna uma lista com questões
    pass

def carregar_ranking(caminho="ranking.txt"):

    # já existe, você pode mover para cá
    pass
def mostrar_questoes(dificuldade) :

def mostrar_ranking() :
   
    ranking = carregar_ranking()

    if not ranking:
        print("Ranking vazio ou não encontrado.")
        return

    ranking_ordenado = sorted(ranking.items(), key=lambda x: x[1], reverse=True)

    print("--- Ranking de Usuários: ---")
    for i, (usuario, pontos) in enumerate(ranking_ordenado, 1):
        print(f"{i}. {usuario} - {pontos} pontos")

def consultar_resposta() :