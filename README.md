# Invoice PDF Extractor

## Descrição

Este projeto é uma automação em Python para leitura e extração de informações de faturas (invoices) em formato PDF. Os dados extraídos são armazenados em um banco de dados MySQL. O sistema também gera logs do processo em um arquivo Excel.

## Funcionalidades

- Leitura de invoices em PDF da pasta input.
- Extração e armazenamento de dados no banco de dados MySQL.
- Criação automática do banco **database_invoices** e das tabelas **Invoices**, *Invoices_Items** e **Payments**, caso não existam.
- Movimentação de arquivos processados corretamente para a pasta data.
- Movimentação de arquivos com erro para a pasta dataerror.
- Geração de um arquivo Excel na pasta output com logs do processo (data, hora, nome do documento, nota e status).

## Benefícios do Projeto

Automatiza a extração e armazenamento de dados de invoices.
Reduz erros associados à digitação manual de dados financeiros.
Facilita consultas e integração com outras aplicações.
Gera relatórios Excel de processamento para auditoria e monitoramento.

## Requisitos

- Banco de Dados
- MySQL instalado e configurado.
- Driver MySQL ODBC instalado.
- Bibliotecas Python


## **Instalar Dependências**

```bash
pip install -r requirements.txt
```

### Certifique-se de instalar as dependências necessárias antes de rodar o projeto:
	- pip install customtkinter pyodbc pandas

### Configuração: 

- Defina as credenciais do banco de dados nas variáveis de ambiente do Windows:

	- DB_USER: Usuário do banco de dados.
	- DB_PASSWORD: Senha do banco de dados.

- Para configurar as variáveis de ambiente:
	Abra o Prompt de Comando e digite:
		setx DB_USER "seu_usuario"
		setx DB_PASSWORD "sua_senha"

- Reinicie o terminal para que as alterações entrem em vigor.

# Como Usar

- Certifique-se de que os invoices estejam na pasta input.
- Execute o script principal:

		python main.py

## Verifique as pastas:

- Os arquivos processados corretamente estarão em data/.
- Os arquivos com erro estarão em dataerror/.
- Consulte os logs do processo no arquivo Excel gerado em output/.

## Estrutura de Pastas
```
|-- input/          # Invoices a serem processadas
|-- data/           # Invoices processadas corretamente
|-- dataerror/      # Invoices com erro
|-- output/         # Arquivo Excel de log do processo
|-- main.py         # Script principal
```
# Tecnologias Utilizadas

- **Python 3.7+**
- **Bibliotecas**:
 - 'CustomTkinter' (interface gráfica)
 - 'PyODBC' (conexão com MySQL)
 - 'Pandas' (manipulação de dados e geração do Excel)

## Licença
Este projeto está licenciado sob a **MIT License** - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

