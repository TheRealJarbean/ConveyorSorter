import tkinter as tk

window = tk.Tk()

def en_red():
    enbuttons[0]["state"] = "disabled"
    disbuttons[0]["state"] = "active"

def en_green():
    enbuttons[1]["state"] = "disabled"
    disbuttons[1]["state"] = "active"

def en_blue():
    enbuttons[2]["state"] = "disabled"
    disbuttons[2]["state"] = "active"

def dis_red():
    disbuttons[0]["state"] = "disabled"
    enbuttons[0]["state"] = "active"

def dis_green():
    disbuttons[1]["state"] = "disabled"
    enbuttons[1]["state"] = "active"

def dis_blue():
    disbuttons[2]["state"] = "disabled"
    enbuttons[2]["state"] = "active"

# Create primary panes
frm_leftpane = tk.Frame(master = window, width = 500, height = 220, pady = 5)
frm_rightpane = tk.Frame(master = window)

# Pack primary panes
frm_leftpane.pack(side = tk.LEFT)
frm_rightpane.pack(side = tk.RIGHT)

# Create and pack left pane content
lbl_currentColor = tk.Label(master = frm_leftpane, text = "Blue")
lbl_currentColor.pack()
frm_currentColor = tk.Frame(master = frm_leftpane, background = "blue", width = 100, height = 100)
frm_currentColor.pack(fill = "both", padx = 20, pady = 20)

# Create and pack enable buttons
enbuttons = [
    tk.Button(master = frm_rightpane, text = "Accept", relief = tk.RAISED, width = 12, state = "disabled", height = 4, command = en_red),
    tk.Button(master = frm_rightpane, text = "Accept", relief = tk.RAISED, width = 12, state = "disabled",  height = 4, command = en_green),
    tk.Button(master = frm_rightpane, text = "Accept", relief = tk.RAISED, width = 12, state = "disabled",  height = 4, command = en_blue)
]

i = 0
for btn in enbuttons:
    btn.grid(row = 0, column = i)
    i += 1

# Create and pack color labels
i = 0
for color in [ "red", "green", "blue"]:
    tk.Frame(master = frm_rightpane, background = color, width = 95, height = 95).grid(row = 1, column = i)
    i += 1

# Create and pack disable buttons
disbuttons = [
    tk.Button(master = frm_rightpane, text = "Reject", relief = tk.RAISED, width = 12, height = 4, command = dis_red),
    tk.Button(master = frm_rightpane, text = "Reject", relief = tk.RAISED, width = 12, height = 4, command = dis_green),
    tk.Button(master = frm_rightpane, text = "Reject", relief = tk.RAISED, width = 12, height = 4, command = dis_blue)
]

i = 0
for btn in disbuttons:
    btn.grid(row = 2, column = i)
    i += 1

window.mainloop()