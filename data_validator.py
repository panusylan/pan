LIQUIDITY_THRESHOLD = 30000

def is_valid_token(contract_address, liquidity):
    try:
        liquidity_value = int(liquidity.replace("$", "").replace("K", "000"))
        return liquidity_value >= LIQUIDITY_THRESHOLD
    except ValueError:
        return False
