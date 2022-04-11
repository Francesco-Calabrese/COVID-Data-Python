# COVID-Data-Python
Displays COVID data for selected country during a given time range

Summary
---------
This program is written in Python and is a stand-alone executable file. The user selects a country and a date range to pull the COVID deaths and cases. That data will be displayed on a line graph for the user to view. The user can select an additional country to compare as well as select the daily change instead of the total count of cases/deaths.

Data is retrieved from CSSEGISandData's GitHub (JHU CSSE COVID-19 Data, and the url: https://github.com/CSSEGISandData/COVID-19).

Usage
-----
The image below is the main screen of the program. There are three sections of this display: menu bar, information menu, and data menu.

![image](https://user-images.githubusercontent.com/96243400/162750770-f3070b37-969a-4376-97e4-12a30565ee67.png)

The menu bar is composed of the compare menu and view menu. The compare menu allows the user to either select one country to view data on, or select another country to view data on. The view menu allows the user to view the total cases/deaths or the daily change of cases/deaths.

The information menu displays information about the program, such as user actions and warning messages.

The data menu allows the user to select the data to submit. Starting from the left to the right is the clear data button, which clears the information menu and selected previous data. Next is the select country drop-down menu. The user can select the country to view via drop-down feature or begin typing the country name. Next is the date range selection, the first is the starting date while the second is the ending date. The final item is the submit button.

If the user selects two countries to compare, and additional dialog box will appear for the user to select an additional country. The user should then close that dialog box and then click the get data button from the data selection menu to submit the data.

![image](https://user-images.githubusercontent.com/96243400/162752948-2d3a1840-012b-416f-9795-7a749e2b413e.png)

Once all of the data is submitted and retrieved two graphs will display. One will contain the deaths (right graph) and one will display the cases (left graph). If two countries were selected, there will be a legend to denote with country is represented by which line. The user can clear data from the main screen or update the data (country, second country, dates, view menu). Once the get data button is submitted, all previous data is removed.

![image](https://user-images.githubusercontent.com/96243400/162751317-66367a9f-3f0e-4320-b1dc-d9c9d85dddae.png)



Requirements
-----------------

<ul>
  <li>altgraph==0.17.2</li>
  <li>Babel==2.9.1</li>
  <li>cycler==0.11.0</li>
  <li>fonttools==4.31.2</li>
  <li>future==0.18.2</li>
  <li>kiwisolver==1.4.2</li>
  <li>matplotlib==3.5.1</li>
  <li>messagebox==0.1.0</li>
  <li>numpy==1.22.3</li>
  <li>packaging==21.3</li>
  <li>pefile==2021.9.3</li>
  <li>Pillow==9.1.0</li>
  <li>pyinstaller==4.10</li>
  <li>pyinstaller-hooks-contrib==2022.3</li>
  <li>pyparsing==3.0.7</li>
  <li>python-dateutil==2.8.2</li>
  <li>pytz==2022.1</li>
  <li>pywin32-ctypes==0.2.0</li>
  <li>six==1.16.0</li>
  <li>tkcalendar==1.6.1</li>
  <li>ttkwidgets==0.12.1</li>
</ul>
