from customtkinter import *

global glb_color_blue, glb_color_transparent, glb_color_pink
glb_color_blue = "deepskyblue3"
glb_color_transparent = "transparent"
glb_color_pink = "deeppink3"

# Program to count the number of times a character occurs in a given string.
print("This is a program to count the number of times a character occurs in a given string.")

root = CTk()
root.geometry ("400x200")
set_appearance_mode("Dark")
set_default_color_theme("dark-blue")
frame = CTkFrame(root, width=400, height=200, border_color=glb_color_blue, border_width=2).pack()

str_input_label = CTkLabel(frame, text="Enter a string :", text_color = glb_color_pink, fg_color = glb_color_transparent)
str_input_label.place(x = 5, y = 10)

str_input = CTkEntry(frame, text_color = glb_color_blue, width = 200)
str_input.place(x = 175, y = 10)

sub_str_label = CTkLabel(frame, text= "Enter the character to count : ", text_color = glb_color_pink, fg_color = glb_color_transparent)
sub_str_label.place(x = 5, y = 45)

sub_str_input = CTkEntry(frame, text_color = glb_color_blue, width = 200)
sub_str_input.place(x = 175, y = 45)

def on_click():

    _str_input = str_input.get()
    _sub_str = sub_str_input.get()

    count = _str_input.count(_sub_str)

    if count == 0 :
        def do_after():
            label.destroy()

        label = CTkLabel(frame, text= f"The string : '{_str_input}' does not contain : '{_sub_str}'.", text_color = "red", fg_color = glb_color_transparent)
        label.place(x = 80, y = 125)
        label.after(3500, do_after)
       # print(f"The string : '{_str_input}' does not contain : '{_sub_str}'.")
    else :
        def do_after():
            label.destroy()

        label = CTkLabel(frame, text= f"The string : '{_str_input}' contains '{_sub_str}', '{count}' times .", text_color = "green", fg_color = glb_color_transparent)
        label.place(x = 80, y = 125)
        label.after(3500, do_after)
        #print(f"The string : '{_str_input}' contains '{_sub_str}', '{count}' times .")


btn = CTkButton(frame, text = "Submit", corner_radius=70, command=on_click)
btn.place(x = 175, y = 80)

root.mainloop()


# str_input = input("Enter a string : ")
# sub_str = input("Enter the character to count : ")

