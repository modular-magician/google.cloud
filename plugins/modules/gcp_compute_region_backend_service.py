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
module: gcp_compute_region_backend_service
description:
- A Region Backend Service defines a regionally-scoped group of virtual machines that
  will serve traffic for load balancing.
short_description: Creates a GCP RegionBackendService
version_added: '2.10'
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
  backends:
    description:
    - The set of backends that serve this RegionBackendService.
    required: false
    type: list
    suboptions:
      balancing_mode:
        description:
        - Specifies the balancing mode for this backend. Defaults to CONNECTION.
        - 'Some valid choices include: "UTILIZATION", "RATE", "CONNECTION"'
        required: false
        default: CONNECTION
        type: str
      capacity_scaler:
        description:
        - A multiplier applied to the group's maximum servicing capacity (based on
          UTILIZATION, RATE or CONNECTION).
        - "~>**NOTE**: This field cannot be set for INTERNAL region backend services
          (default loadBalancingScheme), but is required for non-INTERNAL backend
          service. The total capacity_scaler for all backends must be non-zero."
        - A setting of 0 means the group is completely drained, offering 0% of its
          available Capacity. Valid range is [0.0,1.0].
        required: false
        type: str
      description:
        description:
        - An optional description of this resource.
        - Provide this property when you create the resource.
        required: false
        type: str
      group:
        description:
        - The fully-qualified URL of an Instance Group or Network Endpoint Group resource.
          In case of instance group this defines the list of instances that serve
          traffic. Member virtual machine instances from each instance group must
          live in the same zone as the instance group itself. No two backends in a
          backend service are allowed to use same Instance Group resource.
        - For Network Endpoint Groups this defines list of endpoints. All endpoints
          of Network Endpoint Group must be hosted on instances located in the same
          zone as the Network Endpoint Group.
        - Backend services cannot mix Instance Group and Network Endpoint Group backends.
        - When the `load_balancing_scheme` is INTERNAL, only instance groups are supported.
        - Note that you must specify an Instance Group or Network Endpoint Group resource
          using the fully-qualified URL, rather than a partial URL.
        required: true
        type: str
      max_connections:
        description:
        - The max number of simultaneous connections for the group. Can be used with
          either CONNECTION or UTILIZATION balancing modes.
        - Cannot be set for INTERNAL backend services.
        - For CONNECTION mode, either maxConnections or one of maxConnectionsPerInstance
          or maxConnectionsPerEndpoint, as appropriate for group type, must be set.
        required: false
        type: int
      max_connections_per_instance:
        description:
        - The max number of simultaneous connections that a single backend instance
          can handle. Cannot be set for INTERNAL backend services.
        - This is used to calculate the capacity of the group.
        - Can be used in either CONNECTION or UTILIZATION balancing modes.
        - For CONNECTION mode, either maxConnections or maxConnectionsPerInstance
          must be set.
        required: false
        type: int
      max_connections_per_endpoint:
        description:
        - The max number of simultaneous connections that a single backend network
          endpoint can handle. Cannot be set for INTERNAL backend services.
        - This is used to calculate the capacity of the group. Can be used in either
          CONNECTION or UTILIZATION balancing modes. For CONNECTION mode, either maxConnections
          or maxConnectionsPerEndpoint must be set.
        required: false
        type: int
      max_rate:
        description:
        - The max requests per second (RPS) of the group. Cannot be set for INTERNAL
          backend services.
        - Can be used with either RATE or UTILIZATION balancing modes, but required
          if RATE mode. Either maxRate or one of maxRatePerInstance or maxRatePerEndpoint,
          as appropriate for group type, must be set.
        required: false
        type: int
      max_rate_per_instance:
        description:
        - The max requests per second (RPS) that a single backend instance can handle.
          This is used to calculate the capacity of the group. Can be used in either
          balancing mode. For RATE mode, either maxRate or maxRatePerInstance must
          be set. Cannot be set for INTERNAL backend services.
        required: false
        type: str
      max_rate_per_endpoint:
        description:
        - The max requests per second (RPS) that a single backend network endpoint
          can handle. This is used to calculate the capacity of the group. Can be
          used in either balancing mode. For RATE mode, either maxRate or maxRatePerEndpoint
          must be set. Cannot be set for INTERNAL backend services.
        required: false
        type: str
      max_utilization:
        description:
        - Used when balancingMode is UTILIZATION. This ratio defines the CPU utilization
          target for the group. Valid range is [0.0, 1.0].
        - Cannot be set for INTERNAL backend services.
        required: false
        type: str
  connection_draining:
    description:
    - Settings for connection draining .
    required: false
    type: dict
    suboptions:
      draining_timeout_sec:
        description:
        - Time for which instance will be drained (not accept new connections, but
          still work to finish started).
        required: false
        default: '300'
        type: int
  description:
    description:
    - An optional description of this resource.
    required: false
    type: str
  health_checks:
    description:
    - The set of URLs to HealthCheck resources for health checking this RegionBackendService.
      Currently at most one health check can be specified, and a health check is required.
    required: true
    type: list
  load_balancing_scheme:
    description:
    - Indicates what kind of load balancing this regional backend service will be
      used for. A backend service created for one type of load balancing cannot be
      used with the other(s). Must be `INTERNAL` or `INTERNAL_MANAGED`. Defaults to
      `INTERNAL`.
    - 'Some valid choices include: "INTERNAL", "INTERNAL_MANAGED"'
    required: false
    default: INTERNAL
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
  protocol:
    description:
    - The protocol this RegionBackendService uses to communicate with backends.
    - 'Possible values are HTTP, HTTPS, HTTP2, SSL, TCP, and UDP. The default is HTTP.
      **NOTE**: HTTP2 is only valid for beta HTTP/2 load balancer types and may result
      in errors if used with the GA API.'
    - 'Some valid choices include: "HTTP", "HTTPS", "HTTP2", "SSL", "TCP", "UDP"'
    required: false
    type: str
  session_affinity:
    description:
    - Type of session affinity to use. The default is NONE. Session affinity is not
      applicable if the protocol is UDP.
    - 'Some valid choices include: "NONE", "CLIENT_IP", "CLIENT_IP_PORT_PROTO", "CLIENT_IP_PROTO",
      "GENERATED_COOKIE", "HEADER_FIELD", "HTTP_COOKIE"'
    required: false
    type: str
  timeout_sec:
    description:
    - How many seconds to wait for the backend before considering it a failed request.
      Default is 30 seconds. Valid range is [1, 86400].
    required: false
    type: int
  region:
    description:
    - A reference to the region where the regional backend service resides.
    required: true
    type: str
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
  env_type:
    description:
    - Specifies which Ansible environment you're running this module within.
    - This should not be set unless you know what you're doing.
    - This only alters the User Agent string for any API requests.
    type: str
