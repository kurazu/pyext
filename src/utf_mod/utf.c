#include <Python.h>
#include <stdio.h>

static PyObject *
utf_hello(PyObject * self, PyObject * args)
{
    const char * text;
    if (!PyArg_ParseTuple(args, "s", &text)) {
        return NULL;
    }
    static const char expected[] = {
        /* żółw */
        '\xc5', '\xbc', '\xc3', '\xb3', '\xc5', '\x82', '\x77', '\0'
    };

    unsigned idx;
    for (idx = 0; idx < 8; idx++) {
        if (text[idx] != expected[idx]) {
            return PyUnicode_FromString("ERROR");
        }
    }

    static const char output[] = {
        /* żółty */
        '\xc5', '\xbc', '\xc3', '\xb3', '\xc5', '\x82', '\x74', '\x79', '\0'
    };
    PyObject * result = PyUnicode_FromString(output);
    return result;
}

static PyObject *
utf_len(PyObject * self, PyObject * args)
{
    const char * text;
    if (!PyArg_ParseTuple(args, "s", &text)) {
        return NULL;
    }
    const int len = strlen(text);
    return PyLong_FromLong(len);
}

static PyMethodDef utf_methods[] = {
    {"hello",  utf_hello, METH_VARARGS, "Say hello."},
    {"len",  utf_len, METH_VARARGS, "Count bytes."},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

static struct PyModuleDef utf_module = {
   PyModuleDef_HEAD_INIT,
   "utf",   /* name of module */
   "Module showing UTF handling", /* module documentation, may be NULL */
   -1,       /* size of per-interpreter state of the module,
                or -1 if the module keeps state in global variables. */
   utf_methods
};

PyMODINIT_FUNC
PyInit_utf(void)
{
    return PyModule_Create(&utf_module);
}
