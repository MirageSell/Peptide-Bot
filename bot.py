import os
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo, Update
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(level=logging.INFO)

TOKEN = os.environ.get("BOT_TOKEN")
WEBAPP_URL = "https://miragesell.github.io/Peptide/"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [[
        InlineKeyboardButton(
            text="⚗️ Ouvrir le Calculateur",
            web_app=WebAppInfo(url=WEBAPP_URL)
        )
    ]]
    await update.message.reply_text(
        "👋 Bienvenue sur le *Calculateur Dosage Peptide* !\n\n"
        "1️⃣ Sélectionne ton peptide\n"
        "2️⃣ Entre la quantité du flacon et le volume d'eau\n"
        "3️⃣ Entre ta dose souhaitée\n"
        "4️⃣ Choisis ta seringue\n"
        "➡️ Le nombre d'unités s'affiche instantanément !\n\n"
        "⚗️ _Usage laboratoire uniquement._",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

if __name__ == "__main__":
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    logging.info("Bot démarré...")
    app.run_polling()
