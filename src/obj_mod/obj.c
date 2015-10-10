#include <Python.h>
#include <structmember.h>
#include <string.h>

static PyObject *NativeError;

/* Structure of Native Python objects */
typedef struct {
    // Required header fields
    PyObject_HEAD
    char * pointer;
    long number;
    PyObject * name;
} Native;


static void
Native_dealloc(Native * self)
{
    Py_XDECREF(self->name);
    if (self->pointer != NULL) {
        free(self->pointer);
    }
    Py_TYPE(self)->tp_free((PyObject *)self);
}

static PyObject *
Native_new(PyTypeObject *type, PyObject *args, PyObject *kwargs)
{
    Native *self;

    self = (Native *)type->tp_alloc(type, 0);
    if (self == NULL) {
        return NULL;
    }
    self->number = 0;
    self->name = PyUnicode_FromString("");
    if (self->name == NULL) {
        Py_DECREF(self);
        return NULL;
    }
    self->number = 0;
    self->pointer = (char *)malloc(sizeof(char) * 4);
    if (self->pointer == NULL) {
        Py_DECREF(self->name);
        Py_DECREF(self);
        return PyErr_NoMemory();
    }
    strcpy(self->pointer, "?");

    return (PyObject *)self;
}

static int
Native_init(Native *self, PyObject *args, PyObject *kwargs)
{
    PyObject * name = NULL;
    PyObject * tmp;
    int yes_no;

    static char *kwlist[] = {"name", "number", "yes", NULL};

    if (!PyArg_ParseTupleAndKeywords(
        args, kwargs, "Olp", kwlist, &name, &self->number, &yes_no
    )) {
        return -1;
    }

    if (name) {
        tmp = self->name;
        Py_INCREF(name);
        self->name = name;
        Py_XDECREF(tmp);
    }

    strcpy(self->pointer, yes_no ? "YES" : "NO");

    return 0;
}

static PyObject *
Native_summary(Native* self)
{
    if (self->name == NULL) {
        PyErr_SetString(NativeError, "name");
        return NULL;
    }

    return PyUnicode_FromFormat(
        "Native %S number %li pointer %s",
        self->name, self->number, self->pointer
    );
}

static PyMemberDef Native_members[] = {
    {"name", T_OBJECT_EX, offsetof(Native, name), 0, "Name"},
    {"number", T_LONG, offsetof(Native, number), 0, "Number"},
    {"pointer", T_STRING, offsetof(Native, pointer), READONLY, "Pointer"},
    {NULL}  /* Sentinel */
};

static PyMethodDef Native_methods[] = {
    {"summary", (PyCFunction)Native_summary, METH_NOARGS,
     "Return the name and the other attributes formatted"
    },
    {NULL}  /* Sentinel */
};

static PyTypeObject NativeType = {
    PyVarObject_HEAD_INIT(NULL, 0)
    "obj.Native",              /* tp_name */
    sizeof(Native),            /* tp_basicsize */
    0,                         /* tp_itemsize */
    (destructor)Native_dealloc,/* tp_dealloc */
    0,                         /* tp_print */
    0,                         /* tp_getattr */
    0,                         /* tp_setattr */
    0,                         /* tp_reserved */
    0,                         /* tp_repr */
    0,                         /* tp_as_number */
    0,                         /* tp_as_sequence */
    0,                         /* tp_as_mapping */
    0,                         /* tp_hash  */
    0,                         /* tp_call */
    0,                         /* tp_str */
    0,                         /* tp_getattro */
    0,                         /* tp_setattro */
    0,                         /* tp_as_buffer */
    Py_TPFLAGS_DEFAULT |
        Py_TPFLAGS_BASETYPE,   /* tp_flags */
    "Native objects",          /* tp_doc */
    0,                         /* tp_traverse */
    0,                         /* tp_clear */
    0,                         /* tp_richcompare */
    0,                         /* tp_weaklistoffset */
    0,                         /* tp_iter */
    0,                         /* tp_iternext */
    Native_methods,            /* tp_methods */
    Native_members,            /* tp_members */
    0,                         /* tp_getset */
    0,                         /* tp_base */
    0,                         /* tp_dict */
    0,                         /* tp_descr_get */
    0,                         /* tp_descr_set */
    0,                         /* tp_dictoffset */
    (initproc)Native_init,     /* tp_init */
    0,                         /* tp_alloc */
    Native_new,                /* tp_new */
};

static PyObject *
obj_create(PyObject *self)
{
    int added;
    PyObject * args = PyTuple_New(3);
    if (args == NULL) {
        return NULL;
    }
    PyObject * name = PyUnicode_FromString("Bill");
    if (name == NULL) {
        Py_DECREF(args);
        return NULL;
    }
    added = PyTuple_SetItem(args, 0, name);
    // PyTuple_SetItem is an exception and it steals the reference, even if it fails.
    // We will not have to DECREF name anymore.
    if (added != 0) {
        Py_DECREF(args);
        return NULL;
    }
    PyObject * number = PyLong_FromLong(7);
    if (number == NULL) {
        Py_DECREF(args);
        return NULL;
    }
    added = PyTuple_SetItem(args, 1, number);
    // We will not have to DECREF number anymore.
    if (added != 0) {
        Py_DECREF(args);
        return NULL;
    }
    PyObject * yes = Py_True;
    Py_INCREF(yes);
    added = PyTuple_SetItem(args, 2, yes);
    // We will not have to DECREF yes anymore.
    if (added != 0) {
        Py_DECREF(args);
        return NULL;
    }

    PyObject * kwargs = NULL;
    PyObject * result = PyObject_Call((PyObject *) &NativeType, args, kwargs);
    Py_DECREF(args);
    if (result == NULL) {
        return NULL;
    }
    return result;
}

static PyMethodDef obj_methods[] = {
    /* no module-level functions. */
    {"create", (PyCFunction)obj_create, METH_NOARGS, "Return an obj."},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

static struct PyModuleDef obj_module = {
   PyModuleDef_HEAD_INIT,
   "obj",   /* name of module */
   "Module showing classes", /* module documentation, may be NULL */
   -1,       /* size of per-interpreter state of the module,
                or -1 if the module keeps state in global variables. */
   obj_methods
};

PyMODINIT_FUNC
PyInit_obj(void)
{
    PyObject * module;

    if (PyType_Ready(&NativeType) < 0) {
        return NULL;
    }

    module = PyModule_Create(&obj_module);
    if (module == NULL) {
        return NULL;
    }

    NativeError = PyErr_NewException("obj.NativeError", PyExc_ValueError, NULL);
    Py_INCREF(NativeError);
    PyModule_AddObject(module, "NativeError", NativeError);

    Py_INCREF(&NativeType);
    PyModule_AddObject(module, "Native", (PyObject *)&NativeType);

    return module;
}
