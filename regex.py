import re

phoneNumRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")

# mo = phoneNumRegex.search("My number is 903-016-3612")
#
# print(mo.group())
#
# phoneNumRegex = re.compile(r"(\d\d\d)-(\d\d\d-\d\d\d\d)")
#
# mo = phoneNumRegex.search("My number is 903-016-3612")
#
# print(mo.group(2))

#matching a specific number of repetition.
batRegex = re.compile(r"Spider(wo)+man")
mo = batRegex.search("The adventure of the one and only Spiderman")
if mo == None:
    print("None")
else:
    print(mo.group())

#Phone numbers that matches the regex country code.

# phoneRegex = re.compile(r"(\d\d\d-)?\d\d\d-\d\d\d\d")
#
# mo = phoneRegex.search("My phone number is 016-3612. Call me tomorrow sweetheart.")
# print(mo.group())
