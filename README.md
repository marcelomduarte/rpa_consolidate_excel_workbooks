## Consolidação de Pastas de Trabalho do Excel

Este projeto utiliza a Automação Robótica de Processos (RPA) para automatizar a consolidação de pastas de trabalho do Excel.

### Objetivo do projeto

O objetivo desse projeto é simplificar e agilizar o processo de consolidação de múltiplas pastas de trabalho do Excel em uma única planilha, eliminando a necessidade de realizar essa tarefa manualmente.

### Tecnologias e Ferramentas

🐍 Python <br>
🐼 Pandas <br>
📊 Excel

### Estrutura do projeto

```
rpa_consolidate_excel_workbooks/                       # Pasta principal do projeto
│
├── workbooks/                                         # Pasta para armazenar os dados (pastas de trabalho excel)
│   └─input/data                                       # Pasta contendo as pastas de trabalho do excel que serão consolidadas
│   └─output                                           # Pasta onde será armazenada a pasta de trabalho consolidada
│
├── scripts/                                           # Pasta para armazenar os scripts de automação RPA
│   └─sketch.ipynb                                     # Arquivo que serve como um esboço ou rascunho do projeto
│   └─consolidate_workbooks.py                         # Script principal que realiza a automação de consolidar as pastas de trabalho do excel
│
├── logs/                                              # Pasta para armazenar arquivos de logs
    └─log_erros.txt                                    # Arquivo de log para registrar informações sobre a execução da automação
```

### Como Usar

1. Coloque as pastas de trabalho do Excel que deseja consolidar na pasta `workbooks/input/data`;

2. Altere no script `consolidate_workbooks.py` localizado na pasta `scripts`, a variável `cwd`. Essa variável, refere-se ao diretório da pasta principal do projeto;

3. Execute o script `consolidate_workbooks.py`. Este script irá ler todas as pastas de trabalho do Excel na pasta `workbooks/input/data`, consolidá-las em uma única planilha e salvar o resultado na pasta `workbooks/output`.

4. Verifique o arquivo de log `logs/log_erros.txt` para quaisquer erros ou problemas durante a execução da automação.

5. Os arquivos consolidados estarão disponíveis na pasta `workbooks/output`.

### Contribuições

Contribuições ao projeto são bem-vindas. 

### Licença

Este projeto está licenciado sob a Licença MIT.
