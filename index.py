import bottle
from bottle import route, run, Response, template
import json
import image
import tarcemalloc

def generate_data(num):
    numbers = int(num/8)
    data = []
    i=0
    for i in range(numbers):
        i=i+1
        data.append(i)
    return data

def add_to_list(num):
    data = generate_data(num)
    custom_list.append(data)
    custom_list.append(custom_list)
def call_service():
    directoryName = 'photos'
    image.process(directoryName)

custom_list=[]
@route('/')
def index():    	
    """Home page"""
    title = "Image Processor App"
    call_service()
    num = 20000 * 1024
    add_to_list(num)
    #return jsonify({"msg":"Data generated"})
    return template('index.tpl',data="Request completed!", title=title)

@route('/snapshot')
def snapshot():
    tracemalloc.start() #Start tracemalloc

    ## Your code
    num = 20000 * 1024
    add_to_list(num)

    ##Taking snapshot
    snapshot = tracemalloc.take_snapshot()
    snapshot.dump("snap.out")
    
    #tracemalloc.stop() 

    return jsonify({"msg":"Snapshot generated"})

if __name__ == '__main__':
	run(host='0.0.0.0', port=8000, debug=False, reloader=True)
	
serverApp = bottle.default_app()
