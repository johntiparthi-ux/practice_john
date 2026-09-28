def validate_transaction(amount):
    return amount is not None and amount > 0

amount = 1500

print("Valid transaction" if validate_transaction(amount) else "Invalid transaction")
