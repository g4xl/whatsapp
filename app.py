from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/whatsapp", methods=['POST'])
def whatsapp_reply():
    msg = request.form.get('Body').strip().lower()
    resp = MessagingResponse()
    reply = ""

    if msg == "وصول":
        reply = "تفاصيل تعليمات الوصول والدخول الذاتي..."
    elif msg == "توصيل":
        reply = "تفاصيل تعليمات دخول مناديب الطلبات وفتح الباب الخارجي لهم اون لاين..."
    elif msg == "حجز":
        reply = "تفاصيل طريقة الحجز السريع للوحدات..."
    elif msg == "شروط":
        reply = "تفاصيل شروط الإقامة بشكل مختصر..."
    elif msg == "مرافق":
        reply = "تفاصيل المرافق وكيفية الاستخدام..."
    elif msg == "روابط":
        reply = "الروابط قيد الإنشاء، يرجى المحاولة لاحقاً."
    else:
        reply = (
            "للوصول السريع للتعليمات اختر من القائمة التالية:\n"
            "*وصول* لتعليمات الوصول والدخول الذاتي.\n"
            "*توصيل* لتعليمات دخول مناديب الطلبات وفتح الباب الخارجي لهم اون لاين.\n"
            "*حجز* تعليمات طريقة الحجز السريع للوحدات.\n"
            "*شروط* لمعرفة شروط الإقامة بشكل مختصر.\n"
            "*مرافق* تعليمات مختصرة عن المرافق وكيفية الاستخدام\n"
            "*روابط* تحت الإنشاء"
        )

    resp.message(reply)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
