print("#", True or True, True or False, False or True, False or False)
# True True True False

print("#", 0 or False or 0.0 or 2 or True or "3" or 5.0)
# 2

print("#", 0 or False or 0.0)
#0.0

default_text="World!"
user_name=""
print("# Hello", user_name or default_text or 5/0)
# Hello World!
