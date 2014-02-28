
import bottle
import pymongo

# this is the handler for the default path of the web server

@bottle.route('/')
def index():
    
    # connect to mongoDB
    connection = pymongo.MongoClient('localhost', 27017)

    # attach to test database
    db = connection.akshat


    # get handle for names collection
    name = db.user

    # find a single document
    item = name.find_one()

    return '<b>Hello %s!</b>' % item['name']

@bottle.route('/test')
def test_index():
	return "test page"

bottle.run(host='localhost', port=8080)
