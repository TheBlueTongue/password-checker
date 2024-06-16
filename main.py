import gooeypie as gp
import time



def load_common_passwords(filename):
   with open(filename, 'r') as file:
       common_passwords = file.read().splitlines()
   return common_passwords

common_passwords = load_common_passwords('common passwords list.ini')

def load_dictionary_words(filename):
    with open(filename, 'r') as file:
        dictionary_words = file.read().splitlines()
    return dictionary_words

dictionary_words = load_dictionary_words('words.txt')

password = ''

def open_main_window(password):    

    def check_length(password, password_feedback_length, password_length_text):
        length_score = 0
        l = len(password)
        if len(password) == 0:
            password_feedback_length.text = "Type a password :)"

        else:
            password_length_text.text = "Password Length:"
            if l < 5:
                length_score = 0
                password_feedback_length.text = "Weak"
            elif l >= 5 and l < 10:
                password_feedback_length.text = "Moderate"
                length_score = 50
            
            elif l >= 10:
                password_feedback_length.text = "Strong"
                length_score = 100

        return length_score
             
    def check_case(password, password_case_feedback, password_case_text):
        upper_case_score = 0
 
        if len(password) > 0:
        
            for char in password:
                if char.isupper():
                    upper_case_score += 50
            
            password_case_text.text = 'Uppercase:'
            if upper_case_score == 0:
                password_case_feedback.text = 'Weak'
            elif upper_case_score == 50:
                password_case_feedback.text = 'Moderate'
            elif upper_case_score == 100 or upper_case_score > 100:
                password_case_feedback.text = '🟢'
                upper_case_score = 100
        else:
            password_case_feedback.text = ''

        return upper_case_score

    def check_special_char(password, password_special_char_feedback, password_special_char_text):
        special_char_score = 0

        if len(password) > 0: 
            symbols = "`~!@#$%^&*()_-+={[}]|\:;'<,>.?/}\\\""
            for char in password:
                if char in symbols:
                    special_char_score += 50

            password_special_char_text.text = 'Special Characters:'
            if special_char_score == 0:
                password_special_char_feedback.text = 'Weak'
            elif special_char_score == 50: 
                password_special_char_feedback.text = 'Moderate'
            elif special_char_score == 100 or special_char_score > 100:
                password_special_char_feedback.text = 'Strong'
                special_char_score = 100
        else: 
            password_special_char_feedback.text = ''

        return special_char_score
        
    def check_common_passwords(password, common_password_feedback, common_password_text, common_passwords):
        common_password_score = 0
        
        if len(password) > 0:
            common_password_text.text = 'Common Password:'
            if len(password) > 4:
                if password in common_passwords:
                    common_password_score = 0
                else:
                    common_password_score = 100
                
                if common_password_score == 100:
                    common_password_feedback.text = 'No'
                if common_password_score == 0:
                    common_password_feedback.text = 'Yes'
            
        else: 
            common_password_feedback.text = ''

        return common_password_score

    def check_numbers(password, password_number_feedback, password_number_text):
        numbers_score = 0

        if len(password) > 0:
            numbers = "1234567890"
            for char in password:
                if char in numbers:
                    numbers_score += 50
            
            password_number_text.text = 'Numbers:'
            if numbers_score == 0:
                password_number_feedback.text = 'Weak'
            elif numbers_score == 50: 
                password_number_feedback.text = 'Moderate'
            elif numbers_score == 100 or numbers_score > 100:
                password_number_feedback.text = 'Strong'
                numbers_score = 100
        else:
            password_number_feedback.text = ''

        return numbers_score
    
    def check_dictionary_words(password, password_dictionary_word_text, password_dictionary_word_feedback, dictionary_words):
        dictionary_score = 0

        if len(password) > 0:
            password_dictionary_word_text.text = 'Dictionary Word:'
            if len(password) > 4: 
                if password in dictionary_words:
                    dictionary_score = 0
                    password_dictionary_word_feedback.text = 'Yes'
                else:
                    password_dictionary_word_feedback.text = 'No' 
                    dictionary_score = 100
        else: 
            password_dictionary_word_text.text = ''
        
        return dictionary_score
        
    def overallscore(length_score, upper_case_score, special_char_score, numbers_score, common_passwords_score, dictionary_sore, overall_score_feedback, overall_score_text, password):
        
        if len(password) > 0:
            overall_score_text.text = 'Overall Score:'
            x = length_score + upper_case_score + special_char_score + numbers_score + common_passwords_score + dictionary_sore
            x = x/6
            x = round(x)

            if x < 40:
                y = 'Very Weak'

            elif x < 50: 
                y = 'Weak'

            elif x < 60:
                y = 'Moderate'

            elif x < 70:
                y = 'Almost Strong'

            elif x < 80:
                y = 'Strong'

            elif x < 100:
                y = 'Very Strong'

            elif x == 100:
                y = 'Impossibly Strong'

            overall_score_feedback.text = f'{x}%        ({y})'
            strength_bar.value = x
        else:
            overall_score_feedback.text = 'Type a password :)'

    def help_btn(event):

        pass

    def abt_btn(event):
        def back_btn(event):
            about_text.destroy()
            back_button.destroy()
            open_main_window()

        app.grid_remove
        app.set_grid(2,1)
        
        about_button.destroy()
        input_password.destroy()
        password_prompt.destroy()
        check.destroy()
        password_feedback_length.destroy()
        password_length_text.destroy()
        password_case_feedback.destroy()
        password_case_text.destroy()
        password_special_char_text.destroy()
        password_special_char_feedback.destroy()
        password_number_text.destroy()
        password_number_feedback.destroy()
        help_button.destroy()
        copy_password_button.destroy()
        common_password_text.destroy()
        common_password_feedback.destroy()
        password_dictionary_word_feedback.destroy()
        password_dictionary_word_text.destroy()
        overall_score_feedback.destroy()
        overall_score_text.destroy()
        detailed_feedback.destroy()

        back_button = gp.Button(app, 'Back', back_btn)
        about_text = gp.Label(app, '')
        about_text.text = 'Welcome to Robustness Security, your reliable partner in password protection. \n In todays digital age, safeguarding your online presence is more critical than \n ever. Robustness Security is here to help you ensure that your passwords are \n strong, secure, and resilient against potential threats. '
        app.add(back_button, 2, 1, align='center')
        app.add(about_text, 1, 1)

    def copy_btn(event):

        pass

    def check_btn(event):
        input_password.toggle()

    def on_password_change(event):
        password = input_password.text
        

        length_score = check_length(password, password_feedback_length, password_length_text)
        upper_case_score = check_case(password, password_case_feedback, password_case_text)
        special_char_score = check_special_char(password, password_special_char_feedback, password_special_char_text)
        numbers_score = check_numbers(password, password_number_feedback, password_number_text)
        common_passwords_score = check_common_passwords(password, common_password_feedback, common_password_text, common_passwords)
        dictionary_sore = check_dictionary_words(password, password_dictionary_word_text, password_dictionary_word_feedback, dictionary_words)
        overallscore(length_score, upper_case_score, special_char_score, numbers_score, common_passwords_score, dictionary_sore, overall_score_feedback, overall_score_text, password)
        print (length_score, upper_case_score, special_char_score, numbers_score, common_passwords_score, dictionary_sore)

        return password
    
    def feedback_btn(event):
        
        def back_btn(event):
            password_case_feedback.destroy()
            password_case_text.destroy()
            password_dictionary_word_feedback.destroy()
            password_dictionary_word_text.destroy()
            password_feedback_length.destroy()
            password_length_text.destroy()
            password_number_feedback.destroy()
            password_number_text.destroy()
            password_special_char_feedback.destroy()
            password_special_char_text.destroy()
            common_password_feedback.destroy()
            common_password_text.destroy()


            back_button.destroy()
            open_main_window()

        detailed_feedback.destroy()
        input_password.destroy()
        password_prompt.destroy()
        copy_password_button.destroy()
        about_button.destroy()
        help_button.destroy()
        overall_score_feedback.destroy()
        overall_score_text.destroy()

        check.destroy()
        app.grid_remove
        app.set_grid(7,3)

        back_button = gp.Button(app, 'Back', back_btn)
        
        app.add(password_feedback_length, 1, 2)
        app.add(password_length_text, 1, 1)
        app.add(password_case_text, 2, 1)
        app.add(password_case_feedback, 2, 2)
        app.add(password_special_char_text, 3, 1)
        app.add(password_special_char_feedback, 3, 2)
        app.add(password_number_feedback, 4, 2)
        app.add(password_number_text, 4, 1)
        app.add(common_password_feedback, 5, 2)
        app.add(common_password_text, 5, 1)
        app.add(password_dictionary_word_feedback, 6, 2)
        app.add(password_dictionary_word_text, 6, 1)
        app.add(back_button, 7, 1)

    start_btn.destroy()
    start_lbl.destroy()
    welcome_text.destroy()
    thinking_pb.destroy()
    app.grid_remove()
    app.set_grid(4, 3)

    input_password = gp.Secret(app)
    input_password.text = password

    input_password.add_event_listener('change', on_password_change)
    password_prompt = gp.Label(app, 'Enter Password:')
    check = gp.Button(app, 'Show Password', check_btn)

    password_feedback_length = gp.Label(app, '')
    password_length_text = gp.Label(app, '')
    password_case_feedback = gp.StyleLabel(app, '')
    password_case_text = gp.Label(app, '')
    password_special_char_text = gp.Label(app, '')
    password_special_char_feedback = gp.Label(app, '')
    password_number_feedback = gp.Label(app, '')
    password_number_text = gp.Label(app, '')
    common_password_feedback = gp.Label(app, '')
    common_password_text = gp.Label(app, '')
    password_dictionary_word_text = gp.Label(app, '')
    password_dictionary_word_feedback = gp.Label(app, '')
    overall_score_text = gp.Label(app, '')
    overall_score_feedback = gp.Label(app, '')
    strength_bar = gp.Progressbar(app)
    
    detailed_feedback = gp.Button(app, 'Feedback', feedback_btn)
    help_button = gp.Button(app, 'Help', help_btn)
    about_button = gp.Button(app, 'About', abt_btn)
    copy_password_button = gp.Button(app, 'Copy', copy_btn)

    app.add(strength_bar, 3, 1, column_span = 3, fill=True)
    app.add(password_prompt, 1, 1)
    app.add(input_password, 1, 2)
    app.add(check, 1, 3)
    app.add(copy_password_button, 4, 1)
    app.add(about_button, 4, 3)
    app.add(help_button, 4, 2)
    app.add(overall_score_text, 2, 1)
    app.add(overall_score_feedback, 2, 2)
    app.add(detailed_feedback, 2, 3)

def start_button(event):
    start_lbl.text = 'Loading Assets'
    thinking_pb.value = 0

    for steps in range(20):
        thinking_pb.value += 5
        app.refresh()
        time.sleep(0.02)

    open_main_window(password)

app = gp.GooeyPieApp('Robustness Security')
app.width = 450
app.height = 300

start_btn = gp.Button(app, 'Start', start_button)
start_lbl = gp.Label(app, '')
welcome_text = gp.StyleLabel(app, '')
thinking_pb = gp.Progressbar(app)

welcome_text.font_name = "aharoni"
welcome_text.text = 'Robustness-Security'

app.set_grid(4, 1)
app.add(welcome_text, 1, 1, align='center', valign='bottom')
app.add(start_btn, 2, 1, align='center')
app.add(start_lbl, 3, 1, align='center')
app.add(thinking_pb, 4, 1, fill=True)

app.run()






