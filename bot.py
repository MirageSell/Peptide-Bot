import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo, Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.environ.get("BOT_TOKEN")
WEBAPP_URL = "https://miragesell.github.io/Peptide/"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[
        InlineKeyboardButton(
            text="⚗️ Ouvrir le Calculateur",
            web_app=WebAppInfo(url=WEBAPP_URL)
        )
    ]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "👋 Bienvenue sur le *Calculateur Dosage Peptide* !\n\n"
        "Cet outil te permet de calculer instantanément le volume à prélever "
        "pour tes peptides de recherche.\n\n"
        "📋 *Comment ça marche :*\n"
        "1️⃣ Sélectionne ton peptide\n"
        "2️⃣ Entre la quantité dans le flacon et le volume d'eau ajouté\n"
        "3️⃣ Entre ta dose souhaitée\n"
        "4️⃣ Choisis ta seringue\n"
        "➡️ Le nombre d'unités s'affiche instantanément !\n\n"
        "⚗️ _Usage laboratoire uniquement — non destiné à l'usage humain._",
        parse_mode="Markdown",
        reply_markup=reply_markup
    )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot démarré...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
