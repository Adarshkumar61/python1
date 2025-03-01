resp = {
    "hello": "hii, how are you?",
    "how are you": "I'm good, thanks for asking..",
    "good": "Good to hear this.. How can i help you?",
    "what is your name": "i'm Goldy(R**)",
    "who is your owner": "my owner is Mr. Adarsh singh",
    "who is richest man on earth": "Elon musk",
    "who is founder of facebook": "mark juckerburg",
    "who is ceo of google": "sunder pichai",
    "who is pm of india": "shri Narendra damodar das modi",
    "what can you do": "I can give basic answers like Greetings, my name and some GK, ceo and etc..."
    #dont use question mark
}
def chatbot():
    while True:
        user_input = input("You: ").lower()
        if user_input in resp:
            print("Goldy: ", resp[user_input])
        else:
            print("Sorry this is not in my memory Coming soon..., ask another question..")
chatbot()            