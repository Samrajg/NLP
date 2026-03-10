from collections import Counter

text = "the cat sat on the mat"
words = text.split()

bg = list(zip(words, words[1:]))
bg_counts = Counter(bg)
unigram_counts = Counter(words)

vocabulary = set(words)
V = len(vocabulary)

def get_smoothed_prob(word1, word2):
    count_bg = bg_counts.get((word1, word2), 0)
    count_unigram = unigram_counts.get(word1, 0)
    smoothed_prob = (count_bg + 1) / (count_unigram + V)
    return smoothed_prob

word_a, word_b = "the", "cat"
prob = get_smoothed_prob(word_a, word_b)
print(f"Smoothed Probability of '{word_b}' after '{word_a}': {prob:.4f}")

word_c = "dog"
prob_zero = get_smoothed_prob(word_a, word_c)
print(f"Smoothed Probability of '{word_c}' after '{word_a}' (Unseen): {prob_zero:.4f}")