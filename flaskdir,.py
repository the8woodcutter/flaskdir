from flask import Flask, render_template, request, redirect, session, url_for, jsonify, flash, send_from_directory
from more_itertools import batched
import re
import uuid
import time
import os
import json
import shelve
import hashlib
import random

from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask("flaskdir", static_url_path='', static_folder='static')
da_sekret = (uuid.uuid4().hex * random.randint(1,7))
da_splittah = da_sekret.split()
da_scrambler = random.shuffle(da_splittah)
da_unknown_combo = "".join(da_scrambler)
app.config["SECRET_KEY"] = da_unknown_combo

import funcs

