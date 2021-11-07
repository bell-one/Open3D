# ----------------------------------------------------------------------------
# -                        Open3D: www.open3d.org                            -
# ----------------------------------------------------------------------------
# The MIT License (MIT)
#
# Copyright (c) 2018-2021 www.open3d.org
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
# ----------------------------------------------------------------------------
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: plugin_data.proto

import sys
_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor.FileDescriptor(
    name='plugin_data.proto',
    package='tensorboard.open3d',
    syntax='proto3',
    serialized_options=None,
    serialized_pb=_b(
        '\n\x11plugin_data.proto\x12\x12tensorboard.open3d\"\xb2\r\n\x10Open3DPluginData\x12\x0f\n\x07version\x18\x01 \x01(\x05\x12S\n\x13property_references\x18\x02 \x03(\x0b\x32\x36.tensorboard.open3d.Open3DPluginData.PropertyReference\x12\x44\n\x0b\x62\x61tch_index\x18\x03 \x01(\x0b\x32/.tensorboard.open3d.Open3DPluginData.BatchIndex\x1aw\n\x11PropertyReference\x12P\n\x11geometry_property\x18\x01 \x01(\x0e\x32\x35.tensorboard.open3d.Open3DPluginData.GeometryProperty\x12\x10\n\x08step_ref\x18\x02 \x01(\x04\x1a\x7f\n\tStartSize\x12\r\n\x05start\x18\x01 \x01(\x04\x12\x0c\n\x04size\x18\x02 \x01(\x04\x12\x15\n\rmasked_crc32c\x18\x03 \x01(\r\x12\x11\n\taux_start\x18\x04 \x01(\x04\x12\x10\n\x08\x61ux_size\x18\x05 \x01(\x04\x12\x19\n\x11\x61ux_masked_crc32c\x18\x06 \x01(\r\x1a\x62\n\nBatchIndex\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\x12\x42\n\nstart_size\x18\x02 \x03(\x0b\x32..tensorboard.open3d.Open3DPluginData.StartSize\"\x93\t\n\x10GeometryProperty\x12\x14\n\x10vertex_positions\x10\x00\x12\x12\n\x0evertex_normals\x10\x01\x12\x11\n\rvertex_colors\x10\x02\x12\x16\n\x12vertex_texture_uvs\x10\x03\x12\x14\n\x10triangle_indices\x10\x04\x12\x13\n\x0ftriangle_colors\x10\x05\x12\x14\n\x10triangle_normals\x10\x06\x12\x18\n\x14triangle_texture_uvs\x10\x07\x12\x10\n\x0cline_indices\x10\x08\x12\x0f\n\x0bline_colors\x10\t\x12\x1c\n\x18material_scalar_metallic\x10@\x12\x1d\n\x19material_scalar_roughness\x10\x41\x12\x1f\n\x1bmaterial_scalar_reflectance\x10\x42\x12\x1e\n\x1amaterial_scalar_clear_coat\x10\x44\x12(\n$material_scalar_clear_coat_roughness\x10\x45\x12\x1e\n\x1amaterial_scalar_anisotropy\x10\x46\x12%\n!material_scalar_ambient_occlusion\x10G\x12 \n\x1cmaterial_scalar_transmission\x10I\x12\x1d\n\x19material_scalar_thickness\x10K\x12\'\n#material_scalar_absorption_distance\x10L\x12\x1e\n\x1amaterial_vector_base_color\x10P\x12\x1a\n\x16material_vector_normal\x10S\x12$\n material_vector_absorption_color\x10X\x12!\n\x1dmaterial_texture_map_metallic\x10`\x12\"\n\x1ematerial_texture_map_roughness\x10\x61\x12$\n material_texture_map_reflectance\x10\x62\x12#\n\x1fmaterial_texture_map_clear_coat\x10\x64\x12-\n)material_texture_map_clear_coat_roughness\x10\x65\x12#\n\x1fmaterial_texture_map_anisotropy\x10\x66\x12*\n&material_texture_map_ambient_occlusion\x10g\x12%\n!material_texture_map_transmission\x10i\x12\"\n\x1ematerial_texture_map_thickness\x10k\x12\x1f\n\x1bmaterial_texture_map_albedo\x10l\x12\x1f\n\x1bmaterial_texture_map_normal\x10o\x12)\n%material_texture_map_absorption_color\x10t\x12\'\n#material_texture_map_ao_rough_metal\x10u\"\x92\x01\n\rInferenceData\x12K\n\x10inference_result\x18\x01 \x03(\x0b\x32\x31.tensorboard.open3d.InferenceData.InferenceResult\x1a\x34\n\x0fInferenceResult\x12\r\n\x05label\x18\x01 \x01(\r\x12\x12\n\nconfidence\x18\x02 \x01(\x02\"\x8f\x01\n\x0cLabelToNames\x12J\n\x0elabel_to_names\x18\x01 \x03(\x0b\x32\x32.tensorboard.open3d.LabelToNames.LabelToNamesEntry\x1a\x33\n\x11LabelToNamesEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x62\x06proto3'
    ))

