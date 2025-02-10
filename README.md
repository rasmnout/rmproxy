# RMproxy v1.0.1

**RMproxy** je proxy nástroj určený pro kyberbezpečnost a zabezpečení.

## 📖 Nápověda
Spusťte příkaz pro zobrazení nápovědy:
```sh
mproxy -h  # nebo
mproxy --help
```

## ⚡ Instalace

### Instalace přes PIP
Pokud chcete nainstalovat RMproxy jednoduše přes PIP, použijte:
```sh
sudo pip3 install rmproxy
```
Pokud narazíte na chybu, zkuste:
```sh
sudo pip3 install rmproxy --break-system-packages
```

### Ruční instalace
Pokud chcete RMproxy nainstalovat manuálně, postupujte takto:
```sh
git clone https://github.com/rasmnout/rmproxy
cd rmproxy
python3 setup.py sdist bdist_wheel
pip3 install .
```

---
📌 **RMproxy je součástí Rasmnout Tools**

