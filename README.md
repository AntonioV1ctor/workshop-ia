# Gemini CLI
 
Interface de linha de comando para interagir com o modelo **Gemini 2.5 Flash** da Google, desenvolvida como projeto prático do **Workshop IA** ministrado pelo professor **Renato Gill**.

## Sobre o Projeto
 
O projeto demonstra na prática como funcionam os custos de uso de modelos de linguagem (LLMs), aplicando uma lógica de tokenização rudimentar: cada **4 caracteres** de texto equivale a **1 token**. A partir disso, o custo de cada interação é calculado multiplicando o número de tokens pelo preço unitário definido.
 
Além do cálculo de custos, a ferramenta se integra à API do Gemini para permitir conversas reais, tornando a demonstração mais concreta e interativa.


## Requisitos
 
```
google-genai
python-dotenv
```
 
Instale as dependências com:
 
```bash
pip install -r requirements.txt
```

 
## Configuração
 
1. Crie um arquivo `.env` na raiz do projeto:
```env
GEMINI_API_KEY=sua_chave_aqui
```
 
2. Obtenha sua chave em [aistudio.google.com](https://aistudio.google.com)

## Como Usar
 
```bash
python main.py
```