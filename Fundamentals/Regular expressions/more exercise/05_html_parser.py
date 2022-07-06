import re

title_pattern = r"(?<=<title>)([^<>]*)(?=<\/title>)"
text = input()
title = re.findall(title_pattern, text)
print(f"Title: {' '.join(title)}")

body_pattern = r'<body>.*<\/body>'
body = re.findall(body_pattern, text)

content_pattern = r">([^><]*)<"
content = re.findall(content_pattern, ' '.join(body))
content = "".join(content)
content = content.replace("\\n", "")
print(f"Content: {content}")