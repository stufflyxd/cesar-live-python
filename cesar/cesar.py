from string import ascii_lowercase
def encripta(frase, n = 13):
    """Ecripta o texto passado"""
    encriptado = ""
    for letra in frase:
        letra = letra.lower()
        if letra == " ":
            encriptado.join(letra)