_OPEN3DPLUGINDATA_GEOMETRYPROPERTY = _descriptor.EnumDescriptor(
    name='GeometryProperty',
    full_name='tensorboard.open3d.Open3DPluginData.GeometryProperty',
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(name='vertex_positions',
                                        index=0,
                                        number=0,
                                        serialized_options=None,
                                        type=None),
        _descriptor.EnumValueDescriptor(name='vertex_normals',
                                        index=1,
                                        number=1,
                                        serialized_options=None,
                                        type=None),
        _descriptor.EnumValueDescriptor(name='vertex_colors',
                                        index=2,
                                        number=2,
                                        serialized_options=None,
                                        type=None),
        _descriptor.EnumValueDescriptor(name='vertex_texture_uvs',
                                        index=3,
                                        number=3,
                                        serialized_options=None,
                                        type=None),
        _descriptor.EnumValueDescriptor(name='triangle_indices',
                                        index=4,
                                        number=4,
                                        serialized_options=None,
                                        type=None),
        _descriptor.EnumValueDescriptor(name='triangle_colors',
                                        index=5,
                                        number=5,
                                        serialized_options=None,
                                        type=None),
        _descriptor.EnumValueDescriptor(name='triangle_normals',
                                        index=6,
                                        number=6,
                                        serialized_options=None,
                                        type=None),
        _descriptor.EnumValueDescriptor(name='triangle_texture_uvs',
                                        index=7,
                                        number=7,
                                        serialized_options=None,
                                        type=None),
        _descriptor.EnumValueDescriptor(name='line_indices',
                                        index=8,
                                        number=8,
                                        serialized_options=None,
                                        type=None),
        _descriptor.EnumValueDescriptor(name='line_colors',
                                        index=9,
                                        number=9,
                                        serialized_options=None,
                                        type=None),
        _descriptor.EnumValueDescriptor(name='material_scalar_metallic',
                                        index=10,
                                        number=64,
                                        serialized_options=None,
                                        type=None),
        _descriptor.EnumValueDescriptor(name='material_scalar_roughness',
                                        index=11,
                                        number=65,
                                        serialized_options=None,
                                        type=None),
        _descriptor.EnumValueDescriptor(name='material_scalar_reflectance',
                                        index=12,
                                        number=66,
                                        serialized_options=None,
                                        type=None),
        _descriptor.EnumValueDescriptor(name='material_scalar_clear_coat',
                                        index=13,
                                        number=68,
                                        serialized_options=None,
                                        type=None),
        _descriptor.EnumValueDescriptor(
            name='material_scalar_clear_coat_roughness',
            index=14,
            number=69,
            serialized_options=None,
            type=None),
        _descriptor.EnumValueDescriptor(name='material_scalar_anisotropy',
                                        index=15,
                                        number=70,
                                        serialized_options=None,
                                        type=None),
        _descriptor.EnumValueDescriptor(
            name='material_scalar_ambient_occlusion',
            index=16,
            number=71,
            serialized_options=None,
            type=None),
        _descriptor.EnumValueDescriptor(name='material_scalar_transmission',
                                        index=17,
                                        number=73,
                                        serialized_options=None,
                                        type=None),
        _descriptor.EnumValueDescriptor(name='material_scalar_thickness',
                                        index=18,
                                        number=75,
                                        serialized_options=None,
                                        type=None),
        _descriptor.EnumValueDescriptor(
            name='material_scalar_absorption_distance',
            index=19,
            number=76,
            serialized_options=None,
            type=None),
        _descriptor.EnumValueDescriptor(name='material_vector_base_color',
                                        index=20,
                                        number=80,
                                        serialized_options=None,
                                        type=None),
        _descriptor.EnumValueDescriptor(name='material_vector_normal',
                                        index=21,
                                        number=83,
                                        serialized_options=None,
                                        type=None),
        _descriptor.EnumValueDescriptor(name='material_vector_absorption_color',
                                        index=22,
                                        number=88,
                                        serialized_options=None,
                                        type=None),
        _descriptor.EnumValueDescriptor(name='material_texture_map_metallic',
                                        index=23,
                                        number=96,
                                        serialized_options=None,
                                        type=None),
        _descriptor.EnumValueDescriptor(name='material_texture_map_roughness',
                                        index=24,
                                        number=97,
                                        serialized_options=None,
                                        type=None),
        _descriptor.EnumValueDescriptor(name='material_texture_map_reflectance',
                                        index=25,
                                        number=98,
                                        serialized_options=None,
                                        type=None),
        _descriptor.EnumValueDescriptor(name='material_texture_map_clear_coat',
                                        index=26,
                                        number=100,
                                        serialized_options=None,
                                        type=None),
        _descriptor.EnumValueDescriptor(
            name='material_texture_map_clear_coat_roughness',
            index=27,
            number=101,
            serialized_options=None,
            type=None),
        _descriptor.EnumValueDescriptor(name='material_texture_map_anisotropy',
                                        index=28,
                                        number=102,
                                        serialized_options=None,
                                        type=None),
        _descriptor.EnumValueDescriptor(
            name='material_texture_map_ambient_occlusion',
            index=29,
            number=103,
            serialized_options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='material_texture_map_transmission',
            index=30,
            number=105,
            serialized_options=None,
            type=None),
        _descriptor.EnumValueDescriptor(name='material_texture_map_thickness',
                                        index=31,
                                        number=107,
                                        serialized_options=None,
                                        type=None),
        _descriptor.EnumValueDescriptor(name='material_texture_map_albedo',
                                        index=32,
                                        number=108,
                                        serialized_options=None,
                                        type=None),
        _descriptor.EnumValueDescriptor(name='material_texture_map_normal',
                                        index=33,
                                        number=111,
                                        serialized_options=None,
                                        type=None),
        _descriptor.EnumValueDescriptor(
            name='material_texture_map_absorption_color',
            index=34,
            number=116,
            serialized_options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='material_texture_map_ao_rough_metal',
            index=35,
            number=117,
            serialized_options=None,
            type=None),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=585,
    serialized_end=1756,
)
_sym_db.RegisterEnumDescriptor(_OPEN3DPLUGINDATA_GEOMETRYPROPERTY)

