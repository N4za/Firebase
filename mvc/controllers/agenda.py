import web
import requests
import json

render = web.template.render("mvc/views/", base="template")

class Agenda():

    def GET(self):
        try:
            result = requests.get('https://agenda-c177d-default-rtdb.firebaseio.com/agenda.json').text
            data = json.loads(result)
            return render.agenda(data) 
        except Exception as error:
            print(error.args[0])