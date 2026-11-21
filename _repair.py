"""
Repair picture.py: fix all mojibake caused by PowerShell encoding corruption.
Reads as UTF-8, applies byte-level corrections, writes back as clean UTF-8 (no BOM).
"""
import pathlib, re

src = pathlib.Path("picture.py")

# Read raw bytes so we can do proper byte-level repair
raw = src.read_bytes()

# Strip UTF-8 BOM if present
if raw.startswith(b'\xef\xbb\xbf'):
    raw = raw[3:]

# The file was written as UTF-8 but then read+rewritten as Windows-1252 (cp1252)
# by PowerShell's Set-Content. This double-encoded every multi-byte UTF-8 sequence.
# Strategy: decode as latin-1 to get the raw bytes back, then re-encode as UTF-8.
# We do this carefully: decode as latin-1 (lossless), then fix the double-encoded spans.

text = raw.decode('latin-1')

# Re-encode each character as latin-1 bytes, then decode the whole thing as UTF-8
# to undo the double-encoding. We do this in chunks to handle mixed content.
fixed_bytes = text.encode('latin-1')
try:
    fixed = fixed_bytes.decode('utf-8')
except UnicodeDecodeError:
    # Some sections may already be correct UTF-8 strings stored as latin-1.
    # Use 'replace' as fallback and then clean up replacement chars.
    fixed = fixed_bytes.decode('utf-8', errors='replace')

# Additional cleanup: remove null-adjacent garbage control bytes that crept in
# (0x8d, 0x8f, 0x90 etc. are Windows-1252 private-use chars with no UTF-8 meaning)
fixed = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f\x80-\x9f]', '', fixed)

# Remove BOM-like sequences that may appear mid-string
fixed = fixed.replace('\ufeff', '')

# Write back as clean UTF-8, no BOM
src.write_text(fixed, encoding='utf-8')
print(f"Done. File size: {len(fixed):,} chars")

# Quick sanity check
non_ascii = [(hex(ord(c)), c) for c in sorted(set(fixed)) if ord(c) > 127]
print(f"Unique non-ASCII chars remaining: {len(non_ascii)}")
# Show any that look suspicious (Latin-1 range 0x80-0xFF excluding proper Unicode)
suspicious = [(h, c) for h, c in non_ascii if 0x80 <= ord(c) <= 0xFF]
if suspicious:
    print("Suspicious chars (may still be mojibake):", suspicious[:10])
else:
    print("No suspicious Latin-1 range chars — encoding looks clean.")
