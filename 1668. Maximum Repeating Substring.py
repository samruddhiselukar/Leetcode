class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        # We start with res = 0.
        # This is our counter to track how many times word repeats.
        res = 0

        '''
        This is an infinite loop (while True) that we break manually.

        Inside the loop, we check if word repeated res times is a substring of sequence.

        In Python, word * res repeats the word res times.

        For example:

        if res = 1, word * res = word

        if res = 2, word * res = word + word

        If this repeated word is not in sequence, then clearly the previous value of res was the answer. So we return res - 1.

        Otherwise, if it is found, we increment res and try again.
        '''
        while True:
            if word * res not in sequence:
                return res - 1
            res += 1

        return res
