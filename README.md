# Payload Obfuscation & Encoding Tool (CLI)

## 1. Overview

This project is a Python-based command-line tool designed to demonstrate payload encoding and obfuscation techniques. It allows users to transform input payloads using multiple methods and analyze how these transformations affect structure and complexity.

The tool is built for educational purposes to understand how data can be transformed and how complexity changes through different techniques.

---

## 2. Features

### Encoding Techniques

* Base64 Encoding
* XOR Encoding (user-defined key)

### Obfuscation Techniques

* Random Character Insertion
* HTML Entity Encoding
* Strong Obfuscation (Reverse + Character Shift)
* Multi-layer Obfuscation (XOR → Base64 → Shift)

### Analysis

* Entropy calculation for each transformation
* Comparison of payload complexity

---

## 3. Project Structure

```
.
└── script.py
```

---

## 4. Requirements

* Python 3.x
* No external libraries required

---

## 5. Usage

Run the script:

```
python3 script.py
```

Enter input when prompted:

```
Enter Payload: <your payload>
Enter XOR Key (default: key):
```

---

## 6. Example

### Input

```
<script>alert(1)</script>
```

### Output Includes

* Base64 encoded payload
* XOR encoded payload
* Randomly obfuscated payload
* HTML encoded payload
* Strong obfuscated payload
* Multi-layer obfuscated payload

Each transformation also includes entropy values.

---

## 7. Entropy Analysis

Entropy measures the randomness or complexity of a string.

* Low entropy → readable and predictable
* High entropy → more complex and less readable

This helps in understanding how transformations increase payload complexity.

---

## 8. Use Cases

* Learning encoding and obfuscation techniques
* Understanding payload transformation
* Analyzing data complexity
* Practicing Python scripting

---

## 9. Limitations

* This tool does not execute payloads
* No real-world detection or evasion testing
* Techniques are implemented for educational purposes only



