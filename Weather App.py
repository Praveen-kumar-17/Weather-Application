from  tkinter import *
import requests
import json

root=Tk()
root.title('Weather App ')

def get_data(root):
    city=user.get()
    print(city)
    Api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=003da33b59d01689a7e171acf4d7976c"
    resp=requests.get(Api)
    #print(resp)
    if resp.status_code ==200:
        data=resp.json()
        temp=int(data['main']['temp']-271.15)
        #print(temp)
        pressure=int(data['main']['pressure'])
        wind=int(data['wind']['speed'])
        hum=int(data['main']['humidity'])
        condition=data['weather'][0]['main']
        #print(temp,pressure,wind,hum,condition)

        output="Temperature:"+str(temp)+'°C'+"\n"+'pressure:'+str(pressure)+'hpa'+'\n'+"wind:"+str(wind)+'m/s'+'\n'+'humidty:'+str(hum)+'%'+'\n'+'condition:'+condition
        print(output)
        label.configure(text=output)
    
    

user=Entry(root,width=30,justify='center',font=('poppins',20,'bold'))
user.grid(row=0,column=0)
user.bind('<Return>',get_data)

label=Label(root,font=('poppins',20,'bold'))
label.grid(row=1,column=0)




root.mainloop()
