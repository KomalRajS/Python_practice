#indexing - [start:end:step]

card_number = "1234-5678-9456-4567"

print(card_number[1])
print(card_number[1:4])
print(card_number[:5])
print(card_number[7:])
print(card_number[-1])
print(card_number[-5:-1])
print(card_number[::3])
print(card_number[1:8:6])

last_digits = card_number[-4:]
print(f"Your card number is XXXX-XXXX-XXXX-{last_digits}")
rev_num = card_number[::-1]
print(f"Reversed number = {rev_num}")