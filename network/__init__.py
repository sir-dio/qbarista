from network.client import send, test_connection
from network.request_handler import qBaristaRequestHandler
from network.server import qBaristaServer

available_requests = [
    'Hello!',
    'Shutdown!',
    'Reboot!',
    'Report connection!',
    'Connect: [SSID] [PASSWORD]',
]