_OPEN3DPLUGINDATA_PROPERTYREFERENCE = _descriptor.Descriptor(
    name='PropertyReference',
    full_name='tensorboard.open3d.Open3DPluginData.PropertyReference',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='geometry_property',
            full_name=
            'tensorboard.open3d.Open3DPluginData.PropertyReference.geometry_property',
            index=0,
            number=1,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='step_ref',
            full_name=
            'tensorboard.open3d.Open3DPluginData.PropertyReference.step_ref',
            index=1,
            number=2,
            type=4,
            cpp_type=4,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=234,
    serialized_end=353,
)

_OPEN3DPLUGINDATA_STARTSIZE = _descriptor.Descriptor(
    name='StartSize',
    full_name='tensorboard.open3d.Open3DPluginData.StartSize',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='start',
            full_name='tensorboard.open3d.Open3DPluginData.StartSize.start',
            index=0,
            number=1,
            type=4,
            cpp_type=4,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='size',
            full_name='tensorboard.open3d.Open3DPluginData.StartSize.size',
            index=1,
            number=2,
            type=4,
            cpp_type=4,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='masked_crc32c',
            full_name=
            'tensorboard.open3d.Open3DPluginData.StartSize.masked_crc32c',
            index=2,
            number=3,
            type=13,
            cpp_type=3,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='aux_start',
            full_name='tensorboard.open3d.Open3DPluginData.StartSize.aux_start',
            index=3,
            number=4,
            type=4,
            cpp_type=4,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='aux_size',
            full_name='tensorboard.open3d.Open3DPluginData.StartSize.aux_size',
            index=4,
            number=5,
            type=4,
            cpp_type=4,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='aux_masked_crc32c',
            full_name=
            'tensorboard.open3d.Open3DPluginData.StartSize.aux_masked_crc32c',
            index=5,
            number=6,
            type=13,
            cpp_type=3,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=355,
    serialized_end=482,
)

