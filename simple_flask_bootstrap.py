from flask import Flask, request, render_template
import requests


#__name__ will give the module the name __main__ if the module is run directly. And something else if imported.
app = Flask(__name__)

# What url should trigger our function
@app.route('/', methods=['GET', 'POST'])
def index():
    
    city = 'Stockholm'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={},SE&units=metric&appid=770d56c48281cb08a7b374b8872b6bf3'

    
    if request.method == 'POST':
        print("Im here!")
        city = request.form.get("city")
        print('the city is:' + str(city))
        
    r = requests.get(url.format(city)).json()

    print(r)
    weather = {
        'city': city,
        'temperature' :  r['main']['temp'],
        'description' : r['weather'][0]['description'],
        'icon' : r['weather'][0]['icon']}
    
    #print(weather)
    #print('first' + str(r[0]))
    #print(r)
    

    return render_template("index.html", weather=weather)



@app.route("/andrehoejmark")
def andrehoejmark():
    return render_template("index.html")





























if __name__ == "__main__":
    # will run only if module directly run
    app.run(debug=True)
else:
    #will run only if module imported
    print('I am being imported')

