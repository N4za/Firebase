import web
import requests
import json

render = web.template.render("mvc/views/")

class Login():

    def GET(self):
        try:
            error = ""
            return render.login(error)
        except Exception as error:
            print(error.args[0])

    def POST(self):
        try:
            data_user = web.input()
            email = data_user.email
            password = data_user.password
            response = requests.post(
                'https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=AIzaSyAOm9tNvZjpaMgmGTEIBWJtqxHZbuJaZjs', 
            data=json.dumps({
                'email':email,
                'password':password
                })).text
            data = json.loads(response)
            print(data)
            if data['registered'] == True:
                web.seeother('/agenda')
        except Exception as error:
            print (error.args[0])
            error = data['error']['message']
            return render.login(error)