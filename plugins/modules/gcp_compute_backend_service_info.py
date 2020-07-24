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
module: gcp_compute_backend_service_info
description:
- Gather info for GCP BackendService
short_description: Gather info for GCP BackendService
version_added: '2.7'
author: Google Inc. (@googlecloudplatform)
requirements:
- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0
options:
  filters:
    description:
    - A list of filter value pairs. Available filters are listed here U(https://cloud.google.com/sdk/gcloud/reference/topic/filters).
    - Each additional filter in the list will act be added as an AND condition (filter1
      and filter2) .
    type: list
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
- name: get info on a backend service
  gcp_compute_backend_service_info:
    filters:
    - name = test_object
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
'''

RETURN = '''
resources:
  description: List of resources
  returned: always
  type: complex
  contains:
    affinityCookieTtlSec:
      description:
      - Lifetime of cookies in seconds if session_affinity is GENERATED_COOKIE. If
        set to 0, the cookie is non-persistent and lasts only until the end of the
        browser session (or equivalent). The maximum allowed value for TTL is one
        day.
      - When the load balancing scheme is INTERNAL, this field is not used.
      returned: success
      type: int
    backends:
      description:
      - The set of backends that serve this BackendService.
      returned: success
      type: complex
      contains:
        balancingMode:
          description:
          - Specifies the balancing mode for this backend.
          - For global HTTP(S) or TCP/SSL load balancing, the default is UTILIZATION.
            Valid values are UTILIZATION, RATE (for HTTP(S)) and CONNECTION (for TCP/SSL).
          returned: success
          type: str
        capacityScaler:
          description:
          - A multiplier applied to the group's maximum servicing capacity (based
            on UTILIZATION, RATE or CONNECTION).
          - Default value is 1, which means the group will serve up to 100% of its
            configured capacity (depending on balancingMode). A setting of 0 means
            the group is completely drained, offering 0% of its available Capacity.
            Valid range is [0.0,1.0].
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
          - The fully-qualified URL of an Instance Group or Network Endpoint Group
            resource. In case of instance group this defines the list of instances
            that serve traffic. Member virtual machine instances from each instance
            group must live in the same zone as the instance group itself. No two
            backends in a backend service are allowed to use same Instance Group resource.
          - For Network Endpoint Groups this defines list of endpoints. All endpoints
            of Network Endpoint Group must be hosted on instances located in the same
            zone as the Network Endpoint Group.
          - Backend services cannot mix Instance Group and Network Endpoint Group
            backends.
          - Note that you must specify an Instance Group or Network Endpoint Group
            resource using the fully-qualified URL, rather than a partial URL.
          returned: success
          type: str
        maxConnections:
          description:
          - The max number of simultaneous connections for the group. Can be used
            with either CONNECTION or UTILIZATION balancing modes.
          - For CONNECTION mode, either maxConnections or one of maxConnectionsPerInstance
            or maxConnectionsPerEndpoint, as appropriate for group type, must be set.
          returned: success
          type: int
        maxConnectionsPerInstance:
          description:
          - The max number of simultaneous connections that a single backend instance
            can handle. This is used to calculate the capacity of the group. Can be
            used in either CONNECTION or UTILIZATION balancing modes.
          - For CONNECTION mode, either maxConnections or maxConnectionsPerInstance
            must be set.
          returned: success
          type: int
        maxConnectionsPerEndpoint:
          description:
          - The max number of simultaneous connections that a single backend network
            endpoint can handle. This is used to calculate the capacity of the group.
            Can be used in either CONNECTION or UTILIZATION balancing modes.
          - For CONNECTION mode, either maxConnections or maxConnectionsPerEndpoint
            must be set.
          returned: success
          type: int
        maxRate:
          description:
          - The max requests per second (RPS) of the group.
          - Can be used with either RATE or UTILIZATION balancing modes, but required
            if RATE mode. For RATE mode, either maxRate or one of maxRatePerInstance
            or maxRatePerEndpoint, as appropriate for group type, must be set.
          returned: success
          type: int
        maxRatePerInstance:
          description:
          - The max requests per second (RPS) that a single backend instance can handle.
            This is used to calculate the capacity of the group. Can be used in either
            balancing mode. For RATE mode, either maxRate or maxRatePerInstance must
            be set.
          returned: success
          type: str
        maxRatePerEndpoint:
          description:
          - The max requests per second (RPS) that a single backend network endpoint
            can handle. This is used to calculate the capacity of the group. Can be
            used in either balancing mode. For RATE mode, either maxRate or maxRatePerEndpoint
            must be set.
          returned: success
          type: str
        maxUtilization:
          description:
          - Used when balancingMode is UTILIZATION. This ratio defines the CPU utilization
            target for the group. The default is 0.8. Valid range is [0.0, 1.0].
          returned: success
          type: str
    circuitBreakers:
      description:
      - Settings controlling the volume of connections to a backend service. This
        field is applicable only when the load_balancing_scheme is set to INTERNAL_SELF_MANAGED.
      returned: success
      type: complex
      contains:
        maxRequestsPerConnection:
          description:
          - Maximum requests for a single backend connection. This parameter is respected
            by both the HTTP/1.1 and HTTP/2 implementations. If not specified, there
            is no limit. Setting this parameter to 1 will effectively disable keep
            alive.
          returned: success
          type: int
        maxConnections:
          description:
          - The maximum number of connections to the backend cluster.
          - Defaults to 1024.
          returned: success
          type: int
        maxPendingRequests:
          description:
          - The maximum number of pending requests to the backend cluster.
          - Defaults to 1024.
          returned: success
          type: int
        maxRequests:
          description:
          - The maximum number of parallel requests to the backend cluster.
          - Defaults to 1024.
          returned: success
          type: int
        maxRetries:
          description:
          - The maximum number of parallel retries to the backend cluster.
          - Defaults to 3.
          returned: success
          type: int
    consistentHash:
      description:
      - Consistent Hash-based load balancing can be used to provide soft session affinity
        based on HTTP headers, cookies or other properties. This load balancing policy
        is applicable only for HTTP connections. The affinity to a particular destination
        host will be lost when one or more hosts are added/removed from the destination
        service. This field specifies parameters that control consistent hashing.
        This field only applies if the load_balancing_scheme is set to INTERNAL_SELF_MANAGED.
        This field is only applicable when locality_lb_policy is set to MAGLEV or
        RING_HASH.
      returned: success
      type: complex
      contains:
        httpCookie:
          description:
          - Hash is based on HTTP Cookie. This field describes a HTTP cookie that
            will be used as the hash key for the consistent hash load balancer. If
            the cookie is not present, it will be generated.
          - This field is applicable if the sessionAffinity is set to HTTP_COOKIE.
          returned: success
          type: complex
          contains:
            ttl:
              description:
              - Lifetime of the cookie.
              returned: success
              type: complex
              contains:
                seconds:
                  description:
                  - Span of time at a resolution of a second.
                  - Must be from 0 to 315,576,000,000 inclusive.
                  returned: success
                  type: int
                nanos:
                  description:
                  - Span of time that's a fraction of a second at nanosecond resolution.
                    Durations less than one second are represented with a 0 seconds
                    field and a positive nanos field. Must be from 0 to 999,999,999
                    inclusive.
                  returned: success
                  type: int
            name:
              description:
              - Name of the cookie.
              returned: success
              type: str
            path:
              description:
              - Path to set for the cookie.
              returned: success
              type: str
        httpHeaderName:
          description:
          - The hash based on the value of the specified header field.
          - This field is applicable if the sessionAffinity is set to HEADER_FIELD.
          returned: success
          type: str
        minimumRingSize:
          description:
          - The minimum number of virtual nodes to use for the hash ring.
          - Larger ring sizes result in more granular load distributions. If the number
            of hosts in the load balancing pool is larger than the ring size, each
            host will be assigned a single virtual node.
          - Defaults to 1024.
          returned: success
          type: int
    cdnPolicy:
      description:
      - Cloud CDN configuration for this BackendService.
      returned: success
      type: complex
      contains:
        cacheKeyPolicy:
          description:
          - The CacheKeyPolicy for this CdnPolicy.
          returned: success
          type: complex
          contains:
            includeHost:
              description:
              - If true requests to different hosts will be cached separately.
              returned: success
              type: bool
            includeProtocol:
              description:
              - If true, http and https requests will be cached separately.
              returned: success
              type: bool
            includeQueryString:
              description:
              - If true, include query string parameters in the cache key according
                to query_string_whitelist and query_string_blacklist. If neither is
                set, the entire query string will be included.
              - If false, the query string will be excluded from the cache key entirely.
              returned: success
              type: bool
            queryStringBlacklist:
              description:
              - Names of query string parameters to exclude in cache keys.
              - All other parameters will be included. Either specify query_string_whitelist
                or query_string_blacklist, not both.
              - "'&' and '=' will be percent encoded and not treated as delimiters."
              returned: success
              type: list
            queryStringWhitelist:
              description:
              - Names of query string parameters to include in cache keys.
              - All other parameters will be excluded. Either specify query_string_whitelist
                or query_string_blacklist, not both.
              - "'&' and '=' will be percent encoded and not treated as delimiters."
              returned: success
              type: list
        signedUrlCacheMaxAgeSec:
          description:
          - Maximum number of seconds the response to a signed URL request will be
            considered fresh, defaults to 1hr (3600s). After this time period, the
            response will be revalidated before being served.
          - 'When serving responses to signed URL requests, Cloud CDN will internally
            behave as though all responses from this backend had a "Cache-Control:
            public, max-age=[TTL]" header, regardless of any existing Cache-Control
            header. The actual headers served in responses will not be altered.'
          returned: success
          type: int
    connectionDraining:
      description:
      - Settings for connection draining .
      returned: success
      type: complex
      contains:
        drainingTimeoutSec:
          description:
          - Time for which instance will be drained (not accept new connections, but
            still work to finish started).
          returned: success
          type: int
    creationTimestamp:
      description:
      - Creation timestamp in RFC3339 text format.
      returned: success
      type: str
    customRequestHeaders:
      description:
      - Headers that the HTTP/S load balancer should add to proxied requests.
      returned: success
      type: list
    fingerprint:
      description:
      - Fingerprint of this resource. A hash of the contents stored in this object.
        This field is used in optimistic locking.
      returned: success
      type: str
    description:
      description:
      - An optional description of this resource.
      returned: success
      type: str
    enableCDN:
      description:
      - If true, enable Cloud CDN for this BackendService.
      returned: success
      type: bool
    healthChecks:
      description:
      - The set of URLs to the HttpHealthCheck or HttpsHealthCheck resource for health
        checking this BackendService. Currently at most one health check can be specified,
        and a health check is required.
      - For internal load balancing, a URL to a HealthCheck resource must be specified
        instead.
      returned: success
      type: list
    id:
      description:
      - The unique identifier for the resource.
      returned: success
      type: int
    iap:
      description:
      - Settings for enabling Cloud Identity Aware Proxy.
      returned: success
      type: complex
      contains:
        enabled:
          description:
          - Enables IAP.
          returned: success
          type: bool
        oauth2ClientId:
          description:
          - OAuth2 Client ID for IAP .
          returned: success
          type: str
        oauth2ClientSecret:
          description:
          - OAuth2 Client Secret for IAP .
          returned: success
          type: str
        oauth2ClientSecretSha256:
          description:
          - OAuth2 Client Secret SHA-256 for IAP .
          returned: success
          type: str
    loadBalancingScheme:
      description:
      - Indicates whether the backend service will be used with internal or external
        load balancing. A backend service created for one type of load balancing cannot
        be used with the other.
      returned: success
      type: str
    localityLbPolicy:
      description:
      - The load balancing algorithm used within the scope of the locality.
      - The possible values are - ROUND_ROBIN - This is a simple policy in which each
        healthy backend is selected in round robin order.
      - LEAST_REQUEST - An O(1) algorithm which selects two random healthy hosts and
        picks the host which has fewer active requests.
      - RING_HASH - The ring/modulo hash load balancer implements consistent hashing
        to backends. The algorithm has the property that the addition/removal of a
        host from a set of N hosts only affects 1/N of the requests.
      - RANDOM - The load balancer selects a random healthy host.
      - ORIGINAL_DESTINATION - Backend host is selected based on the client connection
        metadata, i.e., connections are opened to the same address as the destination
        address of the incoming connection before the connection was redirected to
        the load balancer.
      - MAGLEV - used as a drop in replacement for the ring hash load balancer.
      - Maglev is not as stable as ring hash but has faster table lookup build times
        and host selection times. For more information about Maglev, refer to https://ai.google/research/pubs/pub44824
        This field is applicable only when the load_balancing_scheme is set to INTERNAL_SELF_MANAGED.
      returned: success
      type: str
    name:
      description:
      - Name of the resource. Provided by the client when the resource is created.
        The name must be 1-63 characters long, and comply with RFC1035. Specifically,
        the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?`
        which means the first character must be a lowercase letter, and all following
        characters must be a dash, lowercase letter, or digit, except the last character,
        which cannot be a dash.
      returned: success
      type: str
    outlierDetection:
      description:
      - Settings controlling eviction of unhealthy hosts from the load balancing pool.
      - This field is applicable only when the load_balancing_scheme is set to INTERNAL_SELF_MANAGED.
      returned: success
      type: complex
      contains:
        baseEjectionTime:
          description:
          - The base time that a host is ejected for. The real time is equal to the
            base time multiplied by the number of times the host has been ejected.
            Defaults to 30000ms or 30s.
          returned: success
          type: complex
          contains:
            seconds:
              description:
              - Span of time at a resolution of a second. Must be from 0 to 315,576,000,000
                inclusive.
              returned: success
              type: int
            nanos:
              description:
              - Span of time that's a fraction of a second at nanosecond resolution.
                Durations less than one second are represented with a 0 `seconds`
                field and a positive `nanos` field. Must be from 0 to 999,999,999
                inclusive.
              returned: success
              type: int
        consecutiveErrors:
          description:
          - Number of errors before a host is ejected from the connection pool. When
            the backend host is accessed over HTTP, a 5xx return code qualifies as
            an error.
          - Defaults to 5.
          returned: success
          type: int
        consecutiveGatewayFailure:
          description:
          - The number of consecutive gateway failures (502, 503, 504 status or connection
            errors that are mapped to one of those status codes) before a consecutive
            gateway failure ejection occurs. Defaults to 5.
          returned: success
          type: int
        enforcingConsecutiveErrors:
          description:
          - The percentage chance that a host will be actually ejected when an outlier
            status is detected through consecutive 5xx. This setting can be used to
            disable ejection or to ramp it up slowly. Defaults to 100.
          returned: success
          type: int
        enforcingConsecutiveGatewayFailure:
          description:
          - The percentage chance that a host will be actually ejected when an outlier
            status is detected through consecutive gateway failures. This setting
            can be used to disable ejection or to ramp it up slowly. Defaults to 0.
          returned: success
          type: int
        enforcingSuccessRate:
          description:
          - The percentage chance that a host will be actually ejected when an outlier
            status is detected through success rate statistics. This setting can be
            used to disable ejection or to ramp it up slowly. Defaults to 100.
          returned: success
          type: int
        interval:
          description:
          - Time interval between ejection sweep analysis. This can result in both
            new ejections as well as hosts being returned to service. Defaults to
            10 seconds.
          returned: success
          type: complex
          contains:
            seconds:
              description:
              - Span of time at a resolution of a second. Must be from 0 to 315,576,000,000
                inclusive.
              returned: success
              type: int
            nanos:
              description:
              - Span of time that's a fraction of a second at nanosecond resolution.
                Durations less than one second are represented with a 0 `seconds`
                field and a positive `nanos` field. Must be from 0 to 999,999,999
                inclusive.
              returned: success
              type: int
        maxEjectionPercent:
          description:
          - Maximum percentage of hosts in the load balancing pool for the backend
            service that can be ejected. Defaults to 10%.
          returned: success
          type: int
        successRateMinimumHosts:
          description:
          - The number of hosts in a cluster that must have enough request volume
            to detect success rate outliers. If the number of hosts is less than this
            setting, outlier detection via success rate statistics is not performed
            for any host in the cluster. Defaults to 5.
          returned: success
          type: int
        successRateRequestVolume:
          description:
          - The minimum number of total requests that must be collected in one interval
            (as defined by the interval duration above) to include this host in success
            rate based outlier detection. If the volume is lower than this setting,
            outlier detection via success rate statistics is not performed for that
            host. Defaults to 100.
          returned: success
          type: int
        successRateStdevFactor:
          description:
          - 'This factor is used to determine the ejection threshold for success rate
            outlier ejection. The ejection threshold is the difference between the
            mean success rate, and the product of this factor and the standard deviation
            of the mean success rate: mean - (stdev * success_rate_stdev_factor).
            This factor is divided by a thousand to get a double. That is, if the
            desired factor is 1.9, the runtime value should be 1900. Defaults to 1900.'
          returned: success
          type: int
    portName:
      description:
      - Name of backend port. The same name should appear in the instance groups referenced
        by this service. Required when the load balancing scheme is EXTERNAL.
      returned: success
      type: str
    protocol:
      description:
      - The protocol this BackendService uses to communicate with backends.
      - 'The default is HTTP. **NOTE**: HTTP2 is only valid for beta HTTP/2 load balancer
        types and may result in errors if used with the GA API.'
      returned: success
      type: str
    securityPolicy:
      description:
      - The security policy associated with this backend service.
      returned: success
      type: str
    sessionAffinity:
      description:
      - Type of session affinity to use. The default is NONE. Session affinity is
        not applicable if the protocol is UDP.
      returned: success
      type: str
    timeoutSec:
      description:
      - How many seconds to wait for the backend before considering it a failed request.
        Default is 30 seconds. Valid range is [1, 86400].
      returned: success
      type: int
    logConfig:
      description:
      - This field denotes the logging options for the load balancer traffic served
        by this backend service.
      - If logging is enabled, logs will be exported to Stackdriver.
      returned: success
      type: complex
      contains:
        enable:
          description:
          - Whether to enable logging for the load balancer traffic served by this
            backend service.
          returned: success
          type: bool
        sampleRate:
          description:
          - This field can only be specified if logging is enabled for this backend
            service. The value of the field must be in [0, 1]. This configures the
            sampling rate of requests to the load balancer where 1.0 means all logged
            requests are reported and 0.0 means no logged requests are reported.
          - The default value is 1.0.
          returned: success
          type: str
'''

################################################################################
# Imports
################################################################################
from ansible.module_utils.gcp_utils import navigate_hash, GcpSession, GcpModule, GcpRequest
import json

################################################################################
# Main
################################################################################


def main():
    module = GcpModule(argument_spec=dict(filters=dict(type='list', elements='str')))

    if not module.params['scopes']:
        module.params['scopes'] = ['https://www.googleapis.com/auth/compute']

    return_value = {'resources': fetch_list(module, collection(module), query_options(module.params['filters']))}
    module.exit_json(**return_value)


def collection(module):
    return "https://compute.googleapis.com/compute/v1/projects/{project}/global/backendServices".format(**module.params)


def fetch_list(module, link, query):
    auth = GcpSession(module, 'compute')
    return auth.list(link, return_if_object, array_name='items', params={'filter': query})


def query_options(filters):
    if not filters:
        return ''

    if len(filters) == 1:
        return filters[0]
    else:
        queries = []
        for f in filters:
            # For multiple queries, all queries should have ()
            if f[0] != '(' and f[-1] != ')':
                queries.append("(%s)" % ''.join(f))
            else:
                queries.append(f)

        return ' '.join(queries)


def return_if_object(module, response):
    # If not found, return nothing.
    if response.status_code == 404:
        return None

    # If no content, return nothing.
    if response.status_code == 204:
        return None

    try:
        module.raise_for_status(response)
        result = response.json()
    except getattr(json.decoder, 'JSONDecodeError', ValueError) as inst:
        module.fail_json(msg="Invalid JSON response with error: %s" % inst)

    if navigate_hash(result, ['error', 'errors']):
        module.fail_json(msg=navigate_hash(result, ['error', 'errors']))

    return result


if __name__ == "__main__":
    main()
