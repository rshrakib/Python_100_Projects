class VocabularyFlashCard:
    def __init__(self):
        self.flashcard = {}

    def add_flashcard(self, word, meaning):
        self.flashcard[word] = meaning

    def quiz(self):
        if not self.flashcard:
            print("No flashcards available. please add flashcards.")
            return
        print("Starting vocabulary quiz.....")
        for word, meaning in self.flashcard.items():
            user_input = input(f"what does '{word}' meaning? Enter your ans: ").strip().lower()

            if user_input == meaning.lower():
                print("correct")
            else:
                print(f"Wrong! the correct meaning of '{word}' is '{meaning}'")

    def review_flashcard(self):
        if not self.flashcard:
            print("No flashcards available. please add flashcard")
            return
        print("Reviewing vocabulary flashcard: ")
        for word, meaning in self.flashcard.items():
            print(f"Word: {word} - meaning: {meaning}")

flashcard_app = VocabularyFlashCard()
flashcard_app.add_flashcard('Apple', 'Fruit')
flashcard_app.add_flashcard('Car', 'Vehicle')

flashcard_app.quiz()

flashcard_app.review_flashcard()