# Original Questions from Codewars

# Question 1: Counting Sheep...
# # Consider an array/list of sheep where some sheep may be missing from their place. We meed a function that counts the number of sheep present in the array (true means present).

# For Example:
# [True, True, True, False,
#  True, True, True, True,
#  True, False, True, False,
#  True, False, False, True,
#  True, True, True, True,
#  False, False, True, True
# ]

# The correct answer would be 17.
# Hint: Don't forget to check for bad values like null/undefined

# Answer:
# def count_sheep(sheep):
#     count = 0
#     for bah in sheep:
#         if bah == True:
#             count += 1
#     return count


# sheep = [True, True, True, False, True, True, True, True, True, False, True, False, True, False, False, True, True, True, True, True, False, False, True, True]

# Test Function
# count_sheep(sheep)


####################################################################################