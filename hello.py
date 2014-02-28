
import bottle

# this is the handler for the default path of the web server

@bottle.route('/')
def hello():
    	arr = [0,1,2,3,4]
	return bottle.template('views/hello_world',{'user':"akshat",'array': arr})#return '<b>Hello World!</b>'

@bottle.route('/test')
def test_index():
	return "test page"

@bottle.post('/fav_num')
def fav_num():
		num = bottle.request.forms.get("fav_num")
        	if(num == None or num == ""):
			print "no number"
		else:
			print "fav num is %d" % num
		return num

bottle.debug(True)
bottle.run(host='localhost', port=8080)
