from bottle import route, run

@route('/job')
def job():
    return "<!DOCTYPE html>" \
           "<html>" \
           "<head>" \
           "	<title> job </title>" \
           "</head>" \
           "<body>" \
           "<h1><a href='http://localhost:8080/jobs/'> jobs </a> " \
           "<br>" \
           "<a href='http://localhost:8080/bio/'> bio </a> " \
           "<br>"\
           "<a href='http://localhost:8080/pic/'> pic </a></h1> " \
           "</body>" \
           "</html>"

@route('/jobs/')
def jobs():
    return "<!DOCTYPE html>" \
           "<html>" \
           "<head>" \
           "	<title> jobs </title>" \
           "</head>" \
           "<body>" \
           "<h1> steve jobs </h1> " \
           "</body>" \
           "</html>"

@route('/bio/')
def jobs():
    return "<!DOCTYPE html>" \
           "<html>" \
           "<head>" \
           "	<title> bio </title>" \
           "</head>" \
           "<body>" \
           "<h1> bio </h1> " \
           "</body>" \
           "</html>"


@route('/pic/')
def jobs():
    return "<!DOCTYPE html>" \
           "<html>" \
           "<head>" \
           "	<title> pic </title>" \
           "</head>" \
           "<body>" \
           "<h1> pic </h1> " \
           "</body>" \
           "</html>"

run(host='localhost', port=8080, debug=True)