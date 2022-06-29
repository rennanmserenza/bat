from os import system as sys


def retornaEscolhaInt(lista):
    for i, v in enumerate(lista):
            print(f'[{i}] - {v}')        
        
    while True:
        try:
            op = int(input('R.: ').strip())
            
            if op not in range(0, len(lista)):
                raise ValueError('Não te entendi, use apenas valores dentro do intervalo informado')
        except ValueError as e:
            print('Valor inválido:', e)
        else:
            break

    return op

def retornaEscolhaString():
    while True:
        try:
            op = input('Está correta a seleção[S/N]? ').upper().strip()[0]

            if op.isnumeric() or op not in 'SN':
                raise IndexError('Não te entendi, use apenas S e N.')
        except IndexError as e:
            print('Valor inválido:', e)
        else:
            break
    
    return op

def retornaPath(municipio, projeto):
    municipio = "BarraMansa" if (municipio == "Barra Mansa") "CasimiroDeAbreu" elif (municipio == "Casimiro de Abreu") else 

    if projeto == "Tributos":
        projeto_path = "Tributario".lower() if municipio != 'Oriximina' else "Tributario"
    else:
        projeto_path = projeto.lower() if municipio != 'Oriximina' else projeto.capitalize()
    
    return 'Xcopy D:\ProjetosEstudo\PY\\bat\ D:\ProjetosEstudo\PY\\bat\carros  /c /v /f /d /i /w'


def insereTextoBat(texto):    
    arq = open("exec.bat", 'w+')
    arq.write(texto)
    arq.close()

def leTextoBat():
    arq = open("exec.bat")

    linhas = arq.readlines()
    for linha in linhas:
        print(linha)
        
    arq.close()


def main():
    # interface
    municipios = [
          "Barcarena"
        , "BarraMansa"
        , "CasimiroDeAbreu"
        , "DuqueDeCaxias"
        , "Oriximina"
    ]

    projetos = [
          "Tributos"
        , "Portal"
    ]

    ambientes = [
          'Interno'
        , 'Homologa'
        , 'Oficial'
    ]

    # menu
    print(f'\nBem vindo!')
    while True:
        print(f'\nQue município deseja trabalhar?')
        operation = retornaEscolhaInt(municipios)
        municipio = municipios[operation]
        
        print(f'\nProjeto Tributario ou Portal?')
        operation = retornaEscolhaInt(projetos)
        projeto = projetos[operation]
        
        print(f'\nInterno ou Homologação?')
        operation = retornaEscolhaInt(ambientes)
        ambiente = ambientes[operation]

        
        contexto = f'Município: {municipio}; Projeto: {projeto}; Ambiente: {ambiente};'
        print(f'\n{contexto}')
        texto = retornaPath(municipio, projeto)
        print(f'\nDados de Cópia: {texto}')
        
        
        confirmartion = retornaEscolhaString()        
        if confirmartion == 'S':
            print('\nContinuando...')
            break
    
    # manipulação de .bat
    insereTextoBat(texto)

    print('Valor contido no arquivo .bat')
    leTextoBat()    

    # execução .bat
    sys('exec.bat')

if __name__ == "__main__":
    main()


# testes = [
    #     'Xcopy D:\ProjetosEstudo\PY\bat\ D:\ProjetosEstudo\PY\bat\carros  /c /v /f /d /i /w',
    #     'Xcopy D:\ProjetosEstudo\PY\bat\ D:\ProjetosEstudo\PY\bat\carros  /c /v /f /d /i /w /q',        #suprime mensagens na tela do Xcopy \q
    #     'Xcopy D:\ProjetosEstudo\PY\bat\ D:\ProjetosEstudo\PY\bat\carros  /c /v /f /d /i /w /u',        #copia apenas arquivos existentes no destino \u
    #     'Xcopy D:\ProjetosEstudo\PY\bat\ D:\ProjetosEstudo\PY\bat\carros  /c /v /f /d /i /w /k /y',     #suprime confirmação de substituição
    #     'Xcopy D:\ProjetosEstudo\PY\bat\ D:\ProjetosEstudo\PY\bat\carros  /c /v /f /d /i /w /k /y /z'   #para efetuar cópias em rede TESTAR
    # ]