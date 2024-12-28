class Quiz:
    def __init__(self):
        self.questions = []

    def add_question(self, question, choices, correct_ans):
        self.questions.append({
            'question': question,
            'choices': choices,
            'correct_ans': correct_ans
            })

    def take_quiz(self):
        score = 0
        total_questions = len(self.questions)

        for i,q in enumerate(self.questions, start=1):
            print(f"Questions {i}: {q['question']}")
            for idx, choice in enumerate(q['choices'], start=1):
                print(f"{idx}. {choice}")

            ans = input("Enter you choice (1,2,3,4): ")

            if ans.isdigit():
                user_ans = int(ans) - 1
                if 0 <= user_ans < len(q['choices']):
                    if q['choices'][user_ans] == q['correct_ans']:
                        score+=1

        print(f"\n You scored {score} out of {total_questions}")

my_quiz = Quiz()

my_quiz.add_question("what is the sum of 1+2?", ["1","2", "3", "4"], "3")
my_quiz.add_question("what is the sum of 1+3?", ["1","2", "3", "4"], "4")
my_quiz.take_quiz()
