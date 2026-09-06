# Crypto-analyzer

A simple Python script that **provides clear and updated data about crypto**, the version 1.0 just work with quote currencies
and crypto prices but in future versions the script will be able to provide more complex data! The entire process is based on the
free Coingecko API (more about it below).

---

### Requirements

* **Python 3.x** installed on your system.
* **Coingecko API**: the scripts works with both demo and premium APIs but the script is written with the free one, if you want
    to change it open the script with your editor and change 'x-cg-demo-api-key' with 'x-cg-pro-api-key' on line 47, 80 and 108.
    If you do not know where to create your API key, use this link: https://docs.coingecko.com/docs/setting-up-your-api-key and
    follow the instructions. **When you have done just copy your API key in the "api_key" variable on line 18**.
* **"requests" library**: you can easily download it by cloning or
    downloading the **"requirements.txt"** file and by typing in the cmd line:
  ```bash
   pip install -r requirements.txt
  ```


---

### Installation & Execution

There is no complex setup. Just download the script and run it directly from your terminal or editor.

1. **Download the script** (or clone the repository):
   ```bash
   git clone https://github.com/0xAn0m4ly/crypto-analyzer
   cd YOUR-REPO-NAME
   ```

2. **Run the program**:
   ```bash
   py crypto_analyzer.py
   ```

---

### ⚙️ How It Works
The entire process is based on http GET requests from the Coingecko servers.
Once started, the script will guide you through entering the required parameters, please follow the intructions.