notes:
- 'API Reference: U(https://cloud.google.com/compute/docs/reference/latest/regionBackendServices)'
- 'Internal TCP/UDP Load Balancing: U(https://cloud.google.com/compute/docs/load-balancing/internal/)'
- for authentication, you can set service_account_file using the C(gcp_service_account_file)
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
- name: create a health check
  google.cloud.gcp_compute_health_check:
    name: "{{ resource_name }}"
    type: TCP
    tcp_health_check:
      port: 80
    check_interval_sec: 1
    timeout_sec: 1
    project: "{{ gcp_project }}"
    auth_kind: "{{ gcp_cred_kind }}"
    service_account_file: "{{ gcp_cred_file }}"
    state: present
  register: healthcheck

- name: create a region backend service
  google.cloud.gcp_compute_region_backend_service:
    name: test_object
    region: us-central1
    health_checks:
    - "{{ healthcheck.selfLink }}"
    connection_draining:
      draining_timeout_sec: 10
    session_affinity: CLIENT_IP
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
'''

RETURN = '''
backends:
  description:
  - The set of backends that serve this RegionBackendService.
  returned: success
  type: complex
  contains:
    balancingMode:
      description:
      - Specifies the balancing mode for this backend. Defaults to CONNECTION.
      returned: success
      type: str
    capacityScaler:
      description:
      - A multiplier applied to the group's maximum servicing capacity (based on UTILIZATION,
        RATE or CONNECTION).
      - "~>**NOTE**: This field cannot be set for INTERNAL region backend services
        (default loadBalancingScheme), but is required for non-INTERNAL backend service.
        The total capacity_scaler for all backends must be non-zero."
      - A setting of 0 means the group is completely drained, offering 0% of its available
        Capacity. Valid range is [0.0,1.0].
      returned: success
      type: str
    description:
      description:
      - An optional description of this resource.
      - Provide this property when you create the resource.
      returned: success
      type: str
    group:
      description:
      - The fully-qualified URL of an Instance Group or Network Endpoint Group resource.
        In case of instance group this defines the list of instances that serve traffic.
        Member virtual machine instances from each instance group must live in the
        same zone as the instance group itself. No two backends in a backend service
        are allowed to use same Instance Group resource.
      - For Network Endpoint Groups this defines list of endpoints. All endpoints
        of Network Endpoint Group must be hosted on instances located in the same
        zone as the Network Endpoint Group.
      - Backend services cannot mix Instance Group and Network Endpoint Group backends.
      - When the `load_balancing_scheme` is INTERNAL, only instance groups are supported.
      - Note that you must specify an Instance Group or Network Endpoint Group resource
        using the fully-qualified URL, rather than a partial URL.
      returned: success
      type: str
    maxConnections:
      description:
      - The max number of simultaneous connections for the group. Can be used with
        either CONNECTION or UTILIZATION balancing modes.
      - Cannot be set for INTERNAL backend services.
      - For CONNECTION mode, either maxConnections or one of maxConnectionsPerInstance
        or maxConnectionsPerEndpoint, as appropriate for group type, must be set.
      returned: success
      type: int
    maxConnectionsPerInstance:
      description:
      - The max number of simultaneous connections that a single backend instance
        can handle. Cannot be set for INTERNAL backend services.
      - This is used to calculate the capacity of the group.
      - Can be used in either CONNECTION or UTILIZATION balancing modes.
      - For CONNECTION mode, either maxConnections or maxConnectionsPerInstance must
        be set.
      returned: success
      type: int
    maxConnectionsPerEndpoint:
      description:
      - The max number of simultaneous connections that a single backend network endpoint
        can handle. Cannot be set for INTERNAL backend services.
      - This is used to calculate the capacity of the group. Can be used in either
        CONNECTION or UTILIZATION balancing modes. For CONNECTION mode, either maxConnections
        or maxConnectionsPerEndpoint must be set.
      returned: success
      type: int
    maxRate:
      description:
      - The max requests per second (RPS) of the group. Cannot be set for INTERNAL
        backend services.
      - Can be used with either RATE or UTILIZATION balancing modes, but required
        if RATE mode. Either maxRate or one of maxRatePerInstance or maxRatePerEndpoint,
        as appropriate for group type, must be set.
      returned: success
      type: int
    maxRatePerInstance:
      description:
      - The max requests per second (RPS) that a single backend instance can handle.
        This is used to calculate the capacity of the group. Can be used in either
        balancing mode. For RATE mode, either maxRate or maxRatePerInstance must be
        set. Cannot be set for INTERNAL backend services.
      returned: success
      type: str
    maxRatePerEndpoint:
      description:
      - The max requests per second (RPS) that a single backend network endpoint can
        handle. This is used to calculate the capacity of the group. Can be used in
        either balancing mode. For RATE mode, either maxRate or maxRatePerEndpoint
        must be set. Cannot be set for INTERNAL backend services.
      returned: success
      type: str
    maxUtilization:
      description:
      - Used when balancingMode is UTILIZATION. This ratio defines the CPU utilization
        target for the group. Valid range is [0.0, 1.0].
      - Cannot be set for INTERNAL backend services.
      returned: success
      type: str
