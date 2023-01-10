from flask import Flask, request
from tinydb import TinyDB

from checks import check
from search import get_template_name


app = Flask(__name__)
db = TinyDB('templates.json')


@app.post("/get_form")
def handler():
    params = request.args.to_dict()
    template = {}
    for key in params:
        type_field = check(params[key])
        template.update({key: type_field})
    name = get_template_name(template, db)
    if not name:
        print(f'params_in_request - {params}, transform_template - {template}')
        return template
    else:
        print(f'params_in_request - {params}, transform_template - {template}, template_name - {name}')
        return name
