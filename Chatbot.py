def chat_response(user_input):
    user_input = user_input.lower()


    responses={
        "hello":"hi there how can i help you",
        "how are you":"i'm good, just enjoying the weather",
        "bye":"goodby have a great day",
        "what is your name":"my name is iceapple",
        
    }

    return responses.get(user_input, f"i am sorry i didn't get that\nplease repeat" )
def main():
    print("welcome lovely")
    while True:
        user_input = input("Timmy: ")
        if user_input.lower()=='bye' :
            print("chatbot: goodby and have a great day")
            break
        response= chat_response(user_input)
        print(f"chatbot: {response}")
if __name__=="__main__":
    main()