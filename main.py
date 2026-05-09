from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8790503034:AAHSTzB5uiGpdN4DhrLenVvJxbgNa6BaNYE"

PIX = "3a362b35-db5e-4123-87d0-d8ed3cabe1b2"

FOTO = "https://famosasnuas.net/catarina-paolino-ruiva-do-tiktok-so-de-calcinha/"

GRUPO_VIP = "https://t.me/+QpgHUO0MjnlkZDBh"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    texto = """
🔥 VIP COM 50% OFF 🔥

📊 Sinais todos os dias
💰 Alta taxa de acerto
👑 Comunidade exclusiva

Escolha seu plano:
"""

    botoes = [
        [InlineKeyboardButton("📆 MENSAL R$15", callback_data="mensal")],
        [InlineKeyboardButton("📆 3 MESES R$25", callback_data="3meses")],
        [InlineKeyboardButton("👑 VITALÍCIO R$50", callback_data="vitalicio")]
    ]

    reply_markup = InlineKeyboardMarkup(botoes)

    await update.message.reply_photo(
        photo=FOTO,
        caption=texto,
        reply_markup=reply_markup
    )


async def plano(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    if query.data == "mensal":
        valor = "R$15"
        plano = "MENSAL"

    elif query.data == "3meses":
        valor = "R$25"
        plano = "3 MESES"

    elif query.data == "vitalicio":
        valor = "R$50"
        plano = "VITALÍCIO"

    texto = f"""
💎 Plano: {plano}

🔥 Promoção 50% OFF

💰 Valor: {valor}

💳 PAGAMENTO VIA PIX

Chave Pix:
{PIX}

Após pagar envie o comprovante.
"""

    botoes = [
        [InlineKeyboardButton("📤 ENVIAR COMPROVANTE", url="https://t.me/SEU_USUARIO")],
        [InlineKeyboardButton("👑 ENTRAR NO VIP", url=GRUPO_VIP)]
    ]

    reply_markup = InlineKeyboardMarkup(botoes)

    await query.edit_message_caption(
        caption=texto,
        reply_markup=reply_markup
    )


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(plano))

print("BOT ONLINE")

app.run_polling()
