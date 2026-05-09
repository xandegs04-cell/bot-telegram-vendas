from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# ================= CONFIGURAÇÕES =================
TOKEN = "8790503034:AAHSTzB5uiGpdN4DhrLenVvJxbgNa6BaNYE"

# Sua chave Pix
MINHA_CHAVE_PIX = "3a362b35-db5e-4123-87d0-d8ed3cabe1b2"

# Seu @ no Telegram (sem o @) para receber o comprovante
MEU_USUARIO = "xandegs04" 

FOTO = "https://famosasnuas.net/catarina-paolino-ruiva-do-tiktok-so-de-calcinha/"
GRUPO_VIP = "https://t.me/+QpgHUO0MjnlkZDBh"
# =================================================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = """
🔥 **VIP COM 50% OFF** 🔥

🍑 As melhores do Privacy
🔞 As melhores do OnlyFans
👑 Conteúdo exclusivo e diário

**Escolha seu plano abaixo:**
"""
    botoes = [
        [InlineKeyboardButton("📆 MENSAL R$15", callback_data="mensal")],
        [InlineKeyboardButton("📆 3 MESES R$25", callback_data="3meses")],
        [InlineKeyboardButton("👑 VITALÍCIO R$50", callback_data="vitalicio")]
    ]
    
    # Se for comando /start novo, manda foto. Se for "voltar", edita a legenda.
    if update.message:
        await update.message.reply_photo(
            photo=FOTO,
            caption=texto,
            reply_markup=InlineKeyboardMarkup(botoes),
            parse_mode="Markdown"
        )
    else:
        query = update.callback_query
        await query.edit_message_caption(
            caption=texto,
            reply_markup=InlineKeyboardMarkup(botoes),
            parse_mode="Markdown"
        )

async def plano(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    dados = {
        "mensal": ("MENSAL", "R$15"),
        "3meses": ("3 MESES", "R$25"),
        "vitalicio": ("VITALÍCIO", "R$50")
    }
    
    nome_plano, valor = dados[query.data]

    texto_checkout = f"""
💎 **Plano: {nome_plano}**
🔥 Promoção 50% OFF
💰 **Valor: {valor}**

💳 **PAGAMENTO VIA PIX**

Chave Pix:
`{MINHA_CHAVE_PIX}`

⚠️ **Instruções:**
1. Faça o pagamento do valor acima.
2. Clique no botão abaixo para **ENVIAR O COMPROVANTE**.
3. Após o envio, eu te liberarei o link do grupo!
"""
    botoes = [
        [InlineKeyboardButton("📤 ENVIAR COMPROVANTE", url=f"https://t.me/{MEU_USUARIO}")],
        [InlineKeyboardButton("⬅️ VOLTAR", callback_data="voltar")]
    ]

    await query.edit_message_caption(
        caption=texto_checkout,
        reply_markup=InlineKeyboardMarkup(botoes),
        parse_mode="Markdown"
    )

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(start, pattern="voltar"))
    app.add_handler(CallbackQueryHandler(plano))
    
    print("BOT ONLINE - CONTEÚDO PRIVACY/ONLY")
    app.run_polling()
