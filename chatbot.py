resp = {
    "hello" "hii": "Hlw how may i help you ?",
    "hlo": "Hey there! How's it going??",
    "hlw":  "hello What's up?",
    "hii": "hlo what's up ?",
    "how are you": "I'm good, thanks for asking..  what about you?",
    "good": "Good to hear this.. How can i help you?",
    "nothing": "umm.. okk☺️",
    "what are you doing": "just talking to you..😇",
    "who made you": "i am created by RVA,owner: adarsh singh",
    "where are you from": "india",
    "what is your name": "i'm Goldy(RVA)",
    "who is your owner": "my owner is Mr. Adarsh singh",
    "who is richest man on earth": "Elon musk",
    "who is founder of facebook": "mark juckerburg",
    "who is ceo of google": "sunder pichai",
    "who is pm of india": "shri Narendra damodar das modi",
    "what can you do": "I can give do like greetings, some facts, motivatio, some python programs(addition)(subtraction) and other..feel free to ask..☺️",
    "what you can do": "I can give do like greetings, some facts, motivatio, some python programs(addition)(subtraction) and other..feel free to ask..☺️",
    "2+2": "4",
    "what is the value of pi": "22/7 or 3.14",
    "tell me a joke": "your life... ☠️",
    "tell me a dark joke": "dark humour is like food everyone can't gets it...☠️",
    "what is the one motivaion you give": "you only have 2 options: \n 1. Either play safe and die with regrets or \n 2. Take risk and die with a story",
    "what is the criteria to vote in india": "to vote in india you have to 18 or plus",
    "can u solve math problems ?": "yeah bit very basic..",
    "what is 4 * 5": "20",
    "what is 100/5": "20",
    "give me some motivation": "sure:\nif you start...one thing is for sure you will not die with regret\nso just do it.. hope this give you a boost 😊",
    "i want to start a business what should i do":"pick something research about it and just start..good luck",
    "tell me an idea that can really go big": "sure: \n Pharmacy\n makeup for women\n agriculture new technogies\n low rate clother with good quality",
    "thanku": "wlcm have a nice day☺️",
    "thanks": "most welcome ☺️ feel free to ask..",
    "what do u think about ai": "ai is really great and it will gonna boost very much because of its capablities...",
    "create a python program of addition": "sure: \n def add(): \n inp = input('enter first number': )\n inp2= input('enter second number': )\n sum = inp + inp2\n print(sum)\n add())",
    "can u recommend me a book": "hard things by hard things, this book is really good.",
    "can u dance": "i can't, i am a virtual chatbot created By RVA , so i can only give you answers of some questions",
    "who is highest followed person on instagram": "cristiano ronaldo is highest followed person on instgram",
    "who is the goat of football": "cristiano and messi both are goat players..of football",
    "choose one": "messi because he have a world cup but, cristiano is also a very high goated player respect 🫡",
    "tell me one thing that can change my life": "just take risk and see the outcome you will never regret",
    "can u do calculations": "yes but a little bit",
    "can u speak": "i can't, i am a virtual chatbot created By RVA , so i can only give you answers of some questions",
    "who created you": "i am created by RVA owner Adarsh kumar singh",
    "tell me about your owner information":  "'sorry' i can't disclose my owner info or any other person's info as it's private thing 🙂",
    "what u can do that other ai can't": "for your clarification i am not an AI i am just a normal chatbot which can give answers of simple questions..",
    "tell me another joke": "Why did the astronaut break up with his girlfriend? \n Because he needed space!",
    "emoji": "😀😃😄😆🥹😅😂🤣🥲☺️😊😇🙂🙃😉😌😍🥰😘😗😙😚😋😛😝😜🤪🤨🧐🤓😎🥸🤩🥳🙂‍↕️😏😒🙂‍↔️😞😔😔😟😕🙁☹️😣😖😫😩🥺😢😭😤😠😡🤬🤯😳🥵🥶😶‍🌫️😱😨😰😥🤗🤔🫣🤭🫢🫡🤫🫠🤧🤤😑🫤",
    "give me some happy emoji": "sure:\n😀😃😄 ☺️😊😇",
    "give me some sad emoji": "sure:\n🥹😒😞😔😔",
    "i am sad": "ohh..don't be sad 🥹\n here is a joke that make u smile and make your day better ☺️😊\n Why don't skeletons fight each other?\nBecuse they don't have the guts! 😄\nHope that gave you a laugh!",
    "i am happy": "That's awesome!😊",
    "who is goat of cricket": "Sachin Tendulkar is often called the God of Cricket.",
    "describe yourself in one word": "learner",
    "tell me about yourself": "sure, I'm Goldy created by Rva and i answer some questions...and\n something big is coming soon..😎",
    "how to become a developer": "Becoming a developer is an exciting journey! Here's a general roadmap to help you get started:\n 1. Choose Your Path\n2. Learn the Basics of Programming\n3.Get Hands-On with Projects \n best of luck for your future😊",
    "okk": "☺️",
    "what is noun": "noun is a naming word",
    "what is adjective": "adjective is a word that describe noun or pronoun",
    "which is the highest polluted city in india ?": "delhi",
    "which is cleanest city in india": "indore(madhya pradesh).",
    "how many states in india": "28 states",
    "tell me some facts": "Sharks existed before trees!🥸",
    "when u were created": "i was created on March 01/2025",
    "what is your aim": "my aim to provide answers of your questions..",
    "how can i focus on one thing": "by meditation🧘🧘\nmeditation really help to improve mind and it really increase your ability to focus🧿",
    "which is the fastest programming language": "well c and c++ are considered as fastest programming language.",
    "which is faster python or c": "c but python is more powerful becuase it has so much use in ai and different fields also",
    "you are wrong": "i am basic chatbot so maybe i can be wrong sometime",
}
def chatbot():
    print("Hlo wclm to RVA chatbot..".title())
    print("don't use question mark for asking question.".title())
    print("use correct grammer for asking question.".title())
    while True:
        user_input = input("You: ").lower()
        if user_input in resp:
            print("Goldy: ", resp[user_input].title())
        elif user_input == "quit":
            print(" have a nice day..☺️".title())
            break    
        else:
            print("Sorry this is not in my memory Coming soon..., ask other question..\n make sure you used correct grammer.".title())
chatbot()            