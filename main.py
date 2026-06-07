import os
from google import genai
from dotenv import load_dotenv


load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

MODEL = "gemini-2.5-flash"
INPUT_TOKEN_PRICE  = 0.000015
OUTPUT_TOKEN_PRICE = 0.000075

# ANSI
R="\033[0m"; BOLD="\033[1m"; DIM="\033[2m"
G="\033[92m"; Y="\033[93m"; B="\033[94m"; M="\033[95m"; C="\033[96m"; RED="\033[91m"

req_count     = 0
success_count = 0
fail_count    = 0
total_input_tokens  = 0
total_output_tokens = 0

def banner():
    print(f"{DIM}╔══════════════════════════════════════╗{R}")
    print(f"{DIM}║{R}  {BOLD}{B}Gemini CLI{R}  {DIM}·{R}  {M}{MODEL}{R}  {DIM}   ║{R}")
    print(f"{DIM}╚══════════════════════════════════════╝{R}")
    print(f"{DIM}  /quit · /clear · /stats · /help\n{R}")

def send_text(text):
    global req_count, success_count, fail_count
    global total_input_tokens, total_output_tokens
    try:
        response = client.models.generate_content(model=MODEL, contents=text)
        req_count     += 1
        success_count += 1
        # Contagem real de tokens via API (se disponível)
        usage = getattr(response, 'usage_metadata', None)
        inp = getattr(usage, 'prompt_token_count', 0) or 0
        out = getattr(usage, 'candidates_token_count', 0) or 0
        total_input_tokens  += inp
        total_output_tokens += out
        return response, inp, out
    except Exception as e:
        req_count  += 1
        fail_count += 1
        print(f"\n{RED}✕ Erro ao contactar a API: {e}{R}\n")
        return None, 0, 0

def print_token_info(inp, out):
    cost = inp * INPUT_TOKEN_PRICE + out * OUTPUT_TOKEN_PRICE
    print(f"{DIM}  tokens → entrada: {inp} · saída: {out}  |  custo: ${cost:.7f}{R}")

def stats_report():
    total = success_count + fail_count
    rate  = (success_count / total * 100) if total else 0
    cost  = total_input_tokens  * INPUT_TOKEN_PRICE \
          + total_output_tokens * OUTPUT_TOKEN_PRICE

    print(f"\n{DIM}╔══════════════════════════════════════╗{R}")
    print(f"{DIM}║{R}  {BOLD}{B}Relatório da Sessão{R}{DIM}                  ║{R}")
    print(f"{DIM}╠══════════════════════════════════════╣{R}")
    print(f"{DIM}║{R}  Auth          {G}API Key{R}{DIM}               ║{R}")
    print(f"{DIM}║{R}  Requisições   {B}{total}{R}  {G}✓{success_count}{R}  {RED}✕{fail_count}{R}{DIM}           ║{R}")
    print(f"{DIM}║{R}  Sucesso       {G}{rate:.1f}%{R}{DIM}                 ║{R}")
    print(f"{DIM}╠══════════════════════════════════════╣{R}")
    print(f"{DIM}║{R}  Modelo        {M}{MODEL}{R}{DIM}      ║{R}")
    print(f"{DIM}║{R}  Tokens Entrada {C}{total_input_tokens}{R}{DIM}                  ║{R}")
    print(f"{DIM}║{R}  Tokens Saída   {C}{total_output_tokens}{R}{DIM}                  ║{R}")
    print(f"{DIM}║{R}  Custo Total   {Y}${cost:.7f}{R}{DIM}            ║{R}")
    print(f"{DIM}╚══════════════════════════════════════╝{R}\n")

def help_menu():
    cmds = [
        ("/quit",  "Encerra o programa"),
        ("/clear", "Limpa o terminal"),
        ("/stats", "Exibe relatório da sessão"),
        ("/help",  "Mostra este menu"),
    ]
    print(f"\n{DIM}  Comandos disponíveis:{R}")
    for cmd, desc in cmds:
        print(f"  {Y}{cmd:<10}{R}{DIM}{desc}{R}")
    print()

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
            stats_report()
        case "/help":
            help_menu()
        case "":
            pass
        case _:
            response, inp, out = send_text(user_input)
            if response:
                print(f"\n{G}✦ IA »{R} {response.text}")
                print(f"{DIM}{'─' * 42}{R}")
                print_token_info(inp, out)
                print()