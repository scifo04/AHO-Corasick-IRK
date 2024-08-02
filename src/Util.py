def get_suffix (text: str):
    liste = []
    lens = len(text)
    for i in range(1,lens):
        texte = text[i:]
        liste.append(texte)
    return liste

def find_match(suffixes: list, prefixes: list):
    for i in range(len(suffixes)):
        for j in range(len(prefixes)):
            if (suffixes[i] == prefixes[j]):
                return suffixes[i]
    return ""