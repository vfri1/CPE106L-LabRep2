import random
def getWords(filename):
    try:
        with open(filename, "r") as file:
            words = [line.strip().upper() for line in file if line.strip()]
        return tuple(words)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return ()
      
articles = getWords("articles.txt")
nouns = getWords("nouns.txt")
verbs = getWords("verbs.txt")
prepositions = getWords("prepositions.txt")

def sentence():
    return nounPhrase() + " " + verbPhrase()
def nounPhrase():
    return random.choice(articles) + " " + random.choice(nouns)
def verbPhrase():
    return random.choice(verbs) + " " + nounPhrase() + " " + \
           prepositionalPhrase()
def prepositionalPhrase():
    return random.choice(prepositions) + " " + nounPhrase()
  
def main():
    if not (articles and nouns and verbs and prepositions):
        print("Error: Unable to generate sentences due to missing vocabulary.")
        return
    number = int(input("Enter the number of sentences: "))
    for count in range(number):
        print(sentence())
if __name__ == "__main__":
    main()
