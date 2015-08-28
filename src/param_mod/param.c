#include <Python.h>
#include <stdio.h>

static PyObject *
param_hello(PyObject *self, PyObject * args)
{
    const char * name;
    unsigned age;
    if (!PyArg_ParseTuple(args, "sI", &name, &age)) {
        return NULL;
    }
    const char * text;
    static const char * format = "Hello %s age %u!";
    if (asprintf(&text, format, name, age) < 0) {
        PyErr_SetString(PyExc_RuntimeError, "Cannot format output");
        return NULL;
    }
    PyObject * result = PyUnicode_FromString(text);
    free(text);
    return result;
}

static PyMethodDef param_methods[] = {
    {"hello",  param_hello, METH_VARARGS, "Say hello."},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

static struct PyModuleDef param_module = {
   PyModuleDef_HEAD_INIT,
   "param",   /* name of module */
   "Module showing parameter parsing", /* module documentation, may be NULL */
   -1,       /* size of per-interpreter state of the module,
                or -1 if the module keeps state in global variables. */
   param_methods
};

PyMODINIT_FUNC
PyInit_param(void)
{
    return PyModule_Create(&param_module);
}
