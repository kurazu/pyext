#include <Python.h>

static long
fibonacci(long n) {
    if (n == 0) {
        return 0;
    } else if (n == 1) {
        return 1;
    } else {
        return fibonacci(n - 2) + fibonacci(n - 1);
    }
}

static PyObject *
gil_calc(PyObject * self, PyObject * args)
{
    long n;
    if (!PyArg_ParseTuple(args, "l", &n)) {
        return NULL;
    }

    long result;
    result = fibonacci(n);

    return PyLong_FromLong(result);
}

static PyObject *
gil_calc_release(PyObject * self, PyObject * args)
{
    long n;
    if (!PyArg_ParseTuple(args, "l", &n)) {
        return NULL;
    }
    long result;

    Py_BEGIN_ALLOW_THREADS
    result = fibonacci(n);
    Py_END_ALLOW_THREADS

    return PyLong_FromLong(result);
}

static PyMethodDef gil_methods[] = {
    {
        "calc",  gil_calc, METH_VARARGS,
        "Do calculations without releasing GIL"
    },
    {
        "calc_release",  gil_calc_release, METH_VARARGS,
        "Do calculations with releasing GIL"
    },
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

static struct PyModuleDef gil_module = {
   PyModuleDef_HEAD_INIT,
   "gil",   /* name of module */
   "Module showing GIL operations", /* module documentation, may be NULL */
   -1,       /* size of per-interpreter state of the module,
                or -1 if the module keeps state in global variables. */
   gil_methods
};

PyMODINIT_FUNC
PyInit_gil(void)
{
    return PyModule_Create(&gil_module);
}
