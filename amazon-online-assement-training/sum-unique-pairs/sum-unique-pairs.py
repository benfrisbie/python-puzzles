import unittest

def sum_unique_pairs(nums, target):
    needed_nums = set()
    pairs = set()
    pair_count = 0

    for n in nums:
        diff = target - n

        if n in needed_nums and n not in pairs:
            pair_count += 1
            pairs.add(n)
            pairs.add(diff)
        
        needed_nums.add(diff)

    return pair_count


class Tests(unittest.TestCase):
    def test1(self):
        nums = [1, 1, 2, 45, 46, 46] 
        target = 47
        res = sum_unique_pairs(nums, target)
        self.assertEqual(res, 2)

    def test2(self):
        nums = [1, 1]
        target = 2
        res = sum_unique_pairs(nums, target)
        self.assertEqual(res, 1)

    def test3(self):
        nums = [1, 5, 1, 5]
        target = 6
        res = sum_unique_pairs(nums, target)
        self.assertEqual(res, 1)

    def test4(self):
        nums = [10]
        target = 10
        res = sum_unique_pairs(nums, target)
        self.assertEqual(res, 0)


if __name__ == '__main__':
    unittest.main()