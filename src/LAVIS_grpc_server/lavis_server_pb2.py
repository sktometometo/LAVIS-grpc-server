# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: lavis-server.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12lavis-server.proto\"L\n\x05Image\x12\r\n\x05width\x18\x01 \x01(\r\x12\x0e\n\x06height\x18\x02 \x01(\r\x12\x10\n\x08\x65ncoding\x18\x03 \x01(\r\x12\x12\n\nimage_data\x18\x04 \x01(\x0c\"/\n\x16ImageCaptioningRequest\x12\x15\n\x05image\x18\x01 \x01(\x0b\x32\x06.Image\"*\n\x17ImageCaptioningResponse\x12\x0f\n\x07\x63\x61ption\x18\x01 \x01(\t\">\n\x17TextLocalizationRequest\x12\x15\n\x05image\x18\x01 \x01(\x0b\x32\x06.Image\x12\x0c\n\x04text\x18\x02 \x01(\t\"3\n\x18TextLocalizationResponse\x12\x17\n\x07heatmap\x18\x01 \x01(\x0b\x32\x06.Image\"D\n\x1bInstructedGenerationRequest\x12\x15\n\x05image\x18\x01 \x01(\x0b\x32\x06.Image\x12\x0e\n\x06prompt\x18\x02 \x01(\t\"0\n\x1cInstructedGenerationResponse\x12\x10\n\x08response\x18\x01 \x01(\t2\xf7\x01\n\x0bLAVISServer\x12\x46\n\x0fImageCaptioning\x12\x17.ImageCaptioningRequest\x1a\x18.ImageCaptioningResponse\"\x00\x12I\n\x10TextLocalization\x12\x18.TextLocalizationRequest\x1a\x19.TextLocalizationResponse\"\x00\x12U\n\x14InstructedGeneration\x12\x1c.InstructedGenerationRequest\x1a\x1d.InstructedGenerationResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'lavis_server_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _IMAGE._serialized_start=22
  _IMAGE._serialized_end=98
  _IMAGECAPTIONINGREQUEST._serialized_start=100
  _IMAGECAPTIONINGREQUEST._serialized_end=147
  _IMAGECAPTIONINGRESPONSE._serialized_start=149
  _IMAGECAPTIONINGRESPONSE._serialized_end=191
  _TEXTLOCALIZATIONREQUEST._serialized_start=193
  _TEXTLOCALIZATIONREQUEST._serialized_end=255
  _TEXTLOCALIZATIONRESPONSE._serialized_start=257
  _TEXTLOCALIZATIONRESPONSE._serialized_end=308
  _INSTRUCTEDGENERATIONREQUEST._serialized_start=310
  _INSTRUCTEDGENERATIONREQUEST._serialized_end=378
  _INSTRUCTEDGENERATIONRESPONSE._serialized_start=380
  _INSTRUCTEDGENERATIONRESPONSE._serialized_end=428
  _LAVISSERVER._serialized_start=431
  _LAVISSERVER._serialized_end=678
# @@protoc_insertion_point(module_scope)
