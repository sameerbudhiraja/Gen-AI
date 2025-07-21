# tiktoken library for python for tokenization
import tiktoken

# encoder -> convert the input into tokens
encoder = tiktoken.encoding_for_model("gpt-4o")

input = "hello, i'm sameer"

# encoder.encode -> encode the input into the tokens
token = encoder.encode(input)

print("Input encoded in tokens : " , token)
# output :-
# [24912, 11, 49232, 2684, 259]


# encoder.decode -> decodes the tokens into the real text input 
print("Token decoded in input : " , encoder.decode(token))


# Input encoded in tokens :  [24912, 11, 49232, 2684, 259]
# Token decoded in input :  hello, i'm sameer