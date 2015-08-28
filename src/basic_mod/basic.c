#include <Python.h>

static PyObject *
basic_hello(PyObject *self)
{
    const char * msg = "Hello world";
    return PyUnicode_FromString(msg);
}

static PyMethodDef basic_methods[] = {
    {"hello", (PyCFunction)basic_hello, METH_NOARGS, "Return hello world."},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

static struct PyModuleDef basic_module = {
   PyModuleDef_HEAD_INIT,
   "basic",   /* name of module */
   "The simplest module", /* module documentation, may be NULL */
   -1,       /* size of per-interpreter state of the module,
                or -1 if the module keeps state in global variables. */
   basic_methods
};

PyMODINIT_FUNC
PyInit_basic(void)
{
    return PyModule_Create(&basic_module);
}
