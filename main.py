from COVID_Info import COVID_Info
import tkinter
from tkinter import messagebox
from ttkwidgets.autocomplete import AutocompleteCombobox
from tkcalendar import DateEntry
from datetime import date, timedelta

ViewTotalCount = True           #define global variables
CompareOneCountry = True
Country = ""
Country2 = ""

def submitBtn():
    if countryCB.get() != "":       #user selected a country
        if Country != Country2:     #country 1 and 2 are not the same
            if startDate.get_date() < endDate.get_date():       #end date is after start date
                updateInfo("Data Submitted.\n\n")           #update message section
                createCOVIDData()           #create data
            else:       #end date not after start date
                updateInfo("Set end date after start date.\n")
                messagebox.showwarning("Date Warning", "Please set the end date after the start date.")
        else:           #selected the same country
            updateInfo("Please ensure the two countries viewing are not the same countries.\n")
            messagebox.showwarning("Country Selection Warning", "Please ensure countries are not the same.")
    else:           #did not select a country
        updateInfo("Please select a country.\n")
        messagebox.showwarning("Country Selection Warning", "Please select a country.")

def clearBtn():         #clears the data
    global ViewTotalCount           #updates global variables
    ViewTotalCount= True
    global CompareOneCountry
    CompareOneCountry= True
    countryCB.set("")
    global Country
    Country = ""
    global Country2
    Country2 = ""

    updateInfo("Data Cleared\n")
    startDate.delete(0, "end")      #clears the date boxes
    endDate.delete(0, "end")

def comboBox_Updated(event):        #combo box has been selected
    global Country
    Country = countryCB.get()
    updateInfo("Country set to " + Country + ".\n")

def secondCountrySelected(event):       #combo box for country 2 has been selected
    global Country2
    Country2 = country2CB.get()
    updateInfo("Additional country selected is " + Country2 + ".\n")

def compareOneCountry():            #user selected to compare one country
    updateInfo("Comparing one country.\n")
    global CompareOneCountry
    CompareOneCountry = True

def compareTwoCountries():          #user selected to compare two countries
    if Country != "":           #ensures user select a country before trying to select an additional country to view
        updateInfo("Comparing two countries.\n")
        global CompareOneCountry            #updates the global variable
        CompareOneCountry = False

        country2Window = tkinter.Tk()       #creates new window for country 2 to be selected
        country2Window.geometry('300x300')
        country2Window.resizable(False, False)
        country2Window.title("Second Country Selection")
        label = tkinter.Label(text="Select an additional country to compare.", master=country2Window)
        label.pack()

        countries = ["", "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria", "Burkina Faso", "Burma", "Burundi", "Cabo Verde", "Cambodia", "Cameroon", "Canada", "Central African Republic", "Chad", "Chile", "China", "Colombia", "Comoros", "Congo (Brazzaville)", "Congo (Kinssa)", "Costa Rica", "Cote d\'Ivoire", "Croatia", "Cuba", "Cyprus", "Czechia", "Denmark", "Diamond Princess", "Djibouti", "Dominica", "Dominican Republic", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini", "Ethiopia", "Fiji", "Finland", "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Holy See", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Korea, South", "Kosovo", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "MS Zaandam", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Namibia", "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria", "North Macedonia", "Norway", "Oman", "Pakistan", "Palau", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa", "San Mano", "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Sudan", "Spain", "Sri Lanka", "Sudan", "Suriname", "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Timor-Leste", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "US", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "Uruguay", "Uzbekistan", "Vanuatu", "Venezuela", "Vietnam", "West Bank and Gaza", "Yemen"]
        countries.remove(Country)       #removes country 1 from list so user cannot select again

        global country2CB           #sets global variable for country 2
        country2CB = AutocompleteCombobox(country2Window, completevalues=countries)
        country2CB.pack()
        country2CB.bind("<<ComboboxSelected>>", secondCountrySelected)      #sets listener for the combobox
    else:
        updateInfo("Select initial country before selecting an additional country.\n")
        messagebox.showwarning("Country Selection Error", "Initial country not selected. PLease select a country first.")

def totalCount():           #user selected total count
    updateInfo("Viewing total count.\n")
    global ViewTotalCount       #updates global variable
    ViewTotalCount= True

def dailyCount():           #user selected daily count
    updateInfo("Viewing daily count.\n")
    global ViewTotalCount       #updates global variable
    ViewTotalCount = False

def updateInfo(entry):          #updates the information section of the main menu
    info.configure(state='normal')      #sets the text to editable to make entry
    info.insert(0.0, entry)
    info.configure(state='disabled')    #disable text so it is read only

