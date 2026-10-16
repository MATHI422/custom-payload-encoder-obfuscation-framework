from encoder import *
from obfuscator import *
from detector import detect
from reporter import save_results

text = "DEMO_SIGNATURE_TEST"

print("Original:", text)

print("\n--- Encoding ---")

b64 = base64_encode(text)
print("Base64:", b64)
print("Base64 decoded:", base64_decode(b64))

rot = rot13(text)
print("ROT13:", rot)
print("ROT13 decoded:", rot13(rot))

xor = xor_encode(text, 7)
print("XOR:", xor)
print("XOR decoded:", xor_decode(xor, 7))

print("\n--- Obfuscation ---")

rev = reverse_text(text)
print("Reversed:", rev)
print("Restored:", reverse_text(rev))

sep = add_separator(text)
print("Separated:", sep)
print("Restored:", remove_separator(sep))

escaped = escape_text(text)
print("Escaped:", escaped)
print("Restored:", unescape_text(escaped))

split_value = split_text(text)
print("Split:", split_value)

print("\n--- Detection Test ---")

print("Original:", detect(text))
print("Base64:", detect(b64))
print("ROT13:", detect(rot))
print("XOR:", detect(xor))
print("Reversed:", detect(rev))
print("Separated:", detect(sep))
print("Escaped:", detect(escaped))
print("Split:", detect(split_value))

results = [
    ["Original", text, bool(detect(text))],
    ["Base64", b64, bool(detect(b64))],
    ["ROT13", rot, bool(detect(rot))],
    ["XOR", xor, bool(detect(xor))],
    ["Reversed", rev, bool(detect(rev))],
    ["Separated", sep, bool(detect(sep))],
    ["Escaped", escaped, bool(detect(escaped))],
    ["Split", split_value, bool(detect(split_value))]
]

save_results("reports/results.csv", results)

print("\nReport saved to reports/results.csv")
