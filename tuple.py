import math
import random
import statistics
import keyword
import cubed
import emoji

nums = [125, 26, 30, 50, 80, 15, 67, 95, 125]
print(math.pow(12, 14))
print(random.randint(100, 200))
print(statistics.mean(nums))
print(statistics.mode(nums))
print(statistics.median(nums))
print("GMean", statistics.geometric_mean(nums))

print(cubed.makeCube(100))

print(keyword.iskeyword("for"))
print(keyword.iskeyword("fortran"))

print(emoji.emojize(":thumbs_up:"))
