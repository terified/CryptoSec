# 🐍 **Zlib & Base64 / Marshal Decoder**

> **Python Obfuscation Decoder Tool**  
> Created with ❤️ by [@IPLegion](https://t.me/IPLegion) & [@ferotier](https://t.me/ferotier)


![screenshot of tool]([https://cdn.discordapp.com/attachments/1349497155764879548/1369702746613223454/image.png?ex=681cd296&is=681b8116&hm=c979809028ada63fb9e78915bbea43068f686a285f6d0c025314727adbcb846a&])

---

## 📦 **Installation**  

1. **Clone the repository from GitHub:**

    ```bash
    git clone https://github.com/terified/CryptoSec.git
    ```

2. **Navigate to the tool's directory:**

    ```bash
    cd CryptoSec
    ```

3. **Install the required modules:**

    ```bash
    python install_modules.py
    ```

4. **Run CryptoSec:**

    ```bash
    python main.py
    ```

---

## 📖 **How to Use**

### 🔓 **Decode Zlib & Base64**

1. Copy the obfuscated string from your Python file.

2. Open the following file:
    - `C:\Users\Alex\Desktop\CryptoSec\base64_zlib_decode.txt`

3. Paste your obfuscated string in this format:
    ```python
    exec((_)(b'your_encoded_string_here'))
    ```

   **Example:**
   ```python
   _ = lambda __ : __import__('zlib').decompress(__import__('base64').b64decode(__[::-1]))
   exec((_)(b'VeryObfuscatedBase64String=='))
Run the decoder script — it will automatically read from base64_zlib_decode.txt and save the result.

**🔓 Decode Marshal, Gzip, Lzma, Zlib & Base64**
Copy the obfuscated string from your file.

Paste it into any .txt file.

Provide the path to this file when prompted by the decoder program.

**📌 Example:**
_=lambda __:__import__('marshal').loads(__import__('gzip').decompress(__import__('lzma').decompress(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])))))
exec(_('AnotherObfuscatedString'))

**🎨 Authors**
@IPLegion

@ferotier

**🖤 Support**
If you like this tool — leave a ⭐ on the repo and follow the authors!
