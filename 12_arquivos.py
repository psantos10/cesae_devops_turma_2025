meus_contactos = open("contactos.txt", "r+")

# meus_contactos.write("Jorge - 92998664\n")
# meus_contactos.write("Pinto - 93998664\n")

# meus_contactos.close()

conteudo_do_arquivo = meus_contactos.read(100)

print(conteudo_do_arquivo)

meus_contactos.close()

print()

meus_contactos = open("contactos.txt", "r+")
print(f"Nome do arquivo: {meus_contactos.name}")
print(f"Modo de abertura: {meus_contactos.mode}")
print(f"Estado: {meus_contactos.closed}")
meus_contactos.close()
print(f"Estado: {meus_contactos.closed}")
