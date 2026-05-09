from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# ================= CONFIGURAÇÕES =================
TOKEN = "8790503034:AAHSTzB5uiGpdN4DhrLenVvJxbgNa6BaNYE"
MINHA_CHAVE_PIX = "3a362b35-db5e-4123-87d0-d8ed3cabe1b2"
MEU_USUARIO = "xandegs04" 

# MÍDIA
VIDEO_URL = "https://cdn.discordapp.com/attachments/1462641309264248832/1502795489370964148/0509_1.gif?ex=6a0102dd&is=69ffb15d&hm=a4dcc47751fc980cdeda8a98da8d61a14ca675fa9fc20131417134c312de4526&"
FOTO_BACKUP = "https://famosasnuas.net/catarina-paolino-ruiva-do-tiktok-so-de-calcinha/"
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
    
    markup = InlineKeyboardMarkup(botoes)

    if update.message:
        try:
            # Tenta mandar o vídeo
            await update.message.reply_video(
                video=VIDEO_URL,
                caption=texto,
                reply_markup=markup,
                parse_mode="Markdown"
            )
        except:
            # Se o vídeo falhar (link bloqueado), manda a foto
            await update.message.reply_photo(
                photo=FOTO_BACKUP,
                caption=texto,
                reply_markup=markup,
                parse_mode="Markdown"
            )
    else:
        query = update.callback_query
        await query.edit_message_caption(
            caption=texto,
            reply_markup=markup,
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
    app.run_polling()
