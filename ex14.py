from sys import argv

script, user_name = argv
prompt = '>'

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(f"{user_name}{prompt}")

print(f"Where do you live {user_name}?")
lives = input(f"{user_name}{prompt}")

print(f"What kind of computer do you have?")
computer = input(f"{user_name}{prompt}")

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer}. Nice.
""")
