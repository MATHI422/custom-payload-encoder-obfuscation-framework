SIGNATURES = [
    "DEMO_SIGNATURE",
    "TEST_PAYLOAD",
    "LAB_PATTERN"
]


def detect(text):
    found = []

    for signature in SIGNATURES:
        if signature.lower() in text.lower():
            found.append(signature)

    return found
