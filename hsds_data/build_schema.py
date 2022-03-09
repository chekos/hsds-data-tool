import json
from pathlib import Path

import jq
from black import format_str, FileMode

THIS_DIR = Path(__file__).parent
DATA_FILE = THIS_DIR.joinpath("../data/datapackage.json")
SCHEMA_FILE = THIS_DIR.joinpath("hsds_schemas-DRAFT.py")

with open(DATA_FILE, "r") as datafile:
    data_package = json.load(datafile)


def write_org_schema(schema_name, schema_json):
    schema_string = f"hsds_{schema_name}_schema = " + "pa.DataFrameSchema({<COLUMNS>})"

    columns_string = ""

    for field in schema_json:
        if field.get("format"):
            _format = f"format: {field['format']}. "
        else:
            _format = ""

        if field.get("constraints"):
            if not field["constraints"].get("required"):
                field["required"] = False
            else:
                field["required"] = True

            if not field["constraints"].get("unique"):
                field["unique"] = False
            else:
                field["unique"] = True

        if field["type"] == "number":
            field["type"] = "float"
        if field["type"] == "date":
            field["type"] = "datetime64"
        # if field["type"] == "string":
        #     field["type"] = "object"

        if field.get("unique"):
            columns_string += f"""
            "{field['name']}": pa.Column(dtype = "{field['type']}", description = "{_format}{field['description']}", required = {field['required']}, unique = {field['unique']},),"""
        elif field.get("required"):
            columns_string += f"""
            "{field['name']}": pa.Column(dtype = "{field['type']}", description = "{_format}{field['description']}", required = {field['required']},),"""
        else:
            columns_string += f"""
            "{field['name']}": pa.Column(dtype = "{field['type']}", description = "{_format}{field['description']}", required = False, nullable = True,),"""

    final_string = schema_string.replace("<COLUMNS>", columns_string) + "\n"
    return final_string


resources_json = (
    jq.compile(".resources[] | { schema_name: .name, schema: .schema.fields }")
    .input(data_package)
    .all()
)

py_file = "import pandera as pa\nfrom enum import Enum\n\n"
for resource in resources_json:
    py_file += write_org_schema(resource["schema_name"], resource["schema"])


hsds_dict_string = ",".join(
    [
        f""" "{resource['schema_name']}_schema": hsds_{resource['schema_name']}_schema """
        for resource in resources_json
    ]
)
hsds_dict_string = "HSDS_SCHEMAS_DICT = {<ITEMS>}".replace("<ITEMS>", hsds_dict_string)

py_file = py_file + "\n\n" + hsds_dict_string

enum_string = "\n\t".join(
    [
        f"""{resource['schema_name']} = "{resource['schema_name']}" """
        for resource in resources_json
    ]
)
enum_string = "class HSDS_SCHEMAS_ENUM(str, Enum):\n\t<SCHEMAS>".replace(
    "<SCHEMAS>", enum_string
)
py_file = py_file + "\n\n" + enum_string


py_file = format_str(py_file, mode=FileMode())

with open(SCHEMA_FILE, "w") as file:
    file.write(py_file)
