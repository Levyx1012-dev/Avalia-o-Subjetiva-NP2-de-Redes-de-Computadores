## Passo a Passo de Execução

### 1. Instalar o Python

Verifique se o Python 3 está instalado:

```bash
python --version
```

### 2. Baixar os arquivos do projeto

Certifique-se de possuir os arquivos:

```text
servidor.py
cliente.py
```

### 3. Iniciar o servidor

Abra um terminal na pasta do projeto e execute:

```bash
python servidor.py
```

O terminal exibirá:

```text
Servidor escutando na porta 3535...
```

### 4. Iniciar o cliente

Abra um segundo terminal na mesma pasta e execute:

```bash
python cliente.py
```

O terminal exibirá:

```text
Conectado ao servidor!
```

### 5. Enviar mensagens

Digite mensagens no terminal do cliente e pressione Enter.

Exemplo:

```text
Digite uma mensagem: Olá servidor
Digite uma mensagem: Teste de conexão
```

### 6. Receber mensagens

As mensagens enviadas pelo cliente serão exibidas no terminal do servidor.

Exemplo:

```text
Mensagem recebida: Olá servidor
Mensagem recebida: Teste de conexão
```

### 7. Encerrar a aplicação

Digite:

```text
sair
```

A conexão será encerrada e os programas finalizarão sua execução.
