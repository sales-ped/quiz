from collections import namedtuple , defaultdict
from config import ARQUIVO_USUARIO,ARQUIVO_QUESTOES,ARQUIVO_RANKING
#Declarando funcoes publicas
__all__ = ["cadastrar_usuario",
           "cadastrar_questao",
           "cadastrar_pontuacao",
           "atualizar_pontuacao",
           "carregar_ranking"]

#Estrutura de dados
Questao = namedtuple("Questao",["enunciado","opcao_1","opcao_2" , "opcao_3" , "opcao_4" ,"opcao_correta" , "dificuldade"])
Usuario = namedtuple("Usuario",["nomeUsuario", "senha", "status"])

def cadastrar_usuario(nome_usuario , senha , status):#funcao para cadastrar funcionario
    
    #instanciando os dados com uma namdetuple
    usuario = Usuario(nome_usuario , senha , status)
    
    #salvando no arquivo
    with open(ARQUIVO_USUARIO , "a" , encoding="utf-8") as arquivo:
        arquivo.write(f"{usuario.nomeUsuario},{usuario.senha},{usuario.status}\n")
    
    return "Usuario Cadastrado com sucesso !\n"

def cadastrar_questao(enunciado ,opcao_1 , opcao_2 , opcao_3 , opcao_4 , opcao_correta , dificuldade) :#funcao para cadastrar questao
    #instanciando os dados com uma namedtuple
    questao = Questao(enunciado, opcao_1, opcao_2, opcao_3, opcao_4, opcao_correta, dificuldade)
    #salvando os dados da questao em um arquivo
    with open(ARQUIVO_QUESTOES , "a" , encoding="utf-8") as arquivo:
        arquivo.write(f"{questao.enunciado}\n{questao.opcao_1},{questao.opcao_2},{questao.opcao_3},{questao.opcao_4},{questao.opcao_correta},{questao.dificuldade}\n")
        

    return "Questao cadastrada com sucesso !\n"

def cadastrar_pontuacao(nome_usuario , nova_pontuacao):#funcao para cadastrar pontuacao noranking
    ranking = _carregar_ranking()
    if nome_usuario in ranking :
        return f"{nome_usuario} ja esta cadastrado Use a funcao atualizar_pontuacao.\n!"
    ranking[nome_usuario] = nova_pontuacao
    #salvando o ranking atualizado no arquivo
    _salvar_ranking(ranking)
    
    return "Pontuacao cadastrada\n"        
                
def atualizar_pontuacao(nome_usuario , nova_pontuacao) : #Funcao para atualizar a pontuacao no ranking
    
    
    ranking = carregar_ranking()
    if nome_usuario not in ranking :
        return f"{nome_usuario} ainda nao tem pontuacao. Use a funcao cadastrar_pontuacao.\n!"
    
    ranking[nome_usuario] += nova_pontuacao
    
    _salvar_ranking(ranking)
    
    
    return "Pontuacao Atualizada com sucesso !\n"
        
def carregar_ranking():
    #coletando os dados do ranking
    ranking = defaultdict(int)
    try :
        with open(ARQUIVO_RANKING,"r",encoding="utf-8") as arquivo :
            #usando o arquivo como iterador
            for linha in arquivo:
                usuario , pontuacao = linha.strip().split(",")
                ranking[usuario] = int(pontuacao)
                
    except FileNotFoundError :
        pass
    
    return ranking 

def _salvar_ranking(ranking):
    with open(ARQUIVO_RANKING , "w", encoding= "utf-8") as arquivo:
        for nome , pontuacao in ranking.items() :
            arquivo.write(f"{nome},{pontuacao}\n")
