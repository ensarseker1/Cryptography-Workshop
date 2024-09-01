def caesar_decrypt(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]
        # Decrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) - shift - 65) % 26 + 65)
        # Decrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) - shift - 97) % 26 + 97)
        # Decrypt digits
        elif char.isdigit():
            result += chr((ord(char) - shift - 48) % 10 + 48)
        # Other characters (punctuation, etc.) remain the same
        else:
            result += char
    return result

encrypted_text = "Xlmw irgvCtxih qiwweki wlepp gpevmjC lsA RSX xs irgvCtx e qiwweki xsheC! Izir mj mx Aew wyjjmgmirx efsyx 6444 Cievw eks, sv xs fi qsvi tvigmwi mr xli Ciev 88 FG, rsAeheCw mx mw rsx. XsheC iegl ws-geppih Wgvmtx Omhhmi Asyph fi efpi xs kix wirwmxmzi mrjsvqexmsr, mj xliC Aivi irgvCtxih xlmw AeC."

# Try all possible shifts
for shift in range(1, 26):
    decrypted_text = caesar_decrypt(encrypted_text, shift)
    print(f"Shift {shift}:\n{decrypted_text}\n")

