# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class ActivityLogsOperations:
    """ActivityLogsOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~$(python-base-namespace).v2015_04_01.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def list(
        self,
        filter: str,
        select: Optional[str] = None,
        **kwargs
    ) -> "models.EventDataCollection":
        """Provides the list of records from the activity logs.

        :param filter: Reduces the set of data collected.:code:`<br>`This argument is required and it
     also requires at least the start date/time.:code:`<br>`The **$filter** argument is very
     restricted and allows only the following patterns.:code:`<br>`- *List events for a resource
     group*\ : $filter=eventTimestamp ge '2014-07-16T04:36:37.6407898Z' and eventTimestamp le
     '2014-07-20T04:36:37.6407898Z' and resourceGroupName eq 'resourceGroupName'.:code:`<br>`- *List
     events for resource*\ : $filter=eventTimestamp ge '2014-07-16T04:36:37.6407898Z' and
     eventTimestamp le '2014-07-20T04:36:37.6407898Z' and resourceUri eq 'resourceURI'.:code:`<br>`-
     *List events for a subscription in a time range*\ : $filter=eventTimestamp ge
     '2014-07-16T04:36:37.6407898Z' and eventTimestamp le
     '2014-07-20T04:36:37.6407898Z'.:code:`<br>`- *List events for a resource provider*\ :
     $filter=eventTimestamp ge '2014-07-16T04:36:37.6407898Z' and eventTimestamp le
     '2014-07-20T04:36:37.6407898Z' and resourceProvider eq 'resourceProviderName'.:code:`<br>`-
     *List events for a correlation Id*\ : $filter=eventTimestamp ge '2014-07-16T04:36:37.6407898Z'
     and eventTimestamp le '2014-07-20T04:36:37.6407898Z' and correlationId eq
     'correlationID'.:code:`<br>`:code:`<br>`\ **NOTE**\ : No other syntax is allowed.
        :type filter: str
        :param select: Used to fetch events with only the given properties.:code:`<br>`The **$select**
     argument is a comma separated list of property names to be returned. Possible values are:
     *authorization*\ , *claims*\ , *correlationId*\ , *description*\ , *eventDataId*\ ,
     *eventName*\ , *eventTimestamp*\ , *httpRequest*\ , *level*\ , *operationId*\ ,
     *operationName*\ , *properties*\ , *resourceGroupName*\ , *resourceProviderName*\ ,
     *resourceId*\ , *status*\ , *submissionTimestamp*\ , *subStatus*\ , *subscriptionId*.
        :type select: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: EventDataCollection or the result of cls(response)
        :rtype: ~$(python-base-namespace).v2015_04_01.models.EventDataCollection
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.EventDataCollection"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "2015-04-01"

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list.metadata['url']
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
            else:
                url = next_link

            # Construct parameters
            query_parameters = {}  # type: Dict[str, Any]
            query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')
            query_parameters['$filter'] = self._serialize.query("filter", filter, 'str')
            if select is not None:
                query_parameters['$select'] = self._serialize.query("select", select, 'str')

            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = 'application/json'

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize('EventDataCollection', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._deserialize(models.ErrorResponse, response)
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': '/subscriptions/{subscriptionId}/providers/microsoft.insights/eventtypes/management/values'}