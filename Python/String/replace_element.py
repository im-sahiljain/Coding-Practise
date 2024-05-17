s = 'Sahil jain my name'
news = ""
for i in range(len(s)):
    if s[i] == " ":
        news += "*"
    else:
        news += s[i]

print(news)
