from bottle import route,template,error,static_file,run,request,redirect,post, response
import csv

@route('/')
def index():
    return template("use/index.tpl")

@route('/senda' ,method="POST")
def form():


    lykilord = request.forms.get("lykilord")
    notendanafn = request.forms.get("notendanafn")
    notendanafn = notendanafn.strip(" ")

    if lykilord  == "hello":
        if request.get_cookie("visited"):
            response.set_cookie("visited", "", expires=0)

            return "Welcome back! Nice to see you again"


        else:
            response.set_cookie("visited", "yes")
            return "Hello there! Nice to meet you"

    else:
        return "wrong"



@route('/css/<filename:re:.*\.css>')
def send_css(filename):
    return static_file(filename, root='css')

run(host='localhost', port=8080, debug=True)