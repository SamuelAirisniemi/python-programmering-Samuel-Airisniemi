import re

sentence = "Pure mathematics is, in its way, the poetry of logical ideas"
vowels = re.findall(r"[aeiouyAEIOUY]", sentence)

print(f"There are {len(vowels)} vowels in this sentece.")