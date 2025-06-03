def calculate_parity_bits(data_bits):
    m = len(data_bits)
    r = 0
    while (2 ** r) < (m + r + 1):
        r += 1
    n = m + r
    code = ['0'] * n
    j = 0
    for i in range(1, n + 1):
        if (i & (i - 1)) == 0:
            continue
        code[i - 1] = data_bits[j]
        j += 1

    for i in range(r):
        parity_pos = 2 ** i
        parity = 0
        for j in range(1, n + 1):
            if j & parity_pos and j != parity_pos:
                parity ^= int(code[j - 1])
        code[parity_pos - 1] = str(parity)

    return ''.join(code)

def detect_and_correct(received):
    n = len(received)
    r = 0
    while (2 ** r) < (n + 1):
        r += 1

    error_pos = 0
    for i in range(r):
        parity_pos = 2 ** i
        parity = 0
        for j in range(1, n + 1):
            if j & parity_pos:
                parity ^= int(received[j - 1])
        if parity != 0:
            error_pos += parity_pos

    corrected = list(received)
    if error_pos > 0 and error_pos <= len(received):
        corrected[error_pos - 1] = '1' if received[error_pos - 1] == '0' else '0'
    return ''.join(corrected), error_pos
