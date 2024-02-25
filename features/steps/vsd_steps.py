import os
import json
from behave import given, when, then
# from nsd_manager import ncom_nsd_service
from vsd_manager import vsd_api_service


@given('I have initialized the vsd service')
def step_impl(context):
    url = os.environ.get('url', None)
    username = os.environ.get('username', None)
    password = os.environ.get('password', None)
    enterprise = os.environ.get('enterprise', None)

    if not all([url, username, password, enterprise]):
        with open('config.json', 'r') as config_file:
            config = json.load(config_file)
        url = url or config['url']
        username = username or config['username']
        password = password or config['password']
        enterprise = enterprise or config['enterprise']

    context.vsd_service = vsd_api_service(url,username, password, enterprise)
    # context.ncom_service = ncom_nsd_service(base_url, ncom_user, password, ncom_tenant, api_client)

@when('I query the enterprises')
def step_impl(context):
    # context.vsd_service.list_enterprises()
    # @token_required
    context.enterprises = context.vsd_service.list_enterprises()
    assert context.enterprises is not None

@then('I get the enterprises')
def step_impl(context):
    assert context.enterprises==['APX_UPL_ERIC', 'APX_VIJ3_ERIC', 'Audit Enterprise', 'Shared Infrastructure', 'testixr']

