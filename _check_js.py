from pathlib import Path

t = Path(r"D:\DIGIPOR\index.html").read_text(encoding="utf-8")
start = t.find("<script>")
end = t.rfind("</script>")
js = t[start + 8 : end]
print("js length", len(js))
print("start repr", repr(js[:40]))
idx = 0
while True:
    idx = js.find("Repekkal", idx)
    if idx == -1:
        break
    snippet = js[idx : idx + 14]
    print(idx, snippet, [hex(ord(c)) for c in snippet])
    idx += 1
