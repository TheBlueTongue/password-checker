import gooeypie as gp
import time
import pyperclip
from pyhibp import pwnedpasswords
from pyhibp import set_user_agent
# different imports

set_user_agent(ua="Robustness Security") 
# sets the user agent for hibp

def load_common_passwords(filename): #loads list of common passwords
   with open(filename, 'r') as file:
       common_passwords = file.read().splitlines()
   return common_passwords

common_passwords = load_common_passwords('common passwords list.ini')

def load_dictionary_words(filename): #loads list of dictionart words
    with open(filename, 'r') as file:
        dictionary_words = file.read().splitlines()
    return dictionary_words

dictionary_words = load_dictionary_words('words.txt')

user_password = '' #sets initial password to empty

password_visible = False #sets password visibility to false

def open_main_window():  #the main window of the program
    global user_password

    #cheks the length of the password
    def check_length(user_password, password_feedback_length, password_length_text, password_length_image):
        length_score = 0
        l = len(user_password)
        password_length_text.text = "Password Length:"
        if len(user_password) == 0: # if the length is 0, ask the user to type a password
            password_feedback_length.text = "Type a password :)"
            password_length_image.image = 'icons/red circle.png'
        else:   
            if l < 5:
                length_score = 0
                password_feedback_length.text = "Weak"
                password_length_image.image = 'icons/red circle.png'

            elif l >= 5 and l < 10:
                password_feedback_length.text = "Moderate"
                length_score = 50
                password_length_image.image = 'icons/yellow circle.png'
            elif l >= 10:
                password_feedback_length.text = "Strong"
                length_score = 100
                password_length_image.image = 'icons/green circle.png'

        return length_score

    # checks for upper case letters    
    def check_case(user_password, password_case_feedback, password_case_text, password_case_image):
        upper_case_score = 0
        password_case_text.text = 'Uppercase:'
        
        if len(user_password) > 0:
        
            for char in user_password: #adds 50 to the score for each upper case character
                if char.isupper():
                    upper_case_score += 50
            
            
            if upper_case_score == 0:
                password_case_feedback.text = 'Weak'
                password_case_image.image = 'icons/red circle.png'
            elif upper_case_score == 50:
                password_case_feedback.text = 'Moderate'
                password_case_image.image = 'icons/yellow circle.png'
            elif upper_case_score == 100 or upper_case_score > 100: #caps the score to 100
                password_case_feedback.text = 'Strong'
                upper_case_score = 100
                password_case_image.image = 'icons/green circle.png'
        else:
            password_case_feedback.text = ''
            password_case_image.image = 'icons/red circle.png'

        return upper_case_score

    #checks for special characters
    def check_special_char(user_password, password_special_char_feedback, password_special_char_text, password_special_character_image):
        special_char_score = 0
        password_special_char_text.text = 'Special Characters:'
        
        if len(user_password) > 0: 
            symbols = "`~!@#$%^&*()_-+={[}]|\:;'<,>.?/}\\\""
            for char in user_password:
                if char in symbols:
                    special_char_score += 50

            
            if special_char_score == 0:
                password_special_char_feedback.text = 'Weak'
                password_special_character_image.image = 'icons/red circle.png'
            elif special_char_score == 50: 
                password_special_char_feedback.text = 'Moderate'
                password_special_character_image.image = 'icons/yellow circle.png'
            elif special_char_score == 100 or special_char_score > 100:
                password_special_char_feedback.text = 'Strong'
                special_char_score = 100
                password_special_character_image.image = 'icons/green circle.png'
        else: 
            password_special_char_feedback.text = ''
            password_special_character_image.image = 'icons/red circle.png'

        return special_char_score
        
    #checks for common passwords or breached passwords
    def check_common_passwords(user_password, common_password_feedback, common_password_text, common_passwords):
        common_password_score = 0
        internet_connection = True
        try:
            times_pwned = pwnedpasswords.is_password_breached(password=user_password)
        except:
            internet_connection = False

        if internet_connection == False: #if no internet connection use common password else use breached password
            common_password_text.text = 'Common Password:'
            if len(user_password) > 0:
                if user_password in common_passwords:
                    common_password_score = 0
                    common_password_feedback.text = 'Yes'
                else:
                    common_password_score = 100
                    common_password_feedback.text = 'No'
            else: 
                common_password_feedback.text = ''
        else:
            common_password_text.text = "Breached password:"
            if times_pwned == 0:
                common_password_feedback.text = "No"
                common_password_score = 100
            else:
                common_password_feedback.text = 'Yes'
                common_password_score = 0
                
        return common_password_score

    #checks for numbers
    def check_numbers(user_password, password_number_feedback, password_number_text, password_number_image):
        numbers_score = 0
        password_number_text.text = 'Numbers:'
        if len(user_password) > 0:
            numbers = "1234567890"
            for char in user_password:
                if char in numbers:
                    numbers_score += 50
            
            
            if numbers_score == 0:
                password_number_feedback.text = 'Weak'
                password_number_image.image = 'icons/red circle.png'
            elif numbers_score == 50: 
                password_number_feedback.text = 'Moderate'
                password_number_image.image = 'icons/yellow circle.png'
            elif numbers_score == 100 or numbers_score > 100:
                password_number_feedback.text = 'Strong'
                numbers_score = 100
                password_number_image.image = 'icons/green circle.png'
        else:
            password_number_feedback.text = ''
            password_number_image.image = 'icons/red circle.png'

        return numbers_score
    
    #checks to see if password is a dictionary word
    def check_dictionary_words(user_password, password_dictionary_word_text, password_dictionary_word_feedback, dictionary_words):
        dictionary_score = 0
        password_dictionary_word_text.text = 'Dictionary Word:'
        if len(user_password) > 0:
            password_dictionary_word_feedback.text = 'Yes'
            if len(user_password) >= 4: #if length is less then 4, assume its a dictionary word
                if user_password in dictionary_words:
                    dictionary_score = 0
                    password_dictionary_word_feedback.text = 'Yes'
                else:
                    password_dictionary_word_feedback.text = 'No' 
                    dictionary_score = 100
        else: 
            password_dictionary_word_feedback.text = ''
        
        return dictionary_score
    
    # calculates the overall score   
    def overallscore(length_score, upper_case_score, special_char_score, numbers_score, common_passwords_score, dictionary_sore, overall_score_feedback, overall_score_text, user_password):
        overall_score_text.text = 'Overall Score:'
        if len(user_password) > 0:
            
            overall_score = length_score + upper_case_score + special_char_score + numbers_score + common_passwords_score + dictionary_sore
            overall_score = overall_score/6
            overall_score = round(overall_score)

            if overall_score < 40:
                overall_score_word_feedback = 'Very Weak'

            elif overall_score < 50: 
                overall_score_word_feedback = 'Weak'

            elif overall_score < 60:
                overall_score_word_feedback = 'Moderate'

            elif overall_score < 70:
                overall_score_word_feedback = 'Almost Strong'

            elif overall_score < 80:
                overall_score_word_feedback = 'Strong'

            elif overall_score < 100:
                overall_score_word_feedback = 'Very Strong'

            elif overall_score == 100:
                overall_score_word_feedback = 'Impossibly Strong'

            overall_score_feedback.text = f'{overall_score}%        ({overall_score_word_feedback})'
            strength_bar.value = overall_score
        else:
            overall_score_feedback.text = 'Type a password :)'
            strength_bar.value = 0

    # help window
    def help_btn(event):
        def back_btn(event):
            help_text.destroy()
            back_button.destroy()
            open_main_window()

        app.grid_remove()
        app.set_grid(2, 1)
        back_button = gp.Button(app, 'Back', back_btn)
        help_text = gp.Label(app, '')
        help_text.text = (
            "Here is how to use the Robustness Security Password Checker!\n\n"
            "1. Type your password into the provided input field.\n"
            "2. Click the 'Show Password' button to see your password.\n"
            "3. Click the 'Feedback' button to get an analysis of your password's strength.\n"
            "    - **Length**: Indicates how long your password is.\n"
            "    - **Uppercase Letters**: Checks for the presence of 2 uppercase letters.\n"
            "    - **Special Characters**: Checks for 2 special characters like @, #, $, etc.\n"
            "    - **Numbers**: Checks for the presence of 2 numeric characters.\n"
            "    - **Common Password**: Checks if your password is a commonly.\n"
            "    - **Dictionary Words**: Checks if your password is a dictionary word.\n"
            "4. The overall score combines all the criteria to give you an overall rating.\n"
            "5. Use the 'Copy' button to copy your password to the clipboard for easy use.\n"
            "6. Click the 'About' button to learn more about Robustness Security.\n"
           
        )
        app.add(back_button, 2, 1, align='center')
        app.add(help_text, 1, 1)
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
        strength_bar.destroy()
        
    # about window
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
        strength_bar.destroy()

        back_button = gp.Button(app, 'Back', back_btn)
        about_text = gp.Label(app, '')
        about_text.text = ( 
        "At Robustness Security, we provide top-tierassword protection. \n\n"

        "The importance of securing your online presence cannot be overstated. \n\n"
        
        "Our advanced algorithms analyze and assess the strength of your passwords.\n\n"
               
        "We provide detailed feedback and tips on how to create strong passwords. \n\n"
        
        "Our aim is to educate users on best practices for password management.\n\n"
        
        "Our tool is designed to be intuitive, allowing users of all technical levels.\n\n"
                
        "Our dedicated support team is available to assist you with any questions.\n\n"
        
        "Thank you for choosing us. Together, we can build a safer digital world."
        )

        app.add(back_button, 2, 1, align='center')
        app.add(about_text, 1, 1)

    # resets the copy button icon
    def reset_copy_btn():
        copy_password_button.image = "icons/copy-alt.png"

    # copies the users password
    def copy_btn(event):
        pyperclip.copy(user_password)
        copy_password_button.image = "icons/check.png"
        app.after(500, reset_copy_btn)
   
    # analyses the password
    def password_analysis():  
        global user_password
        user_password = input_password.text
        
        length_score = check_length(user_password, password_feedback_length, password_length_text, password_length_image)
        upper_case_score = check_case(user_password, password_case_feedback, password_case_text, password_case_image)
        special_char_score = check_special_char(user_password, password_special_char_feedback, password_special_char_text, password_special_character_image)
        numbers_score = check_numbers(user_password, password_number_feedback, password_number_text, password_number_image)
        common_passwords_score = check_common_passwords(user_password, common_password_feedback, common_password_text, common_passwords)
        dictionary_sore = check_dictionary_words(user_password, password_dictionary_word_text, password_dictionary_word_feedback, dictionary_words)
        overallscore(length_score, upper_case_score, special_char_score, numbers_score, common_passwords_score, dictionary_sore, overall_score_feedback, overall_score_text, user_password)
       

        return user_password

    # hides/ shows the users password
    def check_btn(event):
        global password_visible
        input_password.toggle()
        if password_visible == False:
            password_visible = True
            check.image = 'icons/eye-crossed.png'
            return password_visible
        if password_visible == True:
            password_visible = False
            check.image = 'icons/eye.png'
            return password_visible

    # everytime there is a change to a password analyse it            
    def on_password_change(event):
        password_analysis()
    #detailed feedback window
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
            password_length_image.destroy()
            password_case_image.destroy()
            password_number_image.destroy()
            password_special_character_image.destroy()
            app.grid_remove

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
        strength_bar.destroy()

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

        app.add(password_length_image, 1, 3)
        app.add(password_case_image, 2, 3)
        app.add(password_special_character_image, 3, 3)
        app.add(password_number_image, 4, 3)

    start_btn.destroy()
    start_lbl.destroy()
    welcome_text.destroy()
    thinking_pb.destroy()
    app.grid_remove()
    app.set_grid(4, 3)

    input_password = gp.Secret(app)
    input_password.text = user_password

    input_password.add_event_listener('change', on_password_change)
    password_prompt = gp.Label(app, 'Enter Password:')
   
    # sets and adds different variables in the main window
    
    password_length_text = gp.Label(app, '')
    password_case_text = gp.Label(app, '')
    password_special_char_text = gp.Label(app, '')
    password_number_text = gp.Label(app, '')
    common_password_text = gp.Label(app, '')
    password_dictionary_word_text = gp.Label(app, '')
    overall_score_text = gp.Label(app, '')
    strength_bar = gp.Progressbar(app)
    
    password_case_feedback = gp.StyleLabel(app, '')
    password_special_char_feedback = gp.Label(app, '')
    password_number_feedback = gp.Label(app, '')
    common_password_feedback = gp.Label(app, '')
    password_dictionary_word_feedback = gp.Label(app, '')
    overall_score_feedback = gp.Label(app, '')
    password_feedback_length = gp.Label(app, '')
    detailed_feedback = gp.Button(app, 'Feedback', feedback_btn)
    help_button = gp.ImageButton(app, 'icons/interrogation.png', help_btn)
    about_button = gp.ImageButton(app, 'icons/info.png', abt_btn)
    copy_password_button = gp.ImageButton(app, 'icons/copy-alt.png', copy_btn)
    check = gp.ImageButton(app, 'icons/eye.png', check_btn)

    password_length_image = gp.Image(app, 'icons/green circle.png')
    password_case_image = gp.Image(app, 'icons/green circle.png')
    password_special_character_image = gp.Image(app, 'icons/green circle.png')
    password_number_image = gp.Image(app, 'icons/green circle.png')


    app.add(strength_bar, 3, 1, column_span = 3, fill=True)
    app.add(password_prompt, 1, 1, align='right', valign='middle')
    app.add(input_password, 1, 2, valign='middle')
    app.add(check, 1, 3, align='center', valign='middle')
    app.add(copy_password_button, 4, 1, align='center')
    app.add(about_button, 4, 3, align='center')
    app.add(help_button, 4, 2, align='center')
    app.add(overall_score_text, 2, 1, align='right')
    app.add(overall_score_feedback, 2, 2)
    app.add(detailed_feedback, 2, 3, align='center')
    
    # initially analyses the password
    password_analysis()
#start up window button to main window
def start_button(event):
    start_lbl.text = 'Loading Assets'
    thinking_pb.value = 0

    for steps in range(20): #moves loading bar
        thinking_pb.value += 5
        app.refresh()
        time.sleep(0.02)

    open_main_window()

# startup window and app variables
app = gp.GooeyPieApp('Robustness Security')
app.width = 450
app.height = 300
app.resizable_horizontal = False
app.resizable_vertical = False

start_btn = gp.ImageButton(app, 'icons/play-circle.png', start_button)
start_lbl = gp.Label(app, '')
welcome_text = gp.StyleLabel(app, '')
thinking_pb = gp.Progressbar(app)

welcome_text.font_name = "aharoni"
welcome_text.text = 'Robustness-Security'
welcome_text.font_size = 30

app.set_grid(4, 1)
app.add(welcome_text, 1, 1, align='center', valign='bottom')
app.add(start_btn, 2, 1, align='center')
app.add(start_lbl, 3, 1, align='center')
app.add(thinking_pb, 4, 1, fill=True)
app.set_icon('icons/lock.png')
app.run()






