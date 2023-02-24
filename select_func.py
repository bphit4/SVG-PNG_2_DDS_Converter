import tkinter.filedialog as filedialog
import tkinter.scrolledtext as scrolledtext
import tkinter.ttk as ttk

class Select_Func:
    def __init__(self, master, convert_files_func):
        self.master = master
        self.convert_files_func = convert_files_func
        master.title("SVG to PNG Converter")

        # Create a label and a button to select files using a file dialog
        self.select_label = ttk.Label(master, text="Select SVG files:")
        self.select_button = ttk.Button(master, text="Select", command=self.select_files)

        # Create a scrolled text widget to display the conversion log
        self.log = scrolledtext.ScrolledText(master, height=10, state="disabled")
        self.log.bind("<Control-c>", self.copy_log)

        # Create a button to clear the log
        self.clear_button = ttk.Button(master, text="Clear Log", command=self.clear_log)

        # Create an Export Log button
        self.export_button = ttk.Button(master, text="Export Log", command=self.export_log)

        # Pack the widgets
        self.select_label.pack(pady=(10, 5))
        self.select_button.pack(pady=(0, 10))
        self.log.pack(fill="both", expand=True, padx=10, pady=(0, 10))
        self.clear_button.pack(side="left", padx=10)
        self.export_button.pack(side="right", padx=10)

    def select_files(self):
        # Show a file dialog to select multiple SVG files
        file_paths = filedialog.askopenfilenames(filetypes=[("SVG files", "*.svg")])
        if file_paths:
            self.convert_files(file_paths)

    def convert_files(self, file_paths):
        self.log.config(state="normal")
        results = self.convert_files_func(file_paths)
        for success, message in results:
            if success:
                self.log.insert("end", message + "\n")
            else:
                self.log.insert("end", message + "\n")
        self.log.config(state="disabled")

    def clear_log(self):
        self.log.config(state="normal")
        self.log.delete(1.0, "end")
        self.log.config(state="disabled")

    def copy_log(self, event):
        self.master.clipboard_clear()
        self.master.clipboard_append(self.log.get(1.0, "end"))

    def export_log(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, "w") as f:
                f.write(self.log.get(1.0, "end"))
