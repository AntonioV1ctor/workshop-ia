import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

INPUT_TOKEN_VALUE = 0.000015
OUTPUT_TOKEN_VALUE = 0.000075

total_input_tokens = 0
total_output_tokens = 0
total_cost= 0

R="\033[0m"; BOLD="\033[1m"; DIM="\033[2m"
G="\033[92m"; Y="\033[93m"; B="\033[94m"; M="\033[95m"; C="\033[96m"; RED="\033[91m"

MODEL = "gemini-2.5-flash"

def banner():
    print(f"{DIM}╔══════════════════════════════════════╗{R}")
    print(f"{DIM}║{R}  {BOLD}{B}Gemini CLI{R}  {DIM}·{R}  {M}{MODEL}{R}  {DIM}   ║{R}")
    print(f"{DIM}╚══════════════════════════════════════╝{R}")
    print(f"{DIM}  /quit · /clear · /stats · /help\n{R}")

def calcular_custo(frase, tipo="input"):
    tokens = len(frase) // 4
    preco  = INPUT_TOKEN_VALUE if tipo == "input" else OUTPUT_TOKEN_VALUE
    return tokens, tokens * preco

def send_text(text):
    global total_input_tokens, total_output_tokens, total_cost
    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=text
        )

        inp_tokens, inp_cost = calcular_custo(text, "input")
        out_tokens, out_cost = calcular_custo(response.text, "output")

        total_input_tokens += inp_tokens
        total_output_tokens += out_tokens
        total_cost += inp_cost + out_cost

        print(f"\n{G}✦ IA »{R} {response.text}")
        print(f"{DIM}{'─' * 42}{R}")
        print(f"{DIM}  tokens → entrada: {C}{inp_tokens}{R}{DIM} (${inp_cost:.6f}) · saída: {C}{out_tokens}{R}{DIM} (${out_cost:.6f}){R}\n")
       
    except Exception as e:
        print(f"\n{RED}✕ Erro ao contactar a API: {e}{R}\n")

def show_stats():
    print(f"\n{DIM}╔══════════════════════════════════════╗{R}")
    print(f"{DIM}║{R}  {BOLD}{B}Relatório da Sessão{R}{DIM}                 ║{R}")
    print(f"{DIM}╠══════════════════════════════════════╣{R}")
    print(f"{DIM}║{R}  Modelo          {M}{MODEL}{R}{DIM}    ║{R}")
    print(f"{DIM}║{R}  Tokens Entrada  {C}{total_input_tokens}{R}{DIM}                    {R}")
    print(f"{DIM}║{R}  Tokens Saída    {C}{total_output_tokens}{R}{DIM}                   {R}")
    print(f"{DIM}║{R}  Custo Total     {Y}${total_cost:.6f}{R}{DIM}           ║{R}")
    print(f"{DIM}╚══════════════════════════════════════╝{R}\n")

def help_menu():
    print(f"\n{DIM}  Comandos disponíveis:{R}")
    print(f"  {Y}/quit{R}   {DIM}Encerra o programa{R}")
    print(f"  {Y}/clear{R}  {DIM}Limpa o terminal{R}")
    print(f"  {Y}/stats{R}  {DIM}Exibe relatório da sessão{R}")
    print(f"  {Y}/help{R}   {DIM}Mostra este menu{R}\n")

os.system("clear")
banner()

while True:
    try:
        user_input = input(f"{Y}❯ {R}").strip()
    except (KeyboardInterrupt, EOFError):
        print(f"\n{RED}✦ Encerrando sessão. Até logo!{R}\n")
        break

    match user_input:
        case "/quit":
            print(f"\n{RED}✦ Encerrando sessão. Até logo!{R}\n")
            break
        case "/clear":
            os.system("clear")
            banner()
        case "/stats":
            show_stats()
        case "/help":
            help_menu()
        case "":
            pass
        case _:
            send_text(user_input)