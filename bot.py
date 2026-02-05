from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

# ================== CONFIG ==================
TOKEN = "8583870158:AAHbsfYhgmmvLWxZeoAqm2shjcqyxBW2_wU"

CONTACT_PHONE = "+256-755029410"
CONTACT_EMAIL = "lubegamatthew58@gmail.com"
CONTACT_WHATSAPP = "https://wa.me/256755029410"

# ================== COMMANDS ==================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["1️⃣ What we do", "2️⃣ Prices"],
        ["3️⃣ How to get started", "4️⃣ Contact"],
        ["5️⃣ Business hours", "6️⃣ Location"]
    ]

    reply_markup = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )

    await update.message.reply_text(
        "👋 Welcome to *ChatFlow Africa* 🤖\n\n"
        "We help businesses automate customer conversations.\n\n"
        "👇 Choose an option below:",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

# ================== MESSAGE HANDLER ==================
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if "1" in text:
        await update.message.reply_text(
            "🤖 *What We Do*\n\n"
            "• Telegram & WhatsApp bots\n"
            "• Customer support automation\n"
            "• Lead capture & follow-ups\n"
            "• Business chat automation",
            parse_mode="Markdown"
        )

    elif "2" in text:
        await update.message.reply_text(
            "💰 *Prices*\n\n"
            "• Basic Bot: UGX 150,000\n"
            "• Business Bot: UGX 300,000\n"
            "• Custom Automation: Negotiable",
            parse_mode="Markdown"
        )

    elif "3" in text:
        await update.message.reply_text(
            "🚀 *How to Get Started*\n\n"
            "1️⃣ Tell us your business type\n"
            "2️⃣ We design your bot\n"
            "3️⃣ You approve\n"
            "4️⃣ Bot goes live 🔥",
            parse_mode="Markdown"
        )

    elif "4" in text:
        await update.message.reply_text(
            f"📞 *Contact Us*\n\n"
            f"📱 Phone: {CONTACT_PHONE}\n"
            f"📧 Email: {CONTACT_EMAIL}\n"
            f"💬 WhatsApp: {CONTACT_WHATSAPP}",
            parse_mode="Markdown"
        )

    elif "5" in text:
        await update.message.reply_text(
            "🕒 *Business Hours*\n\n"
            "Monday – Saturday\n"
            "8:00 AM – 8:00 PM",
            parse_mode="Markdown"
        )

    elif "6" in text:
        await update.message.reply_text(
            "📍 *Location*\n\n"
            "Kampala, Uganda 🇺🇬\n"
            "Serving all of Africa 🌍",
            parse_mode="Markdown"
        )

    else:
        await update.message.reply_text(
            "❓ Please choose an option from the menu or type /start"
        )

# ================== MAIN ==================
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 ChatFlow Africa bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
