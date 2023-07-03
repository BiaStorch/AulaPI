n = int(input("Digite o numero de notas: "))
notas = []
for _ in range(n):
    x = int(input())
    notas += [x]
# media
soma = 0
for nota in notas:
    soma += nota
media = soma / len(notas)
# sum(notas)/len(notas)

print("lista:", notas)
print("media:", media)
