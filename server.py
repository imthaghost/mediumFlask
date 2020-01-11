"""server"""

__author__ = "Gary Frederick"
__version__ = "1.0"

from medium import app
import os
import sys

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)
