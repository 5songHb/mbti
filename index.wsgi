import sae
from server import SERVER

application = sae.create_wsgi_app(SERVER)
