import gooeypie as gp
import time

score = 0

def open_main_window():
    def toggle_mask(event):
        input_password.toggle()

    start_btn.destroy()
    start_lbl.destroy()
    welcome_text.destroy()
    thinking_pb.destroy()
    app.grid_remove()
    app.set_grid(4, 2)

    input_password = gp.Secret(app)
    password_prompt = gp.Label(app, 'Enter Password:')
    check = gp.Checkbox(app, 'Show Password')
    check.add_event_listener('change', toggle_mask)

    app.add(password_prompt, 1, 1, align='right', valign='bottom')
    app.add(input_password, 1, 2, align='left', valign='bottom')
    app.add(check, 2, 2)

def welcome_txt():
    welcome_text.font_name = "algerian"
    welcome_text.text = 'Robustness Security'

def start_button(event):
    start_lbl.text = 'Loading Assets'
    thinking_pb.value = 0

    for steps in range(20):
        thinking_pb.value += 5
        app.refresh()
        time.sleep(0.02)

    open_main_window()

app = gp.GooeyPieApp('Robustness Security')
app.width = 300
app.height = 200

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






