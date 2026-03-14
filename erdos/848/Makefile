CXX ?= g++
CXXFLAGS ?= -O3 -march=native -std=c++20 -fopenmp -DNDEBUG

all: erdos848_verifier

erdos848_verifier: erdos848_verifier.cpp
	$(CXX) $(CXXFLAGS) erdos848_verifier.cpp -o erdos848_verifier

clean:
	rm -f erdos848_verifier
