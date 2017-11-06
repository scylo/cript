import sys

def cifrar(frase, senha):
	frase_cifrada =''
	for l in frase:
		if l in dic:
			l_index = dic.index(l)
			frase_cifrada += dic[(l_index +senha) % len(dic)]
		else:
			frase_cifrada += l
	# com_senha.insert(c, ord(frase[c])+senha)

	return frase_cifrada

def decifrar(frase, senha):
	frase_cifrada =''
	for l in frase:
		if l in dic:
			l_index = dic.index(l)
			frase_cifrada += dic[(l_index -senha) % len(dic)]
		else:
			frase_cifrada += l
	# com_senha.insert(c, ord(frase[c])+senha)
	return frase_cifrada
	
print("o programa le o arquivo dic.txt no local do arquivo .py")
arquivo = open("dic.txt", "r")
dic = arquivo.read()

frase = raw_input("Frase:\n")

senha = int(input("digite a senha de 3 digitos.\n"))
if (senha <= 99) or (senha > 999):		
	print "Senha invalida"
	sys.exit()

modo = (input("digite 0 para cifrar ou 1 para decifrar\n"))
if modo == 0:
	print cifrar(frase, senha)			
elif modo == 1:
	print decifrar(frase, senha)
else:
	print "erro"	



# caractere = ord(array[1])
# print caractere
# caractere = ord(array[21])
# print caractere



# tamanho = len(array)
# 	for i in range(0, tamanho):
# 		print(array[i])




