# Event Manager Software

## Descrição
O Event Manager Software é um sistema simples para gerenciamento de eventos. Ele permite criar eventos e registrar participantes. O projeto é desenvolvido em Python com Flask como backend.

## Funcionalidades Implementadas

### Criação e Gerenciamento de Eventos
- Permite criar eventos informando nome e data.
- Lista os eventos cadastrados com ID, nome, data e participantes.

### Registro de Participantes
- Possibilita registrar participantes em eventos.
- Exibe a lista de participantes por evento.

## Como Rodar o Projeto

### Instalar Dependências
Certifique-se de ter o Python instalado. Depois, instale as dependências:
```sh
pip install flask requests
```

### Iniciar o Servidor
No terminal, navegue até a pasta do projeto e execute:
```sh
python event_server.py
```
Se tudo estiver correto, verá a mensagem:
```
Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```

### Executar o Cliente
Em outro terminal, execute:
```sh
python event_manager.py
```
Isso exibirá o menu principal:
```
===== MENU =====
1. Criar evento
2. Listar eventos
3. Registrar participante
4. Listar participantes
5. Sair
Escolha uma opção:
```
Agora você pode interagir com o sistema.

## Testando as Funcionalidades

### Criar um Evento
1. Escolha a opção 1.
2. Digite o nome do evento.
3. Informe a data no formato YYYY-MM-DD.
4. O sistema confirmará a criação.

### Listar Eventos
1. Escolha a opção 2.
2. O sistema exibirá os eventos no formato DD-MM-YYYY.

### Registrar um Participante
1. Escolha a opção 3.
2. Informe o nome do participante.
3. Digite o ID do evento correspondente.
4. O sistema confirmará o registro.

### Listar Participantes
1. Escolha a opção 4.
2. O sistema mostrará os participantes registrados.

### Sair do Sistema
- Escolha a opção 5 para encerrar o programa.
- Para desligar o servidor, pressione CTRL + C no terminal onde ele está rodando.
