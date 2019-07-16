# This file is automatically generated -- do not edit!
{
  "variables": {
    "root_relative_to_gypfile": ".."
  },
  "targets": [
    {
      "target_name": "buildtools_protobuf_lite_proxy",
      "type": "static_library",
      "toolsets": [
        "target",
        "host"
      ],
      "include_dirs": [
        "<(root_relative_to_gypfile)/",
        "<(root_relative_to_gypfile)/include/",
        "<(root_relative_to_gypfile)/../protobuf/src"
      ],
      "defines": [
        "HAVE_PTHREAD=1",
        "GOOGLE_PROTOBUF_NO_RTTI",
        "GOOGLE_PROTOBUF_NO_STATIC_INITIALIZER",
        "PERFETTO_IMPLEMENTATION"
      ],
      "sources": [
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/arena.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/arenastring.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/extension_set.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/generated_message_util.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/io/coded_stream.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/io/zero_copy_stream.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/io/zero_copy_stream_impl_lite.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/message_lite.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/repeated_field.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/stubs/atomicops_internals_x86_gcc.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/stubs/atomicops_internals_x86_msvc.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/stubs/bytestream.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/stubs/common.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/stubs/int128.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/stubs/once.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/stubs/status.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/stubs/statusor.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/stubs/stringpiece.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/stubs/stringprintf.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/stubs/structurally_valid.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/stubs/strutil.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/stubs/time.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/wire_format_lite.cc"
      ],
      "conditions": [
        [
          "OS==\"mac\"",
          {
            "target_conditions": [
              [
                "_toolset==\"target\"",
                {
                  "include_dirs": [
                    "<(SHARED_INTERMEDIATE_DIR)/gen/protos/"
                  ]
                }
              ],
              [
                "_toolset==\"host\"",
                {
                  "include_dirs": [
                    "<(SHARED_INTERMEDIATE_DIR)/gcc_like_host/gen/protos/"
                  ]
                }
              ]
            ]
          }
        ]
      ]
    },
    {
      "target_name": "buildtools_protobuf_lite",
      "type": "none",
      "dependencies": [
        "buildtools_protobuf_lite_proxy"
      ],
      "toolsets": [
        "target",
        "host"
      ]
    },
    {
      "target_name": "buildtools_protoc_proxy",
      "type": "executable",
      "toolsets": [
        "host"
      ],
      "include_dirs": [
        "<(root_relative_to_gypfile)/",
        "<(root_relative_to_gypfile)/include/",
        "<(SHARED_INTERMEDIATE_DIR)/gcc_like_host/gen/protos/",
        "<(root_relative_to_gypfile)/../protobuf/src"
      ],
      "defines": [
        "GOOGLE_PROTOBUF_NO_RTTI",
        "GOOGLE_PROTOBUF_NO_STATIC_INITIALIZER",
        "PERFETTO_IMPLEMENTATION"
      ],
      "sources": [
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/main.cc"
      ],
      "dependencies": [
        "buildtools_protoc_lib#host"
      ]
    },
    {
      "target_name": "buildtools_protoc",
      "type": "none",
      "dependencies": [
        "buildtools_protoc_proxy"
      ],
      "toolsets": [
        "host"
      ],
      "actions": [
        {
          "action_name": "copy_as_expected_output",
          "action": [
            "cp",
            "<@(_inputs)",
            "<@(_outputs)"
          ],
          "inputs": [
            "<@(PRODUCT_DIR)/buildtools_protoc_proxy"
          ],
          "outputs": [
            "<(SHARED_INTERMEDIATE_DIR)/gcc_like_host/protoc"
          ]
        }
      ]
    },
    {
      "target_name": "buildtools_protoc_lib_proxy",
      "type": "static_library",
      "toolsets": [
        "host"
      ],
      "include_dirs": [
        "<(root_relative_to_gypfile)/",
        "<(root_relative_to_gypfile)/include/",
        "<(SHARED_INTERMEDIATE_DIR)/gcc_like_host/gen/protos/",
        "<(root_relative_to_gypfile)/../protobuf/src"
      ],
      "defines": [
        "HAVE_PTHREAD=1",
        "GOOGLE_PROTOBUF_NO_RTTI",
        "GOOGLE_PROTOBUF_NO_STATIC_INITIALIZER",
        "PERFETTO_IMPLEMENTATION"
      ],
      "sources": [
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/code_generator.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/command_line_interface.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/cpp/cpp_enum.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/cpp/cpp_enum_field.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/cpp/cpp_extension.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/cpp/cpp_field.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/cpp/cpp_file.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/cpp/cpp_generator.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/cpp/cpp_helpers.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/cpp/cpp_map_field.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/cpp/cpp_message.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/cpp/cpp_message_field.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/cpp/cpp_primitive_field.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/cpp/cpp_service.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/cpp/cpp_string_field.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/csharp/csharp_doc_comment.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/csharp/csharp_enum.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/csharp/csharp_enum_field.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/csharp/csharp_field_base.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/csharp/csharp_generator.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/csharp/csharp_helpers.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/csharp/csharp_map_field.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/csharp/csharp_message.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/csharp/csharp_message_field.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/csharp/csharp_primitive_field.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/csharp/csharp_reflection_class.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/csharp/csharp_repeated_enum_field.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/csharp/csharp_repeated_message_field.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/csharp/csharp_repeated_primitive_field.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/csharp/csharp_source_generator_base.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/csharp/csharp_wrapper_field.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/java/java_context.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/java/java_doc_comment.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/java/java_enum.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/java/java_enum_field.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/java/java_enum_field_lite.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/java/java_enum_lite.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/java/java_extension.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/java/java_extension_lite.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/java/java_field.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/java/java_file.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/java/java_generator.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/java/java_generator_factory.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/java/java_helpers.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/java/java_lazy_message_field.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/java/java_lazy_message_field_lite.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/java/java_map_field.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/java/java_map_field_lite.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/java/java_message.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/java/java_message_builder.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/java/java_message_builder_lite.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/java/java_message_field.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/java/java_message_field_lite.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/java/java_message_lite.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/java/java_name_resolver.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/java/java_primitive_field.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/java/java_primitive_field_lite.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/java/java_service.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/java/java_shared_code_generator.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/java/java_string_field.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/java/java_string_field_lite.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/javanano/javanano_enum.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/javanano/javanano_enum_field.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/javanano/javanano_extension.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/javanano/javanano_field.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/javanano/javanano_file.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/javanano/javanano_generator.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/javanano/javanano_helpers.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/javanano/javanano_map_field.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/javanano/javanano_message.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/javanano/javanano_message_field.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/javanano/javanano_primitive_field.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/js/js_generator.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/objectivec/objectivec_enum.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/objectivec/objectivec_enum_field.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/objectivec/objectivec_extension.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/objectivec/objectivec_field.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/objectivec/objectivec_file.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/objectivec/objectivec_generator.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/objectivec/objectivec_helpers.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/objectivec/objectivec_map_field.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/objectivec/objectivec_message.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/objectivec/objectivec_message_field.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/objectivec/objectivec_oneof.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/objectivec/objectivec_primitive_field.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/plugin.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/plugin.pb.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/python/python_generator.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/ruby/ruby_generator.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/subprocess.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/zip_writer.cc"
      ],
      "dependencies": [
        "buildtools_protobuf_full#host"
      ]
    },
    {
      "target_name": "buildtools_protoc_lib",
      "type": "none",
      "dependencies": [
        "buildtools_protoc_lib_proxy"
      ],
      "toolsets": [
        "host"
      ]
    },
    {
      "target_name": "buildtools_protobuf_full_proxy",
      "type": "static_library",
      "toolsets": [
        "host"
      ],
      "include_dirs": [
        "<(root_relative_to_gypfile)/",
        "<(root_relative_to_gypfile)/include/",
        "<(SHARED_INTERMEDIATE_DIR)/gcc_like_host/gen/protos/",
        "<(root_relative_to_gypfile)/../protobuf/src"
      ],
      "defines": [
        "HAVE_PTHREAD=1",
        "GOOGLE_PROTOBUF_NO_RTTI",
        "GOOGLE_PROTOBUF_NO_STATIC_INITIALIZER",
        "PERFETTO_IMPLEMENTATION"
      ],
      "sources": [
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/any.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/any.pb.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/api.pb.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/importer.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/compiler/parser.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/descriptor.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/descriptor.pb.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/descriptor_database.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/duration.pb.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/dynamic_message.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/empty.pb.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/extension_set_heavy.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/field_mask.pb.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/generated_message_reflection.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/io/gzip_stream.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/io/printer.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/io/strtod.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/io/tokenizer.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/io/zero_copy_stream_impl.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/map_field.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/message.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/reflection_ops.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/service.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/source_context.pb.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/struct.pb.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/stubs/mathlimits.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/stubs/substitute.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/text_format.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/timestamp.pb.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/type.pb.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/unknown_field_set.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/util/field_comparator.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/util/field_mask_util.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/util/internal/datapiece.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/util/internal/default_value_objectwriter.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/util/internal/error_listener.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/util/internal/field_mask_utility.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/util/internal/json_escaping.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/util/internal/json_objectwriter.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/util/internal/json_stream_parser.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/util/internal/object_writer.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/util/internal/proto_writer.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/util/internal/protostream_objectsource.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/util/internal/protostream_objectwriter.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/util/internal/type_info.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/util/internal/type_info_test_helper.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/util/internal/utility.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/util/json_util.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/util/message_differencer.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/util/time_util.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/util/type_resolver_util.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/wire_format.cc",
        "<(root_relative_to_gypfile)/../protobuf/src/google/protobuf/wrappers.pb.cc"
      ],
      "dependencies": [
        "buildtools_protobuf_lite#host"
      ]
    },
    {
      "target_name": "buildtools_protobuf_full",
      "type": "none",
      "dependencies": [
        "buildtools_protobuf_full_proxy"
      ],
      "toolsets": [
        "host"
      ]
    }
  ]
}