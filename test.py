import Array2048
import tkinter as tk

class application(tk.Tk):
    def __init__(self):  
        peerIP = input("Input Peer IP")
        datatable = Array2048.Array2048
        tk.Tk.__init__(self, className="2048 Multiplayer")

    def drawtable(self, ):
        table = SimpleTable(self, 4,4)
        table.pack(side="top", fill="x")
        table.set(0,0,"test")
        
                

class SimpleTable(tk.Frame):
    def __init__(self, parent, rows=10, columns=2):
        # use black background so it "peeks through" to 
        # form grid lines
        tk.Frame.__init__(self, parent, background="black")
        self._widgets = []
        for row in range(rows):
            current_row = []
            for column in range(columns):
                label = tk.Label(self, text="%s/%s" % (row, column), 
                                 borderwidth=0, width=10)
                label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                current_row.append(label)
            self._widgets.append(current_row)

        for column in range(columns):
            self.grid_columnconfigure(column, weight=1)


    def set(self, row, column, value):
        widget = self._widgets[row][column]
        widget.configure(text=value)


App = application()
App.mainloop()