def longest_chain(w):
    words = set()
    for word in w:
        words.add(word)
    max_chain = 0
    for word in words:
        if len(word) <= max_chain: # skip word if it cannot be greater than max_chain
            continue
        max_candidate = find_longest_chain(word, words, 0, [ 0 ])
        max_chain = max(max_candidate, max_chain)
    return max_chain

def find_longest_chain(word, words, current_chain, max_chain):
    if word not in words: # set: O(1) --> better than list: O(n)
        return 0
    current_chain += 1
    max_chain[0] = current_chain
    for i in range(len(word)):
        new_word = word[:i] + word[i+1:]
        find_longest_chain(new_word, words, current_chain, max_chain)
    return max_chain[0]

if __name__ == "__main__":
    w = [ "a",  "b",  "ba", "bca", "bda", "bdca" ]
    print(longest_chain(w))
    w = [ "bdcafg", "bdcaf", "a",  "b",  "ba", "bca", "bda", "bdca" ]
    print(longest_chain(w))
