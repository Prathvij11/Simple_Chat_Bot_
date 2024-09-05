import datetime


class SimpleChatbot:
    def __init__(self):       
        self.responses = {
            "hi": "Hello! How can I help you today?",
            "hello": "Hi there! What can I do for you?",
            "how are you": "I'm just a program, but thanks for asking! How about you?",
            "what's your name": "I'm a simple chatbot created to help you.",
            "bye": "Goodbye! Have a great day!",
            "time": self.get_time(),
            
            "default": "Sorry, I don't understand that. Can you please rephrase?"
        }

    def get_time(self):
        now = datetime.datetime.now()
        return now.strftime("%H:%M:%S")



    def get_response(self,user_input):
        user_input = user_input.lower()
       

        for key in self.responses:
            if key in user_input:
                return self.responses[key]
            elif "time" in self.responses:
                return self.get_time()
            else:
                self.responses["default"]
    


chatbot = SimpleChatbot()
    
print("Chatbot: Hello! Type something to start the conversation (type 'bye' to exit).")
    
while True:
       
    user_input = input("You: ")

    response = chatbot.get_response(user_input)
        
        
    print("Chatbot:", response)
 