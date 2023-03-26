from passlib.context import CryptContext

CRIPTO = CryptContext(schemes=['bcrypt'], deprecated='auto')

def verificar_senha(senha: str, hash_senha: str) -> bool:
    """
    Função que verifica se a senha está correta, 
    comparando a senha em texto puro, informada pelo usuário, 
    e o hash da senha que estará salvo no banco duramente de criação da conta.

    Returns:
        bool: Retorna a confirmação se a senha é verdadeira
    """
    return CRIPTO.verify(senha, hash_senha)

def gerar_hash_senha(senha: str) -> str:
    """
    Função que gera o hash
    
    Returns:
        str: Retorna o hash depois da criptografia de senha
    """
    return CRIPTO.hash(senha)