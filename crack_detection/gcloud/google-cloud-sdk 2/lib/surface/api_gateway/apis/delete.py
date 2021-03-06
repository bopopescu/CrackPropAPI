# -*- coding: utf-8 -*- #
# Copyright 2020 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""`gcloud api-gateway apis delete` command."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.api_lib.api_gateway import apis
from googlecloudsdk.api_lib.api_gateway import operations
from googlecloudsdk.api_lib.endpoints import services_util as endpoints
from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.api_gateway import common_flags
from googlecloudsdk.command_lib.api_gateway import operations_util
from googlecloudsdk.command_lib.api_gateway import resource_args
from googlecloudsdk.core.console import console_io


@base.ReleaseTracks(base.ReleaseTrack.ALPHA)
class Delete(base.DeleteCommand):
  """Deletes an API."""

  @staticmethod
  def Args(parser):
    """Args is called by calliope to gather arguments for this command.

    Args:
      parser: An argparse parser that you can use to add arguments that go
          on the command line after this command. Positional arguments are
          allowed.
    """
    base.ASYNC_FLAG.AddToParser(parser)
    resource_args.AddApiResourceArg(parser, 'will be deleted', positional=True)

  def Run(self, args):
    """Run 'api-gateway apis delete'.

    Args:
      args: argparse.Namespace, The arguments that this command was invoked
          with.

    Returns:
      The response from the Delete API call (or None if cancelled).
    """

    api_ref = args.CONCEPTS.api.Parse()
    service_name = common_flags.ProcessApiRefToEndpointsService(api_ref)

    # Prompt with a warning before continuing.
    console_io.PromptContinue(
        message='Are you sure? This will delete the API \'{}\', '
        'along with all of the associated consumer '
        'information.'.format(api_ref.RelativeName()),
        prompt_string='Continue anyway',
        default=True,
        throw_if_unattended=True,
        cancel_on_no=True)

    self.__DeleteEndpointsService(service_name)
    resp = apis.ApiClient().Delete(api_ref)

    wait = 'Waiting for API [{}] to be deleted'.format(
        api_ref.Name())

    return operations_util.PrintOperationResult(
        resp.name, operations.OperationsClient(), wait_string=wait,
        is_async=args.async_)

  def __DeleteEndpointsService(self, service_name):
    messages = endpoints.GetMessagesModule()
    client = endpoints.GetClientInstance()

    request = messages.ServicemanagementServicesDeleteRequest(
        serviceName=service_name)
    operation = client.services.Delete(request)

    return endpoints.ProcessOperationResult(operation, False)
