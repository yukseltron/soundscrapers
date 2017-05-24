import cherrypy
import main

class Root(object):
    @cherrypy.expose
    def index(self):
        return main.main()

if __name__ == '__main__':
   cherrypy.quickstart(Root(), '/')