_OPEN3DPLUGINDATA_BATCHINDEX = _descriptor.Descriptor(
    name='BatchIndex',
    full_name='tensorboard.open3d.Open3DPluginData.BatchIndex',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='filename',
            full_name='tensorboard.open3d.Open3DPluginData.BatchIndex.filename',
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='start_size',
            full_name=
            'tensorboard.open3d.Open3DPluginData.BatchIndex.start_size',
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=484,
    serialized_end=582,
)

_OPEN3DPLUGINDATA = _descriptor.Descriptor(
    name='Open3DPluginData',
    full_name='tensorboard.open3d.Open3DPluginData',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='version',
            full_name='tensorboard.open3d.Open3DPluginData.version',
            index=0,
            number=1,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='property_references',
            full_name='tensorboard.open3d.Open3DPluginData.property_references',
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='batch_index',
            full_name='tensorboard.open3d.Open3DPluginData.batch_index',
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR),
    ],
    extensions=[],
    nested_types=[
        _OPEN3DPLUGINDATA_PROPERTYREFERENCE,
        _OPEN3DPLUGINDATA_STARTSIZE,
        _OPEN3DPLUGINDATA_BATCHINDEX,
    ],
    enum_types=[
        _OPEN3DPLUGINDATA_GEOMETRYPROPERTY,
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=42,
    serialized_end=1756,
)

_INFERENCEDATA_INFERENCERESULT = _descriptor.Descriptor(
    name='InferenceResult',
    full_name='tensorboard.open3d.InferenceData.InferenceResult',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='label',
            full_name='tensorboard.open3d.InferenceData.InferenceResult.label',
            index=0,
            number=1,
            type=13,
            cpp_type=3,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='confidence',
            full_name=
            'tensorboard.open3d.InferenceData.InferenceResult.confidence',
            index=1,
            number=2,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=1853,
    serialized_end=1905,
)

_INFERENCEDATA = _descriptor.Descriptor(
    name='InferenceData',
    full_name='tensorboard.open3d.InferenceData',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='inference_result',
            full_name='tensorboard.open3d.InferenceData.inference_result',
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR),
    ],
    extensions=[],
    nested_types=[
        _INFERENCEDATA_INFERENCERESULT,
    ],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=1759,
    serialized_end=1905,
)

_LABELTONAMES_LABELTONAMESENTRY = _descriptor.Descriptor(
    name='LabelToNamesEntry',
    full_name='tensorboard.open3d.LabelToNames.LabelToNamesEntry',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='key',
            full_name='tensorboard.open3d.LabelToNames.LabelToNamesEntry.key',
            index=0,
            number=1,
            type=13,
            cpp_type=3,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='value',
            full_name='tensorboard.open3d.LabelToNames.LabelToNamesEntry.value',
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=_b('8\001'),
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=2000,
    serialized_end=2051,
)

_LABELTONAMES = _descriptor.Descriptor(
    name='LabelToNames',
    full_name='tensorboard.open3d.LabelToNames',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='label_to_names',
            full_name='tensorboard.open3d.LabelToNames.label_to_names',
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR),
    ],
    extensions=[],
    nested_types=[
        _LABELTONAMES_LABELTONAMESENTRY,
    ],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=1908,
    serialized_end=2051,
)

_OPEN3DPLUGINDATA_PROPERTYREFERENCE.fields_by_name[
    'geometry_property'].enum_type = _OPEN3DPLUGINDATA_GEOMETRYPROPERTY
_OPEN3DPLUGINDATA_PROPERTYREFERENCE.containing_type = _OPEN3DPLUGINDATA
_OPEN3DPLUGINDATA_STARTSIZE.containing_type = _OPEN3DPLUGINDATA
_OPEN3DPLUGINDATA_BATCHINDEX.fields_by_name[
    'start_size'].message_type = _OPEN3DPLUGINDATA_STARTSIZE
_OPEN3DPLUGINDATA_BATCHINDEX.containing_type = _OPEN3DPLUGINDATA
_OPEN3DPLUGINDATA.fields_by_name[
    'property_references'].message_type = _OPEN3DPLUGINDATA_PROPERTYREFERENCE
_OPEN3DPLUGINDATA.fields_by_name[
    'batch_index'].message_type = _OPEN3DPLUGINDATA_BATCHINDEX
