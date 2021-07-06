#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2017 Google
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# ----------------------------------------------------------------------------
#
#     ***     AUTO GENERATED CODE    ***    AUTO GENERATED CODE     ***
#
# ----------------------------------------------------------------------------
#
#     This file is automatically generated by Magic Modules and manual
#     changes will be clobbered when the file is regenerated.
#
#     Please read more about how to change this file at
#     https://www.github.com/GoogleCloudPlatform/magic-modules
#
# ----------------------------------------------------------------------------

from __future__ import absolute_import, division, print_function

__metaclass__ = type

################################################################################
# Documentation
################################################################################

ANSIBLE_METADATA = {'metadata_version': '1.1', 'status': ["preview"], 'supported_by': 'community'}

DOCUMENTATION = '''
---
module: gcp_compute_global_address
description:
- Represents a Global Address resource. Global addresses are used for HTTP(S) load
  balancing.
short_description: Creates a GCP GlobalAddress
author: Google Inc. (@googlecloudplatform)
requirements:
- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0
options:
  state:
    description:
    - Whether the given object should exist in GCP
    choices:
    - present
    - absent
    default: present
    type: str
  address:
    description:
    - The static external IP address represented by this resource.
    required: false
    type: str
  description:
    description:
    - An optional description of this resource.
    required: false
    type: str
  name:
    description:
    - Name of the resource. Provided by the client when the resource is created. The
      name must be 1-63 characters long, and comply with RFC1035. Specifically, the
      name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?`
      which means the first character must be a lowercase letter, and all following
      characters must be a dash, lowercase letter, or digit, except the last character,
      which cannot be a dash.
    required: true
    type: str
  ip_version:
    description:
    - The IP Version that will be used by this address. The default value is `IPV4`.
    - 'Some valid choices include: "IPV4", "IPV6"'
    required: false
    type: str
  prefix_length:
    description:
    - The prefix length of the IP range. If not present, it means the address field
      is a single IP address.
    - This field is not applicable to addresses with addressType=EXTERNAL, or addressType=INTERNAL
      when purpose=PRIVATE_SERVICE_CONNECT .
    required: false
    type: int
  address_type:
    description:
    - The type of the address to reserve.
    - "* EXTERNAL indicates public/external single IP address."
    - "* INTERNAL indicates internal IP ranges belonging to some network."
    - 'Some valid choices include: "EXTERNAL", "INTERNAL"'
    required: false
    default: EXTERNAL
    type: str
  purpose:
    description:
    - 'The purpose of the resource. Possible values include: * VPC_PEERING - for peer
      networks * PRIVATE_SERVICE_CONNECT - for ([Beta](U(https://terraform.io/docs/providers/google/guides/provider_versions.html))
      only) Private Service Connect networks .'
    required: false
    type: str
  network:
    description:
    - The URL of the network in which to reserve the IP range. The IP range must be
      in RFC1918 space. The network cannot be deleted if there are any reserved IP
      ranges referring to it.
    - This should only be set when using an Internal address.
    - 'This field represents a link to a Network resource in GCP. It can be specified
      in two ways. First, you can place a dictionary with key ''selfLink'' and value
      of your resource''s selfLink. Alternatively, you can add `register: name-of-resource`
      to a gcp_compute_network task and then set this network field to "{{ name-of-resource
      }}"'
    required: false
    type: dict
  project:
    description:
    - The Google Cloud Platform project to use.
    type: str
  auth_kind:
    description:
    - The type of credential used.
    type: str
    required: true
    choices:
    - application
    - machineaccount
    - serviceaccount
  service_account_contents:
    description:
    - The contents of a Service Account JSON file, either in a dictionary or as a
      JSON string that represents it.
    type: jsonarg
  service_account_file:
    description:
    - The path of a Service Account JSON file if serviceaccount is selected as type.
    type: path
  service_account_email:
    description:
    - An optional service account email address if machineaccount is selected and
      the user does not wish to use the default email.
    type: str
  scopes:
    description:
    - Array of scopes to be used
    type: list
    elements: str
  env_type:
    description:
    - Specifies which Ansible environment you're running this module within.
    - This should not be set unless you know what you're doing.
    - This only alters the User Agent string for any API requests.
    type: str
notes:
- 'API Reference: U(https://cloud.google.com/compute/docs/reference/v1/globalAddresses)'
- 'Reserving a Static External IP Address: U(https://cloud.google.com/compute/docs/ip-addresses/reserve-static-external-ip-address)'
- for authentication, you can set service_account_file using the C(GCP_SERVICE_ACCOUNT_FILE)
  env variable.
- for authentication, you can set service_account_contents using the C(GCP_SERVICE_ACCOUNT_CONTENTS)
  env variable.
- For authentication, you can set service_account_email using the C(GCP_SERVICE_ACCOUNT_EMAIL)
  env variable.
- For authentication, you can set auth_kind using the C(GCP_AUTH_KIND) env variable.
- For authentication, you can set scopes using the C(GCP_SCOPES) env variable.
- Environment variables values will only be used if the playbook values are not set.
- The I(service_account_email) and I(service_account_file) options are mutually exclusive.
'''

