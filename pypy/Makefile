shared_library_test: hello.so
	gcc -L/home/bineesh/notebook/problemsolving/pypy -Wall -o share_library_test shared_library_method.c -lhello
	export LD_LIBRARY_PATH=/home/bineesh/notebook/problemsolving/pypy
hello.so: hello.o hello.c
	gcc -shared -o libhello.so hello.o
hello.o: hello.c
	gcc -c -Wall -Werror -fpic hello.c
