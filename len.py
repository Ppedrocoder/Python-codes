def len(lista):
    if lista==[]:
        return 0
    return 1+len(lista[:-1])
a=list(input().split())
print(len(a))