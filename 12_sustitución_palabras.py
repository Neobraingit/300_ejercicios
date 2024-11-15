
# Un programa en el que una palabra sea sustituida por otra en todas sus ocurrencias

texto = input('Introduce un texto a analizar: '.lower())
palabra_a_reemplazar = input('Introduce la palabra a reemplazar: '.lower())
nueva_palabra = input('Nueva palabra: '.lower())

texto_modificado = texto.replace(palabra_a_reemplazar, nueva_palabra)
print ('Texto_modificado: ', texto_modificado)
    