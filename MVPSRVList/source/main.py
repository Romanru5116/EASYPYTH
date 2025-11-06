Import tkinter as tk

def button_click():
    """Function to be called when the button is clicked."""
    label.config(text="Button was clicked!")

# Create the main window
root = tk.Tk()
root.title("Tkinter Example")
root.geometry("300x200") # Set initial window size

# Create a Label widget
label = tk.Label(root, text="Hello, Srvlist!")
label.pack(pady=20) # Add padding for better spacing

# Create a Button widget
button = tk.Button(root, text="service1", command=button_click)
button.pack()

# Start the Tkinter event loop
root.mainloop()
