from bottle import route, run
#Orri Steinn 29.08.17
@route('/hello')
def hello():
    return "<!DOCTYPE html>" \
           "<html>" \
           "<head>" \
           "	<title> Hello </title>" \
           "</head>" \
           "<body>" \
           "<h1> hello World</h1>" \
           "<p>Where Are You</p>" \
           "<h1><i>I Need HELP</i></h1>" \
           "</body>" \
           "</html>"
#Verkefni 2 liður 2 og 3




run(host='localhost', port=8080, debug=True)