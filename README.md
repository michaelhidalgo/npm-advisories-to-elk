# npm-advisories-to-elk
A better way to visualize NPM advisories and understand what modules are vulnerable in the NPM registry. For more information, [Check out this blog post](https://blog.michaelhidalgo.info/2019/06/a-better-way-to-visualiza-npm-security.html)

# Screenshots

![main screenshot](https://github.com/michaelhidalgo/npm-advisories-to-elk/blob/master/resources/main.jpg)



![NPM advisories by severity](https://github.com/michaelhidalgo/npm-advisories-to-elk/blob/master/resources/security-advisories-by-severity.jpg)


# Installation:

+ Fork or clone this repository
+ Create a virtual environment virtualenv env
+ Activated virtual environment source /env/bin/activate
+ Install dependenciees pip3 install -r requirements.txt
+ Export following environment variables with Elasticsearch IP address and port:
  ```
  export es_hostname='Your ELK IP'
  export es_port='Your ELK port (9200 by default)'  
  
  ```
+ run python3 main.py
