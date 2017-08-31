from bottle import route, run
#Orri Steinn 29.08.17
@route('/nafn/<id>')
def nafn(id):

       if id == "1":
              return "<!DOCTYPE html>" \
                     "<html>" \
                     "<head>" \
                     "	<title> Nafn </title>" \
                     "</head>" \
                     "<body>" \
                     "<h1> 	Gunnar</h1>" \
                     "</body>" \
                     "</html>"
       elif id == "2":
              return "<!DOCTYPE html>" \
                     "<html>" \
                     "<head>" \
                     "	<title> Nafn </title>" \
                     "</head>" \
                     "<body>" \
                     "<h1> Daníe</h1>" \
                     "</body>" \
                     "</html>"
       elif id == "3":
              return "<!DOCTYPE html>" \
                     "<html>" \
                     "<head>" \
                     "	<title> Nafn </title>" \
                     "</head>" \
                     "<body>" \
                     "<h1> 	Þórarinn</h1>" \
                     "</body>" \
                     "</html>"
       else:
             return "<!DOCTYPE html>" \
                     "<html>" \
                     "<head>" \
                     "	<title> Nafn </title>" \
                     "</head>" \
                     "<body>" \
                     "<h1> hver </h1>" \
                     "</body>" \
                     "</html>"









run(host='localhost', port=8080, debug=True)