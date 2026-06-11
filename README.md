# Gemini CLI

Uma interface de linha de comando simples para conversar com o modelo **Gemini 2.5 Flash**, da Google, direto do seu terminal. O projeto foi feito como exercício prático do **Workshop IA**, ministrado pelo professor **Renato Gil**.

Além de permitir conversas reais com a IA, a ferramenta estima o **custo de cada interação** em tempo real, mostrando na prática como funciona a cobrança por tokens nos modelos de linguagem (LLMs).

> **Sobre a contagem de tokens:** este projeto usa uma aproximação didática — a cada **4 caracteres** de texto equivale a **1 token**. Não é o tokenizador real do Gemini, mas serve bem para entender a lógica de custo. Por isso, os valores exibidos são uma **estimativa**, não a cobrança exata.

## Requisitos

- Python 3.10 ou superior (o código usa `match/case`)
- Uma chave de API do Google AI Studio

As dependências estão em `requirements.txt`:

```
google-genai
python-dotenv
```

## Instalação

1. Clone ou baixe este repositório.

2. (Opcional, mas recomendado) crie um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate   # no Windows: venv\Scripts\activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

## Configuração

1. Pegue sua chave gratuita em [aistudio.google.com](https://aistudio.google.com).

2. Crie um arquivo chamado `.env` na raiz do projeto com o seguinte conteúdo:

```env
GEMINI_API_KEY=sua_chave_aqui
```

> O arquivo `.env` guarda sua chave em segredo, fora do código. Não compartilhe esse arquivo nem suba ele para o GitHub.

## Como executar

Com tudo configurado, basta rodar:

```bash
python main.py
```

A tela vai ser limpa e você verá o banner do programa com o nome do modelo e a lista de comandos disponíveis. A partir daí é só começar a digitar.

## Como usar

### Conversando com a IA

Quando aparecer o cursor `❯`, é só digitar sua mensagem normalmente e apertar **Enter**. O programa envia o texto para o Gemini e mostra a resposta logo abaixo.

```
❯ Me explique o que é uma API em uma frase
```

### Comandos especiais

Além de conversar, você pode usar estes comandos (sempre começando com `/`):

| Comando  | O que faz                                  |
|----------|--------------------------------------------|
| `/help`  | Mostra a lista de comandos                 |
| `/stats` | Exibe o relatório de consumo da sessão     |
| `/clear` | Limpa a tela e mostra o banner novamente   |
| `/quit`  | Encerra o programa                         |

> Apertar **Enter** com a linha vazia não faz nada — o programa simplesmente espera você digitar. Você também pode encerrar a qualquer momento com **Ctrl+C**.

## Como interpretar as saídas

### Resposta de cada mensagem

Depois de cada pergunta, a saída tem três partes:

```
✦ IA » Uma API é um conjunto de regras que permite que dois programas conversem entre si.
──────────────────────────────────────────
  tokens → entrada: 9 (0.000135) · saída: 19 (0.001425)
```

- **`✦ IA »`** — a resposta gerada pelo modelo.
- **`entrada: 9 (0.000135)`** — quantos tokens a **sua mensagem** consumiu e quanto isso custou em dólares.
- **`saída: 19 (0.001425)`** — quantos tokens a **resposta da IA** consumiu e o custo dela.

A entrada e a saída têm preços diferentes (a saída costuma ser mais cara), por isso aparecem separadas.

### Relatório da sessão (`/stats`)

A qualquer momento você pode digitar `/stats` para ver o acumulado de tudo que foi gasto desde que o programa abriu:

```
╔══════════════════════════════════════╗
║  Relatório da Sessão                  ║
╠══════════════════════════════════════╣
║  Modelo          gemini-2.5-flash     ║
║  Tokens Entrada  42                   ║
║  Tokens Saída    118                  ║
║  Custo Total     $0.009210            ║
╚══════════════════════════════════════╝
```

- **Modelo** — qual modelo está sendo usado.
- **Tokens Entrada / Saída** — a soma de todos os tokens de cada tipo durante a sessão.
- **Custo Total** — quanto você gastou no total (entrada + saída de todas as mensagens).

Esses números **zeram** quando você fecha o programa, pois valem apenas para a sessão atual.

## Estrutura do projeto

```
.
├── main.py            # toda a lógica da CLI
├── requirements.txt   # dependências
├── .env               # sua chave da API (você cria)
└── README.md          # este arquivo
```
