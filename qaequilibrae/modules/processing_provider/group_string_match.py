from qaequilibrae.i18n.translate import trlt as tr


group_id_number = {
    "modelbuilding": 1,
    "data": 2,
    "pathsandassignment": 3,
    "publictransport": 4,
}

group_name = {
    1: "Model Building",
    2: "Data",
    3: "Paths and assignment",
    4: "Public Transport",
}


def translate_group(context, group): 
    num = group_id_number[group]
    name = tr(context, group_name[num])

    return f"{num}. {name}"
