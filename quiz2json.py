from pynput.keyboard import Key, Listener
import pyperclip, time


incomming_question = True

question = ''
answer = ''

running = True

all_questions = {}
print('Waiting for question...')

def on_press(key):

    global incomming_question, all_questions, answer, question, running

    if (running):

        if (key == Key.esc):
            print('Output saved to questions_output.txt')
            open('questions_output.txt', 'w').write(str(all_questions))
            input('Hit ENTER to exit')
            exit(0)
        
        if '03' in str(key):
            time.sleep(0.05)
            if incomming_question:
                question = pyperclip.paste()
                incomming_question = False
                print('Waiting for answer...')
            else:
                answer = pyperclip.paste()
                all_questions[question] = answer
                print('========== Question added. ==========')
                print('Question: ' + question)
                print('Answer: ' + answer)
                print('=====================================')
                incomming_question = True
                print('Waiting for question...')

# Collect events until released
with Listener(
        on_press=on_press) as listener:
    listener.join()