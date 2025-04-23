from collections import defaultdict
import re

__all__ = [
           "validar_senha",
           "validar_status",
           "validar_dificuldade",
           "verificar_login",
           "validar_opcao"
           ]

def validar_senha(senha): #Funcao para verificar se a senha do usuario segue o padrao
    
    
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
    if re.search(r"[!@#$%¨&*()_+=^~?}{}[/]]" , senha) :
        raise ValueError("A senha nao pode conter cacteres especiais\nTente Novamente!")  

    return True

def validar_status(status): #Verifica se o status foi descrito de maneira correta (s/n)
    sts = str(status).lower()
    
    if sts not in ('s', 'n'):
        raise ValueError("Responda apenas com s (sim) ou n (não)! Tente novamente.")
    
    return True
                
def validar_dificuldade(dificuldade): #verifica se a dificuldade foi descrita de maneira correta
    dfc = dificuldade.strip().lower()
    dificuldades = ["facil","medio","dificil"]
     
    if dfc not in dificuldades :
        raise ValueError("Dificuldade inválida. Use: fácil, médio ou difícil.\n")
    
    return True

def validar_opcao(opcao_correta): 
    op = opcao_correta.strip().upper()
    opcoes = ["A","B","C","D"]
    
    if op not in opcoes :
        raise ValueError("Digite uma opcao valida !\n")
    
    return True

def verificar_login(nome_usuario , senha): #retorna que o usuario possui cadastro , e o status do usuario
    dados_usuarios = _carregar_usuarios()
    
    if nome_usuario not in dados_usuarios :
        raise ValueError("Usuario ou senha incorretos ! ")
    if dados_usuarios[nome_usuario]["senha"] != senha :
        raise ValueError("Usuario ou senha incorretos ! ")    
    
    sts = dados_usuarios[nome_usuario]["status"] 
    return True , sts



