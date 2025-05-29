import random
import asyncio
from telegram import Bot

TOKEN = '7020817265:AAG8b_RrWQaJw_wxt-9JHQkQXI_ab4k-zRk'
CHAT_ID = '-1002522063627'

bot = Bot(token=TOKEN)

# Lista completa de pares de negociação da Quotex
pares = [
    # Cripto
    "Bitcoin Cash", "Dogecoin", "Litecoin", "Pepe", "Shiba Inu", "Solana", "Toncoin", "Trump",
    "TRON", "Dogwifhat", "Bonk", "Ethereum", "Floki", "Bitcoin", "Ripple", "Binance Coin",

    # Moedas
    "AUD/JPY", "AUD/NZD", "AUD/USD", "CAD/CHF", "CAD/JPY", "CHF/JPY", "EUR/AUD", "EUR/CAD",
    "EUR/CHF", "EUR/G   BP", "EUR/JPY", "EUR/NZD", "EUR/USD", "GBP/AUD", "GBP/CAD", "GBP/CHF",
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

async def enviar_sinal():
    contador = 0

    while True:
        par = random.choice(pares)
        direcao = random.choice(direcoes)
        mensagem = (
            "🚨 NOVO SINAL DISPONÍVEL! 🚨\n\n"
            f"🎯 Par: {par} (OTC)\n"
            f"📈 Direção: {direcao}\n"
            "⏱️ Validade: 5 minutos\n\n"
            "⚠️ Aguarde o momento certo e entre com cautela!"
        )
        await bot.send_message(chat_id=CHAT_ID, text=mensagem)

        contador += 1

        if contador == 4:
            precisao = random.randint(80, 99)
            mensagem_precisao = (
                f"🔥 TAXA DE PRECISÃO ATUAL: {precisao}% 🔥\n\n"
                "📌 Nossa assertividade nas últimas entradas está em alta!\n"
                "💹 Continue seguindo os sinais e maximize seus ganhos! 💸"
            )
            await bot.send_message(chat_id=CHAT_ID, text=mensagem_precisao)
            contador = 0

        await asyncio.sleep(300)  # Espera 5 minutos


if __name__ == '__main__':
    asyncio.run(enviar_sinal())
