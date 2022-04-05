import tkinter as tk

window = tk.Tk()

# Frames
frm_leftpane = tk.Frame(master = window, width = 200, height = 60)
frm_rightpane = tk.Frame(master = window, width = 200, height = 60)
frm_enbuttons = tk.Frame(master = frm_rightpane, width = 200, height = 10)
frm_disbuttons = tk.Frame(master = frm_rightpane, width = 200, height = 10)
frm_colors = tk.Frame(master = frm_rightpane, width = 200, height = 40)

# Packing frames
frm_leftpane.pack(side = tk.LEFT)
frm_rightpane.pack(side = tk.RIGHT)
frm_enbuttons.pack(side = tk.TOP)
frm_colors.pack(side = tk.TOP)
frm_disbuttons.pack(side = tk.TOP)

# Color labels
lbl_purple = tk.Label(master = frm_colors, text = "Purple", background = "purple", width = 40, height = 40)
lbl_blue = tk.Label(master = frm_colors, text = "Blue", background = "blue", width = 40, height = 40)
lbl_green = tk.Label(master = frm_colors, text = "Green", background = "green", width = 40, height = 40)
lbl_red = tk.Label(master = frm_colors, text = "Red", background = "red", width = 40, height = 40)
lbl_yellow = tk.Label(master = frm_colors, text = "Yellow", background = "yellow", width = 40, height = 40)

# Pack color labels
lbl_purple.pack(side = tk.LEFT)
lbl_blue.pack(side = tk.LEFT)
lbl_green.pack(side = tk.LEFT)
lbl_red.pack(side = tk.LEFT)
lbl_yellow.pack(side = tk.LEFT)

# Enable Buttons
btn_enpurple = tk.Button(master = frm_enbuttons, text = "Accept", width = 40, height = 40)
btn_enblue = tk.Button(master = frm_enbuttons, text = "Accept", width = 40, height = 40)
btn_engreen = tk.Button(master = frm_enbuttons, text = "Accept", width = 40, height = 40)
btn_enred = tk.Button(master = frm_enbuttons, text = "Accept", width = 40, height = 40)
btn_enyellow = tk.Button(master = frm_enbuttons, text = "Accept", width = 40, height = 40)

# Pack enable buttons
btn_enpurple.pack(side = tk.LEFT)
btn_enblue.pack(side = tk.LEFT)
btn_engreen.pack(side = tk.LEFT)
btn_enred.pack(side = tk.LEFT)
btn_enyellow.pack(side = tk.LEFT)

# Disable Buttons
btn_dispurple = tk.Button(master = frm_disbuttons, text = "Reject", width = 40, height = 40)
btn_disblue = tk.Button(master = frm_disbuttons, text = "Reject", width = 40, height = 40)
btn_disgreen = tk.Button(master = frm_disbuttons, text = "Reject", width = 40, height = 40)
btn_disred = tk.Button(master = frm_disbuttons, text = "Reject", width = 40, height = 40)
btn_disyellow = tk.Button(master = frm_disbuttons, text = "Reject", width = 40, height = 40)

# Pack enable buttons
btn_dispurple.pack(side = tk.LEFT)
btn_disblue.pack(side = tk.LEFT)
btn_disgreen.pack(side = tk.LEFT)
btn_disred.pack(side = tk.LEFT)
btn_disyellow.pack(side = tk.LEFT)

window.mainloop()
