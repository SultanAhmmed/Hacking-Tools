# GhostGate

![image](https://github.com/user-attachments/assets/3f822cb4-ce15-4095-b04e-797a7dc29fb1)


GhostGate is a simple Python-based CLI utility to generate stealthy, mask‑style shortened URLs. By leveraging a custom shortening API and keyword‑injected mask patterns, your links vanish into the shadows and look more trustworthy (or intriguingly suspicious!).

## Features

* Shortens any URL via the [spoo.me](https://spoo.me) API
* Inject custom masking domains (default: `google.com`)
* Append one or multiple keywords for context (e.g., `login`, `auth`)
* Optionally set a human‑readable alias
* Cross‑platform terminal compatibility (Windows, macOS, Linux)

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)

   * [Interactive Mode](#interactive-mode)
   * [Arguments & Options](#arguments--options)
   * [Examples](#examples)
3. [Configuration](#configuration)
4. [Contributing](#contributing)
5. [License](#license)
6. [Author](#author)

## Installation

1. **Download the files**

   ```bash
   cd GhostGate
   ```

2. **Install dependencies**
   GhostGate relies on the `requests` library:

   ```bash
   pip install requests
   ```

3. **Make script executable (optional)**

   On Unix‑like systems (macOS, Linux):

   ```bash
   chmod +x ghostgate.py
   ```

## Usage

GhostGate runs in interactive CLI mode. Simply execute the script and follow the prompts.

### Interactive Mode

```bash
python ghostgate.py
```

Steps:

1. Enter the URL you want to mask (with or without `https://`).
2. Specify your masking domain (default: `google.com`).
3. Provide an optional custom alias (e.g., `spoo.me/my-alias`).
4. Enter one or more comma‑separated keywords (default: `login`).
5. Receive your masked URL!

### Arguments & Options

| Option             | Description                                          | Default      |
| ------------------ | ---------------------------------------------------- | ------------ |
| `url`              | The target URL to shorten and mask                   | *required*   |
| `--domain`, `-d`   | Masking domain                                       | `google.com` |
| `--alias`, `-a`    | Custom alias for the shortened link                  | *none*       |
| `--keywords`, `-k` | Comma‑separated list of keywords for the masked link | `login`      |

> **Note:** CLI flags are not yet implemented in the interactive script but are planned for future releases.

### Examples

```bash
# Basic usage
python ghostgate.py
# Input: example.com
# Domain: google.com
# Alias: (leave blank)
# Keywords: login,auth
# Output: https://google.com-login-auth@spoo.me/abc123

# With uppercase protocol
python ghostgate.py
# Input: https://longsite.org/path?query=1
# Domain: custom.com
# Alias: mylink
# Keywords: download
# Output: https://custom.com-download@mylink
```

## Configuration

You can customize default values by modifying constants at the top of `ghostgate.py`:

```python
DEFAULT_DOMAIN = "google.com"
DEFAULT_KEYWORDS = ["login"]
API_ENDPOINT = "https://spoo.me"
```

Future versions will support a configuration file (e.g., `config.yml`).

## Contributing

Contributions are welcome! To contribute:

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/YourFeature`)
3. Commit changes (`git commit -m "Add some feature"`)
4. Push to branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

Please follow the existing code style and include tests for new features.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

**Sultan Ahmmed**

* GitHub: [github.com/SultanAhmmed](https://github.com/SultanAhmmed)

---

*GhostGate – Your links vanish into the shadows...*