def createCOVIDData():      #COVID_Info arguments: country1, start date, end date, country2, total count
    if ViewTotalCount:              #viewing total count and comparing one country
        if CompareOneCountry:
            COVID = COVID_Info(Country, startDate.get_date(), endDate.get_date(),
                               "", True)
        else:                       #viewing total count and comparing two countries
            COVID = COVID_Info(Country, startDate.get_date(), endDate.get_date(),
                               Country2, True)
    else:
        if CompareOneCountry:       #viewing daily cases and comparing one country
            COVID = COVID_Info(Country, startDate.get_date(), endDate.get_date(),
                               "", False)
        else:                       #viewing daily cases and comparing two countries
            COVID = COVID_Info(Country, startDate.get_date(), endDate.get_date(),
                               Country2, False)
    COVID.getData()             #gets the data and set variables
    COVID.displayGraphs()       #displays the graph

window = tkinter.Tk()           #sets the Main GUI
window.title("COVID Data")
window.resizable(False, False)

#menu bar creation
menuBar = tkinter.Menu(window)

compareMenu = tkinter.Menu(menuBar, tearoff=0)          #menu bar for one/two countries to compare
compareMenu.add_command(label="One Country", command=compareOneCountry)
compareMenu.add_command(label="Two Countries", command=compareTwoCountries)
menuBar.add_cascade(label="Compare", menu=compareMenu)

viewMenu = tkinter.Menu(menuBar, tearoff=0)             #menu bar for total count or daily change to view
viewMenu.add_command(label="Total Count", command=totalCount)
viewMenu.add_command(label="Daily Change", command=dailyCount)
menuBar.add_cascade(label="View", menu=viewMenu)

window.config(menu=menuBar)

#information section to display all messages to the user
frameInformation = tkinter.Frame(master=window)
info = tkinter.Text(master=frameInformation)
info.insert(0.0, "Starting...")
info.configure(state='disabled')               #disable text so it is read only
info.pack()
frameInformation.pack(fill=tkinter.BOTH, expand=True)

#select data section
frameSelectData = tkinter.Frame(master=window, padx=10, pady=10)

    #clears the data
clearBtn = tkinter.Button(text="Clear Data", master=frameSelectData, command=clearBtn)
clearBtn.grid(row=0, column=0, padx=5)

    #country label
countryLbl = tkinter.Label(text="Enter Country:", master=frameSelectData)
countryLbl.grid(row=0, column=1, padx=5)

    #country autocomplete combo box
countries = ["", "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria", "Burkina Faso", "Burma", "Burundi", "Cabo Verde", "Cambodia", "Cameroon", "Canada", "Central African Republic", "Chad", "Chile", "China", "Colombia", "Comoros", "Congo (Brazzaville)", "Congo (Kinssa)", "Costa Rica", "Cote d\'Ivoire", "Croatia", "Cuba", "Cyprus", "Czechia", "Denmark", "Diamond Princess", "Djibouti", "Dominica", "Dominican Republic", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini", "Ethiopia", "Fiji", "Finland", "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Holy See", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Korea, South", "Kosovo", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "MS Zaandam", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Namibia", "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria", "North Macedonia", "Norway", "Oman", "Pakistan", "Palau", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa", "San Mano", "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Sudan", "Spain", "Sri Lanka", "Sudan", "Suriname", "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Timor-Leste", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "US", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "Uruguay", "Uzbekistan", "Vanuatu", "Venezuela", "Vietnam", "West Bank and Gaza", "Yemen"]
countryCB = AutocompleteCombobox(frameSelectData, completevalues=countries)
countryCB.bind("<<ComboboxSelected>>", comboBox_Updated)
countryCB.grid(row=0, column=2, padx=5)

    #date label
datesLbl = tkinter.Label(text="Enter Dates:", master=frameSelectData)
datesLbl.grid(row=0, column=3, padx=5)

    #start date from 22JAN2020 to yesterday
startDate = DateEntry(frameSelectData, mindate=date(2020, 1, 22), maxdate=(date.today() - timedelta(days=1)))
startDate.grid(row=0, column=4, padx=5)
startDate.delete(0, "end")

    #end date from 22JAN2020 to yesterday
endDate = DateEntry(frameSelectData, mindate=date(2020, 1, 22), maxdate=(date.today() - timedelta(days=1)))
endDate.grid(row=0, column=5, padx=5)
endDate.delete(0, "end")

    #submit button
submitBtn = tkinter.Button(text="Submit Data", master=frameSelectData, command=submitBtn)
submitBtn.grid(row=0, column=6, padx=5)

frameSelectData.pack()

#Loops the Main GUI
window.mainloop()