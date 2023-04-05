class CaesarCipher:
    def __init__(self, shift):
        self.shift = shift

    def transform_message(self, message, prefix):
        ignore = [' ', '.', '!', '?', '[', ']', 
                  '(', ')', '-', '_', ':', ';']
        new_message = ''
        message = message.upper()
        for letter in message:
            if letter in ignore:
                letter = ord(letter)
            else:
                if prefix == '+':
                    letter = (ord(letter) + self.shift) % 26 + ord('A')
                else:
                    letter = (ord(letter) - self.shift) % 26 + ord('A') if ord(letter) in range(65,91) else ord(letter)
            new_message += chr(letter)
        return new_message

cipher = CaesarCipher(3)
message = 'This is a simple message to test things. I hope everything works!'
e_message = cipher.transform_message(message, '+')
print(e_message)
d_message = cipher.transform_message(e_message, '-')
print(d_message)
