import tkinter as tk
from tkinter import messagebox
import subprocess
import os

# Define the base directory where your scripts are located
BASE_DIR = '/media/sf_Win_Kali/CompNet_Project'  # Update this path if different

# Define the paths to your scripts
SCRIPTS = {
    'HTTP': os.path.join(BASE_DIR, 'http_client.py'),
    'DNS': os.path.join(BASE_DIR, 'dns_client.py'),
    'SMTP': os.path.join(BASE_DIR, 'smtp_client.py'),
    'FTP': os.path.join(BASE_DIR, 'ftp_client.py'),
    'POP3': os.path.join(BASE_DIR, 'docker_files', 'pop3_client.py'),  # POP3 is in docker_files
}

# Function to execute a script
def run_script(script_path):
    if os.path.exists(script_path):
        try:
            # Determine if the script requires sudo (only if necessary)
 
            # Adjust this condition based on your specific requirements
            if 'dhcp_client.py' in script_path:
                cmd = ['sudo', 'python3', script_path]
            else:
                cmd = ['python3', script_path]
            
            # Execute the script and capture output
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            output, error = process.communicate()
            
            # Prepare the output to display
            display_output = output if output else error
            
            # Create a new window to display the output
            output_window = tk.Toplevel(root)
            output_window.title(f"Output - {os.path.basename(script_path)}")
            output_window.geometry("600x400")  # Adjust size as needed
            
            # Add a scrollable text widget
            text_widget = tk.Text(output_window, wrap='word')
            text_widget.insert('1.0', display_output)
            text_widget.config(state='disabled')  # Make the text read-only
            text_widget.pack(expand=True, fill='both')
            
            # Add a scrollbar
            scrollbar = tk.Scrollbar(output_window, command=text_widget.yview)
            text_widget['yscrollcommand'] = scrollbar.set
            scrollbar.pack(side='right', fill='y')
            
        except Exception as e:
            # Display any exceptions in a message box
            messagebox.showerror("Execution Error", f"An error occurred while executing the script:\n{e}")
    else:
        # Display an error if the script path does not exist
        messagebox.showerror("File Not Found", f"The script was not found:\n{script_path}")

# Create the main window
root = tk.Tk()
root.title("Network Protocol Tester")
root.geometry("400x450")  # Adjust the window size as needed

# Create a label for the GUI
label = tk.Label(root, text="Select a Protocol to Test", font=("Helvetica", 16))
label.pack(pady=15)

# Function to create buttons
def create_button(protocol_name, script_path):
    button = tk.Button(
        root,
        text=protocol_name,
        width=35,
        height=2,
        command=lambda: run_script(script_path)
    )
    button.pack(pady=10)

# Create buttons for each protocol
for protocol, path in SCRIPTS.items():
    create_button(protocol, path)

# Start the GUI event loop
root.mainloop()
