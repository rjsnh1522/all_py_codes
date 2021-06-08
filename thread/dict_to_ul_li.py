data = {
         u'offense_source': u'172.26.6.73',
         u'destination_networks': [u'other'],
         u'policy_category_count': 0,
         u'last_updated_time': 1575969270970,
         u'inactive': False,
         u'flow_count': 0,
         u'domain_id': 3,
         u'follow_up': False,
         u'severity': 5,
         u'credibility': 2,
         u'device_count': 2,
         u'username_count': 0,
         u'magnitude': 2,
         u'relevance': 1,
         u'source_network': u'other',
         u'status': u'OPEN',
         u'source_count': 1,
         u'description': u'Excessive Firewall Denies Between Hosts\n containing Firewall Deny\n',
         u'rules': [{u'type': u'CRE_RULE', u'id': 100033}],
         u'start_time': 1575969003552,
         u'source_address_ids': [438],
         u'offense_type': 0,
         u'category_count': 2,
         u'categories': [u'Firewall Deny', u'ACL Deny'],
         u'event_count': 823,
         u'log_sources': [{u'type_id': 73, u'type_name': u'FortiGate', u'id': 812, u'name': u'FortiGate @ 172.26.6.254'}],
         u'security_category_count': 2,
         u'protected': False,
         u'assigned_to': None,
         u'local_destination_address_ids': []
}

data = {
    "a": [1234, {"b": "a", "c": [
        {"d": 1234,
         "e": [123, 456, {"ab": "1235"},
               [1234445, 0000, {"kd": "cdd"}]
               ]
         }
    ]}]
}

class DictValueRequiredError(Exception):
    """Dict value required"""

def return_str(data):
    return f"<li>{data}</li>"


def loop_in_list(data, r=""):
    r = ""
    for item in data:
        if type(item) == dict:
            r += loop_in_dict(item)
        if type(item) == str or type(item) == int or type(item) == bool or item is None:
            r += return_str(item)
        if type(item) == list:
            r += loop_in_list(item, r)
    return f"<ul> {r}</ul>"


def loop_in_dict(data):
    g = ""
    for k, v in data.items():
        if type(v) == str or type(v) == int or type(v) == bool or v is None:
            g += f"<li><b>{k}</b> {v}</li>"
        if type(v) == dict:
            r = loop_in_dict(v)
            g += f"<li><b>{k}</b> {r}</li>"
        if type(v) == list:
            r = loop_in_list(v)
            g += f"<li><b>{k}</b> {r}</li>"
    return g


def loop_and_make_ul_li(data):
    ret_str = ""
    for item in data:
        if type(item) == dict:
            ret = loop_in_dict(item)
            ret_str = f"<ul>{ret}</ul>"
        if type(item) == str:
            ret = return_str(item)
            ret_str = f"<ul>{ret}</ul>"
        if type(item) == list:
            ret = loop_in_list(item)
            ret_str = f"<ul>{ret}</ul>"
    return ret_str


def ul_li_gen(data):
    if type(data) != dict:
        raise DictValueRequiredError

    ul_li_str = ""
    for key, val in data.items():

        if type(val) == str or type(val) == int or type(val) == bool or val is None:
            k = str(val)
            ul_li_str += f"<li><b>{key}</b> {k}</li>"
        elif type(val) == list:
            k = loop_in_list(val)
            ul_li_str += f"<li><b>{key}</b> {k}</li>"
        else:
            k = loop_and_make_ul_li(val)
            ul_li_str += f"<li><b>{key}</b> {k}</li>"
    print(f"<ul> {ul_li_str} </ul>")


ul_li_gen(data)



