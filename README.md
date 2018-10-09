# Booru
A GPL3 API wrapper for *booru image boards.

Currently supports:
* Gelbooru

Planned: 
* Danbooru

Here is an example:

    from booru import Booru
    
    #Initialise the Booru
    br = Booru("safebooru.org")

    #Retrieve the API wrapper
    manager = br.request_manager

    #Retrieve an image
    image = manager.most_recent()

    #Get an URL from the image
    br.generate_url(image)

## Installing

### From pip  
TODO

### From source  
    git clone https://github.com/jgrondier/booru.git
    cd booru
    pip install . --user