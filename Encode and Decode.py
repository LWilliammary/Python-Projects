#!/usr/bin/env python
# coding: utf-8

# # Encoding and Decoding Text

# In[1]:


# import tkinter module
from tkinter import *

# import other necessary modules
import random
import time
import datetime


# In[2]:


# creating root object
root = Tk()


# In[3]:


# Define the size of window
root.geometry("1500x6000")


# In[4]:


# setting up the title of window
root.title("Python Encoding and Decoding")

Tops = Frame(root, width = 1600, relief = SUNKEN)
Tops.pack(side = TOP)

f1 = Frame(root, width = 800, height = 700,relief = SUNKEN)
f1.pack(side = LEFT)


# In[5]:


#Display Current Date and Time

localtime = time.asctime(time.localtime(time.time()))

lblInfo = Label(Tops, font = ('helvetica', 25, 'bold'),
		text = "Encoding and Decoding",
					fg = "Black", bd = 10, anchor='w')
					
lblInfo.grid(row = 0, column = 0)

lblInfo = Label(Tops, font=('arial', 20, 'bold'),
			text = localtime, fg = "Black",
						bd = 10, anchor = 'w')
						
lblInfo.grid(row = 1, column = 0)

rand = StringVar()
Msg = StringVar()
key = StringVar()
mode = StringVar()
Result = StringVar()


# In[6]:


# exit function
def qExit():
	root.destroy()


# In[7]:


# Function to reset the window
def Reset():
	rand.set("")
	Msg.set("")
	key.set("")
	mode.set("")
	Result.set("")


# In[8]:


# reference

# labels
lblMsg = Label(f1, font = ('arial', 16, 'bold'),
		text = "Enter the Text", bd = 16, anchor = "w")
		
lblMsg.grid(row = 1, column = 0)

txtMsg = Entry(f1, font = ('arial', 16, 'bold'),
		textvariable = Msg, bd = 10, insertwidth = 4,
				bg = "white", justify = 'right')
				
txtMsg.grid(row = 1, column = 1)

lblkey = Label(f1, font = ('arial', 16, 'bold'),
			text = "KEY Value", bd = 16, anchor = "w")
			
lblkey.grid(row = 2, column = 0)

txtkey = Entry(f1, font = ('arial', 16, 'bold'),
		textvariable = key, bd = 10, insertwidth = 4,
				bg = "white", justify = 'right')
				
txtkey.grid(row = 2, column = 1)

lblmode = Label(f1, font = ('arial', 16, 'bold'),
		text = "MODE(Enter 'e' for 'encrypt text', 'd' for 'decrypt text')",
								bd = 16, anchor = "w")
								
lblmode.grid(row = 3, column = 0)

txtmode = Entry(f1, font = ('arial', 16, 'bold'),
		textvariable = mode, bd = 10, insertwidth = 4,
				bg = "white", justify = 'right')
				
txtmode.grid(row = 3, column = 1)

lblService = Label(f1, font = ('arial', 16, 'bold'),
			text = "Display the Result", bd = 16, anchor = "w")
			
lblService.grid(row = 2, column = 2)

txtService = Entry(f1, font = ('arial', 16, 'bold'), 
			textvariable = Result, bd = 10, insertwidth = 4,
					bg = "white", justify = 'right')
						
txtService.grid(row = 2, column = 3)


# In[9]:


#cipher Text
import base64


# In[10]:


# Function to encode  (e)
def encode(key, clear):
	enc = []
	
	for i in range(len(clear)):
		key_c = key[i % len(key)]
		enc_c = chr((ord(clear[i]) +
					ord(key_c)) % 256)
					
		enc.append(enc_c)
		
	return base64.urlsafe_b64encode("".join(enc).encode()).decode()


# In[11]:


# Function to decode (d)
def decode(key, enc):
	dec = []
	
	enc = base64.urlsafe_b64decode(enc).decode()
	for i in range(len(enc)):
		key_c = key[i % len(key)]
		dec_c = chr((256 + ord(enc[i]) -
						ord(key_c)) % 256)
							
		dec.append(dec_c)
	return "".join(dec)


# In[12]:


def Ref():
	print("Message= ", (Msg.get()))

	clear = Msg.get()
	k = key.get()
	m = mode.get()

	if (m == 'e'):
		Result.set(encode(k, clear))
	else:
		Result.set(decode(k, clear))


# In[13]:


# Display Message Button 
btnTotal = Button(f1, padx = 16, pady = 8, bd = 16, fg = "black",
						font = ('arial', 16, 'bold'), width = 10,
					text = "Display Message", bg = "Yellow",
						command = Ref).grid(row = 7, column = 1)


# In[14]:


# Reset Button Function
btnReset = Button(f1, padx = 16, pady = 8, bd = 16,
				fg = "black", font = ('arial', 16, 'bold'),
					width = 10, text = "Reset", bg = "Yellow",
				command = Reset).grid(row = 7, column = 2)


# In[15]:


# Exit Button Function
btnExit = Button(f1, padx = 16, pady = 8, bd = 16, 
				fg = "black", font = ('arial', 16, 'bold'),
					width = 10, text = "Exit", bg = "Yellow",
				command = qExit).grid(row = 7, column = 3)


# In[16]:


# Window alive Status
root.mainloop()


# In[ ]:




