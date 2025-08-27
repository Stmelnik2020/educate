# user_input = input("Entry some text: ")
# break_command = input("Entry break command: ")


# def talking(sentence: str, exit_word: str) -> str:
#     """
#     creates a loop to input strings
#     """
#     while True:
#         if sentence.lower() != exit_word.lower():
#             print(f"You write: {sentence}")
#             new_sentence = input(f"Entry some more text (if you want to stop the program type {exit_word}): ") 
#             talking(new_sentence, break_command)
#             break
#         else:
#             print ("loop end")
#             break

# talking(user_input, break_command)

#-------------------------------------------------

# user_input = input("Type some text: ")
# break_command = input("Type break command: ")

# while user_input:
#     if user_input.lower() != break_command.lower():
#         print(f"You write {user_input}")
#         user_input = input(f"Type some more text (to stop type {break_command.lower()}): ")
#     else:
#         print("Loop end")
#         break

#-------------------------------------------------

user_input = input("Type some text: ")

while user_input:
    print(f"You write {user_input}")
    user_input = input(f"Type some more text: ")