EXAMPLES = '''
- name: create a global address
  google.cloud.gcp_compute_global_address:
    name: test_object
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
'''

RETURN = '''
address:
  description:
  - The static external IP address represented by this resource.
  returned: success
  type: str
creationTimestamp:
  description:
  - Creation timestamp in RFC3339 text format.
  returned: success
  type: str
description:
  description:
  - An optional description of this resource.
  returned: success
  type: str
id:
  description:
  - The unique identifier for the resource. This identifier is defined by the server.
  returned: success
  type: int
name:
  description:
  - Name of the resource. Provided by the client when the resource is created. The
    name must be 1-63 characters long, and comply with RFC1035. Specifically, the
    name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?`
    which means the first character must be a lowercase letter, and all following
    characters must be a dash, lowercase letter, or digit, except the last character,
    which cannot be a dash.
  returned: success
  type: str
ipVersion:
  description:
  - The IP Version that will be used by this address. The default value is `IPV4`.
  returned: success
  type: str
region:
  description:
  - A reference to the region where the regional address resides.
  returned: success
  type: str
prefixLength:
  description:
  - The prefix length of the IP range. If not present, it means the address field
    is a single IP address.
  - This field is not applicable to addresses with addressType=EXTERNAL, or addressType=INTERNAL
    when purpose=PRIVATE_SERVICE_CONNECT .
  returned: success
  type: int
addressType:
  description:
  - The type of the address to reserve.
  - "* EXTERNAL indicates public/external single IP address."
  - "* INTERNAL indicates internal IP ranges belonging to some network."
  returned: success
  type: str
purpose:
  description:
  - 'The purpose of the resource. Possible values include: * VPC_PEERING - for peer
    networks * PRIVATE_SERVICE_CONNECT - for ([Beta](U(https://terraform.io/docs/providers/google/guides/provider_versions.html))
    only) Private Service Connect networks .'
  returned: success
  type: str
network:
  description:
  - The URL of the network in which to reserve the IP range. The IP range must be
    in RFC1918 space. The network cannot be deleted if there are any reserved IP ranges
    referring to it.
  - This should only be set when using an Internal address.
  returned: success
  type: dict
'''

################################################################################
# Imports
################################################################################

from ansible_collections.google.cloud.plugins.module_utils.gcp_utils import navigate_hash, GcpSession, GcpModule, GcpRequest, replace_resource_dict
import json
import re
import time

################################################################################
# Main
################################################################################


def main():
    """Main function"""

    module = GcpModule(
        argument_spec=dict(
            state=dict(default='present', choices=['present', 'absent'], type='str'),
            address=dict(type='str'),
            description=dict(type='str'),
            name=dict(required=True, type='str'),
            ip_version=dict(type='str'),
            prefix_length=dict(type='int'),
            address_type=dict(default='EXTERNAL', type='str'),
            purpose=dict(type='str'),
            network=dict(type='dict'),
        )
    )

    if not module.params['scopes']:
        module.params['scopes'] = ['https://www.googleapis.com/auth/compute']

    state = module.params['state']
    kind = 'compute#address'

    fetch = fetch_resource(module, self_link(module), kind)
    changed = False

    if fetch:
        if state == 'present':
            if is_different(module, fetch):
                update(module, self_link(module), kind)
                fetch = fetch_resource(module, self_link(module), kind)
                changed = True
        else:
            delete(module, self_link(module), kind)
            fetch = {}
            changed = True
    else:
        if state == 'present':
            fetch = create(module, collection(module), kind)
            changed = True
        else:
            fetch = {}

    fetch.update({'changed': changed})

    module.exit_json(**fetch)


def create(module, link, kind):
    auth = GcpSession(module, 'compute')
    return wait_for_operation(module, auth.post(link, resource_to_request(module)))


