## Example usage:
```
apt update && apt install tesseract-ocr tesseract-ocr-eng python3-pip libglvnd-dev jq && \
python3 -m pip install --upgrade pip && \
pip install --user --break-system-packages dawshs_jff && \
python3 -m dawshs_jff.scripts.jff http://20.240.40.44 --code 3fc077ba | jq
```
