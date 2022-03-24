import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window= tkinter.Tk()

        #configure the main window
        self.main_window.geometry("500x200")
        self.main_window.title('!Bulid Your Own Pizza!')
        self.main_window['background']='#856ff8'

        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame1 = tkinter.Frame(self.main_window)
        self.mid_frame2 = tkinter.Frame(self.main_window)
        self.bottom_frame1 = tkinter.Frame(self.main_window)
        self.bottom_frame2 = tkinter.Frame(self.main_window)
        self.bottom_frame3 = tkinter.Frame(self.main_window)
        self.bottom_frame4 = tkinter.Frame(self.main_window)
        self.bottom_frame5 = tkinter.Frame(self.main_window)
        self.bottom_frame6 = tkinter.Frame(self.main_window)

        #enter customer name
        self.prompt_label1 = tkinter.Label(self.top_frame,text='Enter Customer Name:')

        self.name_entry = tkinter.Entry(self.top_frame, width=10)

        self.prompt_label1.pack(side="left")
        self.name_entry.pack(side="left")

        #creat radiobutton

        self.radio_var = tkinter.IntVar()

        self.radio_var.set(2)

        self.rb1 = tkinter.Radiobutton(self.mid_frame1, text = 'Stuffed($4.00)', variable = self.radio_var,
        value=4)

        self.rb2 = tkinter.Radiobutton(self.mid_frame1, text = 'Thin     ($2.00)', variable = self.radio_var,
        value=2)
        
        self.rb3 = tkinter.Radiobutton(self.mid_frame1, text = 'Thick   ($3.00)', variable = self.radio_var,
        value=3)

        #pack the radiobuttons.
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        # Create three IntVar objects to use with the checkbuttons.    
        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()

        # Set the intVar objects to 0.
        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)

        self.cb1 = tkinter.Checkbutton(self.mid_frame2, text="Pepperoni($1.00)", variable =self.cb_var1, onvalue = 1, offvalue = 0)
        self.cb2 = tkinter.Checkbutton(self.mid_frame2, text="Sausage    ($3.00)", variable =self.cb_var2, onvalue = 3, offvalue = 0)
        self.cb3 = tkinter.Checkbutton(self.mid_frame2, text="Chicken    ($2.00)", variable =self.cb_var3, onvalue = 2, offvalue = 0)

        #pack the checkbutton
        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()

        
       
        #Yes, we have to pack the frames too!
        self.top_frame.pack(side="top")
        self.mid_frame1.pack(side="left")
        self.mid_frame2.pack(side="right")
        self.bottom_frame1.pack(side="bottom")
        self.bottom_frame2.pack(side="bottom")
        self.bottom_frame3.pack(side="bottom")
        self.bottom_frame4.pack(side="bottom")
        self.bottom_frame5.pack(side="bottom")
        self.bottom_frame6.pack(side="bottom")
        

        

        

        self.calbutton = tkinter.Button(self.bottom_frame6, text= 'Calculation', command= self.calculation)

        self.quit_button = tkinter.Button(self.bottom_frame1,text='Quit', command= self.main_window.destroy)


        self.calbutton.pack(side= "left")
        self.quit_button.pack(side="right")
        

        tkinter.mainloop()
        
    def calculation(self):
        
        crust_price= self.radio_var.get() + self.cb_var1.get() + self.cb_var2.get() + self.cb_var3.get()
        customer_name = self.name_entry.get()

        

        tkinter.messagebox.showinfo('Results', str(customer_name) + " " + "has spends" +" "+ str(crust_price) + '$' + " " + "on pizza crust and toppings!")


        






my_gui = MyGUI() 