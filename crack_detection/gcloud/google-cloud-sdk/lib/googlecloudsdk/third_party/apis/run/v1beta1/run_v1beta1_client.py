"""Generated client library for run version v1beta1."""
# NOTE: This file is autogenerated and should not be edited by hand.
from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.run.v1beta1 import run_v1beta1_messages as messages


class RunV1beta1(base_api.BaseApiClient):
  """Generated client library for service run version v1beta1."""

  MESSAGES_MODULE = messages
  BASE_URL = u'https://run.googleapis.com/'
  MTLS_BASE_URL = u''

  _PACKAGE = u'run'
  _SCOPES = [u'https://www.googleapis.com/auth/cloud-platform']
  _VERSION = u'v1beta1'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = u'google-cloud-sdk'
  _CLIENT_CLASS_NAME = u'RunV1beta1'
  _URL_VERSION = u'v1beta1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new run handle."""
    url = url or self.BASE_URL
    super(RunV1beta1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.customresourcedefinitions = self.CustomresourcedefinitionsService(self)
    self.projects_locations_customresourcedefinitions = self.ProjectsLocationsCustomresourcedefinitionsService(self)
    self.projects_locations = self.ProjectsLocationsService(self)
    self.projects = self.ProjectsService(self)

  class CustomresourcedefinitionsService(base_api.BaseApiService):
    """Service class for the customresourcedefinitions resource."""

    _NAME = u'customresourcedefinitions'

    def __init__(self, client):
      super(RunV1beta1.CustomresourcedefinitionsService, self).__init__(client)
      self._upload_configs = {
          }

    def List(self, request, global_params=None):
      r"""Rpc to list custom resource definitions.

      Args:
        request: (RunCustomresourcedefinitionsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListCustomResourceDefinitionsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'run.customresourcedefinitions.list',
        ordered_params=[],
        path_params=[],
        query_params=[u'continue_', u'fieldSelector', u'includeUninitialized', u'labelSelector', u'limit', u'parent', u'resourceVersion', u'watch'],
        relative_path=u'apis/apiextensions.k8s.io/v1beta1/customresourcedefinitions',
        request_field='',
        request_type_name=u'RunCustomresourcedefinitionsListRequest',
        response_type_name=u'ListCustomResourceDefinitionsResponse',
        supports_download=False,
    )

  class ProjectsLocationsCustomresourcedefinitionsService(base_api.BaseApiService):
    """Service class for the projects_locations_customresourcedefinitions resource."""

    _NAME = u'projects_locations_customresourcedefinitions'

    def __init__(self, client):
      super(RunV1beta1.ProjectsLocationsCustomresourcedefinitionsService, self).__init__(client)
      self._upload_configs = {
          }

    def List(self, request, global_params=None):
      r"""Rpc to list custom resource definitions.

      Args:
        request: (RunProjectsLocationsCustomresourcedefinitionsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListCustomResourceDefinitionsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/locations/{locationsId}/customresourcedefinitions',
        http_method=u'GET',
        method_id=u'run.projects.locations.customresourcedefinitions.list',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'continue_', u'fieldSelector', u'includeUninitialized', u'labelSelector', u'limit', u'resourceVersion', u'watch'],
        relative_path=u'v1beta1/{+parent}/customresourcedefinitions',
        request_field='',
        request_type_name=u'RunProjectsLocationsCustomresourcedefinitionsListRequest',
        response_type_name=u'ListCustomResourceDefinitionsResponse',
        supports_download=False,
    )

  class ProjectsLocationsService(base_api.BaseApiService):
    """Service class for the projects_locations resource."""

    _NAME = u'projects_locations'

    def __init__(self, client):
      super(RunV1beta1.ProjectsLocationsService, self).__init__(client)
      self._upload_configs = {
          }

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = u'projects'

    def __init__(self, client):
      super(RunV1beta1.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }
