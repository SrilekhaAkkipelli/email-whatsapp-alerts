"""
Gmail to WhatsApp Alert System - GUI
Tkinter-based interface for configuring and running the alert system.
"""

import tkinter as tk
from tkinter import filedialog, messagebox
import email_alerts_runtime


class EmailAlertApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Gmail to WhatsApp Alerts")
        self.master.geometry("450x520")
        self.master.resizable(False, False)
        self.gmail_file = None
        self._build_ui()

    def _build_ui(self):
        # Title
        tk.Label(self.master, text="📧 Gmail → WhatsApp Alerts",
                 font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=15)

        fields = [
            ("Gmail Credentials File:", None),
            ("Twilio SID:", None),
            ("Twilio Auth Token:", None),
            ("WhatsApp From Number:", None),
            ("WhatsApp To Number:", None),
            ("Unread Threshold:", None),
            ("Batch Size:", None),
            ("Daily Limit:", None),
            ("Keywords (comma separated):", None),
        ]

        self.entries = {}
        for i, (label, _) in enumerate(fields, start=1):
            tk.Label(self.master, text=label, anchor='w').grid(
                row=i, column=0, padx=10, pady=6, sticky='w')

            if i == 1:
                btn = tk.Button(self.master, text="Browse", command=self._browse)
                btn.grid(row=i, column=1, padx=10)
                self.browse_label = tk.Label(self.master, text="No file selected",
                                              fg='gray', font=("Arial", 8))
                self.browse_label.grid(row=i, column=1, padx=(90, 10))
            else:
                entry = tk.Entry(self.master, width=30)
                entry.grid(row=i, column=1, padx=10, pady=6)
                self.entries[label] = entry

        # Defaults
        self.entries["Unread Threshold:"].insert(0, "50")
        self.entries["Batch Size:"].insert(0, "3")
        self.entries["Daily Limit:"].insert(0, "9")
        self.entries["Keywords (comma separated):"].insert(0, "urgent,invoice,meeting,bank,approved")

        # Run button
        tk.Button(self.master, text="▶  Run Alert System", bg="#25D366", fg="white",
                  font=("Arial", 11, "bold"), command=self._run,
                  width=20, height=2).grid(row=11, column=0, columnspan=2, pady=20)

    def _browse(self):
        self.gmail_file = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
        if self.gmail_file:
            self.browse_label.config(text=self.gmail_file.split('/')[-1], fg='black')

    def _run(self):
        try:
            if not self.gmail_file:
                messagebox.showerror("Error", "Please select Gmail credentials file.")
                return

            keywords = [k.strip() for k in
                        self.entries["Keywords (comma separated):"].get().split(",")]

            email_alerts_runtime.run_alerts(
                credentials_file=self.gmail_file,
                twilio_sid=self.entries["Twilio SID:"].get(),
                twilio_auth=self.entries["Twilio Auth Token:"].get(),
                from_number=self.entries["WhatsApp From Number:"].get(),
                to_number=self.entries["WhatsApp To Number:"].get(),
                batch_size=int(self.entries["Batch Size:"].get()),
                daily_limit=int(self.entries["Daily Limit:"].get()),
                keywords=keywords,
                unread_threshold=int(self.entries["Unread Threshold:"].get()),
            )
            messagebox.showinfo("Success", "✅ Email alerts sent successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred:\n{e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = EmailAlertApp(root)
    root.mainloop()

# update 13 - 2025-01-17
# update 29 - 2025-01-27
# update 36 - 2025-01-30
# update 49 - 2025-02-07
# update 59 - 2025-02-11
# update 60 - 2025-02-13
# update 87 - 2025-03-04
# update 98 - 2025-03-11
# update 101 - 2025-03-14
# update 102 - 2025-03-14
# update 104 - 2025-03-15
# update 109 - 2025-03-18
# update 113 - 2025-03-22
# update 129 - 2025-04-02
# update 142 - 2025-04-07
# update 151 - 2025-04-14