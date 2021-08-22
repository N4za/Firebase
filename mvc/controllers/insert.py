import web
import requests
import json

render = web.template.render("mvc/views/", base="template")

class Insert():

    def GET(self):
        try:
            return render.insert()
        except Exception as e:
            return "Error " + str(e.args)

    def POST(self):
        try:
            data_user = web.input()
            nombre = data_user.nombre
            email = data_user.email
            result = requests.post('https://agendav1-default-rtdb.firebaseio/agenda.json', 
            data=json.dumps({
                
                'nombre':nombre, 
                'email':email
                
                }))
            print(result)
            web.seeother('/agenda')
        except Exception as error:
            print(error.args[0])
            return render.insert()