def update(module, link, kind):
    delete(module, self_link(module), kind)
    create(module, collection(module), kind)


def delete(module, link, kind):
    auth = GcpSession(module, 'compute')
    return wait_for_operation(module, auth.delete(link))


def resource_to_request(module):
    request = {
        u'kind': 'compute#address',
        u'address': module.params.get('address'),
        u'description': module.params.get('description'),
        u'name': module.params.get('name'),
        u'ipVersion': module.params.get('ip_version'),
        u'prefixLength': module.params.get('prefix_length'),
        u'addressType': module.params.get('address_type'),
        u'purpose': module.params.get('purpose'),
        u'network': replace_resource_dict(module.params.get(u'network', {}), 'selfLink'),
    }
    return_vals = {}
    for k, v in request.items():
        if v or v is False:
            return_vals[k] = v

    return return_vals


def fetch_resource(module, link, kind, allow_not_found=True):
    auth = GcpSession(module, 'compute')
    return return_if_object(module, auth.get(link), kind, allow_not_found)


def self_link(module):
    return "https://compute.googleapis.com/compute/v1/projects/{project}/global/addresses/{name}".format(**module.params)


def collection(module):
    return "https://compute.googleapis.com/compute/v1/projects/{project}/global/addresses".format(**module.params)


def return_if_object(module, response, kind, allow_not_found=False):
    # If not found, return nothing.
    if allow_not_found and response.status_code == 404:
        return None

    # If no content, return nothing.
    if response.status_code == 204:
        return None

    try:
        module.raise_for_status(response)
        result = response.json()
    except getattr(json.decoder, 'JSONDecodeError', ValueError):
        module.fail_json(msg="Invalid JSON response with error: %s" % response.text)

    if navigate_hash(result, ['error', 'errors']):
        module.fail_json(msg=navigate_hash(result, ['error', 'errors']))

    return result


def is_different(module, response):
    request = resource_to_request(module)
    response = response_to_hash(module, response)

    # Remove all output-only from response.
    response_vals = {}
    for k, v in response.items():
        if k in request:
            response_vals[k] = v

    request_vals = {}
    for k, v in request.items():
        if k in response:
            request_vals[k] = v

    return GcpRequest(request_vals) != GcpRequest(response_vals)


# Remove unnecessary properties from the response.
# This is for doing comparisons with Ansible's current parameters.
def response_to_hash(module, response):
    return {
        u'address': response.get(u'address'),
        u'creationTimestamp': response.get(u'creationTimestamp'),
        u'description': response.get(u'description'),
        u'id': response.get(u'id'),
        u'name': response.get(u'name'),
        u'ipVersion': response.get(u'ipVersion'),
        u'region': response.get(u'region'),
        u'prefixLength': response.get(u'prefixLength'),
        u'addressType': response.get(u'addressType'),
        u'purpose': response.get(u'purpose'),
        u'network': response.get(u'network'),
    }


def region_selflink(name, params):
    if name is None:
        return
    url = r"https://compute.googleapis.com/compute/v1/projects/.*/regions/.*"
    if not re.match(url, name):
        name = "https://compute.googleapis.com/compute/v1/projects/{project}/regions/%s".format(**params) % name
    return name


def async_op_url(module, extra_data=None):
    if extra_data is None:
        extra_data = {}
    url = "https://compute.googleapis.com/compute/v1/projects/{project}/global/operations/{op_id}"
    combined = extra_data.copy()
    combined.update(module.params)
    return url.format(**combined)


def wait_for_operation(module, response):
    op_result = return_if_object(module, response, 'compute#operation')
    if op_result is None:
        return {}
    status = navigate_hash(op_result, ['status'])
    wait_done = wait_for_completion(status, op_result, module)
    return fetch_resource(module, navigate_hash(wait_done, ['targetLink']), 'compute#address')


def wait_for_completion(status, op_result, module):
    op_id = navigate_hash(op_result, ['name'])
    op_uri = async_op_url(module, {'op_id': op_id})
    while status != 'DONE':
        raise_if_errors(op_result, ['error', 'errors'], module)
        time.sleep(1.0)
        op_result = fetch_resource(module, op_uri, 'compute#operation', False)
        status = navigate_hash(op_result, ['status'])
    return op_result


def raise_if_errors(response, err_path, module):
    errors = navigate_hash(response, err_path)
    if errors is not None:
        module.fail_json(msg=errors)


if __name__ == '__main__':
    main()
