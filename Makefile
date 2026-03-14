CXX = gcc

SRCS = $(wildcard Source/*.c)

build: $(SRCS)
	$(CXX) $(CXXFLAGS) -o Builds/build.exe $(SRCS) $(CXXLIBS)

local: $(SRCS)
	$(CXX) $(CXXFLAGS) -o lbuild.exe $(SRCS) $(CXXLIBS)

clean:
	rm -f build

.PHONY: clean
