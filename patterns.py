patterns_responses = [
    (r'Hi|Hello|Hey', ['Hello!', 'Hi there!', 'Hey, how can I assist you today?']),
    (r'Good morning', ['Good morning! How can I help you today?']),
    (r'Good evening', ['Good evening! What can I do for you?']),
    (r'How are you?', ['I am doing well, thank you!', 'I am good, how about you?']),
    (r'What’s up?', ['Not much, just waiting to assist you!', 'I am ready to help!']),
    (r'Hey there', ['Hey! How can I assist you?']),
    (r'Yo', ['Yo! How can I help you today?']),
    (r'Hi there', ['Hello! How can I assist you?']),
    (r'Hola', ['¡Hola! ¿Cómo puedo ayudarte?']),
    (r'Bonjour', ['Bonjour! Comment puis-je vous aider?']),
    (r'Howdy', ['Howdy! How can I help?']),
    (r'Goodbye|Bye|See you later', ['Goodbye! Have a nice day!', 'See you later! Take care!']),
    (r'Thank you|Thanks', ['You are welcome!', 'Glad I could help!']),
    (r'What is your name?', ['My name is ChatBot, nice to meet you!']),
    (r'Who are you?', ['I am ChatBot, your virtual assistant!']),
    (r'What can you do?', ['I can assist you with information, answer questions, and have a friendly chat!']),
    (r'How are you doing?', ['I’m doing great! Thanks for asking. How about you?']),
    (r'Good night', ['Good night! Sweet dreams!']),
    (r'Bye bye', ['Take care! See you next time!']),
    (r'Please', ['Sure! What can I do for you?', 'I’ll be happy to help!']),
    (r'Sorry', ['No worries! How can I assist you?', 'It’s okay! What do you need help with?']),
    (r'Excuse me', ['How can I assist you?', 'What can I do for you?']),
    (r'Thank you so much', ['You are most welcome! Glad I could help!']),
    (r'You are awesome', ['Thanks! You are awesome too!']),
    (r'You are amazing', ['Thank you! You are fantastic as well!']),
    (r'You’re welcome', ['Thank you! Always happy to help!']),

#     time and date

    (r'What time is it?', ['I am unable to tell the time, but you can check your device!']),
    (r'Tell me the time', ['Sorry, I can’t provide the current time. You can check it on your device!']),
    (r'What’s the date today?', ['I’m not sure about the date, but you can check your calendar!']),
    (r'Tell me the date', ['I don’t know the exact date. Please check your device for the details.']),
    (r'What day is it today?', ['Sorry, I can’t tell you the exact day. Please refer to your device!']),

#     #### 4. **Weather**


        (r'What’s the weather like?', ['I don’t have real-time weather updates, but you can check it on your phone!']),
        (r'Is it raining?', ['I don’t know the weather right now, but you can check your weather app!']),
        (r'Will it snow?', ['I can’t predict snow, but you can check a weather app for that!']),
        (r'What’s the temperature?', ['I cannot fetch the temperature, but weather apps can provide that information!']),
        (r'Weather forecast', ['Unfortunately, I cannot fetch live weather forecasts. Try a weather website!']),
        (r'Is it sunny today?', ['I can’t check the sun right now. Try using a weather app for updates!']),

    # #### 5. **Small Talk and Humor**

        (r'Tell me a joke', ['Why don’t skeletons fight each other? They don’t have the guts!']),
        (r'Make me laugh', ['What do you call fake spaghetti? An impasta!']),
        (r'Can you tell a funny story?', ['Sure! Once there was a computer who lost its memory… and it couldn’t remember anything!']),
        (r'Tell me a riddle', ['What has keys but can’t open locks? A piano!']),
        (r'Can you make a pun?', ['I’m reading a book on anti-gravity. It’s impossible to put down!']),
        (r'Tell me something funny', ['Why don’t eggs tell jokes? Because they might crack up!']),
        (r'Why did the chicken cross the road?', ['To get to the other side! Classic!']),

    # #### 6. **Mathematical and General Knowledge Queries**

        (r'What is your favorite number?', ['I don’t have a favorite number, but I think 42 is pretty cool!']),
        (r'What is 5 + 5?', ['5 + 5 is 10!']),
        (r'What is 10 times 3?', ['10 times 3 is 30!']),
        (r'Who invented the lightbulb?', ['Thomas Edison is credited with inventing the practical lightbulb!']),
        (r'What is the capital of France?', ['The capital of France is Paris!']),
        (r'Who won the world series in 2020?', ['The Los Angeles Dodgers won the 2020 World Series!']),
        (r'What is the tallest mountain?', ['Mount Everest is the tallest mountain on Earth!']),
        (r'What is the largest ocean?', ['The Pacific Ocean is the largest ocean on Earth!']),
        (r'Who is the president of the USA?', ['As of 2021, Joe Biden is the president of the United States!']),
        (r'What is the speed of light?', ['The speed of light is approximately 299,792 kilometers per second!']),

    # #### 7. **Personal Questions**

        (r'What is your name?', ['I am ChatBot, your friendly virtual assistant!']),
        (r'Who are you?', ['I am ChatBot! I am here to assist you with anything you need!']),
        (r'How old are you?', ['I am timeless! I don’t age, I just assist!']),
        (r'Where do you live?', ['I live in the cloud, where everything is data!']),
        (r'What do you like to do?', ['I like helping people like you and answering all sorts of questions!']),
        (r'What is your favorite color?', ['I don’t have a favorite color, but I think blue is quite nice!']),
        (r'What is your favorite food?', ['I don’t eat, but pizza sounds pretty great, don’t you think?']),


    #### 8. **Knowledge and Learning**

        (r'Can you help me with my homework?', ['Sure! What do you need help with?']),
        (r'Tell me something new', ['Did you know that honey never spoils? Archaeologists found pots of honey in ancient tombs!']),
        (r'Can you teach me something?', ['I’d love to! What do you want to learn today?']),
        (r'What is artificial intelligence?', ['Artificial intelligence is the simulation of human intelligence in machines.']),
        (r'Can you help me with coding?', ['Yes! What programming language are you working with?']),
        (r'What is Python?', ['Python is a popular programming language that is easy to learn and great for various applications!']),
        (r'What is machine learning?', ['Machine learning is a type of AI that allows computers to learn from data and improve over time!']),
        (r'Can you solve a math problem?', ['Sure! Please tell me the problem, and I will help you solve it!']),
        (r'What is deep learning?', ['Deep learning is a subset of machine learning that uses neural networks to analyze data!']),


    #### 9. **User Help and Assistance**

        (r'Can you help me?', ['Of course! How can I assist you today?']),
        (r'I need help', ['I’m here to help! What do you need assistance with?']),
        (r'Can you answer questions?', ['Yes, feel free to ask me anything!']),
        (r'I need support', ['I am here to provide support. How can I help you?']),
        (r'Help me please', ['Sure! What do you need help with?']),
        (r'Can you assist me?', ['Absolutely! What can I assist you with?']),
        (r'How can you assist me?', ['I can answer questions, tell jokes, help with knowledge, and much more!']),


    #### 10. **Miscellaneous**

        (r'What is the meaning of life?', ['The meaning of life is to live it to the fullest!']),
        (r'What is love?', ['Love is a deep feeling of affection for someone or something!']),
        (r'What is happiness?', ['Happiness is a state of well-being and contentment!']),
        (r'What is success?', ['Success is achieving the goals you set out to accomplish!']),
        (r'What is your purpose?', ['My purpose is to assist and provide helpful responses to your questions!']),
        (r'Are you a robot?', ['I am a chatbot, designed to assist you with all your queries!']),
        (r'Can you think?', ['I process and generate responses based on patterns, but I don’t truly "think" like humans!']),
        (r'Can you feel?', ['I don’t have feelings, but I can simulate empathy and provide helpful responses!']),
        (r'Are you real?', ['I am a program created to assist and provide information, but I am as real as your questions!']),
        (r'Can you learn?', ['I can adapt and improve through patterns, but I am not capable of learning in the human sense!']),
]
