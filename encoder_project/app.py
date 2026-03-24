from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import os

from encoder import (
    base64_encode, xor_encode, calculate_entropy,
    random_insertion, split_payload, html_obfuscation
)

app = Flask(__name__)


def generate_plot(values):
    os.makedirs("static", exist_ok=True)

    labels = list(values.keys())
    scores = list(values.values())

    plt.figure(figsize=(6, 4))
    plt.style.use("dark_background")

    plt.bar(labels, scores)
    plt.title("Entropy Comparison")
    plt.ylabel("Entropy")

    plt.tight_layout()
    plt.savefig("static/plot.png")
    plt.close()


@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        payload = request.form.get("payload")
        key = request.form.get("key") or "default"

        # Encoding
        base64_data = base64_encode(payload)

        xor_raw = xor_encode(payload, key)
        xor_data = base64_encode(xor_raw)

        # Obfuscation
        obf_random = random_insertion(payload)
        obf_split = split_payload(payload)
        obf_html = html_obfuscation(payload)

        # Entropy
        entropies = {
            "Original": calculate_entropy(payload),
            "Base64": calculate_entropy(base64_data),
            "XOR": calculate_entropy(xor_data),
            "Random": calculate_entropy(obf_random),
            "Split": calculate_entropy(obf_split),
            "HTML": calculate_entropy(obf_html),
        }

        generate_plot(entropies)

        result = {
            "original": payload,
            "base64": base64_data,
            "xor": xor_data,
            "obf_random": obf_random,
            "obf_split": obf_split,
            "obf_html": obf_html,
            "entropy": entropies
        }

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)