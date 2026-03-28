CXX = gcc

SRCS = $(wildcard Source/*.c)

build: $(SRCS)
	$(CXX) $(CXXFLAGS) -o Builds/build $(SRCS) $(CXXLIBS)

local: $(SRCS)
	$(CXX) $(CXXFLAGS) -o lbuild $(SRCS) $(CXXLIBS)

clean:
	rm -f build

.PHONY: clean
