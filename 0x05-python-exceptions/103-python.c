#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - prints info about Python lists
 * @p: Python object (list)
 */
void print_python_list(PyObject *p)
{
    Py_ssize_t size, alloc, i;
    PyObject *item;

    printf("[*] Python list info\n");

    size = PyList_Size(p);
    alloc = ((PyListObject *)p)->allocated;

    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", alloc);

    for (i = 0; i < size; ++i)
    {
        item = PyList_GetItem(p, i);
        printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
        if (PyBytes_Check(item))
            print_python_bytes(item);
    }
}

/**
 * print_python_bytes - prints info about Python bytes
 * @p: Python object (bytes)
 */
void print_python_bytes(PyObject *p)
{
    Py_ssize_t size, i;
    char *str;

    printf("[.] bytes object info\n");

    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    str = PyBytes_AsString(p);

    printf("  size: %zd\n", size);
    printf("  trying string: %s\n", str);

    printf("  first 10 bytes:");
    for (i = 0; i < size && i < 10; ++i)
        printf(" %02x", str[i]);

    printf("\n");
}

/**
 * print_python_float - prints info about Python float
 * @p: Python object (float)
 */
void print_python_float(PyObject *p)
{
    printf("[.] float object info\n");

    if (!PyFloat_Check(p))
    {
        printf("  [ERROR] Invalid Float Object\n");
        return;
    }

    printf("  value: %f\n", ((PyFloatObject *)p)->ob_fval);
}
