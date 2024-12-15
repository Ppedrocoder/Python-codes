def sum(lista):
    if lista==[]:
        return 0
    return lista[-1]+sum(lista[:-1])
a=list(map(int,input().split()))
print(sum(a))