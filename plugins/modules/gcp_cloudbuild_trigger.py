#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2017 Google
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# ----------------------------------------------------------------------------
#
#     ***     AUTO GENERATED CODE    ***    AUTO GENERATED CODE     ***
#     ***     DIFF TEST DIFF TEST    ***
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
module: gcp_cloudbuild_trigger
description:
- Configuration for an automated build in response to source repository changes.
short_description: Creates a GCP Trigger
version_added: '2.8'
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
  id:
    description:
    - The unique identifier for the trigger.
    required: false
    type: str
  name:
    description:
    - Name of the trigger. Must be unique within the project.
    required: false
    type: str
    version_added: '2.10'
  description:
    description:
    - Human-readable description of the trigger.
    required: false
    type: str
  disabled:
    description:
    - Whether the trigger is disabled or not. If true, the trigger will never result
      in a build.
    required: false
    type: bool
  substitutions:
    description:
    - Substitutions data for Build resource.
    required: false
    type: dict
  filename:
    description:
    - Path, from the source root, to a file whose contents is used for the template.
      Either a filename or build template must be provided.
    required: false
    type: str
  ignored_files:
    description:
    - ignoredFiles and includedFiles are file glob matches using http://godoc/pkg/path/filepath#Match
      extended with support for `**`.
    - If ignoredFiles and changed files are both empty, then they are not used to
      determine whether or not to trigger a build.
    - If ignoredFiles is not empty, then we ignore any files that match any of the
      ignored_file globs. If the change has no files that are outside of the ignoredFiles
      globs, then we do not trigger a build.
    required: false
    type: list
  included_files:
    description:
    - ignoredFiles and includedFiles are file glob matches using http://godoc/pkg/path/filepath#Match
      extended with support for `**`.
    - If any of the files altered in the commit pass the ignoredFiles filter and includedFiles
      is empty, then as far as this filter is concerned, we should trigger the build.
    - If any of the files altered in the commit pass the ignoredFiles filter and includedFiles
      is not empty, then we make sure that at least one of those files matches a includedFiles
      glob. If not, then we do not trigger a build.
    required: false
    type: list
  trigger_template:
    description:
    - Template describing the types of source changes to trigger a build.
    - Branch and tag names in trigger templates are interpreted as regular expressions.
      Any branch or tag change that matches that regular expression will trigger a
      build.
    required: false
    type: dict
    suboptions:
      project_id:
        description:
        - ID of the project that owns the Cloud Source Repository. If omitted, the
          project ID requesting the build is assumed.
        required: false
        type: str
      repo_name:
        description:
        - Name of the Cloud Source Repository. If omitted, the name "default" is assumed.
        required: false
        default: default
        type: str
      dir:
        description:
        - Directory, relative to the source root, in which to run the build.
        - This must be a relative path. If a step's dir is specified and is an absolute
          path, this value is ignored for that step's execution.
        required: false
        type: str
      branch_name:
        description:
        - Name of the branch to build. Exactly one a of branch name, tag, or commit
          SHA must be provided.
        - This field is a regular expression.
        required: false
        type: str
      tag_name:
        description:
        - Name of the tag to build. Exactly one of a branch name, tag, or commit SHA
          must be provided.
        - This field is a regular expression.
        required: false
        type: str
      commit_sha:
        description:
        - Explicit commit SHA to build. Exactly one of a branch name, tag, or commit
          SHA must be provided.
        required: false
        type: str
  build:
    description:
    - Contents of the build template. Either a filename or build template must be
      provided.
    required: false
    type: dict
    suboptions:
      tags:
        description:
        - Tags for annotation of a Build. These are not docker tags.
        required: false
        type: list
      images:
        description:
        - A list of images to be pushed upon the successful completion of all build
          steps.
        - The images are pushed using the builder service account's credentials.
        - The digests of the pushed images will be stored in the Build resource's
          results field.
        - If any of the images fail to be pushed, the build status is marked FAILURE.
        required: false
        type: list
      timeout:
        description:
        - Amount of time that this build should be allowed to run, to second granularity.
          If this amount of time elapses, work on the build will cease and the build
          status will be TIMEOUT.
        - This timeout must be equal to or greater than the sum of the timeouts for
          build steps within the build.
        - The expected format is the number of seconds followed by s.
        - Default time is ten minutes (600s).
        required: false
        default: 600s
        type: str
        version_added: '2.10'
      steps:
        description:
        - The operations to be performed on the workspace.
        required: true
        type: list
        suboptions:
          name:
            description:
            - The name of the container image that will run this particular build
              step.
            - If the image is available in the host's Docker daemon's cache, it will
              be run directly. If not, the host will attempt to pull the image first,
              using the builder service account's credentials if necessary.
            - The Docker daemon's cache will already have the latest versions of all
              of the officially supported build steps (U(https://github.com/GoogleCloudPlatform/cloud-builders)).
            - The Docker daemon will also have cached many of the layers for some
              popular images, like "ubuntu", "debian", but they will be refreshed
              at the time you attempt to use them.
            - If you built an image in a previous build step, it will be stored in
              the host's Docker daemon's cache and is available to use as the name
              for a later build step.
            required: true
            type: str
          args:
            description:
            - A list of arguments that will be presented to the step when it is started.
            - If the image used to run the step's container has an entrypoint, the
              args are used as arguments to that entrypoint. If the image does not
              define an entrypoint, the first element in args is used as the entrypoint,
              and the remainder will be used as arguments.
            required: false
            type: list
          env:
            description:
            - A list of environment variable definitions to be used when running a
              step.
            - The elements are of the form "KEY=VALUE" for the environment variable
              "KEY" being given the value "VALUE".
            required: false
            type: list
          id:
            description:
            - Unique identifier for this build step, used in `wait_for` to reference
              this build step as a dependency.
            required: false
            type: str
          entrypoint:
            description:
            - Entrypoint to be used instead of the build step image's default entrypoint.
            - If unset, the image's default entrypoint is used .
            required: false
            type: str
          dir:
            description:
            - Working directory to use when running this step's container.
            - If this value is a relative path, it is relative to the build's working
              directory. If this value is absolute, it may be outside the build's
              working directory, in which case the contents of the path may not be
              persisted across build step executions, unless a `volume` for that path
              is specified.
            - If the build specifies a `RepoSource` with `dir` and a step with a `dir`,
              which specifies an absolute path, the `RepoSource` `dir` is ignored
              for the step's execution.
            required: false
            type: str
          secret_env:
            description:
            - A list of environment variables which are encrypted using a Cloud Key
              Management Service crypto key. These values must be specified in the
              build's `Secret`.
            required: false
            type: list
          timeout:
            description:
            - Time limit for executing this build step. If not defined, the step has
              no time limit and will be allowed to continue to run until either it
              completes or the build itself times out.
            required: false
            type: str
          timing:
            description:
            - Output only. Stores timing information for executing this build step.
            required: false
            type: str
          volumes:
            description:
            - List of volumes to mount into the build step.
            - Each volume is created as an empty volume prior to execution of the
              build step. Upon completion of the build, volumes and their contents
              are discarded.
            - Using a named volume in only one step is not valid as it is indicative
              of a build request with an incorrect configuration.
            required: false
            type: list
            suboptions:
              name:
                description:
                - Name of the volume to mount.
                - Volume names must be unique per build step and must be valid names
                  for Docker volumes. Each named volume must be used by at least two
                  build steps.
                required: true
                type: str
              path:
                description:
                - Path at which to mount the volume.
                - Paths must be absolute and cannot conflict with other volume paths
                  on the same build step or with certain reserved volume paths.
                required: true
                type: str
          wait_for:
            description:
            - The ID(s) of the step(s) that this build step depends on.
            - This build step will not start until all the build steps in `wait_for`
              have completed successfully. If `wait_for` is empty, this build step
              will start when all previous build steps in the `Build.Steps` list have
              completed successfully.
            required: false
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
- 'API Reference: U(https://cloud.google.com/cloud-build/docs/api/reference/rest/)'
- 'Automating builds using build triggers: U(https://cloud.google.com/cloud-build/docs/running-builds/automate-builds)'
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
- The id for this resource is created by the API after you create the resource the
  first time. If you want to manage this resource after creation, you'll have to copy
  the generated id into the playbook. If you do not, new triggers will be created
  on subsequent runs.
'''

EXAMPLES = '''
- name: create a repository
  google.cloud.gcp_sourcerepo_repository:
    name: projects/{{ gcp_project }}/repos/{{ resource_name }}
    project: "{{ gcp_project }}"
    auth_kind: "{{ gcp_cred_kind }}"
    service_account_file: "{{ gcp_cred_file }}"
    state: present

- name: create a trigger
  google.cloud.gcp_cloudbuild_trigger:
    trigger_template:
      branch_name: master
      project_id: test_project
      repo_name: test_object
    filename: cloudbuild.yaml
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
'''

RETURN = '''
id:
  description:
  - The unique identifier for the trigger.
  returned: success
  type: str
name:
  description:
  - Name of the trigger. Must be unique within the project.
  returned: success
  type: str
description:
  description:
  - Human-readable description of the trigger.
  returned: success
  type: str
disabled:
  description:
  - Whether the trigger is disabled or not. If true, the trigger will never result
    in a build.
  returned: success
  type: bool
createTime:
  description:
  - Time when the trigger was created.
  returned: success
  type: str
substitutions:
  description:
  - Substitutions data for Build resource.
  returned: success
  type: dict
filename:
  description:
  - Path, from the source root, to a file whose contents is used for the template.
    Either a filename or build template must be provided.
  returned: success
  type: str
ignoredFiles:
  description:
  - ignoredFiles and includedFiles are file glob matches using http://godoc/pkg/path/filepath#Match
    extended with support for `**`.
  - If ignoredFiles and changed files are both empty, then they are not used to determine
    whether or not to trigger a build.
  - If ignoredFiles is not empty, then we ignore any files that match any of the ignored_file
    globs. If the change has no files that are outside of the ignoredFiles globs,
    then we do not trigger a build.
  returned: success
  type: list
includedFiles:
  description:
  - ignoredFiles and includedFiles are file glob matches using http://godoc/pkg/path/filepath#Match
    extended with support for `**`.
  - If any of the files altered in the commit pass the ignoredFiles filter and includedFiles
    is empty, then as far as this filter is concerned, we should trigger the build.
  - If any of the files altered in the commit pass the ignoredFiles filter and includedFiles
    is not empty, then we make sure that at least one of those files matches a includedFiles
    glob. If not, then we do not trigger a build.
  returned: success
  type: list
triggerTemplate:
  description:
  - Template describing the types of source changes to trigger a build.
  - Branch and tag names in trigger templates are interpreted as regular expressions.
    Any branch or tag change that matches that regular expression will trigger a build.
  returned: success
  type: complex
  contains:
    projectId:
      description:
      - ID of the project that owns the Cloud Source Repository. If omitted, the project
        ID requesting the build is assumed.
      returned: success
      type: str
    repoName:
      description:
      - Name of the Cloud Source Repository. If omitted, the name "default" is assumed.
      returned: success
      type: str
    dir:
      description:
      - Directory, relative to the source root, in which to run the build.
      - This must be a relative path. If a step's dir is specified and is an absolute
        path, this value is ignored for that step's execution.
      returned: success
      type: str
    branchName:
      description:
      - Name of the branch to build. Exactly one a of branch name, tag, or commit
        SHA must be provided.
      - This field is a regular expression.
      returned: success
      type: str
    tagName:
      description:
      - Name of the tag to build. Exactly one of a branch name, tag, or commit SHA
        must be provided.
      - This field is a regular expression.
      returned: success
      type: str
    commitSha:
      description:
      - Explicit commit SHA to build. Exactly one of a branch name, tag, or commit
        SHA must be provided.
      returned: success
      type: str
build:
  description:
  - Contents of the build template. Either a filename or build template must be provided.
  returned: success
  type: complex
  contains:
    tags:
      description:
      - Tags for annotation of a Build. These are not docker tags.
      returned: success
      type: list
    images:
      description:
      - A list of images to be pushed upon the successful completion of all build
        steps.
      - The images are pushed using the builder service account's credentials.
      - The digests of the pushed images will be stored in the Build resource's results
        field.
      - If any of the images fail to be pushed, the build status is marked FAILURE.
      returned: success
      type: list
    timeout:
      description:
      - Amount of time that this build should be allowed to run, to second granularity.
        If this amount of time elapses, work on the build will cease and the build
        status will be TIMEOUT.
      - This timeout must be equal to or greater than the sum of the timeouts for
        build steps within the build.
      - The expected format is the number of seconds followed by s.
      - Default time is ten minutes (600s).
      returned: success
      type: str
    steps:
      description:
      - The operations to be performed on the workspace.
      returned: success
      type: complex
      contains:
        name:
          description:
          - The name of the container image that will run this particular build step.
          - If the image is available in the host's Docker daemon's cache, it will
            be run directly. If not, the host will attempt to pull the image first,
            using the builder service account's credentials if necessary.
          - The Docker daemon's cache will already have the latest versions of all
            of the officially supported build steps (U(https://github.com/GoogleCloudPlatform/cloud-builders)).
          - The Docker daemon will also have cached many of the layers for some popular
            images, like "ubuntu", "debian", but they will be refreshed at the time
            you attempt to use them.
          - If you built an image in a previous build step, it will be stored in the
            host's Docker daemon's cache and is available to use as the name for a
            later build step.
          returned: success
          type: str
        args:
          description:
          - A list of arguments that will be presented to the step when it is started.
          - If the image used to run the step's container has an entrypoint, the args
            are used as arguments to that entrypoint. If the image does not define
            an entrypoint, the first element in args is used as the entrypoint, and
            the remainder will be used as arguments.
          returned: success
          type: list
        env:
          description:
          - A list of environment variable definitions to be used when running a step.
          - The elements are of the form "KEY=VALUE" for the environment variable
            "KEY" being given the value "VALUE".
          returned: success
          type: list
        id:
          description:
          - Unique identifier for this build step, used in `wait_for` to reference
            this build step as a dependency.
          returned: success
          type: str
        entrypoint:
          description:
          - Entrypoint to be used instead of the build step image's default entrypoint.
          - If unset, the image's default entrypoint is used .
          returned: success
          type: str
        dir:
          description:
          - Working directory to use when running this step's container.
          - If this value is a relative path, it is relative to the build's working
            directory. If this value is absolute, it may be outside the build's working
            directory, in which case the contents of the path may not be persisted
            across build step executions, unless a `volume` for that path is specified.
          - If the build specifies a `RepoSource` with `dir` and a step with a `dir`,
            which specifies an absolute path, the `RepoSource` `dir` is ignored for
            the step's execution.
          returned: success
          type: str
        secretEnv:
          description:
          - A list of environment variables which are encrypted using a Cloud Key
            Management Service crypto key. These values must be specified in the build's
            `Secret`.
          returned: success
          type: list
        timeout:
          description:
          - Time limit for executing this build step. If not defined, the step has
            no time limit and will be allowed to continue to run until either it completes
            or the build itself times out.
          returned: success
          type: str
        timing:
          description:
          - Output only. Stores timing information for executing this build step.
          returned: success
          type: str
        volumes:
          description:
          - List of volumes to mount into the build step.
          - Each volume is created as an empty volume prior to execution of the build
            step. Upon completion of the build, volumes and their contents are discarded.
          - Using a named volume in only one step is not valid as it is indicative
            of a build request with an incorrect configuration.
          returned: success
          type: complex
          contains:
            name:
              description:
              - Name of the volume to mount.
              - Volume names must be unique per build step and must be valid names
                for Docker volumes. Each named volume must be used by at least two
                build steps.
              returned: success
              type: str
            path:
              description:
              - Path at which to mount the volume.
              - Paths must be absolute and cannot conflict with other volume paths
                on the same build step or with certain reserved volume paths.
              returned: success
              type: str
        waitFor:
          description:
          - The ID(s) of the step(s) that this build step depends on.
          - This build step will not start until all the build steps in `wait_for`
            have completed successfully. If `wait_for` is empty, this build step will
            start when all previous build steps in the `Build.Steps` list have completed
            successfully.
          returned: success
          type: list
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

################################################################################
# Main
################################################################################


def main():
    """Main function"""

    module = GcpModule(
        argument_spec=dict(
            state=dict(default='present', choices=['present', 'absent'], type='str'),
            id=dict(type='str'),
            name=dict(type='str'),
            description=dict(type='str'),
            disabled=dict(type='bool'),
            substitutions=dict(type='dict'),
            filename=dict(type='str'),
            ignored_files=dict(type='list', elements='str'),
            included_files=dict(type='list', elements='str'),
            trigger_template=dict(
                type='dict',
                options=dict(
                    project_id=dict(type='str'),
                    repo_name=dict(default='default', type='str'),
                    dir=dict(type='str'),
                    branch_name=dict(type='str'),
                    tag_name=dict(type='str'),
                    commit_sha=dict(type='str'),
                ),
            ),
            build=dict(
                type='dict',
                options=dict(
                    tags=dict(type='list', elements='str'),
                    images=dict(type='list', elements='str'),
                    timeout=dict(default='600s', type='str'),
                    steps=dict(
                        required=True,
                        type='list',
                        elements='dict',
                        options=dict(
                            name=dict(required=True, type='str'),
                            args=dict(type='list', elements='str'),
                            env=dict(type='list', elements='str'),
                            id=dict(type='str'),
                            entrypoint=dict(type='str'),
                            dir=dict(type='str'),
                            secret_env=dict(type='list', elements='str'),
                            timeout=dict(type='str'),
                            timing=dict(type='str'),
                            volumes=dict(
                                type='list', elements='dict', options=dict(name=dict(required=True, type='str'), path=dict(required=True, type='str'))
                            ),
                            wait_for=dict(type='list', elements='str'),
                        ),
                    ),
                ),
            ),
        )
    )

    if not module.params['scopes']:
        module.params['scopes'] = ['https://www.googleapis.com/auth/cloud-platform']

    state = module.params['state']

    fetch = fetch_resource(module, self_link(module))
    changed = False

    if fetch:
        if state == 'present':
            if is_different(module, fetch):
                update(module, self_link(module))
                fetch = fetch_resource(module, self_link(module))
                changed = True
        else:
            delete(module, self_link(module))
            fetch = {}
            changed = True
    else:
        if state == 'present':
            fetch = create(module, collection(module))
            changed = True
        else:
            fetch = {}

    fetch.update({'changed': changed})

    module.exit_json(**fetch)


def create(module, link):
    auth = GcpSession(module, 'cloudbuild')
    return return_if_object(module, auth.post(link, resource_to_request(module)))


def update(module, link):
    auth = GcpSession(module, 'cloudbuild')
    return return_if_object(module, auth.patch(link, resource_to_request(module)))


def delete(module, link):
    auth = GcpSession(module, 'cloudbuild')
    return return_if_object(module, auth.delete(link))


def resource_to_request(module):
    request = {
        u'id': module.params.get('id'),
        u'name': module.params.get('name'),
        u'description': module.params.get('description'),
        u'disabled': module.params.get('disabled'),
        u'substitutions': module.params.get('substitutions'),
        u'filename': module.params.get('filename'),
        u'ignoredFiles': module.params.get('ignored_files'),
        u'includedFiles': module.params.get('included_files'),
        u'triggerTemplate': TriggerTriggertemplate(module.params.get('trigger_template', {}), module).to_request(),
        u'build': TriggerBuild(module.params.get('build', {}), module).to_request(),
    }
    return_vals = {}
    for k, v in request.items():
        if v or v is False:
            return_vals[k] = v

    return return_vals


def fetch_resource(module, link, allow_not_found=True):
    auth = GcpSession(module, 'cloudbuild')
    return return_if_object(module, auth.get(link), allow_not_found)


def self_link(module):
    return "https://cloudbuild.googleapis.com/v1/projects/{project}/triggers/{id}".format(**module.params)


def collection(module):
    return "https://cloudbuild.googleapis.com/v1/projects/{project}/triggers".format(**module.params)


def return_if_object(module, response, allow_not_found=False):
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
        u'id': response.get(u'id'),
        u'name': response.get(u'name'),
        u'description': response.get(u'description'),
        u'disabled': response.get(u'disabled'),
        u'createTime': response.get(u'createTime'),
        u'substitutions': response.get(u'substitutions'),
        u'filename': response.get(u'filename'),
        u'ignoredFiles': response.get(u'ignoredFiles'),
        u'includedFiles': response.get(u'includedFiles'),
        u'triggerTemplate': TriggerTriggertemplate(response.get(u'triggerTemplate', {}), module).from_response(),
        u'build': TriggerBuild(response.get(u'build', {}), module).from_response(),
    }


class TriggerTriggertemplate(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = {}

    def to_request(self):
        return remove_nones_from_dict(
            {
                u'projectId': self.request.get('project_id'),
                u'repoName': self.request.get('repo_name'),
                u'dir': self.request.get('dir'),
                u'branchName': self.request.get('branch_name'),
                u'tagName': self.request.get('tag_name'),
                u'commitSha': self.request.get('commit_sha'),
            }
        )

    def from_response(self):
        return remove_nones_from_dict(
            {
                u'projectId': self.request.get(u'projectId'),
                u'repoName': self.request.get(u'repoName'),
                u'dir': self.request.get(u'dir'),
                u'branchName': self.request.get(u'branchName'),
                u'tagName': self.request.get(u'tagName'),
                u'commitSha': self.request.get(u'commitSha'),
            }
        )


class TriggerBuild(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = {}

    def to_request(self):
        return remove_nones_from_dict(
            {
                u'tags': self.request.get('tags'),
                u'images': self.request.get('images'),
                u'timeout': self.request.get('timeout'),
                u'steps': TriggerStepsArray(self.request.get('steps', []), self.module).to_request(),
            }
        )

    def from_response(self):
        return remove_nones_from_dict(
            {
                u'tags': self.request.get(u'tags'),
                u'images': self.request.get(u'images'),
                u'timeout': self.request.get(u'timeout'),
                u'steps': TriggerStepsArray(self.request.get(u'steps', []), self.module).from_response(),
            }
        )


class TriggerStepsArray(object):
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
                u'name': item.get('name'),
                u'args': item.get('args'),
                u'env': item.get('env'),
                u'id': item.get('id'),
                u'entrypoint': item.get('entrypoint'),
                u'dir': item.get('dir'),
                u'secretEnv': item.get('secret_env'),
                u'timeout': item.get('timeout'),
                u'timing': item.get('timing'),
                u'volumes': TriggerVolumesArray(item.get('volumes', []), self.module).to_request(),
                u'waitFor': item.get('wait_for'),
            }
        )

    def _response_from_item(self, item):
        return remove_nones_from_dict(
            {
                u'name': item.get(u'name'),
                u'args': item.get(u'args'),
                u'env': item.get(u'env'),
                u'id': item.get(u'id'),
                u'entrypoint': item.get(u'entrypoint'),
                u'dir': item.get(u'dir'),
                u'secretEnv': item.get(u'secretEnv'),
                u'timeout': item.get(u'timeout'),
                u'timing': item.get(u'timing'),
                u'volumes': TriggerVolumesArray(item.get(u'volumes', []), self.module).from_response(),
                u'waitFor': item.get(u'waitFor'),
            }
        )


class TriggerVolumesArray(object):
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
        return remove_nones_from_dict({u'name': item.get('name'), u'path': item.get('path')})

    def _response_from_item(self, item):
        return remove_nones_from_dict({u'name': item.get(u'name'), u'path': item.get(u'path')})


if __name__ == '__main__':
    main()
