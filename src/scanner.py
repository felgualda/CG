from src.EDs.ponto import Ponto
from src.EDs.objeto import Objeto

def carregar_objeto(caminho):
    objetos = {}

    pilha_derivacao = []
    last_derivacao = 0

    with open(caminho, 'r') as f:
        for linha in f:
            linha = linha.strip()
            
            if not linha:
                continue

            elif linha.startswith('.'):
                qtde = linha.count(".")
                nome_derivacao = linha[(qtde+1):]

                novo_objeto = Objeto(nome_derivacao,[],[0,0],[1,1],0,Ponto([0,0,1]),objetos[pilha_derivacao[-1]] if pilha_derivacao else None)
                objetos[nome_derivacao] = novo_objeto

                #print(linha)
                #print(f"qtde: {qtde} lastderivacao: {last_derivacao} e pilha: {pilha_derivacao}")
                #print()

                if qtde > last_derivacao:
                    pilha_derivacao.append(nome_derivacao)
                    last_derivacao = qtde
                elif qtde == last_derivacao:
                    pilha_derivacao.pop()
                    pilha_derivacao.append(nome_derivacao)
                    #last_derivacao = qtde
                elif qtde < last_derivacao:
                    for i in range(last_derivacao-qtde + 1):
                        pilha_derivacao.pop()
                    pilha_derivacao.append(nome_derivacao)
                    #print(pilha_derivacao)
                    novo_objeto.set_pai(objetos[pilha_derivacao[-2]])
                    last_derivacao = qtde

            elif linha.startswith('!'): #origem
                entrada = linha[1:]
                try:
                    x, y = map(float, entrada.split(','))
                    #print(f"ponto {x,y} é ORIGEM para o objeto {pilha_derivacao[-1]}")

                    pai_logico = Ponto([x, y, 0.0])

                    objetos[pilha_derivacao[-2]].add_ponto_logico(pai_logico)
                    objetos[pilha_derivacao[-1]].set_origem(pai_logico)
                except ValueError:
                    print(f"erro na linha: {linha}")

            elif ',' in linha:
                try:
                    x, y = map(float, linha.split(','))
                    #print(f"ponto {x,y} registrado para o objeto {pilha_derivacao[-1]}")
                    objetos[pilha_derivacao[-1]].add_ponto_local(Ponto([x, y, 0.0]))
                except ValueError:
                    print(f"erro na linha: {linha}")

    return objetos
