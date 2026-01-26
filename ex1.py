import re
patterns = [
    ("[0-9]+", "I started with 0 confidence but completed 100 successful projects."),
    ("[A-Z][a-z]+", "Virudhunagar Boys Create History"),
    ("[aeiou]+", "Simple coding practice session"),
    ("[a-z]+@[a-z]+\.com", "Contact me at developer@google.com")
]
for pattern, text in patterns:
    print("Pattern:",pattern)
    print("Text:",text)
    matches=re.findall(pattern,text)
    if matches:
        print("Matches found:",matches)
    else:
        print("No matches found")
