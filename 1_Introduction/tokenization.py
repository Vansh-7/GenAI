import tiktoken

encoder = tiktoken.encoding_for_model('gpt-4o')

# vocab size => unique words type
vocab_size = encoder.n_vocab
print("Vocab Size: ",  vocab_size) # 2,00,019 (200K)

# encoding
text = "The cat sat on the mat"
tokens = encoder.encode(text) #Encoding:  [976, 9059, 10139, 402, 290, 2450]
print("Encoding: ", tokens)

# decoding
my_tokens = [976, 9059, 10139, 402, 290, 2450]
decoded = encoder.decode(my_tokens)
print("Decoded: ", decoded) #Decoded:  The cat sat on the mat