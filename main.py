from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# ================= CONFIGURAÇÕES =================
TOKEN = "8790503034:AAHSTzB5uiGpdN4DhrLenVvJxbgNa6BaNYE"

# Sua chave Pix
MINHA_CHAVE_PIX = "3a362b35-db5e-4123-87d0-d8ed3cabe1b2"

# Seu @ no Telegram (sem o @)
MEU_USUARIO = "xandegs04" 

# CONFIGURAÇÃO DE MÍDIA
# Cole o link do vídeo abaixo (precisa ser link direto .mp4)
VIDEO_URL = "https://files.catbox.moe/btcjb8.mp4"
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
    
    reply_markup = InlineKeyboardMarkup(botoes)

    if update.message:
        try:
            # TENTA MANDAR O VÍDEO
            await update.message.reply_video(
                video=VIDEO_URL,
                caption=texto,
