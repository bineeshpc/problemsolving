unset LD_LIBRARY_PATH
export LD_LIBRARY_PATH=/home/bineesh/notebook/problemsolving/pypy:LD_LIBRARY_PATH
make
./share_library_test
python setup.py build_ext --inplace

echo pypy cshared
/home/bineesh/pypy-2.5.1-linux64/bin/pypy pypy_cshared.py

echo python cshared
python python_cshared.py

echo pypy cython
/home/bineesh/pypy-2.5.1-linux64/bin/pypy pypy_cython.py

echo python cython
python python_cython.py
