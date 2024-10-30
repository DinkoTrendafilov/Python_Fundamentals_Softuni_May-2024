messages = input().split()

final_message = []

for message in messages:
    number = ""
    current_message = ""
    for char in message:
        if char.isdigit():
            number += char
        else:
            break
    message = message.replace(number, "")
    number = int(number)
    current_message += chr(number)
    if len(message) >= 2:
        message = message[-1] + message[1:-1] + message[0]
    current_message += message
    final_message.append(current_message)

print(*final_message)
