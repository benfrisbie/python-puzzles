import unittest

def top_k_keywords(reviews, keywords, k):
    keyword_count = {}
    keywords.sort()
    for keyword in [keyword.lower() for keyword in keywords]:
        keyword_count[keyword] = 0
        for review in reviews:
            if keyword in review.lower():
                keyword_count[keyword] += 1

    tops = []
    for i in range(k):
        top = max(keyword_count, key=keyword_count.get)
        tops.append(top)
        keyword_count.pop(top)

    return tops


class Tests(unittest.TestCase):
    def test1(self):
        k = 2
        keywords = ["anacell", "cetracular", "betacellular"]
        reviews = [
          "Anacell provides the best services in the city",
          "betacellular has awesome services",
          "Best services provided by anacell, everyone should use anacell"
        ]
        res = top_k_keywords(reviews, keywords, k)
        self.assertEqual(res, ["anacell", "betacellular"])

    def test2(self):
        k = 2
        keywords = ["anacell", "betacellular", "cetracular", "deltacellular", "eurocell"]
        reviews = [
            "I love anacell Best services; Best services provided by anacell",
            "betacellular has great services",
            "deltacellular provides much better services than betacellular",
            "cetracular is worse than anacell",
            "Betacellular is better than deltacellular."
        ]
        res = top_k_keywords(reviews, keywords, k)
        print(res)
        self.assertEqual(res, ["betacellular", "anacell"])

    def test3(self):
        k = 3
        keywords = ["eurocell", "deltacellular", "cetracular", "betacellular", "anacell"]
        reviews = [
            "I love anacell Best services; Best services provided by anacell",
            "betacellular has great services",
            "deltacellular provides much better services than betacellular",
            "cetracular is worse than anacell",
            "Betacellular is better than deltacellular."
        ]
        res = top_k_keywords(reviews, keywords, k)
        print(res)
        self.assertEqual(res, ["betacellular", "anacell", "deltacellular"])


if __name__ == '__main__':
    unittest.main()