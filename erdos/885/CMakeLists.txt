cmake_minimum_required(VERSION 3.16)
project(ep885_search CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

add_executable(ep885
  src/main.cpp
  src/util.cpp
  src/smooth.cpp
  src/divisors.cpp
  src/delta_index.cpp
  src/logging.cpp
  src/eclat.cpp
)

target_include_directories(ep885 PRIVATE include)

if (MSVC)
  target_compile_options(ep885 PRIVATE /W4 /O2)
else()
  target_compile_options(ep885 PRIVATE -O2 -Wall -Wextra -Wpedantic)
endif()

