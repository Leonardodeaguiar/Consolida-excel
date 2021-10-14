from os import chdir, getcwd
import openpyxl
import pandas as pd
import glob

# caminho e extensao
extensao = '.xlsx'
caminho = getcwd().split('C:')[1]

# funcao para consolidar os arquivos xlsx


def consolidar_excel(extensao, caminho):

    # atribuicao do caminho com os arquivos
    chdir(caminho)

    # glob dos arquivos
    arquivos = [item for item in glob.glob(f'*{extensao}')]
    # percorre e concatena arquivos com pandas
    arquivo_consolidado = pd.concat(
        [pd.read_excel(arquivo, index_col=0, skiprows=2) for arquivo in arquivos])

    # exporta arquivo consolidado
    arquivo_consolidado.to_excel('arquivo_consolidado.xlsx')


consolidar_excel(extensao, caminho)
