resp = {
    "hello" "hii": "Hlw how may i help you ?",
    "hlo": "hello how can i assist you ?",
    "hlw":  "hello how can i assist you ?",
    "how are you": "I'm good, thanks for asking..  what about you?",
    "good": "Good to hear this.. How can i help you?",
    "what is your name": "i'm Goldy(RVA)",
    "who is your owner": "my owner is Mr. Adarsh singh",
    "who is richest man on earth": "Elon musk",
    "who is founder of facebook": "mark juckerburg",
    "who is ceo of google": "sunder pichai",
    "who is pm of india": "shri Narendra damodar das modi",
    "what can you do": "I can give basic answers like Greetings, my name and some GK, ceo and etc...",
    "2+2": "4",
    "tell me a joke": "your life... ☠️",
    "tell me a dark joke": "dark humour is like food everyone can't gets it...☠️",
    "what is the one motivaion you give": "you only have 2 options: \n 1. Either play safe and die with regrets or \n 2. Take risk and die with a story",
    "what is the criteria to vote in india": "to vote in india you have to 18 or plus",
    "can u solve math problems ?": "yeah bit very basic..",
    "what is 4 * 5": "20",
    "what is 100/5": "20",
    "i want to start a business what should i do":"pick something research about it and just start..good luck",
    "tell me an idea that can really go big": "sure: \n Pharmacy\n makeup for womens\n agriculture new technogies\n low rate clother with good quality",
    "thanku": "wlcm have a nice day☺️",
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
    "what u can do that other ai can't": "for your clarification i am not an AI i am just a normal chatbot which can give answers of simple questions..",
    "tell me another joke": "Why did the astronaut break up with his girlfriend? \n Because he needed space!"
    #dont use question mark
}
def chatbot():
    print("Hlo wclm to RVA chatbot..".title())
    print("don't use question mark for asking question.".title())
    print("use correct grammer for asking question.".title())
    while True:
        user_input = input("You: ").lower()
        if user_input in resp:
            print("Goldy: ", resp[user_input])
        elif user_input == "quit":
            print(" have a nice day..☺️")
            break    
        else:
            print("Sorry this is not in my memory Coming soon..., ask another question..")
chatbot()            