from collections import defaultdict
import re

def validar_senha(senha): #Funcao para verificar se a senha do usuario segue o padrao
    
    try:
    #deve ter 8 digitos
        if len(senha) != 8 :
            raise ValueError("A senha deve conter 8 digitos! !\nTente novamete !")
    #deve conter pelo menos 1 numero
        if not re.search(r"\d" , senha) :
            raise ValueError("A senha deve conter pelo menos 1 numero !\nTente novamente!")
    #deve conter pelo menos 1 letra maiuscula
        if not re.search(r"[A-Z]" , senha) :
            raise ValueError("A senha deve conter pelo menos 1 letra maiuscula!\nTente Novamente!")
    #nao pode ter cacteres especiais
        if re.search(r"[!@#$%¨&*()_+=^~?}{}[/]]") :
            raise ValueError("A senha nao pode conter cacteres especiais\nTente Novamente!")  
    except ValueError as erro :    
        return f"Erro: {erro}"

    return True
    
def validar_status(status): #Verifica se o status foi descrito de maneira correta (s/n)
    sts = str(status).lower()
    try:
        if sts not in ('s', 'n'):
            raise ValueError("Responda apenas com s (sim) ou n (não)! Tente novamente.")
    except ValueError as erro:
        return f"Erro: {erro}"
    
    return True

def verificar_login(nome_usuario , senha): #retorna que o usuario possui cadastro , e o status do usuario
    dados_usuarios = _carregar_usuarios()
    try:
        if nome_usuario not in dados_usuarios :
            raise ValueError("Usuario ou senha incorretos ! ")
        if dados_usuarios[nome_usuario]["senha"] != senha :
            raise ValueError("Usuario ou senha incorretos ! ")
    
    except ValueError as erro :
        return "Erro: {erro}"
    
    sts = dados_usuarios[nome_usuario]["status"] 
    return True , sts
                
def validar_dificuldade(dificuldade): #verifica se a dificuldade foi descrita de maneira correta
    dfc = dificuldade.strip().lower()
    dificuldades = ["facil","medio","dificil"]
    try :    
        if dfc not in dificuldades :
            raise ValueError("Digite apenas opcaoes validas : \n")
    except ValueError as erro :
        return erro
    return True

def validar_opcao(opcao_correta): 
    op = opcao_correta.strip().upper()
    opcoes = ["A","B","C","D"]
    try:
        if op not in opcoes :
            raise ValueError("Digite uma opcao valida !\n")
    except ValueError as erro :
        return erro
    
    return True

def _carregar_usuarios():
    usuarios = defaultdict(dict)
    try :    
        with open("usuarios.txt" , "r") as arquivo :
            for linha in arquivo :
                nome_usuario , senha , status = linha.strip().split(",")      
                usuarios[nome_usuario]["senha"] = senha 
                usuarios[nome_usuario]["status"] = status
    except FileNotFoundError :
        pass
    return usuarios

