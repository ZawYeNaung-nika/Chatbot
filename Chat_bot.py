import nltk
from nltk.chat.util import Chat, reflections
pairs = [
    [
        r"မင်္ဂလာပါ|Hi|Hello",
        ["မင်္ဂလာပါ Simbolo မှ ကြိုဆိုပါတယ်"],
    ],
    [
        r"သင်တန်း|အတန်း|တတ်ချင်လို့ပါ|အပ်ချင်လိုပါ",
        ["AI အတန်းရယ် Data Science အတန်းလေးရယ်ရှိပါတယ်"],
    ],
    [
        r"AI| Artificial Intelligence|အတန်း|သင်တန်း|တတ်ချင်လို့ပါ|အပ်ချင်လိုပါ",
        ["Artificial Intelligence အတန်းမှာဆို Python Programming ကနေ Applied NLP,Computer Vision အထိ အတန်း (၆) တန်းရှိပါတယ်"],
    ],
    [
        r"DS|Data Science|အတန်း|သင်တန်း|တတ်ချင်လို့ပါ|အပ်ချင်လိုပါ",
        ["Data Science အတန်းမှာဆို Python programming သင်တန်းကနေ Power BI အထိ အတန်း(၇)တန်းရှိပါတယ်"],
    ],
    [
        r"ကာလ|အချိန်|အချိန်ကာလ ဘယ်လောက်ကြာနိုင်လဲ| ဘယ်လောက်တတ်ရမလဲ|ဘယ်လောက်တတ်ရမလဲ",
        ["Pathway တစ်ခုစီ အပြီးထိတတ်မည်ဆိုပါက တစ်နှစ်ကြာနိုင်ပါတယ်။ Pathway များမှ သင်တန်းတစ်ခုစီဆိုရင် (၂) ခန့်ကြာမြင့်ပါမည်။"],
    ],
    [
        r"အတန်းကြေး|class|class ကြေး|Course|Course Fee|Fee|ဘယ်လောက်လဲ|သိပါရစေ|သိချင်ပါတယ်",
        ["သင်တန်းကြေးကတော့ မြန်မာငွေ - ၂၀,၀၀၀/-ကျပ်ကျသင့်ပါမည်ဖြစ်ပြီး Kpay၊ Wavepay ဖြင့် ပေးချေနိုင်ပါသည်။"],
    ],
    [
        r"သင်ကြားပုံ|class system|သင်ကြားရေးစနစ် က ဘယ်လိုလဲ|ဘယ်လိုသင်တာလဲ",
        ["သင်တန်:ရဲ့ သင်ကြားပုံက တစ်ပတ်ကို နှစ်ရက် zoom  မှ သင်ကြားပြီး Google Class မှာ record ပြန်တင်ပေးပြီး Assignment System ဖြစ်လို့ ပုံမှန် Assignment တင်ပေးပြီး Project တစ်ခုတင်ပေးရပါတယ်"],
    ],
    [
        r"Thank| ပြောပြလို့|ရှင်းပြပေးလို့ |ဖြေကြားပေးလို့|ကျေးဇူးပါ|ကျေးဇူး|နားလည်ပါပြီ",
        ["ဟုတ်ကဲ့စိတ်ဝင်စားလိုကျေးဇူးပါ။ အကယ်၍ သိချင်တာတစ်ခုရှိပါက မေးထားလို့ရပါတယ်။ Admin လာတဲ့အခါ ဖြေ‌ကြားပေးပါ့မယ်"],
    ],
]

#define pronuns
reflections = {
    "ကျွန်တော်": "အကိုရေ",
    "ကျွန်မ": "အမရေ",
    "ငါ": "မင်း",
    "Bro": "Bro",
    "Sis": "Sis",
    "အကိုရေ": "ကျွန်တော်",
    "အမရေ": "ကျွန်မ",
    "မင်း": "ငါ",
    "Bro": "Bro",
    "Sis": "Sis"
}
chatbot = Chat(pairs, reflections)
def burmese_chatbot():
    print("မင်္ဂလာပါ! Simbolo သင်တန်းမှ ဆိုကြိုပါတယ်။ 'bye' လို့ရိုက်ပါက ပြီးဆုံးပါမည်")
    while True:
        user_input = input("You:  ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye!")
            break
        responses = chatbot.respond(user_input)
        print("Chatbot: ", responses)
    chatbot.converse()


if __name__ == "__main__":
    burmese_chatbot()