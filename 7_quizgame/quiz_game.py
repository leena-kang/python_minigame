import time
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer 
    

prompts = [
    'What are the bubbly edges of a french macaron called? \na) ridges \nb) foot \nc) bumps \nd) none of the above\n',
    'Why bang  piped macaron batter on surface? \na) release air bubbles \nb) flatten them \nc) release stress \nd) you don\'t have to\n',
    'What temp should you bake your macarons? \na) 350F \nb) 300F \nc) 290F \nd)varies\n', 
    'When should you bake your macarons? \na) in daylight \nb) asap \nc) doesn\'t matter \nd) when skin is formed\n'
    
]

questions = [
    Question(prompts[0], 'b'),
    Question(prompts[1], 'a'),
    Question(prompts[2], 'd'),
    Question(prompts[3], 'd'),
]

def quiz():
    print('Welcome! The theme for this quiz is...')
    time.sleep(1.5)
    print('The BEAUTIFUL...')
    time.sleep(1.5)
    print('Most UNFORGIVING...')
    time.sleep(1.5)
    print('FRENCH MACARON!!! WOOHOOOO~')
    time.sleep(1.0)
    ready = input('Are you ready? (y) for yes, (n) for no\n')

    score = 0

    if ready == 'y':
        for question in questions:
            user_ans = input(question.prompt)
            if user_ans == question.answer:
                score += 1
            else:
                score = score
        
        print(f'You got {score}/{len(questions)} correct!' )
        if score/(len(questions)) == 1:
            time.sleep(0.8)
            print('AMAZING! Are you a pastry chef?')
        else:
            time.sleep(0.8)
            print('Maybe next time you can get a perfect score!')
    
    elif ready == 'n':
        print('No worries. Goodbye!')
    else:
        print('Invalid input. Try again please!')
    
quiz()


