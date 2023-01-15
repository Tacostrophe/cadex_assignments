# Specify extensions of files to delete when cleaning
CLEANEXTS   = o

# Specify the target file and the install directory
OUTPUTFILE=triangle_area.exe
LIBNAME=triangle_area
INSTALLDIR=../binaries
SOURCE=triangle_area.cpp
MAIN=main.cpp

# Default target
.PHONY: all
all: build clean set_lib_path

# Build hello from hello.cpp
.PHONY: build
build:
	mkdir -p $(INSTALLDIR)
	$(CXX) -c $(SOURCE)
	$(CXX) -shared -fPIC -o $(INSTALLDIR)/lib$(LIBNAME).so $(subst .cpp,.o,$(SOURCE))
	$(CXX) -L $(INSTALLDIR) -Wall -o $(INSTALLDIR)/$(OUTPUTFILE) $(MAIN) -l$(LIBNAME)

## Delete outputfile_exe from sources
.PHONY: clean
clean:
	for file in $(CLEANEXTS); do rm -f *.$$file; done

.PHONY: set_lib_path
set_lib_path:
	export LD_LIBRARY_PATH=$(INSTALLDIR)
