# Custom Payload Encoder & Obfuscation Framework

A controlled cybersecurity laboratory project that demonstrates how reversible encoding and string transformations affect a simple static signature-matching detector.

## Features
- Base64 encoding and decoding
- ROT13 transformation
- XOR encoding and decoding
- String reversal
- Separator insertion/removal
- Escape-sequence representation
- Character splitting
- Basic signature detection
- CSV result reporting

## Requirements
- Python 3
- Linux/Kali Linux recommended
- No third-party Python packages required

## Run
```bash
python3 main.py
```

The program uses the harmless test string `DEMO_SIGNATURE_TEST` and stores results in `reports/results.csv`.

## Project Structure
- `main.py` - coordinates the framework
- `encoder.py` - Base64, ROT13 and XOR functions
- `obfuscator.py` - string transformation functions
- `detector.py` - basic signature-matching simulator
- `reporter.py` - CSV report generator

## Ethical Scope
This project uses harmless text strings and a locally implemented detector. It is intended only for authorized educational and defensive-security study. It does not interact with real malware or attempt to bypass production security products.
