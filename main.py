import gooeypie as gp
import time




def open_main_window():
    score = 0

    def check_length(password, password_feedback_length, password_length_text):
        if len(password) == 0:
            password_feedback_length.text = "Type a password :)"

        else:
            l = len(password)*10
            password_length_text.text = "Password Length:"
            if l < 50:
                password_feedback_length.text = "Weak"
            elif l >= 50 and l < 80:
                password_feedback_length.text = "Moderate"
            elif l >= 80:
                password_feedback_length.text = "Strong"
            
            
            
            return l
        
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
        

    def check_common_passwords():
        pass

    def check_numbers():

    
        pass
        
    def check_dictionary_words():

        pass 

    def overallscore():
        pass

    def help_btn(event):
        pass

    def abt_btn(event):
        input_password.destroy()
        password_prompt.destroy()
        check.destroy()
        password_feedback_length.destroy()
        password_length_text = gp.Label(app, '')
        password_case_feedback = gp.StyleLabel(app, '')
        password_case_text = gp.Label(app, '')
        password_special_char_text = gp.Label(app, '')
        password_special_char_feedback = gp.Label(app, '')
        help_button = gp.Button(app, 'Help', help_btn)
        about_button = gp.Button(app, 'About', abt_btn)
        copy_password_button = gp.Button(app, 'Copy', copy_btn)
        pass
    def copy_btn(event):

        pass
    def check_btn(event):
        input_password.toggle()

    def on_password_change(event):
        password = input_password.text
        

        l = check_length(password, password_feedback_length, password_length_text)
        upper_case_score = check_case(password, password_case_feedback, password_case_text)
        special_char_score = check_special_char(password, password_special_char_feedback, password_special_char_text)

    start_btn.destroy()
    start_lbl.destroy()
    welcome_text.destroy()
    thinking_pb.destroy()
    app.grid_remove()
    app.set_grid(10, 3)

    input_password = gp.Secret(app)
    input_password.add_event_listener('change', on_password_change)
    password_prompt = gp.Label(app, 'Enter Password:')
    check = gp.Button(app, 'Show Password', check_btn)
    password_feedback_length = gp.Label(app, '')
    password_length_text = gp.Label(app, '')
    password_case_feedback = gp.StyleLabel(app, '')
    password_case_text = gp.Label(app, '')
    password_special_char_text = gp.Label(app, '')
    password_special_char_feedback = gp.Label(app, '')
    help_button = gp.Button(app, 'Help', help_btn)
    about_button = gp.Button(app, 'About', abt_btn)
    copy_password_button = gp.Button(app, 'Copy', copy_btn)

    app.add(password_prompt, 1, 1, align='right')
    app.add(input_password, 1, 2)
    app.add(check, 1, 3)
    app.add(copy_password_button, 10, 1, align='center')
    app.add(about_button, 10, 3, align='center')
    app.add(help_button, 10, 2, align='center')
    app.add(password_feedback_length, 2, 2, columnspan = 2)
    app.add(password_length_text, 2, 1)
    app.add(password_case_text, 3, 1)
    app.add(password_case_feedback, 3, 2)
    app.add(password_special_char_text, 4, 1)
    app.add(password_special_char_feedback, 4, 2)

def welcome_txt():
    welcome_text.font_name = "aharoni"
    welcome_text.text = 'Robustness-Security'

def start_button(event):
    start_lbl.text = 'Loading Assets'
    thinking_pb.value = 0

    for steps in range(20):
        thinking_pb.value += 5
        app.refresh()
        time.sleep(0.02)

    open_main_window()

app = gp.GooeyPieApp('Robustness Security')
app.width = 400
app.height = 300

start_btn = gp.Button(app, 'Start', start_button)
start_lbl = gp.Label(app, '')
welcome_text = gp.StyleLabel(app, '')
thinking_pb = gp.Progressbar(app)

welcome_txt()
app.set_grid(4, 1)
app.add(welcome_text, 1, 1, align='center', valign='bottom')
app.add(start_btn, 2, 1, align='center')
app.add(start_lbl, 3, 1, align='center')
app.add(thinking_pb, 4, 1, fill=True)

app.run()






