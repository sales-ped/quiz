from collections import namedtuple , defaultdict

#Declarando funcoes publicas
_all__ = ["cadastrar_usuario",
           "cadastrar_questao",
           "cadastrar_pontuacao",
           "atualizar_pontuacao",
           ]
#Arquivos
ARQUIVO_USUARIO = "usuarios.txt"
ARQUIVO_QUESTOES = "questoes.txt"
ARQUIVO_RANKING = "ranking.txt"

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
    ranking = _carregar_ranking()
    if nome_usuario not in ranking :
        return f"{nome_usuario} ainda nao tem pontuacao. Use a funcao cadastrar_pontuacao.\n!"
    
    ranking[nome_usuario] += nova_pontuacao
    
    _salvar_ranking(ranking)
    return "Pontuacao Atualizada com sucesso !\n"
        
#funcao encapsuladas
def _carregar_ranking():
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
    
if __name__ == "__main__" :

    #teste cadastrar usuario
    print("---Teste Cadastro de Usuario---")
    print(cadastrar_usuario(nome_usuario="Sandino" , senha="S1234567" , status="s"))
    
    #teste cadastrar questao
    print("---Teste Cadastro de questao---")
    print(cadastrar_questao(enunciado="Qual a melhor linguagem de programacao ?" , opcao_1="Python" , opcao_2="Java" , opcao_3="Depende" , opcao_4="Javascript" , opcao_correta="C" , dificuldade="Facil"))
   
    #teste carregar ranking
    print("---Teste carregar ranking---")
    r = _carregar_ranking()
    if not ranking:
        print("Ranking vazio")
    else:
        for usuario , pontuacao in r.items() :
            print(f"Usuario = {usuario} potuacao :{pontuacao}")
    print()
    #teste cadastro de pontuacao
    print("---Teste Cadastrar Pontuacao ---")
    print(cadastrar_pontuacao(nome_usuario="Pedro" , nova_pontuacao=10))
    #teste atualizacao de pontuacao
    print("---Teste Atualizar pontuacao---")
    print(atualizar_pontuacao(nome_usuario="Pedro" , nova_pontuacao=5))