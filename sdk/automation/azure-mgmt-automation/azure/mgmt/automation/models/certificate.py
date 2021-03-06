# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .proxy_resource import ProxyResource


class Certificate(ProxyResource):
    """Definition of the certificate.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Fully qualified resource Id for the resource
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource.
    :vartype type: str
    :ivar thumbprint: Gets the thumbprint of the certificate.
    :vartype thumbprint: str
    :ivar expiry_time: Gets the expiry time of the certificate.
    :vartype expiry_time: datetime
    :ivar is_exportable: Gets the is exportable flag of the certificate.
    :vartype is_exportable: bool
    :ivar creation_time: Gets the creation time.
    :vartype creation_time: datetime
    :ivar last_modified_time: Gets the last modified time.
    :vartype last_modified_time: datetime
    :param description: Gets or sets the description.
    :type description: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'thumbprint': {'readonly': True},
        'expiry_time': {'readonly': True},
        'is_exportable': {'readonly': True},
        'creation_time': {'readonly': True},
        'last_modified_time': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'thumbprint': {'key': 'properties.thumbprint', 'type': 'str'},
        'expiry_time': {'key': 'properties.expiryTime', 'type': 'iso-8601'},
        'is_exportable': {'key': 'properties.isExportable', 'type': 'bool'},
        'creation_time': {'key': 'properties.creationTime', 'type': 'iso-8601'},
        'last_modified_time': {'key': 'properties.lastModifiedTime', 'type': 'iso-8601'},
        'description': {'key': 'properties.description', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Certificate, self).__init__(**kwargs)
        self.thumbprint = None
        self.expiry_time = None
        self.is_exportable = None
        self.creation_time = None
        self.last_modified_time = None
        self.description = kwargs.get('description', None)
