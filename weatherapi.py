import requests
import urllib
from urllib.request import urlopen
import webbrowser
from tkinter import *
from tkinter import messagebox

def writeCSS():
            myfile = open("style.css", "w")
            myfile.write("html {background-image: linear-gradient(to bottom right, skyblue, white);}\n")
            myfile.write("*{font-family:Tahoma;}\n")
            myfile.write(".pagecontainer{\n")
            myfile.write("  max-width:5000px;\n")
            myfile.write("  margin: 50px 300px 0px;\n")
            myfile.write("}\n")
            myfile.write(".header {\n")
            myfile.write("  background-color: #0192E6;\n")
            myfile.write("  padding: 20px;\n")
            myfile.write("  text-align: center;\n")
            myfile.write("  color: white;\n")
            myfile.write("}\n")
            myfile.write(".weather {\n")
            myfile.write("  background-color: #0BA5FE;\n")
            myfile.write("  padding: 20px;\n")
            myfile.write("  text-align: center;\n")
            myfile.write("  color: white;\n")
            myfile.write("}\n")
            myfile.write(".weather2 {\n")
            myfile.write("  background-color: #2AB0FE;\n")
            myfile.write("  padding: 20px;\n")
            myfile.write("  text-align: center;\n")
            myfile.write("  color: white;\n")
            myfile.write("}\n")
            myfile.write(".forecast {\n")
            myfile.write("  background-color: #61caff;\n")
            myfile.write("  padding: 20px;\n")
            myfile.write("  text-align: center;\n")
            myfile.write("  color: white;\n")
            myfile.write("}\n")

def writeHTML(state,img,date,temp,mintemp,maxtemp,windspeed):
            myfile = open("Weather.html","w")
            myfile.write("<head>\n")
            myfile.write("<link rel=\"stylesheet\" type=\"text/css\" href=\"style.css\">\n")
            myfile.write("</head>\n")
            myfile.write("<body>\n")
            myfile.write("<div class=\"pagecontainer\">\n")
            myfile.write("  <div class=\"header\">\n")
            myfile.write("      <h1>")
            myfile.write(cityname)
            myfile.write(" Weather</h1>\n") 
            myfile.write("  </div>\n")
            myfile.write("  <div class = \"weather\">\n")
            myfile.write("      <h5>")
            myfile.write(date)
            myfile.write("</h5>\n")
            myfile.write("      <img src=\"")
            myfile.write(img)
            myfile.write("\" style=\"width:10%\">\n")
            myfile.write("      <h4>")
            myfile.write(state)
            myfile.write("</h4>\n")
            myfile.write("      <h2>")
            myfile.write(str(temp))
            myfile.write("°C</h2>\n")
            myfile.write("  </div>\n")
            myfile.write("  <div class = \"weather2\">\n")
            myfile.write("      <h4>")
            myfile.write("Low of: ")
            myfile.write(str(mintemp))
            myfile.write("°C</h4>\n")
            myfile.write("      <h4>")
            myfile.write("High of: ")
            myfile.write(str(maxtemp))
            myfile.write("°C</h4>\n")
            myfile.write("      <h4>")
            myfile.write("Windspeed: ")
            myfile.write(str(windspeed))
            myfile.write(" mph</h4>\n")
            myfile.write("  </div>\n")
            myfile.write("</div>\n")
            myfile.write("</body>\n")
            myfile.close()


# test for internet connection
def internet_on():
        try:
            urlopen('https://www.google.com', timeout=3)
            return True
        except urllib.error.URLError as Error:
            return False

def main():

    def runit():
        print(e1.get())
        #print(a.get())
        response1 = requests.get("https://www.metaweather.com/api/location/search/?query=" + e1.get())
        if (response1.status_code == 200):
            firstresponse = response1.json()
            if not firstresponse:
                messagebox.showerror("Error","City not found. Please ensure a city name is entered, and is spelled correctly.")
                print ("fake and bad")
            else:
                global woeid
                global cityname
                woeid = (firstresponse[0]['woeid'])
                cityname = (firstresponse[0]['title'])
                woeid = str(woeid)
                print(woeid)
                root.destroy()

    def deleteClick(event):
        e1.delete(0,END)
        usercheck=True




    if internet_on():


        root = Tk()
        root.title("Weather")
        #a = StringVar()
        image1 = PhotoImage(file = "images/wt1.png",)
        l0 = Label(root, image = image1)
        l0.grid(row=0,column=1)
        l1 = Label(root, height = 3, text = "Name of City:")
        l1.grid(row=1,column=0)
        e1 = Entry(root )
        e1.insert(0,"Enter city name")
        e1.grid(row=1,column=1)
        e1.bind("<Button>",deleteClick,)
        b1 = Button(root,text="Submit",command=runit, height = 2, cursor = "hand1", width = 10)
        b1.grid(row=1,column=2)

        root.mainloop()

        response = requests.get("https://www.metaweather.com/api/location/" +woeid+ "/")

        if (response.status_code == 200):
                      wjson = response.json()
                      state = (wjson["consolidated_weather"][0]['weather_state_name'])
                      abbr = (wjson["consolidated_weather"][0]['weather_state_abbr'])
                      date = (wjson["consolidated_weather"][0]['applicable_date'])
                      tempi = (wjson["consolidated_weather"][0]['the_temp'])
                      mintempi = (wjson["consolidated_weather"][0]['min_temp'])
                      maxtempi = (wjson["consolidated_weather"][0]['max_temp'])
                      windspeedi = (wjson["consolidated_weather"][0]['wind_speed'])

                      windspeed = round(windspeedi)
                      temp = round(tempi)
                      mintemp = round(mintempi)
                      maxtemp = round(maxtempi)

                      if(abbr == "lc"):
                          img="images/lc.svg"
                      elif(abbr == "c"):
                          img="images/c.svg"
                      elif(abbr == "h"):
                          img="images/h.svg"
                      elif(abbr == "hc"):
                          img="images/hc.svg"
                      elif(abbr == "hr"):
                          img="images/hr.svg"
                      elif(abbr == "lr"):
                          img="images/lr.svg"
                      elif(abbr == "s"):
                          img="images/s.svg"
                      elif(abbr == "sl"):
                          img="images/sl.svg"
                      elif(abbr == "sn"):
                          img="images/sn.svg"
                      elif(abbr == "t"):
                          img="images/t.svg"

              
                          
                              
                      writeHTML(state,img,date,temp,mintemp,maxtemp,windspeed)
                      writeCSS()
                      #print(state, temp, mintemp, maxtemp, windspeed,)
                      print("Files have been written. Please proceed")
                      url = 'Weather.html'
                      chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
                      webbrowser.get(chrome_path).open(url)
      
                        
                              
        else:
                state = "An Error has occured"
                writeHTML(state)
                print("An error has occured")
                messagebox.showerror("Error", "An Error has occured")
    else:
        print("Internet disconnected. Please connect to the internet before running the program.")
        messagebox.showerror("Error","Internet disconnected. Please connect to the internet before running the program.")
        return

    
    

    
main()
