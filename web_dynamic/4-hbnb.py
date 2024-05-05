#!/usr/bin/python3
"""
This Flask application dynamically generates an HTML page that includes
dropdown menus for locations (states/cities) and amenities, along with
listings for rentals.
"""
from flask import Flask, render_template
from models import storage
import uuid

# Initialize the Flask web server
app = Flask('web_dynamic')
# Disable strict slashes in URL routing to allow both trailing and
non-trailing slashes
app.url_map.strict_slashes = False


@app.route('/4-hbnb')
def display_hbnb():
    """
    This function generates a webpage with dropdown menus for states and
    cities, amenities, and places available for rent.
    It also assigns a unique cache ID to each request to manage caching
    effectively.
    """
    # Retrieve all instances of 'State' from the storage
    states = storage.all('State')
    # Retrieve all instances of 'Amenity' from the storage
    amenities = storage.all('Amenity')
    # Retrieve all instances of 'Place' from the storage
    places = storage.all('Place')
    # Generate a unique identifier for this request
    cache_id = uuid.uuid4()
    # Render the template with the retrieved data and cache ID
    return render_template('4-hbnb.html',
                           states=states,
                           amenities=amenities,
                           places=places,
                           cache_id=cache_id)


@app.teardown_appcontext
def teardown_db(*args, **kwargs):
    """
    This function ensures that the database or file storage is properly
    closed when the application context is torn down.
    This is crucial for resource management and preventing memory leaks.
    """
    # Close the storage connection
    storage.close()


if __name__ == '__main__':
    """
    This block runs the Flask application if the script is executed directly.
    It starts the web server on all network interfaces (0.0.0.0) and
    listens on port 5000.
    """
    app.run(host='0.0.0.0', port=5000)
