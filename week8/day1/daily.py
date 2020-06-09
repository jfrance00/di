# Write a Python class to get all possible unique subsets from a set of distinct integers.
# Example:
# Input : [4, 5, 6]
# Expected Output : [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]]

class Numbers():

     def powerset(set):
        result = [[]]
        for x in set:
            new_subset = [subset + [x] for subset in result]
            result.extend(new_subset)
        return result


list = [1,2,3,4]
# print(Numbers.powerset(list))



class ZeroSum():

    def powerset(set):
        result = [[]]
        for x in set:
            new_subset = [subset + [x] for subset in result]
            result.extend(new_subset)
        return result

    def list_of_three(powerset):
        three_item_list = []
        for item in powerset:
            if len(item) == 3:
                three_item_list.append(item)
        return three_item_list

    def sums_zero(subset):
        all_zeros = []
        for item in subset:
            if item[0] + item[1] + item[2] == 0:
                all_zeros.append(item)
        return all_zeros



test = [1,-5, 8, 4, 9]
test_powerset = ZeroSum.powerset(test)
threes = ZeroSum.list_of_three(test_powerset)
print(ZeroSum.sums_zero(threes))



