from datetime import datetime, timedelta
from urllib.request import urlopen
import matplotlib.pyplot as plt
import pylab

def formatDate(dateToFormat):       #formats the date as needed by the website to retrieve data
    dateStr = datetime.strftime(dateToFormat, '%m-%d-%Y')
    return dateStr

class COVID_Info:

    def __init__(self, country, start, end, country2, isTotalCount):            #set initial variables
        self.country = country
        self.start = start
        self.end = end
        self.country2 = country2
        self.isTotalCount = isTotalCount
        self.deaths = 0
        self.cases = 0
        self.casesCountry2 = 0
        self.deathsCountry2 = 0
        self.dateArr = []
        self.casesArr = []
        self.deathArr = []
        self.deathCountry2Arr = []
        self.casesCountry2Arr = []
        self.arrIndex = 0
        self.plt = plt

    def getData(self):
        daysBetween = self.end - self.start     #iterates from the start date to the end date
        for i in range(daysBetween.days + 1):
            day = self.start + timedelta(days=i)        #gets the next day to retrive data for that day
            self.dateArr.append(str(day))           #adds the date to the date array

            #opens the website and saves the data in the html variable
            url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{}.csv".format(formatDate(day))
            page=urlopen(url)
            html_bytes = page.read()
            html = html_bytes.decode("utf-8")

            x = html.split("\n")            #splits the document into lines
            counter = 0
            self.cases = 0
            self.deaths = 0
            self.casesCountry2 = 0
            self.deathsCountry2 = 0
            isCountry = False
            isCountry2= False
            for line in x:              #iterates through all of the lines in the document
                items = str(line).split(",")        #splits the line into items, some lines have 13 items, others 14
                isCountry = False
                isCountry2 = False
                for item in items:          #iterates through all of the items in the line
                    if item == self.country:        #if the item is the country
                        counter = 0             #sets a counter
                        isCountry = True        #sets a country flag
                    if item == self.country2 and self.country2 != "":       #same as above but for country 2
                        counter = 0
                        isCountry2 = True
                    if isCountry:           #the line contains the country information
                        if counter == 4:        #3 items after the country is the cases value
                            self.cases = self.cases + int(item)         #adds the cases for all provinces/states/cities for the country
                        if counter == 5:        #4 items after the country is the death value
                            self.deaths = self.deaths + int(item)       #adds the deaths for all provinces/states/cities for the country
                        counter = counter + 1       #adds to the counter
                    if isCountry2:          #same as above but for country 2
                        if counter == 4:
                            self.casesCountry2 = self.casesCountry2 + int(item)
                        if counter == 5:
                            self.deathsCountry2 = self.deathsCountry2 + int(item)
                        counter = counter + 1

            self.casesArr.append(self.cases)        #adds the cases and deaths to the lists
            self.deathArr.append(self.deaths)
            if self.country2 != "":             #same as above but for country 2
                self.casesCountry2Arr.append(self.casesCountry2)
                self.deathCountry2Arr.append(self.deathsCountry2)

    def displayGraphs(self):        #displays the graphs of cases and deaths
        yAxisCases = []
        yAxisCasesCountry2 = []
        yAxisDeaths = []
        yAxisDeathsCountry2 = []
        casesPlotTitle = ""
        deathPlotTitle = ""

        if self.isTotalCount:      #if total count is selected, set yAxis
            yAxisCases = self.casesArr
            yAxisCasesCountry2 = self.casesCountry2Arr
            yAxisDeaths = self.deathArr
            yAxisDeathsCountry2 = self.deathCountry2Arr

            if self.country2 == "":         #no additional country selected
                casesPlotTitle = "Number of Cases {}".format(self.country)      #sets the title for the graphs
                deathPlotTitle = "Number of Deaths {}".format(self.country)
            else:       #2 countries selected
                casesPlotTitle = "Number of Cases {} vs {}".format(self.country, self.country2)     #sets the title for the graphs (2 countries)
                deathPlotTitle = "Number of Deaths {} vs {}".format(self.country, self.country2)
        else:       #daily change is selected, sets yAxis
            for i in range(len(self.dateArr)-1):        #goes through the cases/death arrays and finds the difference for the yAxis values
                yAxisCases.append(self.casesArr[i+1] - self.casesArr[i])
                yAxisDeaths.append(self.deathArr[i+1] - self.deathArr[i])
                if(self.country2 != ""):        #same as above but for country 2
                    yAxisCasesCountry2.append(self.casesCountry2Arr[i+1] - self.casesCountry2Arr[i])
                    yAxisDeathsCountry2.append(self.deathCountry2Arr[i+1] - self.deathCountry2Arr[i])
            self.dateArr.pop(len(self.dateArr)-1)       #removes the last day so cases/death/dates array are the same length

            if self.country2 == "":     #sets the graph titles for a single country
                casesPlotTitle = "Number of Daily Change Cases {}".format(self.country)
                deathPlotTitle = "Number of Daily Change Deaths {}".format(self.country)
            else:               #sets the graph titles for two countries
                casesPlotTitle = "Number of Daily Change Cases {} vs {}".format(self.country, self.country2)
                deathPlotTitle = "Number of Daily Change Deaths {} vs {}".format(self.country, self.country2)

        #generates cases graph for country/countries selected.
        self.plt.figure(1)      #figure 1 graph is the cases graph. selects this chart for manipulation
        self.plt.clf()          #clears old data if present

        fig = pylab.gcf()       #sets the title of the figure
        fig.canvas.manager.set_window_title('Cases')

        self.plt.plot(self.dateArr, yAxisCases, color='r', label=self.country)          #plots the data,title,axis
        self.plt.title(casesPlotTitle)
        self.plt.xlabel("Date")
        self.plt.ylabel("Cases")
        self.plt.ticklabel_format(useOffset=False, style='plain', axis='y')     #removes the scientific notation

        if self.country2 != "":         #updates the graph to include country 2
            self.plt.plot(self.dateArr, yAxisCasesCountry2, color='g', label=self.country2)
        self.plt.legend()

        mngr = self.plt.get_current_fig_manager()        #sets the position of the graph
        mngr.window.wm_geometry("+50+100")

        #generates death graph for country/countries selected. Same as above but for the death chart.
        self.plt.figure(2)          #selects the death graph for manipulation
        self.plt.clf()

        fig = pylab.gcf()
        fig.canvas.manager.set_window_title('Deaths')

        self.plt.plot(self.dateArr, yAxisDeaths, color='r', label=self.country)
        self.plt.title(deathPlotTitle)
        self.plt.xlabel("Date")
        self.plt.ylabel("Deaths")
        self.plt.ticklabel_format(useOffset=False, style='plain', axis='y')

        if self.country2 != "":         #updates the graph to include country 2
            self.plt.plot(self.dateArr, yAxisDeathsCountry2, color='g', label=self.country2)
        self.plt.legend()

        mngr = self.plt.get_current_fig_manager()        #sets the position of the graph
        mngr.window.wm_geometry("+700+100")

        #shows the plots to the user
        self.plt.show()