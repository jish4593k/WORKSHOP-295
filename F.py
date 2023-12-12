import tensorflow as tf
from tensorflow import keras
from tkinter import Tk, Label, Entry, Button, StringVar

def get_password_strength(password):
 
    model = keras.Sequential([
        keras.layers.Dense(64, input_shape=(len(password),), activation='relu'),
        keras.layers.Dense(1, activation='sigmoid')
    ])

  
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    
    password_numeric = [ord(char) for char in password]

    
    prediction = model.predict(tf.constant([password_numeric]))

    # Return a strength score (you can define your own threshold)
    return prediction[0][0]

class PasswordStrengthGUI:
    def __init__(self, master):
        self.master = master
        master.title("Password Strength Checker")

        self.label = Label(master, text="Enter your password:")
        self.label.pack()

        self.entry_password = Entry(master, show="*")
        self.entry_password.pack()

        self.strength_var = StringVar()
        self.strength_label = Label(master, textvariable=self.strength_var)
        self.strength_label.pack()

        self.check_strength_button = Button(master, text="Check Strength", command=self.check_password_strength)
        self.check_strength_button.pack()

    def check_password_strength(self):
        password = self.entry_password.get()
        strength = get_password_strength(password)

        if strength > 0.7:
            strength_text = "Strong Password"
        elif 0.4 <= strength <= 0.7:
            strength_text = "Medium Password"
        else:
            strength_text = "Weak Password"

        self.strength_var.set(strength_text)

if __name__ == '__main__':
    root = Tk()
    app = PasswordStrengthGUI(root)
    root.mainloop()
