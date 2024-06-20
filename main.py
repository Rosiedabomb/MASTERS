import tkinter as tk
from tkinter import filedialog, messagebox
import sys
import os
from functions import extract_peak_values # functions i have defined in other file called 'functions.py'
from functions import predict_strain_90th, predict_strainrate_90th

#adding the file location to the path.
#script_dir = os.path.dirname(os.path.abspath(__file__)) # __file__ is a special variable holding path of current script.
#sys.path.append(script_dir)

#defining a functions to happen on button clicks:
def Upload_file_action(event=None):
    file_path = filedialog.askopenfilename()
    if file_path: 
        path.set(file_path)
        file_name.set(os.path.basename(file_path))
        print('file path selected')

#runs when predict button is clicked
def predict(event=None):
    if path.get() != 'file path will appear here':
        peak_la, peak_ra, peak_rv = extract_peak_values(path.get())
        strain_prediction_value.set(predict_strain_90th(peak_la, peak_ra, peak_rv))
        strainrate_prediction_value.set(predict_strainrate_90th(peak_la, peak_ra, peak_rv))
        print('predict button pressed')
        #also need to add predictive error bar.
    else:
        #do nothing/come up with popup 'upload file first'
        messagebox.showwarning("No File Selected", "Please upload a file first.")


#CREATING THE MAIN WINDOW
window = tk.Tk()
window.configure(bg='#C90062')
window.title("Brain Strain Predictor") # set title
window.geometry('475x225')
window.iconbitmap('C:/Users/Rosie/Documents/04_FINAL FOURTH YEAR/MASTERS/GUI/brain_icon_3.ico')

#defining variables as StringVars so they automatically update
path = tk.StringVar(value='...')
strain_prediction_value = tk.StringVar(value='...')
strainrate_prediction_value = tk.StringVar(value='...')
file_name = tk.StringVar(value='filename will appear here')

#creating widgets - labels are just text displayed, entries allow user input, buttons are clickable
#labels
strain_label = tk.Label(window, text="Strain 90th percentile, prediction:")
strain_prediction = tk.Label(window, textvariable=strain_prediction_value)
strainrate_label = tk.Label(window, text="Strain rate 90th percentile, prediction:")
strainrate_prediction = tk.Label(window, textvariable=strainrate_prediction_value)
file_selected_label = tk.Label(window, textvariable=file_name,bg='#C90062')
prediction_interval_strainrate = tk.Label(window, text='+/- 0.026 (95%)') #smaller
prediction_interval_strain = tk.Label(window, text='+/- 0.06 (95%)') #larger

#buttons -  command above
upload_file_button = tk.Button(window, text="Upload file",command=Upload_file_action)
predict_button = tk.Button(window, text="Predict",command=predict)


# Place widgets with padding
upload_file_button.grid(row=0, column=0, columnspan=3, pady=10)
file_selected_label.grid(row=1, column=0, columnspan=3, pady=5)
strain_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
strain_prediction.grid(row=2, column=1, padx=10, pady=5, sticky="w")
prediction_interval_strain.grid(row=2, column=2, padx=0, pady=5, sticky="w")
strainrate_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
strainrate_prediction.grid(row=3, column=1, padx=10, pady=5, sticky="w")
prediction_interval_strainrate.grid(row=3, column=2, padx=0, pady=5, sticky="w")
predict_button.grid(row=4, column=0, columnspan=3, pady=20)

window.mainloop()