connectionDraining:
  description:
  - Settings for connection draining .
  returned: success
  type: complex
  contains:
    drainingTimeoutSec:
      description:
      - Time for which instance will be drained (not accept new connections, but still
        work to finish started).
      returned: success
      type: int
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
fingerprint:
  description:
  - Fingerprint of this resource. A hash of the contents stored in this object. This
    field is used in optimistic locking.
  returned: success
  type: str
healthChecks:
  description:
  - The set of URLs to HealthCheck resources for health checking this RegionBackendService.
    Currently at most one health check can be specified, and a health check is required.
  returned: success
  type: list
id:
  description:
  - The unique identifier for the resource.
  returned: success
  type: int
loadBalancingScheme:
  description:
  - Indicates what kind of load balancing this regional backend service will be used
    for. A backend service created for one type of load balancing cannot be used with
    the other(s). Must be `INTERNAL` or `INTERNAL_MANAGED`. Defaults to `INTERNAL`.
  returned: success
  type: str
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
protocol:
  description:
  - The protocol this RegionBackendService uses to communicate with backends.
  - 'Possible values are HTTP, HTTPS, HTTP2, SSL, TCP, and UDP. The default is HTTP.
    **NOTE**: HTTP2 is only valid for beta HTTP/2 load balancer types and may result
    in errors if used with the GA API.'
  returned: success
  type: str
