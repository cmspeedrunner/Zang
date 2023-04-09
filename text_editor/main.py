import tkinter as tk
from tkinter.filedialog import *
import os
code_font = ("Lucida Console", 20)


def highlight_syntax(event=None):
    '''Highlight syntax elements in different colors'''
    # Remove any previous tags
    text.tag_remove('keyword', '1.0', 'end')
    text.tag_remove('quote', '1.0', 'end')
    text.tag_remove('digit', '1.0', 'end')
    text.tag_remove('usingf', '1.0', 'end')
    # Highlight keywords in blue
    for keyword in ['if', 'elif', 'else', 'for', "while", "fn",]:
        start = '1.0'
        while True:
            start = text.search(r'\m{}\M'.format(keyword), start, 'end', count=stop_search, regexp=True)
            if not start:
                break
            end = start + '+{}c'.format(len(keyword))
            text.tag_add('keyword', start, end)
            start = end
    for keyword in ["end", "then", "to", "and","break","return","continue", "or"]:
        start = '1.0'
        while True:
            start = text.search(r'\m{}\M'.format(keyword), start, 'end', count=stop_search, regexp=True)
            if not start:
                break
            end = start + '+{}c'.format(len(keyword))
            text.tag_add('intermediates', start, end)
            start = end
    for keyword in ["writeln","rq_get","sys_stdout", "sys.stdin" "rq_html", "rq_post","find","pop","get","extend","append","len","split","classof","zang_i","tostr", "trim", "open","writeln_ret", "toint", "tofloat","put","msg", "passc","read", "append","pop", "opentab", "clear", "is_number", "is_string","is_list","is_function","len","extend","run", "let"]:
        start = '1.0'
        while True:
            start = text.search(r'\m{}\M'.format(keyword), start, 'end', count=stop_search, regexp=True)
            if not start:
                break
            end = start + '+{}c'.format(len(keyword))
            text.tag_add('definers', start, end)
            start = end
            
    for keyword in ["math_pi", "zang_sysv","zang_argv", "math_inf", "col_red","random", "col_green", "col_reset", "col_yellow", "col_blue","col_purple","nil","string_letters", "string_digits", "string_punct","zang_version", "zang_platform", "zang_link","True", "False"]:
        start = '1.0'
        while True:
            start = text.search(r'\m{}\M'.format(keyword), start, 'end', count=stop_search, regexp=True)
            if not start:
                break
            end = start + '+{}c'.format(len(keyword))
            text.tag_add('inbuilts', start, end)
            start = end
    # Highlight text between quotes in orange
    start = '1.0'
    while True:
        start = text.search('"', start, 'end', count=stop_search, regexp=True)
        if not start:
            break
        end = text.search('"', start + '+1c', 'end', count=stop_search, regexp=True)
        if not end:
            break
        text.tag_add('quote', start, end + '+1c')
        start = end + '+1c'
    # Highlight digits in green
    start = '1.0'
    while True:
        start = text.search(r'\d', start, 'end', count=stop_search, regexp=True)
        if not start:
            break
        end = start + '+1c'
        text.tag_add('digit', start, end)
        start = end


    for keyword in ["using", "using"]:
        start = '1.0'
        while True:
            start = text.search(r'\m{}\M'.format(keyword), start, 'end', count=stop_search, regexp=True)
            if not start:
                break
            end = start + '+{}c'.format(len(keyword))
            text.tag_add('usingf', start, end)
            start = end
    # Highlight text between quotes in orange
    start = '1.0'
    while True:
        start = text.search(r'\d', start, 'end', count=stop_search, regexp=True)
        if not start:
            break
        end = start + '+1c'
        text.tag_add('quote', start, end)
        start = end

root = tk.Tk()
root.title('Text Editor')
root.iconbitmap("C:\\Windows\\System32\\cmd.exe")
# Create text widget and scrollbar
text = tk.Text(root, bg="#333333", fg="#ffffff", font=code_font)
scrollbar = tk.Scrollbar(root, command=text.yview)
text.configure(yscrollcommand=scrollbar.set)
text.pack()


# Add 'keyword', 'quote', and 'digit' tags for highlighting
text.tag_configure('keyword', foreground='pink')
text.tag_configure('quote', foreground='orange')
text.tag_configure('digit', foreground='light green')
text.tag_configure('intermediates', foreground='light blue')
text.tag_configure('definers', foreground='cyan')
text.tag_configure('inbuilts', foreground='yellow')
text.tag_configure('usingf', foreground='purple')


# Bind key events for syntax highlighting
text.bind('<KeyRelease>', highlight_syntax)
text.bind('<ButtonRelease-1>', highlight_syntax)

# Pack widgets
text.pack(side='left', fill='both', expand=True)
scrollbar.pack(side='right', fill='y')

# Define stop_search
stop_search = tk.IntVar()

def open_file():
    file_path = askopenfilename(defaultextension=".zang", filetypes=[("Zang Files", "*.zang"), ("All Files", "*.*")])
    if not file_path:
        return
    text.delete(1.0, tk.END)
    with open(file_path, "r") as file:
        text.insert(1.0, file.read())

# Create a function to save a file
def save_file():
    file_path = asksaveasfilename(defaultextension=".zang", filetypes=[("Zang Files", "*.zang"), ("All Files", "*.*")])
    if not file_path:
        return
    with open(file_path, "w") as file:
        file.write(text.get(1.0, tk.END))


# Create a menu bar with code font and dark mode colors
menu_bar = tk.Menu(root, bg="#333333", fg="#ffffff", font=code_font)
file_menu = tk.Menu(menu_bar, tearoff=0, bg="#333333", fg="#ffffff", font=code_font)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save as", command=save_file)

file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

root.config(menu=menu_bar)

# Set the background color of the window to black
root.configure(bg="#000000")
def open_terminal():
    # Create a Toplevel window for the terminal
    terminal_window = tk.Toplevel(root)
    terminal_window.title("Terminal")
    root.iconbitmap("C:\\Windows\\System32\\cmd.exe")
    terminal_window.iconbitmap("C:\\Windows\\System32\\cmd.exe")

    # Create a text widget for the terminal output
    terminal_output = tk.Text(terminal_window, bg="#000000", fg="#ffffff", font=code_font)
    terminal_output.pack(fill=tk.BOTH, expand=True)

    # Create a text widget for the terminal input
    terminal_input = tk.Entry(terminal_window, bg="#000000", fg="#ffffff", font=code_font)
    terminal_input.pack(fill=tk.BOTH)

    # Set focus to the terminal input widget
    terminal_input.focus()

    # Create a function to execute a command in the terminal
    import subprocess

    def run_command():
        command = terminal_input.get()
    # Use subprocess.Popen to run the command and capture its output
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()
    # Display the command and user input in the terminal
        terminal_output.insert(tk.END, f"USER> {command}\n", "user_input")
    # Display the output and error (if any) in the terminal
        if output:
            terminal_output.insert(tk.END, f"{output.decode()}")
        if error:
            terminal_output.insert(tk.END, f"{error.decode()}")
        terminal_input.delete(0, tk.END)

# Define the tag for user input
    terminal_output.tag_configure("user_input", foreground="#00ff00")

    # Bind the Enter key to the run_command function
    terminal_input.bind("<Return>", lambda event: run_command())
file_menu.add_command(label="Open Shell", command=open_terminal)
root.mainloop()