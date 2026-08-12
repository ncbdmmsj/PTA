import re
def process(s):
    s = re.sub(r'\s+',' ',s).strip()
    s = re.sub(r'\s([!?.,\'])',r'\1',s)
    s = re.sub(r'[A-HJ-Z]', lambda x: x.group().lower(), s)
    s = re.sub(r'\bI\b', 'yoU', s)
    s = re.sub(r'\bme\b', 'yoU', s)
    s = re.sub(r'\bcan you\b', 'I can', s)
    s = re.sub(r'\bcould you\b', 'I could', s)
    s = s.replace('?', '!')
    s = s.replace('yoU', 'you')
    return s

n = int(input())
for _ in range(n):
    s = input()
    print(s)
    ai = process(s)
    print(f"AI: {ai}")
