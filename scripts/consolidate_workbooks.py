# Importando as bibliotecas necessárias
import pandas as pd # Biblioteca de estrutura de dados primária
import os           # Permite acessar os arquivos e diretórios do sistema operacional
import datetime     # Manipula datas e horas

# Ignora o aviso
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

# Diretório
cwd = 'C:\\Users\\Spider\\OneDrive - HTPDATA\\Arquivos\\Profissional\\Portfolio\\Python\\rpa_consolidate_excel_workbooks'
if os.getcwd() != cwd:  # Obtém o diretório de trabalho atual
    os.chdir(cwd)       # Altera o direitório de trabalho atual

# Listar os nomes de arquivos
filenames = os.listdir('workbooks\\input\\data')

# Definir as colunas para o DataFrame 'consolidado'
columns = [
    'Segmento',
    'País',
    'Produto',
    'Qtde de Unidades Vendidas',
    'Preço Unitário',
    'Valor Total',
    'Desconto',
    'Valor Total c/ Desconto',
    'Custo Total',
    'Lucro',
    'Data',
    'Mês',
    'Ano'
]

# Criar um DataFrame vazio com as colunas especificadas
df_consolidated = pd.DataFrame(columns=columns)

# Iterar sobre todos os arquivos
# Realizar a consolidação (apenas .xlsx)
for filename in filenames:
    if filename.endswith('.xlsx'):
        
        data_filename = filename.split('-')
        segment = data_filename[0]
        country = data_filename[1].replace('.xlsx', '')
        
        try:
            filepath = os.path.join(cwd, 'workbooks', 'input', 'data', filename)
            df = pd.read_excel(filepath)
            df.insert(0, 'Segmento', segment)
            df.insert(1, 'País', country) 
            #df_consolidated = pd.concat([df_consolidated, df], ignore_index=True, sort=False)
            df_consolidated = pd.concat([df_consolidated, df])
        except:
            with open('logs\\log_erros.txt', 'w') as file:
                file.write(f'Erro ao tentar consolidar o arquivo {filename}.')
    else:
        with open('logs\\log_erros.txt', 'w') as file:
            file.write(f'O arquivo {filename} não é um arquivo Excel válido!')

# Obter a data e hora atuais
agora = datetime.datetime.now()

# Exportar o DataFrame consolidado para um arquivo excel
df_consolidated.to_excel(f'workbooks\\output\\report-consolidated-{agora.strftime('%d-%m-%Y')}.xlsx', 
                     index=False,
                     sheet_name='ReportConsolidated')