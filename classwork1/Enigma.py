
encoder = {'a': 'b', 'b':'k' , 'c': 'g'}
decoder = {'b': 'a', 'k':'b', 'g': 'c'}
message=[]
decoded=[]
def enigma(letters,encoder):
    for letter in letters:
        letter=encoder[letter]
        message.append(letter)
    return message
def my_decoder(encoded_message,decoder):
    for let in encoded_message:
        let=decoder[let]
        decoded.append(let)
    return decoded

encoded_message=enigma('cab',encoder)
decoded_message=my_decoder(encoded_message,decoder)
encoded_message=''.join(encoded_message)
decoded_message=''.join(decoded_message)
my_string = 'encoded message = ' + encoded_message + ' decoded_message = ' + decoded_message
print(my_string)