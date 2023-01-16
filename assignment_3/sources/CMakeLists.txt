cmake_minimum_required(VERSION 3.10)

set(APP_NAME "project")
set(LIB_NAME "triangle_area")
set(EXECUTABLE_FILE "main.cpp")
set(LIB_FILE "triangle_area.cpp")

project(${APP_NAME})

add_library(${LIB_NAME} SHARED ${LIB_FILE})

add_executable(${APP_NAME} ${EXECUTABLE_FILE})

if (UNIX)
    set(CMAKE_SHARED_LIBRARY_SUFFIX ".so")
endif (UNIX)

target_link_libraries(${APP_NAME} LINK_PUBLIC ${LIB_NAME})