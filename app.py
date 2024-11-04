import os
from flask import Flask, request, jsonify
from twilio.twiml.messaging_response import MessagingResponse
from dotenv import load_dotenv

# تحميل متغيرات البيئة من ملف .env
load_dotenv()

app = Flask(__name__)

# إعدادات Twilio
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_WHATSAPP_NUMBER = os.getenv('TWILIO_WHATSAPP_NUMBER')

@app.route('/whatsapp', methods=['POST'])
def whatsapp_reply():
    """Respond to incoming messages with a friendly reply."""
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()

    # منطق الردود الآلية
    if 'مرحبا' in incoming_msg or 'hello' in incoming_msg:
        response = "أهلاً! كيف يمكنني مساعدتك اليوم؟"
    elif 'مساعدة' in incoming_msg or 'help' in incoming_msg:
        response = "هذه قائمة بالأوامر المتاحة:\n1. معلومات\n2. دعم\n3. اتصل بنا"
    elif 'معلومات' in incoming_msg or 'info' in incoming_msg:
        response = "نحن نقدم أفضل الخدمات لدعم أعمالك."
    else:
        response = "عذرًا، لم أفهم طلبك. اكتب 'مساعدة' لرؤية الأوامر المتاحة."

    msg.body(response)
    return str(resp)

if __name__ == '__main__':
    app.run(debug=True)
