from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import askinteger
from tkinter.simpledialog import askstring
import pickle as pkl
from datetime import datetime
import matplotlib.pyplot as plt

f=open('my_pickle.pkl','rb+')
accounts=pkl.load(f)

# an already created dictionary is loaded to pickle file
# accounts is the dictionary which have all the details of the customers

from tkinter import *
import requests

class RealTimeCurrencyConverter():
	def __init__(self,url):
		self.data= requests.get(url).json()
		self.currencies = self.data['rates']
		# get the data from the given url , which is in json file
        # stor the data in the dictionary
	def convert(self, from_currency, to_currency, amount): 
		initial_amount = amount 
		#first convert it into INR if it is not in INR.
		# because our base currency is INR
		if to_currency != 'INR' : 
			amount = amount / self.currencies[from_currency] 
	
		# limiting the precision to 4 decimal places 
		amount = round(amount * self.currencies[to_currency], 4) 
		return amount

class ATM:
    cus=0
    def __init__(self,accounts):
        self.root = Tk()
        self.accounts = accounts
        from PIL import ImageTk, Image
        
        self.root.iconbitmap('atm.ico')
        # the above syntax is used to create a atm icon in the tkinter window
        self.bg=ImageTk.PhotoImage(Image.open("atm_bg.jpg"))
        # opens the image from the file location, but the type of image file has to be specified
        self.bg_label=Label(self.root,image=self.bg)
        self.bg_label.place(x=0,y=0,relwidth=1,relheight=1)
        # background image of atm is being added in the tkinter window

        self.root.geometry("2560x1440+0+0")
        # the window will be in full screen
        self.root.title("ATM MANAGEMENT SYSTEM",)
        self.root.configure(bg='#f0eb8d')
        self.Label_front1=Label(self.root,text=' NITPY BANK',font=('Arial Rounded MT Bold',70),bg="#F0EB8D",fg='brown').pack()
        self.Label_front=Label(self.root,text='Your money is safe with us',bg="#F0EB8D",font=('Calibri',40),fg='brown').pack()
        # two labels created to display the name of the bank and its slogan 

        self.login_label = Label(self.root,text="Login Page",font=('Arial Rounded MT Bold',60),fg='brown',bg='#97deff').place(x=200,y=300)
        
        
        self.credential_label = Label(self.root,text="Name",font=('Britannic Bold',30),fg='brown',bg='#F0EB8D')
        self.credential_entry = Entry(self.root,bg='#F0EB8D',width=100,font=('Calibri',40))
        self.user_label = Label(self.root,text="PIN",font=('Britannic Bold',30),fg='brown',bg='#F0EB8D')
        self.user_entry = Entry(self.root,bg='#F0EB8D',width=100,font=('Calibri',40),show='*')

        # two entry's are defined to get name and pin as input from the customer
        # two labels created to show which is name and pin
        # we are using the name of the customer as debit or credit card to authenticate

        self.user_label.place(x=200,y=600)
        self.user_entry.place(x=400,y=600,width=200,height=50)
        self.credential_label.place(x=200,y=500)
        self.credential_entry.place(x=400,y=500,width=500,height=50)
        self.submit = Button(self.root,width=10,text="Login",command=self.authenticate,bg='#F0EB8D',font=('Arial Rounded MT Bold',30),fg='blue') 
        
        self.submit.place(x=200,y=700)

       # creating a button to proceed for the next page for further transactions
        self.root.mainloop()
    

    def authenticate(self):
        # this the authentication part to authenticate the user
        self.flag=-1
        self.user_name=self.credential_entry.get()
        # we are getting the customer name as input
        
        if self.user_name in accounts:
            # if the entered username is present in accounts dictionary
            p=accounts[self.user_name]
            # store the username in dictionary p
            self.pin=self.user_entry.get()
            # get pin as input from customer
            if(self.pin==p['pin']):
                # if the entered pin matches the pin in dictionary,authenticated
                self.cus=accounts[self.user_name]
                #store the data in 'cus' dictionary
                self.flag=1
                
                self.root.destroy()
                # the root window is destroyed
                self.root=Tk()
                # a new window is created and we are going to add the functionalites 
                from PIL import ImageTk, Image

                self.root.iconbitmap('atm.ico')
                self.bg=ImageTk.PhotoImage(Image.open("atm_bg.jpg"))
                self.bg_label=Label(self.root,image=self.bg)
                self.bg_label.place(x=0,y=0,relwidth=1,relheight=1)

                self.root.geometry('1920x1080+0+0')
                self.root.title("ATM MANAGEMENT SYSTEM",)
                self.root.configure(bg='#f0eb8d')
                self.Label_front1=Label(self.root,text=' NITPY BANK',font=('Arial Rounded MT Bold',70),bg="#F0EB8D",fg='brown').pack()
                self.Label_front=Label(self.root,text='Your money is safe with us',bg="#F0EB8D",font=('Calibri',40),fg='brown').pack()
                
                
                self.amount=Label(text='Enter the amount',font=('arial',20),fg='brown').pack()
                self.e=Entry(self.root,bg='#F0EB8D',width=30,font=('Calibri',40))
                self.e.pack()
                # an entry field is created to get the amount for further transactions
                # this particular field acts as input for deposit, withdraw and money transfer from customer

                self.deposit1 = Button(self.root,width=10,text="DEPOSIT",command=lambda:self.deposit(int(self.e.get())),font=('calibri',40),fg='RED',bg='BLUE')
                self.deposit1.place(x=20,y=300)

                # a button for deposit created where we use int() function to make the entry as input to deposit function

                self.withdraw1 = Button(self.root,width=10,text="WITHDRAW",command=lambda:self.withdraw(int(self.e.get())),font=('calibri',40),fg='RED',bg='BLUE')
                self.withdraw1.place(x=20,y=500)
                # a button for withdraw created where we use int() function to make the entry as input to withdraw function

                self.balance1 = Button(self.root,width=15,text="CHECK BALANCE",command=self.check_balance,font=('calibri',40),fg='RED',bg='BLUE')
                self.balance1.place(x=20,y=700)
                # a button is created to check the balance of the customer, which will take the data from pickle file

                self.update=Button(self.root,width=10,text="UPDATE",command=updatedata,font=('calibri',40),fg='red',bg='blue').place(x=20,y=850)
                # this button dump the data to pickle file 
                self.transfer=Button(self.root,width=17,text="MONEY TRANSFER",command=lambda:self.money_transfer(int(self.e.get())),font=('calibri',40),fg='red',bg='blue').place(x=500,y=300)
                # transfer button is created to perform the functionality of money transfer
                self.statement=Button(self.root,width=19,text="ACCOUNT STATEMENT",command=self.distrans,font=('calibri',40),fg='red',bg='blue').place(x=500,y=500)
                # a statement button is created for displaying the account statement of the customer

                self.currency=Button(self.root,width=19,text="CURRENCY EXCHANGER",command=self.currency_exchanger,font=('calibri',40),fg='red',bg='blue').place(x=500,y=700)
                # currency button is created for exchanging INR to any specified currencies 
                
                self.pin=Button(self.root,width=19,text="CHANGE PIN",command=self.change_pin,font=('calibri',40),fg='red',bg='blue').place(x=500,y=850)
                # pin button is used for performing the functionality of changing pin
                self.number_trans=Button(self.root,width=18,text="TRANSACTIONS_BAR",command=self.number_transactions_BAR,font=('calibri',40),fg='red',bg='blue').place(x=1100,y=300)
                
                self.number_trans=Button(self.root,width=18,text="TRANSACTIONS_PIE",command=self.number_transactions_PIE,font=('calibri',40),fg='red',bg='blue').place(x=1100,y=500)
                # the above two buttons are used for data visualization
                # it shows number of deposits,withdraws and money transfers happening in the account holder's account
                # here we are using bar graph and pie chart
                self.exit=Button(self.root,width=18,text="EXIT",command=self.root.destroy,font=('calibri',40),fg='red',bg='blue').place(x=1100,y=700)
                # Finally a exit button to destroy the window and close the application
                
                self.root.mainloop()
            else:
                self.label3=Label(self.root,text='incorrect pin number',font=('Arial Rounded MT Bold',30),fg='RED').place(x=1000,y=800)
                # if the entered pin is wrong , which is checked from the 'cus' dictionary
                # prints the message that entered pin is incorrect
        else:
            self.label4=Label(self.root,text='AUTHENTICATION UNSUCCESSFUL',font=('Arial Rounded MT Bold',28),fg='RED').place(x=1000,y=400)
            self.label5=Label(self.root,text='RETRY!',font=('Arial Rounded MT Bold',30),fg='RED').place(x=1000,y=600)
            # if we are not entering username or pin
            # it displays authentication unsuccsessful
            # we have to retry

    
    def deposit(self, amount):
        
        self.cus['bal'] += amount
        amount_deposited=self.cus['bal']
        # the amount is added as the parameter 
        # we are getting the input from a entry field which is there in authenticate funtion
        # entered amount is added with the balance
        # balance is stored in 'cus' dictionary 

        messagebox.showinfo('Transaction Successful' ,f'The new balance is {amount_deposited}')
        # message box is added whenever there is a successful deposit

        t = datetime.now()
        k1 = t.strftime("%d-%m-%y")
        k2 = t.strftime("%H:%M:%S")
        # date time module is imported to print date and time

        trans={}
        trans['des']='Deposited'
        trans['amt']=amount
        trans['time']=k2
        trans['day']=k1
        trans['finbal']=self.cus['bal']

        self.cus['trans'].append(trans)
        # a new dictionary called trans is defined
        # inside that dictionary we are adding necessary fields which we need to print the account statement
        # atlast the trans dictionary is appended to 'cus' dicitonary

    def withdraw(self,amount):
        if self.cus['bal']>0 and self.cus['bal']>amount:
            self.cus['bal']-=amount
            amount_withdraw=self.cus['bal']
            messagebox.showinfo('Transaction Successful' ,f'The new balance is {amount_withdraw}')
            # if the transaction was successful
            # we are notifying the customer using the message box

            t = datetime.now()
            k1 = t.strftime("%d-%m-%y")
            k2 = t.strftime("%H:%M:%S")
            # date time module is imported to print date and time

            trans={}
            trans['des']='Withdrawed'
            trans['amt']=amount
            trans['time']=k2
            trans['day']=k1
            trans['finbal']=self.cus['bal']
            self.cus['trans'].append(trans)
            # a new dictionary called trans is defined
            # inside that dictionary we are adding necessary fields which we need to print the account statement
            # atlast the trans dictionary is appended to 'cus' dicitonary
                
        else:
            messagebox.showinfo('Transaction Unsuccessful' ,f'Insufficient Balance in your Account ')
            # if the transaction was not happening 
            # we are printing the message in a message box


    def check_balance(self):
        amount_balance=self.cus['bal']
        # the balance is stored in 'cus' dictionary
        messagebox.showinfo('Balance Statement' ,f'Balance in your account is {amount_balance} ')
        # the message box will be displaying the balance in the customer's account


    def money_transfer(self,amount_trans):
        messagebox.showinfo('Information','AMOUNT ENTERED')
        client_username = askstring('Username', 'Enter the client Username')
        # using simpledialog box from tkinter 
        # askstring means it takes input as string inside the dialog box

        if client_username in accounts:
            messagebox.showinfo('Authentication Successful','The Sender and Receiver is Verified ')
            # if the usernmae is correct or present in pickle file
            # then authentication is successful
            self.p=accounts[client_username]
            # we are adding value 'client username 'in p dicitionary 

            if self.cus['bal']>amount_trans:
            
                self.cus['bal']=self.cus['bal']-amount_trans
                self.p['bal']=self.p['bal']+amount_trans
                # if the balance amount is more than than the entered amount
                # from sender side amount is deducted which is there in 'cus' dictionary
                # the receive side is amount is added to his account and present in 'p ' dicitionary

                messagebox.showinfo('Information','Transaction was Successful ')
                # message box showing that transaction was successful
                t = datetime.now()
                k1 = t.strftime("%d-%m-%y")
                k2 = t.strftime("%H:%M:%S")
                trans={}
                trans['des']='MONEY TRANSFER'
                trans['amt']=amount_trans
                trans['time']=k2
                trans['day']=k1
                trans['finbal']=self.cus['bal']
                self.cus['trans'].append(trans)
                
                 # a new dictionary called trans is defined
                 # inside that dictionary we are adding necessary fields which we need to print the account statement
                 # atlast the trans dictionary is appended to 'cus' dicitonary
            
            else:
                messagebox.showinfo('Information','Insufficient Balance in your account')

                # if balance is not there in your account means 
                # dialog box prints insufficient balance in your account
        else:
            messagebox.showinfo('Information ','Authentication is Unsuccessful')
                # if authentication is not successful then it shows as authentication unsuccessful

    def curr_converter(self):
        url = 'https://api.exchangerate-api.com/v4/latest/INR'
        # this is the url where we daily get the INR to other currency exchange value
        converter = RealTimeCurrencyConverter(url)
        # creating a object instance
        # we are calling the realtimeconverter class
        try:
            amount = int(self.currrency.get())
            # we are getting the input for amount to be exchanged
            source = self.currency_codes[self.clicked_currency.get()]
            # we are selecting the currency we want from the currency code dictionary which stores all the currency values
            if self.cus['bal']>amount:
                #print(converter.convert('INR',source,amount))
                self.cus['bal']=self.cus['bal']-amount
                a=self.cus['bal']
                messagebox.showinfo('Currency Exchange Successful',f'Your balance is {a}')
                self.show_change.config(text=str(converter.convert('INR',source,amount)))
                # amount is deducted from the balance which is stored in 'cus ' dictionary
                # showing the message was successful in a message box
                # we are calling the convert function from realtimecurrencyexchange class using the converter object
                # displaying the amount --> foreign currency which was specified
                t = datetime.now()
                k1 = t.strftime("%d-%m-%y")
                k2 = t.strftime("%H:%M:%S")
                trans={}
                trans['des']='Currency Exchange'
                trans['amt']=amount
                trans['time']=k2
                trans['day']=k1
                trans['finbal']=self.cus['bal']
                self.cus['trans'].append(trans)
            else:
            #messagebox.showinfo('UNSUCESSFUL','Insufficient Balance in your account')
                check = messagebox.askretrycancel('UNSUCESSFUL','Insufficient Balance in your account')
                # if the balance not there , it asks to retry by adding a less amount
                if check:
                    self.currency_exchanger()
                    # the function is calleds
        except ValueError:
             messagebox.showerror('Invalid Input','Give input')
             self.currency_exchanger()
             # if the amount is not given
             # a message box with error message comes to give input 
        except KeyError:
             messagebox.showerror('INVALID INPUT','Enter Currency')
             self.currency_exchanger()
             # if the currency is not selected
             # an error message is popped and asks customer to choose a currency
        
    def currency_exchanger(self):
        # import currency_exchanger
        # self.root.destroy()
        # currency_exchanger.currency_exchanger()
        curr_master = Toplevel(self.root)
        self.currency_codes = {"United Arab Emirates dirham":"AED","Afghan afghani":"AFN","Albanian lek":"ALL","Armenian dram":"AMD","Netherlands Antillean guilder":"ANG","Angolan kwanza":"AOA","Argentine peso":"ARS","Australian dollar":"AUD","Aruban florin":"AWG","Azerbaijani manat":"AZN","Bosnia and Herzegovina convertible mark":"BAM","Barbados dollar":"BBD","Bangladeshi taka":"BDT","Bulgarian lev":"BGN","Bahraini dinar":"BHD","Burundian franc":"BIF","Bermudian dollar":"BMD","Brunei dollar":"BND","Boliviano":"BOB","Bolivian Mvdol (funds code)":"BOV","Brazilian real":"BRL","Bahamian dollar":"BSD","Bhutanese ngultrum":"BTN","Botswana pula":"BWP","Belarusian ruble":"BYN","Belize dollar":"BZD","Canadian dollar":"CAD","Congolese franc":"CDF","WIReuro (complementary currency)":"CHE","Swiss franc":"CHF","WIRfranc (complementary currency)":"CHW","Unidad de Fomento(funds code)":"CLF","Chilean peso":"CLP","Colombian peso":"COP","Unidad de Valor Real (UVR) (funds code)[6]":"COU","Costa Rican colon":"CRC","Cuban convertible peso":"CUC","Cuban peso":"CUP","Cape Verdean escudo":"CVE","Czech koruna":"CZK","Djiboutian franc":"DJF","Danish krone":"DKK","Dominican peso":"DOP","Algerian dinar":"DZD","Egyptian pound":"EGP","Eritrean nakfa":"ERN","Ethiopian birr":"ETB","Euro":"EUR","Fiji dollar":"FJD","Falkland Islands pound":"FKP","Pound sterling":"GBP","Georgian lari":"GEL","Ghanaian cedi":"GHS","Gibraltar pound":"GIP","Gambian dalasi":"GMD","Guinean franc":"GNF","Guatemalan quetzal":"GTQ","Guyanese dollar":"GYD","Hong Kong dollar":"HKD","Honduran lempira":"HNL","Haitian gourde":"HTG","Hungarian forint":"HUF","Indonesian rupiah":"IDR","Israeli new shekel":"ILS","Indian rupee":"INR","Iraqi dinar":"IQD","Iranian rial":"IRR","Icelandic króna(plural: krónur)":"ISK","Jamaican dollar":"JMD","Jordanian dinar":"JOD","Japanese yen":"JPY","Kenyan shilling":"KES","Kyrgyzstani som":"KGS","Cambodian riel":"KHR","Comoro franc":"KMF","North Korean won":"KPW","South Korean won":"KRW","Kuwaiti dinar":"KWD","Cayman Islands dollar":"KYD","Kazakhstani tenge":"KZT","Lao kip":"LAK","Lebanese pound":"LBP","Sri Lankan rupee":"LKR","Liberian dollar":"LRD","Lesotho loti":"LSL","Libyan dinar":"LYD","Moroccan dirham":"MAD","Moldovan leu":"MDL","Malagasy ariary":"MGA","Macedonian denar":"MKD","Myanmar kyat":"MMK","Mongolian tögrög":"MNT","Macanese pataca":"MOP","Mauritanian ouguiya":"MRU","Mauritian rupee":"MUR","Maldivian rufiyaa":"MVR","Malawian kwacha":"MWK","Mexican peso":"MXN","Mexican Unidad de Inversion(UDI) (funds code)":"MXV","Malaysian ringgit":"MYR","Mozambican metical":"MZN","Namibian dollar":"NAD","Nigerian naira":"NGN","Nicaraguan córdoba":"NIO","Norwegian krone":"NOK","Nepalese rupee":"NPR","New Zealand dollar":"NZD","Omani rial":"OMR","Panamanian balboa":"PAB","Peruvian sol":"PEN","Papua New Guinean kina":"PGK","Philippine peso[10]":"PHP","Pakistani rupee":"PKR","Polish złoty":"PLN","Paraguayan guaraní":"PYG","Qatari riyal":"QAR","Romanian leu":"RON","Serbian dinar":"RSD","Renminbi[11]":"CNY","Russian ruble":"RUB","Rwandan franc":"RWF","Saudi riyal":"SAR","Solomon Islands dollar":"SBD","Seychelles rupee":"SCR","Sudanese pound":"SDG","Swedish krona(plural: kronor)":"SEK","Singapore dollar":"SGD","Saint Helena pound":"SHP","Sierra Leonean leone(new leone)[12][13][14]":"SLE","Sierra Leonean leone(old leone)[12][13][14][15]":"SLL","Somali shilling":"SOS","Surinamese dollar":"SRD","South Sudanese pound":"SSP","São Tomé and Príncipe dobra":"STN","Salvadoran colón":"SVC","Syrian pound":"SYP","Swazi lilangeni":"SZL","Thai baht":"THB","Tajikistani somoni":"TJS","Turkmenistan manat":"TMT","Tunisian dinar":"TND","Tongan paanga":"TOP","Turkish lira":"TRY","Trinidad and Tobago dollar":"TTD","New Taiwan dollar":"TWD","Tanzanian shilling":"TZS","Ukrainian hryvnia":"UAH","Ugandan shilling":"UGX","United States dollar":"USD","United States dollar (next day) (funds code)":"USN","Uruguay Peso en Unidades Indexadas (URUIURUI) (funds code)":"UYI","Uruguayan peso":"UYU","Unidad previsional[17]":"UYW","Uzbekistan sum":"UZS","Venezuelan digital bolívar[18]":"VED","Venezuelan sovereign bolívar[10]":"VES","Vietnamese đồng":"VND","Vanuatu vatu":"VUV","Samoan tala":"WST","CFA franc BEAC":"XAF","Silver(onetroy ounce)":"XAG","Gold(onetroy ounce)":"XAU","European Composite Unit(EURCO) (bond market unit)":"XBA","European Monetary Unit(E.M.U.-6) (bond market unit)":"XBB","European Unit of Account 9(E.U.A.-9) (bond market unit)":"XBC","European Unit of Account 17(E.U.A.-17) (bond market unit)":"XBD","East Caribbean dollar":"XCD","Special drawing rights":"XDR","CFA franc BCEAO":"XOF","Palladium(onetroy ounce)":"XPD","CFP franc(franc Pacifique)":"XPF","Platinum(onetroy ounce)":"XPT","SUCRE":"XSU","Code reserved for testing":"XTS","ADB Unit of Account":"XUA","No currency":"XXX","Yemeni rial":"YER","South African rand":"ZAR","Zambian kwacha":"ZMW","Zimbabwean dollar(fifth)[e]":"ZWL"}
        from PIL import ImageTk, Image
        
        self.root.iconbitmap('atm.ico')
        self.bg1=ImageTk.PhotoImage(Image.open("atm_bg.jpg"))

        # adding background image for the money exchange window 
        self.bg_label1=Label(curr_master,image=self.bg1)
        self.bg_label1.place(x=0,y=0,relwidth=1,relheight=1)

        self.clicked_currency= StringVar()
        self.clicked_currency.set("Select Currency")
        # creating the select pop up for selcting the currency
        drop = OptionMenu(curr_master,self.clicked_currency,*self.currency_codes.keys())
        drop.config(bg="#ffb699", highlightbackground="#ff5566",
                               highlightcolor="#ff5566", highlightthickness=2)
        
        # an option menu created to choose the currency from dictionary
        # it is shown option menu because we are getting the currency from currency code dictionary --> *self.currency_codes.keys()
        drop.pack()
        self.currency=Label(curr_master,text='Enter The Amount',font=('calibri',50)).pack()
        # create a Label to ask customer to enter the amount
        self.currrency=Entry(curr_master,bg='#F0EB8D',width=30,font=('Calibri',40))
        self.currrency.pack()
        # an Entry field is created to get input amount from customer
        self.show_change = Label(curr_master,text='')
        self.show_change.pack()
        self.currency=Button(curr_master,text='CONVERT',font=('CALIBRI,40'),bg='blue',fg='RED',command=self.curr_converter).pack()
        # a Convert button created to convert the  entered INR to specified Foreign Currency
        curr_master.mainloop()

    def distrans(self):      
        translst=self.cus['trans']
        statement = []
        for i in translst:
            a=i['des']
            b=i['amt']
            c=i['day']
            d=i['time']
            e=i['finbal']
            # messagebox.showinfo('INFO',f'{a},{b},{c},{d},{e}')
            s=f'{a},{b},{c},{d},{e}'
            statement.append(s)
            # getting all the values and storing it in a variable using f-string
        
    
        # Create our master object to the Application
        master = Tk()
        master.title('ACCOUNT STATEMENT')
        # Create the text widget
        text_widget = Text(master, height=25, width=50)
        
        # Create a scrollbar
        scroll_bar = Scrollbar(master)
        
        # Pack the scroll bar
        # Place it to the right side, using tk.RIGHT
        scroll_bar.pack(side=RIGHT)
        
        # Pack it into our tkinter application
        # Place the text widget to the left side
        text_widget.pack(side=LEFT)
        
        long_text = "\n".join(statement)
        
        # Insert text into the text widget
        text_widget.insert(END, long_text)

    

    def number_transactions_BAR(self):
        transactions=[]
        a,b,c,d=0,0,0,0
        transaction_list=self.cus['trans']
        for i in transaction_list:
            if i['des']=='Deposited':
                a=a+1
            elif i['des']=='Withdrawed':
                b=b+1
            elif i['des']=='MONEY TRANSFER':
                c=c+1
            elif i['des']=='Currency Exchange':
                d=d+1

        transactions.append(a)
        transactions.append(b)
        transactions.append(c)
        transactions.append(d)
        # we are creating a empty list transactions
        # we are looping through transactions list which have data derieved from 'cus' dictionary
        # we are getting the counts of deposits, withdraws ,money transfers and Currency exchange 
        # we are storing it in a list
        
        transactions_description=['Deposited','Withdrawed','MONEY TRANSFER','Currency Exchange']
        plt.title('Transactions')
        plt.bar(transactions_description,transactions)
        # a bar graph is created with x and y coordinates as transactions and transactions_descriptions
        plt.show()

    def number_transactions_PIE(self):
        transactions=[]
        a,b,c,d=0,0,0,0
        transaction_list=self.cus['trans']
        for i in transaction_list:
            if i['des']=='Deposited':
                a=a+1
            elif i['des']=='Withdrawed':
                b=b+1
            elif i['des']=='MONEY TRANSFER':
                c=c+1
            elif i['des']=='Currency Exchange':
                d=d+1

        transactions.append(a)
        transactions.append(b)
        transactions.append(c)
        transactions.append(d)
        # we are creating a empty list transactions
        # we are looping through transactions list which have data derieved from 'cus' dictionary
        # we are getting the counts of deposits, withdraws ,money transfers and Currency Exchange
        # we are storing it in a list
        
        transactions_description=['Deposited','Withdrawed','MONEY TRANSFER','Currency Exchange']
        plt.title('Transactions')
        plt.pie(transactions,labels=transactions_description)
        # a pie chart is created with transactions descriptions as labels and transactions as corresponding values

        plt.show()
              

    def change_pin(self):
        self.new_pin = askstring('CHANGE PIN', 'Enter the New Pin',show='*')
        # dialog box which asks the customer to enter the new pin he wants to change
        self.cus['pin']=self.new_pin
        messagebox.showinfo('SUCCESSFUL','Pin Exchange Successful')
        # if its changed , it shows Successful via message box
        return self.cus['pin']

def updatedata():
    f=open('my_pickle.pkl','wb')
    pkl.dump(accounts,f)
    # the data is stored into the pickle file at last
    # for that we are using dictionaries
    f.close()

s = ATM(accounts)
# onject s instance created
# through s class is utilized