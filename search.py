from tinydb import Query


def get_template_name(params, db):
    template = Query()
    result = db.search(template.fragment(params))
    if result:
        return result[0]['name']
    else:
        return None
