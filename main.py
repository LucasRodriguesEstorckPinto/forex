import random
import asyncio
from telegram import Bot
from datetime import datetime
import pytz

# 🔑 Configurações
TOKEN = '7020817265:AAG8b_RrWQaJw_wxt-9JHQkQXI_ab4k-zRk'
CHAT_ID = '-1002522063627'

# Definir o fuso horário de São Paulo
fuso_sp = pytz.timezone('America/Sao_Paulo')

bot = Bot(token=TOKEN)

# 🔗 Lista de ativos e direções
pares = [
    # Cripto
    "Bitcoin Cash", "Dogecoin", "Litecoin", "Pepe", "Shiba Inu", "Solana", "Toncoin", "Trump",
    "TRON", "Dogwifhat", "Bonk", "Ethereum", "Floki", "Bitcoin", "Ripple", "Binance Coin",

    # Moedas
    "AUD/JPY", "AUD/NZD", "AUD/USD", "CAD/CHF", "CAD/JPY", "CHF/JPY", "EUR/AUD", "EUR/CAD",
    "EUR/CHF", "EUR/GBP", "EUR/JPY", "EUR/NZD", "EUR/USD", "GBP/AUD", "GBP/CAD", "GBP/CHF",
    "GBP/JPY", "GBP/NZD", "GBP/USD", "NZD/CAD", "NZD/CHF", "NZD/JPY", "NZD/USD", "USD/CAD",
    "USD/CHF", "USD/JPY",

    # Matérias-primas
    "Silver", "UKBrent", "USCrude", "Gold",

    # Ações
    "McDonald's", "Microsoft", "Pfizer", "Intel", "American Express", "Boeing", "Facebook",
    "Johnson & Johnson", "Dow Jones", "Nikkei 225", "NASDAQ 100", "S&P/ASX 200",
    "FTSE China A50 Index", "CAC 40", "FTSE 100", "Hong Kong 50", "IBEX 35", "EURO STOXX 50"
]

direcoes = ["↑ CALL - VAI SUBIR", "↓ PUT - VAI CAIR"]
expiracoes = ["M1", "M2", "M5", "M15"]

# 🎯 Relatório
wins = 0
losses = 0
total_operacoes = 0


async def enviar_sinal():
    global wins, losses, total_operacoes

    for _ in range(5):  # Número de sinais na sessão
        par = random.choice(pares)
        direcao = random.choice(direcoes)
        expiracao = random.choice(expiracoes)
        hora_atual = datetime.now(fuso_sp).strftime('%H:%M')

        # 📥 Mensagem de entrada
        mensagem_entrada = (
            "🚨 *ENTRADA CONFIRMADA!* 🚨\n\n"
            f"🎯 *ATIVO:* {par} (OTC)\n"
            f"⏳ *TEMPO:* {expiracao}\n"
            f"📈 *DIREÇÃO:* {direcao}\n"
            f"⏰ *HORÁRIO:* {hora_atual}\n\n"
            "[👉 Opere agora](https://broker-qx.pro/sign-up/?lid=1372744)\n\n"
        )

        # Envia a mensagem e captura o ID da mensagem
        msg = await bot.send_message(
            chat_id=CHAT_ID,
            text=mensagem_entrada,
            parse_mode="Markdown"
        )

        mensagem_id = msg.message_id  # Pegando o ID da mensagem enviada

        await asyncio.sleep(900)  # Espera 15 minutos simulando operação


        # 🏆 Resultado com 60% de chance de WIN
        resultado = "WIN" if random.random() < 0.6 else "LOSS"


        if resultado == "WIN":
            wins += 1
            await bot.send_photo(
                chat_id=CHAT_ID,
                photo=open('./win.png', 'rb'),
                reply_to_message_id=mensagem_id
            )
        else:
            losses += 1
            await bot.send_photo(
                chat_id=CHAT_ID,
                photo=open('./loss.png', 'rb'),
                reply_to_message_id=mensagem_id
            )

        total_operacoes += 1
        await asyncio.sleep(30)  # Pequena pausa antes do próximo sinal

    # 📊 Relatório final
    taxa_acerto = (wins / total_operacoes) * 100 if total_operacoes > 0 else 0

    mensagem_relatorio = (
        "📊 *RELATÓRIO DA SESSÃO*\n\n"
        f"✅ *WINS:* {wins}\n"
        f"❌ *LOSSES:* {losses}\n"
        f"🎯 *TAXA DE ACERTO:* {taxa_acerto:.2f}%\n"
        f"📈 *TOTAL DE OPERAÇÕES:* {total_operacoes}\n\n"
        "🚀 *Sessão finalizada! Rumo ao topo!*"
    )

    await bot.send_message(chat_id=CHAT_ID, text=mensagem_relatorio, parse_mode="Markdown")
    await asyncio.sleep(300)
    # 🔄 Resetar os contadores
    wins = 0
    losses = 0
    total_operacoes = 0


if __name__ == '__main__':
    asyncio.run(enviar_sinal())
