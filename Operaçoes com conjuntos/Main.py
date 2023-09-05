def uniao (a, b):
    resultado = a.union(b)
    return resultado
    
def intersecao (a, b):
    resultado = a.intersection(b)
    if len(resultado) == 0:
        return "Conjuntos disjuntos"
    else:
        return resultado

def diferenca (a, b):
    resultado = a.difference(b)
    return resultado

def produto_cartesiano(a, b):
    resultado = []
    for i in a:
        for j in b:
            resultado.append((i, j))
    return resultado

def main():
    print("Escolha sua operaçao: ")
    print("1 - União")
    print("2 - Interseção")
    print("3 - Diferença")
    print("4 - Produto Cartesiano")
    opcao = int(input("Digite sua opção: "))
    if opcao == 1:
        a = set(input("Digite os elementos do conjunto A: ").split(","))
        b = set(input("Digite os elementos do conjunto B: ").split(","))
        print(uniao(a, b))
    elif opcao == 2:
        a = set(input("Digite os elementos do conjunto A: ").split(","))
        b = set(input("Digite os elementos do conjunto B: ").split(","))
        print(intersecao(a, b))
    elif opcao == 3:
        a = set(input("Digite os elementos do conjunto A: ").split(","))
        b = set(input("Digite os elementos do conjunto B: ").split(","))
        print(diferenca(a, b))
    elif opcao == 4:
        a = set(input("Digite os elementos do conjunto A: ").split(","))
        b = set(input("Digite os elementos do conjunto B: ").split(","))
        print(produto_cartesiano(a, b))
    else:
        print("Opção inválida!")

if __name__ == "__main__":
    main()
