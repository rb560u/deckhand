# Copyright 2017 AT&T Intellectual Property.  All other rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import copy
import yaml

import falcon

from oslo_db import exception as db_exc
from oslo_log import log as logging
from oslo_serialization import jsonutils as json

from deckhand.control import base as api_base
from deckhand.db.sqlalchemy import api as db_api
from deckhand.engine import document_validation
from deckhand import errors as deckhand_errors

LOG = logging.getLogger(__name__)


class RevisionsResource(api_base.BaseResource):
    """API resource for realizing CRUD endpoints for Document Revisions."""

    def on_get(self, req, resp, revision_id):
        """Returns all documents for a `revision_id`.
        
        Returns a multi-document YAML response containing all the documents
        matching the filters specified via query string parameters. Returned
        documents will be as originally posted with no substitutions or
        layering applied.
        """
        revision = db_api.revision_get(revision_id)
        resp.status = falcon.HTTP_201
        resp.body = revision['documents']
