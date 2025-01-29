# Event Manager Software

## Como Rodar o Projeto

### 1. Instalar Dependências  
Certifique-se de ter o Python instalado e execute:  
```sh
pip install flask requests
```

### 2. Iniciar o Servidor  
No terminal, execute:  
```sh
python event_server.py
```
O servidor será iniciado em:  
```
http://0.0.0.0:5000/
```

### 3. Executar o Cliente  
Em outro terminal, execute:  
```sh
python event_manager.py
```

## Funcionalidades

- **Criar evento**: Adiciona um evento informando nome e data.  
- **Listar eventos**: Exibe todos os eventos cadastrados.  
- **Registrar participante**: Associa um participante a um evento.  
- **Listar participantes**: Mostra os participantes de um evento.  

Acesse o sistema via terminal e escolha as opções do menu para interagir.