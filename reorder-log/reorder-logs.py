import unittest

def reorder_logs(logs):
    reordered_letters = dict()
    reordered_digits = list()
    reordered = list()

    for log in logs:
        words = log.split(" ")
        if words[1].isdigit():
            reordered_digits.append(log)
        else:
            reordered_letters[' '.join(words[1:])] = log

    for letters in sorted(reordered_letters.keys()):
        reordered.append(reordered_letters[letters])

    return reordered + reordered_digits
    



class Tests(unittest.TestCase):
    def test1(self):
        logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
        expected = ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
        self.assertEqual(reorder_logs(logs), expected)

if __name__ == "__main__":
    unittest.main()