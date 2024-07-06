from funcs import get_welcome_msg

print(get_welcome_msg("Omar", 12))

"""
import time
t1 = time.time()
for i in range(5):
    print(f"Message {i}: {get_welcome_msg('Youssef', 'CTO')}")
t2 = time.time()
print(f"Total time using approach 1: {t2 - t1} secs")
print("*************************************")

t1 = time.time()
m1 = get_welcome_msg("Youssef", "CTO")
for i in range(5):
    print(f"Message 1: {m1}")

t2 = time.time()
print(f"Total time using approach 2: {t2 - t1} secs")

m2 = get_welcome_msg("Yassin", "CEO")
print(f"New Message: {m2}")
"""