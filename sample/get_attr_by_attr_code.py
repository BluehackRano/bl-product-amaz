from __future__ import print_function
from bl_product_amaz.amz_attrs import AMZ_attrs
from pprint import pprint

api_instance = AMZ_attrs()

try:

    res = api_instance.get_attr_by_attr_code("1001")

    pprint(res)

except Exception as e:
    print("Exception when calling get_sub_attr_by_attr_code %s\n" % e)