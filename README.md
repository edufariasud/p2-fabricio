# Trabalho de Redis - Professor Fabricio

Este projeto demonstra o uso do Redis em uma arquitetura de microserviços com FastAPI e PostgreSQL, cobrindo cache, filas e rate limiting.

## 🚀 Fases do Projeto

### Fase 01: Ambiente Docker
O projeto utiliza Docker Compose para gerenciar três serviços principais:
- **Redis**: Banco em memória para cache e filas.
- **API**: Backend FastAPI para gerenciamento de tarefas.
- **Worker**: Processador de tarefas em background (Consumidor).

### Fase 02: Camada de Cache
Implementada no endpoint `GET /items-lento`.
- **TTL**: 30 segundos.
- **Header**: `X-Cache` (HIT ou MISS).
- **Simulação**: O sistema aguarda 2 segundos em caso de MISS para demonstrar o ganho de performance do cache.

### Fase 03: Fila (Produtor/Consumidor)
- **Produtor**: Endpoint `POST /enviar-pedido` usa `LPUSH` para enviar mensagens.
- **Consumidor**: O serviço `worker` usa `BRPOP` para processar mensagens de forma assíncrona.

### Fase 04: Analytics e Rate Limiting
- **Analytics**: Contador global de requisições usando `INCR`.
- **Rate Limiting**: Limite de 10 requisições por minuto por IP para proteção da API.

---

## 🛠️ Como Executar

1. **Subir os containers**:
   ```bash
   docker-compose up --build
   ```

2. **Acessar a Documentação (Swagger)**:
   Abra `http://localhost:8000/docs` no seu navegador.

## 🧪 Como Testar

- **Cache**: Chame `GET /items-lento` e veja a latência diminuir após a primeira chamada. Verifique o header `X-Cache`.
- **Fila**: Chame `POST /enviar-pedido` e observe os logs do terminal do serviço `fastapi_worker`.
- **Rate Limiting**: Chame qualquer rota mais de 10 vezes em um minuto e receba um erro `429`.
- **Status**: Verifique `GET /status` para ver os contadores globais.