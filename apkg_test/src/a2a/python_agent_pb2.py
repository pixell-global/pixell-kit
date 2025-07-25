# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: python_agent.proto
# Protobuf Python Version: 6.31.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    6,
    31,
    0,
    '',
    'python_agent.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12python_agent.proto\x12\x13pixell.python_agent\"\x87\x02\n\x0e\x45xecuteRequest\x12\x0c\n\x04\x63ode\x18\x01 \x01(\t\x12\x41\n\x07\x63ontext\x18\x02 \x03(\x0b\x32\x30.pixell.python_agent.ExecuteRequest.ContextEntry\x12\r\n\x05\x66iles\x18\x03 \x03(\x0c\x12\x12\n\nsession_id\x18\x04 \x01(\t\x12\x38\n\rresource_tier\x18\x05 \x01(\x0e\x32!.pixell.python_agent.ResourceTier\x12\x17\n\x0ftimeout_seconds\x18\x06 \x01(\x05\x1a.\n\x0c\x43ontextEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01\"\xfd\x01\n\x0f\x45xecuteResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0e\n\x06stdout\x18\x02 \x01(\t\x12\x0e\n\x06stderr\x18\x03 \x01(\t\x12\x42\n\x07results\x18\x04 \x03(\x0b\x32\x31.pixell.python_agent.ExecuteResponse.ResultsEntry\x12\r\n\x05\x65rror\x18\x05 \x01(\t\x12\x36\n\x07metrics\x18\x06 \x01(\x0b\x32%.pixell.python_agent.ExecutionMetrics\x1a.\n\x0cResultsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01\"\xb2\x01\n\x0bStreamChunk\x12\x38\n\x04type\x18\x01 \x01(\x0e\x32*.pixell.python_agent.StreamChunk.ChunkType\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\x12\x11\n\ttimestamp\x18\x03 \x01(\x03\"H\n\tChunkType\x12\n\n\x06STDOUT\x10\x00\x12\n\n\x06STDERR\x10\x01\x12\n\n\x06RESULT\x10\x02\x12\x0c\n\x08PROGRESS\x10\x03\x12\t\n\x05\x45RROR\x10\x04\")\n\x13SessionStateRequest\x12\x12\n\nsession_id\x18\x01 \x01(\t\"\xc0\x01\n\x14SessionStateResponse\x12K\n\tvariables\x18\x01 \x03(\x0b\x32\x38.pixell.python_agent.SessionStateResponse.VariablesEntry\x12\x12\n\ncreated_at\x18\x02 \x01(\x03\x12\x15\n\rlast_accessed\x18\x03 \x01(\x03\x1a\x30\n\x0eVariablesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01\"Q\n\x0cRetryRequest\x12\x12\n\nsession_id\x18\x01 \x01(\t\x12-\n\x05patch\x18\x02 \x01(\x0b\x32\x1e.pixell.python_agent.CodePatch\"\x88\x01\n\tCodePatch\x12\x36\n\x05\x65\x64its\x18\x01 \x03(\x0b\x32\'.pixell.python_agent.CodePatch.LineEdit\x1a\x43\n\x08LineEdit\x12\x13\n\x0bline_number\x18\x01 \x01(\x05\x12\x10\n\x08old_line\x18\x02 \x01(\t\x12\x10\n\x08new_line\x18\x03 \x01(\t\"]\n\x10\x45xecutionMetrics\x12\x19\n\x11\x65xecution_time_ms\x18\x01 \x01(\x03\x12\x19\n\x11memory_used_bytes\x18\x02 \x01(\x03\x12\x13\n\x0b\x63pu_percent\x18\x03 \x01(\x05*0\n\x0cResourceTier\x12\t\n\x05SMALL\x10\x00\x12\n\n\x06MEDIUM\x10\x01\x12\t\n\x05LARGE\x10\x02\x32\x80\x03\n\x0bPythonAgent\x12T\n\x07\x45xecute\x12#.pixell.python_agent.ExecuteRequest\x1a$.pixell.python_agent.ExecuteResponse\x12X\n\rStreamExecute\x12#.pixell.python_agent.ExecuteRequest\x1a .pixell.python_agent.StreamChunk0\x01\x12\x66\n\x0fGetSessionState\x12(.pixell.python_agent.SessionStateRequest\x1a).pixell.python_agent.SessionStateResponse\x12Y\n\x0eRetryWithPatch\x12!.pixell.python_agent.RetryRequest\x1a$.pixell.python_agent.ExecuteResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'python_agent_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_EXECUTEREQUEST_CONTEXTENTRY']._loaded_options = None
  _globals['_EXECUTEREQUEST_CONTEXTENTRY']._serialized_options = b'8\001'
  _globals['_EXECUTERESPONSE_RESULTSENTRY']._loaded_options = None
  _globals['_EXECUTERESPONSE_RESULTSENTRY']._serialized_options = b'8\001'
  _globals['_SESSIONSTATERESPONSE_VARIABLESENTRY']._loaded_options = None
  _globals['_SESSIONSTATERESPONSE_VARIABLESENTRY']._serialized_options = b'8\001'
  _globals['_RESOURCETIER']._serialized_start=1301
  _globals['_RESOURCETIER']._serialized_end=1349
  _globals['_EXECUTEREQUEST']._serialized_start=44
  _globals['_EXECUTEREQUEST']._serialized_end=307
  _globals['_EXECUTEREQUEST_CONTEXTENTRY']._serialized_start=261
  _globals['_EXECUTEREQUEST_CONTEXTENTRY']._serialized_end=307
  _globals['_EXECUTERESPONSE']._serialized_start=310
  _globals['_EXECUTERESPONSE']._serialized_end=563
  _globals['_EXECUTERESPONSE_RESULTSENTRY']._serialized_start=517
  _globals['_EXECUTERESPONSE_RESULTSENTRY']._serialized_end=563
  _globals['_STREAMCHUNK']._serialized_start=566
  _globals['_STREAMCHUNK']._serialized_end=744
  _globals['_STREAMCHUNK_CHUNKTYPE']._serialized_start=672
  _globals['_STREAMCHUNK_CHUNKTYPE']._serialized_end=744
  _globals['_SESSIONSTATEREQUEST']._serialized_start=746
  _globals['_SESSIONSTATEREQUEST']._serialized_end=787
  _globals['_SESSIONSTATERESPONSE']._serialized_start=790
  _globals['_SESSIONSTATERESPONSE']._serialized_end=982
  _globals['_SESSIONSTATERESPONSE_VARIABLESENTRY']._serialized_start=934
  _globals['_SESSIONSTATERESPONSE_VARIABLESENTRY']._serialized_end=982
  _globals['_RETRYREQUEST']._serialized_start=984
  _globals['_RETRYREQUEST']._serialized_end=1065
  _globals['_CODEPATCH']._serialized_start=1068
  _globals['_CODEPATCH']._serialized_end=1204
  _globals['_CODEPATCH_LINEEDIT']._serialized_start=1137
  _globals['_CODEPATCH_LINEEDIT']._serialized_end=1204
  _globals['_EXECUTIONMETRICS']._serialized_start=1206
  _globals['_EXECUTIONMETRICS']._serialized_end=1299
  _globals['_PYTHONAGENT']._serialized_start=1352
  _globals['_PYTHONAGENT']._serialized_end=1736
# @@protoc_insertion_point(module_scope)
