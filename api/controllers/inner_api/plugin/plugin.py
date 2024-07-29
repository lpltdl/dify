import time
from collections.abc import Generator

from flask_restful import Resource, reqparse

from controllers.console.setup import setup_required
from controllers.inner_api import api
from controllers.inner_api.plugin.wraps import get_tenant, plugin_data
from controllers.inner_api.wraps import plugin_inner_api_only
from core.plugin.backwards_invocation.model import PluginBackwardsInvocation
from core.plugin.entities.request import (
    RequestInvokeLLM,
    RequestInvokeModeration,
    RequestInvokeRerank,
    RequestInvokeSpeech2Text,
    RequestInvokeTextEmbedding,
    RequestInvokeTool,
    RequestInvokeTTS,
)
from core.tools.entities.tool_entities import ToolInvokeMessage
from libs.helper import compact_generate_response
from models.account import Tenant


class PluginInvokeLLMApi(Resource):
    @setup_required
    @plugin_inner_api_only
    @get_tenant
    @plugin_data(payload_type=RequestInvokeLLM)
    def post(self, user_id: str, tenant_model: Tenant, payload: RequestInvokeLLM):
        def generator():
            response = PluginBackwardsInvocation.invoke_llm(user_id, tenant_model, payload)
            if isinstance(response, Generator):
                for chunk in response:
                    yield chunk.model_dump_json().encode() + b'\n\n'
            else:
                yield response.model_dump_json().encode() + b'\n\n'

        return compact_generate_response(generator())


class PluginInvokeTextEmbeddingApi(Resource):
    @setup_required
    @plugin_inner_api_only
    @get_tenant
    @plugin_data(payload_type=RequestInvokeTextEmbedding)
    def post(self, user_id: str, tenant_model: Tenant, payload: RequestInvokeTextEmbedding):
        pass


class PluginInvokeRerankApi(Resource):
    @setup_required
    @plugin_inner_api_only
    @get_tenant
    @plugin_data(payload_type=RequestInvokeRerank)
    def post(self, user_id: str, tenant_model: Tenant, payload: RequestInvokeRerank):
        pass


class PluginInvokeTTSApi(Resource):
    @setup_required
    @plugin_inner_api_only
    @get_tenant
    @plugin_data(payload_type=RequestInvokeTTS)
    def post(self, user_id: str, tenant_model: Tenant, payload: RequestInvokeTTS):
        pass


class PluginInvokeSpeech2TextApi(Resource):
    @setup_required
    @plugin_inner_api_only
    @get_tenant
    @plugin_data(payload_type=RequestInvokeSpeech2Text)
    def post(self, user_id: str, tenant_model: Tenant, payload: RequestInvokeSpeech2Text):
        pass


class PluginInvokeModerationApi(Resource):
    @setup_required
    @plugin_inner_api_only
    @get_tenant
    @plugin_data(payload_type=RequestInvokeModeration)
    def post(self, user_id: str, tenant_model: Tenant, payload: RequestInvokeModeration):
        pass


class PluginInvokeToolApi(Resource):
    @setup_required
    @plugin_inner_api_only
    @get_tenant
    @plugin_data(payload_type=RequestInvokeTool)
    def post(self, user_id: str, tenant_model: Tenant, payload: RequestInvokeTool):
        def generator():
            for i in range(10):
                time.sleep(0.1)
                yield (
                    ToolInvokeMessage(
                        type=ToolInvokeMessage.MessageType.TEXT,
                        message=ToolInvokeMessage.TextMessage(text='helloworld'),
                    )
                    .model_dump_json()
                    .encode()
                    + b'\n\n'
                )

        return compact_generate_response(generator())


class PluginInvokeNodeApi(Resource):
    @setup_required
    @plugin_inner_api_only
    @get_tenant
    def post(self, user_id: str, tenant_model: Tenant):
        parser = reqparse.RequestParser()
        args = parser.parse_args()

        return {'message': 'success'}


api.add_resource(PluginInvokeLLMApi, '/invoke/llm')
api.add_resource(PluginInvokeTextEmbeddingApi, '/invoke/text-embedding')
api.add_resource(PluginInvokeRerankApi, '/invoke/rerank')
api.add_resource(PluginInvokeTTSApi, '/invoke/tts')
api.add_resource(PluginInvokeSpeech2TextApi, '/invoke/speech2text')
api.add_resource(PluginInvokeModerationApi, '/invoke/moderation')
api.add_resource(PluginInvokeToolApi, '/invoke/tool')
api.add_resource(PluginInvokeNodeApi, '/invoke/node')
