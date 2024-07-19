from profanity_check import predict, predict_prob

text = "This is a sample sentence with some profanity."

# Check if the text contains profanity
contains_profanity = predict([text])

# Get the probability of profanity in the text
profanity_probability = predict_prob([text])

print(f"Contains profanity: {contains_profanity}")
print(f"Profanity probability: {profanity_probability}")
