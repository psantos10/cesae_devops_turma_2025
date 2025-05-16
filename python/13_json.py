import json

utilizadores_json = '{"nome": "Marta", "idade": 19, "cidade": "Porto"}'

print(utilizadores_json)

utilizadores = json.loads(utilizadores_json)

print(utilizadores)
# print(utilizadores_json["nome"])
print(utilizadores["nome"])
print()

print(type(utilizadores_json))
print(type(utilizadores))

novo_json = json.dumps(utilizadores, sort_keys=True)
print(novo_json)
print(type(novo_json))

