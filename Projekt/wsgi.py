#
# IMPORTANT: Put any additional includes below this line.  If placed above this
# line, it's possible required libraries won't be in your searchable path
#

#from flaskapp import app as application
#from run import app as application

from flaskr import app as application

#from flaskr import init_db
#from test_run import app as application

# for testing
if __name__ == "__main__":
    from wsgiref.simple_server import make_server
    httpd = make_server('localhost', 8051, application)
    # Wait for a single request, serve it and quit.
    httpd.serve_forever()