sessionAffinity:
  description:
  - Type of session affinity to use. The default is NONE. Session affinity is not
    applicable if the protocol is UDP.
  returned: success
  type: str
timeoutSec:
  description:
  - How many seconds to wait for the backend before considering it a failed request.
    Default is 30 seconds. Valid range is [1, 86400].
  returned: success
  type: int
region:
  description:
  - A reference to the region where the regional backend service resides.
  returned: success
  type: str
'''

################################################################################
# Imports
################################################################################

from ansible_collections.google.cloud.plugins.module_utils.gcp_utils import (
    navigate_hash,
    GcpSession,
    GcpModule,
    GcpRequest,
    remove_nones_from_dict,
    replace_resource_dict,
)
import json
import time

################################################################################
# Main
################################################################################


def main():
    """Main function"""

    module = GcpModule(
        argument_spec=dict(
            state=dict(default='present', choices=['present', 'absent'], type='str'),
            backends=dict(
                type='list',
                elements='dict',
                options=dict(
                    balancing_mode=dict(default='CONNECTION', type='str'),
                    capacity_scaler=dict(type='str'),
                    description=dict(type='str'),
                    group=dict(required=True, type='str'),
                    max_connections=dict(type='int'),
                    max_connections_per_instance=dict(type='int'),
                    max_connections_per_endpoint=dict(type='int'),
                    max_rate=dict(type='int'),
                    max_rate_per_instance=dict(type='str'),
                    max_rate_per_endpoint=dict(type='str'),
                    max_utilization=dict(type='str'),
                ),
            ),
            connection_draining=dict(type='dict', options=dict(draining_timeout_sec=dict(default=300, type='int'))),
            description=dict(type='str'),
            health_checks=dict(required=True, type='list', elements='str'),
            load_balancing_scheme=dict(default='INTERNAL', type='str'),
            name=dict(required=True, type='str'),
            protocol=dict(type='str'),
            session_affinity=dict(type='str'),
            timeout_sec=dict(type='int'),
            region=dict(required=True, type='str'),
        )
    )

    if not module.params['scopes']:
        module.params['scopes'] = ['https://www.googleapis.com/auth/compute']

    state = module.params['state']
    kind = 'compute#backendService'

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
    auth = GcpSession(module, 'compute')
    return wait_for_operation(module, auth.put(link, resource_to_request(module)))


def delete(module, link, kind):
    auth = GcpSession(module, 'compute')
    return wait_for_operation(module, auth.delete(link))


def resource_to_request(module):
    request = {
        u'kind': 'compute#backendService',
        u'backends': RegionBackendServiceBackendsArray(module.params.get('backends', []), module).to_request(),
        u'connectionDraining': RegionBackendServiceConnectiondraining(module.params.get('connection_draining', {}), module).to_request(),
        u'description': module.params.get('description'),
        u'healthChecks': module.params.get('health_checks'),
        u'loadBalancingScheme': module.params.get('load_balancing_scheme'),
        u'name': module.params.get('name'),
        u'protocol': module.params.get('protocol'),
        u'sessionAffinity': module.params.get('session_affinity'),
        u'timeoutSec': module.params.get('timeout_sec'),
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
    return "https://www.googleapis.com/compute/v1/projects/{project}/regions/{region}/backendServices/{name}".format(**module.params)


def collection(module):
    return "https://www.googleapis.com/compute/v1/projects/{project}/regions/{region}/backendServices".format(**module.params)


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
        u'backends': RegionBackendServiceBackendsArray(response.get(u'backends', []), module).from_response(),
        u'connectionDraining': RegionBackendServiceConnectiondraining(response.get(u'connectionDraining', {}), module).from_response(),
        u'creationTimestamp': response.get(u'creationTimestamp'),
        u'description': response.get(u'description'),
        u'fingerprint': response.get(u'fingerprint'),
        u'healthChecks': response.get(u'healthChecks'),
        u'id': response.get(u'id'),
        u'loadBalancingScheme': module.params.get('load_balancing_scheme'),
        u'name': module.params.get('name'),
        u'protocol': response.get(u'protocol'),
        u'sessionAffinity': response.get(u'sessionAffinity'),
        u'timeoutSec': response.get(u'timeoutSec'),
    }


def async_op_url(module, extra_data=None):
    if extra_data is None:
        extra_data = {}
    url = "https://www.googleapis.com/compute/v1/projects/{project}/regions/{region}/operations/{op_id}"
    combined = extra_data.copy()
    combined.update(module.params)
    return url.format(**combined)


def wait_for_operation(module, response):
    op_result = return_if_object(module, response, 'compute#operation')
    if op_result is None:
        return {}
    status = navigate_hash(op_result, ['status'])
    wait_done = wait_for_completion(status, op_result, module)
    return fetch_resource(module, navigate_hash(wait_done, ['targetLink']), 'compute#backendService')


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


class RegionBackendServiceBackendsArray(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = []

    def to_request(self):
        items = []
        for item in self.request:
            items.append(self._request_for_item(item))
        return items

    def from_response(self):
        items = []
        for item in self.request:
            items.append(self._response_from_item(item))
        return items

    def _request_for_item(self, item):
        return remove_nones_from_dict(
            {
                u'balancingMode': item.get('balancing_mode'),
                u'capacityScaler': item.get('capacity_scaler'),
                u'description': item.get('description'),
                u'group': item.get('group'),
                u'maxConnections': item.get('max_connections'),
                u'maxConnectionsPerInstance': item.get('max_connections_per_instance'),
                u'maxConnectionsPerEndpoint': item.get('max_connections_per_endpoint'),
                u'maxRate': item.get('max_rate'),
                u'maxRatePerInstance': item.get('max_rate_per_instance'),
                u'maxRatePerEndpoint': item.get('max_rate_per_endpoint'),
                u'maxUtilization': item.get('max_utilization'),
            }
        )

    def _response_from_item(self, item):
        return remove_nones_from_dict(
            {
                u'balancingMode': item.get(u'balancingMode'),
                u'capacityScaler': item.get(u'capacityScaler'),
                u'description': item.get(u'description'),
                u'group': item.get(u'group'),
                u'maxConnections': item.get(u'maxConnections'),
                u'maxConnectionsPerInstance': item.get(u'maxConnectionsPerInstance'),
                u'maxConnectionsPerEndpoint': item.get(u'maxConnectionsPerEndpoint'),
                u'maxRate': item.get(u'maxRate'),
                u'maxRatePerInstance': item.get(u'maxRatePerInstance'),
                u'maxRatePerEndpoint': item.get(u'maxRatePerEndpoint'),
                u'maxUtilization': item.get(u'maxUtilization'),
            }
        )


class RegionBackendServiceConnectiondraining(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = {}

    def to_request(self):
        return remove_nones_from_dict({u'drainingTimeoutSec': self.request.get('draining_timeout_sec')})

    def from_response(self):
        return remove_nones_from_dict({u'drainingTimeoutSec': self.request.get(u'drainingTimeoutSec')})


if __name__ == '__main__':
    main()