_OPEN3DPLUGINDATA_GEOMETRYPROPERTY.containing_type = _OPEN3DPLUGINDATA
_INFERENCEDATA_INFERENCERESULT.containing_type = _INFERENCEDATA
_INFERENCEDATA.fields_by_name[
    'inference_result'].message_type = _INFERENCEDATA_INFERENCERESULT
_LABELTONAMES_LABELTONAMESENTRY.containing_type = _LABELTONAMES
_LABELTONAMES.fields_by_name[
    'label_to_names'].message_type = _LABELTONAMES_LABELTONAMESENTRY
DESCRIPTOR.message_types_by_name['Open3DPluginData'] = _OPEN3DPLUGINDATA
DESCRIPTOR.message_types_by_name['InferenceData'] = _INFERENCEDATA
DESCRIPTOR.message_types_by_name['LabelToNames'] = _LABELTONAMES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Open3DPluginData = _reflection.GeneratedProtocolMessageType(
    'Open3DPluginData',
    (_message.Message,),
    dict(
        PropertyReference=_reflection.GeneratedProtocolMessageType(
            'PropertyReference',
            (_message.Message,),
            dict(
                DESCRIPTOR=_OPEN3DPLUGINDATA_PROPERTYREFERENCE,
                __module__='plugin_data_pb2'
                # @@protoc_insertion_point(class_scope:tensorboard.open3d.Open3DPluginData.PropertyReference)
            )),
        StartSize=_reflection.GeneratedProtocolMessageType(
            'StartSize',
            (_message.Message,),
            dict(
                DESCRIPTOR=_OPEN3DPLUGINDATA_STARTSIZE,
                __module__='plugin_data_pb2'
                # @@protoc_insertion_point(class_scope:tensorboard.open3d.Open3DPluginData.StartSize)
            )),
        BatchIndex=_reflection.GeneratedProtocolMessageType(
            'BatchIndex',
            (_message.Message,),
            dict(
                DESCRIPTOR=_OPEN3DPLUGINDATA_BATCHINDEX,
                __module__='plugin_data_pb2'
                # @@protoc_insertion_point(class_scope:tensorboard.open3d.Open3DPluginData.BatchIndex)
            )),
        DESCRIPTOR=_OPEN3DPLUGINDATA,
        __module__='plugin_data_pb2'
        # @@protoc_insertion_point(class_scope:tensorboard.open3d.Open3DPluginData)
    ))
_sym_db.RegisterMessage(Open3DPluginData)
_sym_db.RegisterMessage(Open3DPluginData.PropertyReference)
_sym_db.RegisterMessage(Open3DPluginData.StartSize)
_sym_db.RegisterMessage(Open3DPluginData.BatchIndex)

InferenceData = _reflection.GeneratedProtocolMessageType(
    'InferenceData',
    (_message.Message,),
    dict(
        InferenceResult=_reflection.GeneratedProtocolMessageType(
            'InferenceResult',
            (_message.Message,),
            dict(
                DESCRIPTOR=_INFERENCEDATA_INFERENCERESULT,
                __module__='plugin_data_pb2'
                # @@protoc_insertion_point(class_scope:tensorboard.open3d.InferenceData.InferenceResult)
            )),
        DESCRIPTOR=_INFERENCEDATA,
        __module__='plugin_data_pb2'
        # @@protoc_insertion_point(class_scope:tensorboard.open3d.InferenceData)
    ))
_sym_db.RegisterMessage(InferenceData)
_sym_db.RegisterMessage(InferenceData.InferenceResult)

LabelToNames = _reflection.GeneratedProtocolMessageType(
    'LabelToNames',
    (_message.Message,),
    dict(
        LabelToNamesEntry=_reflection.GeneratedProtocolMessageType(
            'LabelToNamesEntry',
            (_message.Message,),
            dict(
                DESCRIPTOR=_LABELTONAMES_LABELTONAMESENTRY,
                __module__='plugin_data_pb2'
                # @@protoc_insertion_point(class_scope:tensorboard.open3d.LabelToNames.LabelToNamesEntry)
            )),
        DESCRIPTOR=_LABELTONAMES,
        __module__='plugin_data_pb2'
        # @@protoc_insertion_point(class_scope:tensorboard.open3d.LabelToNames)
    ))
_sym_db.RegisterMessage(LabelToNames)
_sym_db.RegisterMessage(LabelToNames.LabelToNamesEntry)

_LABELTONAMES_LABELTONAMESENTRY._options = None
# @@protoc_insertion_point(module_scope)
