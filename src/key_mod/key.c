#include <Python.h>

static PyObject *
key_belongs(PyObject *self, PyObject * args, PyObject * kwargs)
{
    static char * keywords[] = {
        "mapping", "item", "category", NULL
    };
    PyObject * mapping;
    PyObject * item;
    PyObject * category;

    /* All objects parsed are borrowed references, no DECREF needed. */
    if (!PyArg_ParseTupleAndKeywords(
        args, kwargs, "OOO", keywords,
        &mapping, &item, &category
    )) {
        return NULL;
    }
    /* GetItem returns a new reference that needs to be decremented */
    PyObject * category_sequence = PyObject_GetItem(mapping, category);
    if (category_sequence == NULL) {
        return NULL;
    }

    int contains = PySequence_Contains(category_sequence, item);
    Py_DECREF(category_sequence);
    if (contains == -1) {
        return NULL;
    }

    PyObject * result;
    result = contains ? Py_True : Py_False;
    Py_INCREF(result);

    return result;
}

static PyMethodDef key_methods[] = {
    {
        "belongs",  (PyCFunction)key_belongs, METH_VARARGS | METH_KEYWORDS,
        "Check if item belongs to category in mapping"
    },
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

static struct PyModuleDef key_module = {
   PyModuleDef_HEAD_INIT,
   "key",   /* name of module */
   "Module showing api and keywords", /* module documentation, may be NULL */
   -1,       /* size of per-interpreter state of the module,
                or -1 if the module keeps state in global variables. */
   key_methods
};

PyMODINIT_FUNC
PyInit_key(void)
{
    return PyModule_Create(&key_module);
}
