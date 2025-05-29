import random
import asyncio
from telegram import Bot

TOKEN = '7020817265:AAG8b_RrWQaJw_wxt-9JHQkQXI_ab4k-zRk'
CHAT_ID = '-1002522063627'

bot = Bot(token=TOKEN)

# Lista completa de pares de negociação da Quotex extraídos das imagens
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

direcoes = ["↑ CALL", "↓ PUT"]

async def enviar_sinal():
    while True:
        par = random.choice(pares)
        direcao = random.choice(direcoes)
        mensagem = f"📊 SINAL GERADO:\nPar: {par} (OTC)\nEntrada: {direcao}\n⏱️ Validade: 5 minutos"
        await bot.send_message(chat_id=CHAT_ID, text=mensagem)
        await asyncio.sleep(120)  # Espera 5 segundos

if __name__ == '__main__':
    asyncio.run(enviar_sinal())
