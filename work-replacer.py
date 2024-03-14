# Emoji Replacer
# Kate jiang
# 2/27/2024


def main():
    thing = input("Type something: ")
    thing = translate(thing)
    print(thing)

def translate(a: str):
    a = a.replace("100", "💯")
    a = a.replace("noodles", "🍜")
    return a

main()    