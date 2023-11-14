import bottle
from bottle import route, run, Response, template
import json
import image
import tracemalloc

def call_service():
    directoryName = 'photos'
    image.process(directoryName)

@route('/')
def index():
	#Start tracemalloc
	tracemalloc.start()
	
    """Home page"""
    title = "Image Processor App"
    call_service()
	
	snapshot = tracemalloc.take_snapshot() # Taking snapshot
    top_stats = snapshot.statistics('lineno') # Getting statistics

 	# ... Printing to console ...
    print("[ Top 10 ]") 
    for stat in top_stats[:10]:
        print(stat)
    # ... Printing to console ...
	
		return template('index.tpl',data="Request completed!", title=title)

if __name__ == '__main__':
	run(host='0.0.0.0', port=8000, debug=False, reloader=True)
	
serverApp = bottle.default_app()
