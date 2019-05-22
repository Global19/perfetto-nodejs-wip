/*
 * Copyright (C) 2017 The Android Open Source Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

/*******************************************************************************
 * AUTOGENERATED - DO NOT EDIT
 *******************************************************************************
 * This file has been generated from the protobuf message
 * perfetto/config/data_source_descriptor.proto
 * by
 * ../../tools/proto_to_cpp/proto_to_cpp.cc.
 * If you need to make changes here, change the .proto file and then run
 * ./tools/gen_tracing_cpp_headers_from_protos
 */

#ifndef INCLUDE_PERFETTO_TRACING_CORE_DATA_SOURCE_DESCRIPTOR_H_
#define INCLUDE_PERFETTO_TRACING_CORE_DATA_SOURCE_DESCRIPTOR_H_

#include <stdint.h>
#include <string>
#include <type_traits>
#include <vector>

#include "perfetto/base/export.h"

// Forward declarations for protobuf types.
namespace perfetto {
namespace protos {
class DataSourceDescriptor;
}
}  // namespace perfetto

namespace perfetto {

class PERFETTO_EXPORT DataSourceDescriptor {
 public:
  DataSourceDescriptor();
  ~DataSourceDescriptor();
  DataSourceDescriptor(DataSourceDescriptor&&) noexcept;
  DataSourceDescriptor& operator=(DataSourceDescriptor&&);
  DataSourceDescriptor(const DataSourceDescriptor&);
  DataSourceDescriptor& operator=(const DataSourceDescriptor&);
  bool operator==(const DataSourceDescriptor&) const;
  bool operator!=(const DataSourceDescriptor& other) const {
    return !(*this == other);
  }

  // Raw proto decoding.
  void ParseRawProto(const std::string&);
  // Conversion methods from/to the corresponding protobuf types.
  void FromProto(const perfetto::protos::DataSourceDescriptor&);
  void ToProto(perfetto::protos::DataSourceDescriptor*) const;

  const std::string& name() const { return name_; }
  void set_name(const std::string& value) { name_ = value; }

  bool will_notify_on_stop() const { return will_notify_on_stop_; }
  void set_will_notify_on_stop(bool value) { will_notify_on_stop_ = value; }

  bool will_notify_on_start() const { return will_notify_on_start_; }
  void set_will_notify_on_start(bool value) { will_notify_on_start_ = value; }

  bool handles_incremental_state_clear() const {
    return handles_incremental_state_clear_;
  }
  void set_handles_incremental_state_clear(bool value) {
    handles_incremental_state_clear_ = value;
  }

 private:
  std::string name_ = {};
  bool will_notify_on_stop_ = {};
  bool will_notify_on_start_ = {};
  bool handles_incremental_state_clear_ = {};

  // Allows to preserve unknown protobuf fields for compatibility
  // with future versions of .proto files.
  std::string unknown_fields_;
};

}  // namespace perfetto

#endif  // INCLUDE_PERFETTO_TRACING_CORE_DATA_SOURCE_DESCRIPTOR_H_
