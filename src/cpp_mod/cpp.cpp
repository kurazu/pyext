#include <Python.h>
#include <sstream>
#include <string>

static PyObject *
cpp_format(PyObject *self, PyObject * args)
{
    const char * name;
    unsigned age;
    if (!PyArg_ParseTuple(args, "sI", &name, &age)) {
        return NULL;
    }
    std::stringstream ss;
    ss << name << " is " << age << " years old.";
    std::string formatted = ss.str();
    const char * formatted_cstring = formatted.c_str();
    return PyUnicode_FromString(formatted_cstring);
}

static PyMethodDef cpp_methods[] = {
    {"format", cpp_format, METH_VARARGS, "Format age and name."},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

static struct PyModuleDef cpp_module = {
   PyModuleDef_HEAD_INIT,
   "cpp",   /* name of module */
   "The simplest C++ module", /* module documentation, may be NULL */
   -1,       /* size of per-interpreter state of the module,
                or -1 if the module keeps state in global variables. */
   cpp_methods
};

PyMODINIT_FUNC
PyInit_cpp(void)
{
    return PyModule_Create(&cpp_module);
}
