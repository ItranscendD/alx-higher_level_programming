#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - Print basic info about Python bytes objects
 * @p: Python bytes object
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *str;

	printf("[.] bytes object info\n");
	printf("  size: %ld\n", PyBytes_Size(p));
	printf("  trying string: %s\n", PyBytes_AsString(p));
	printf("  first %ld bytes: ", PyBytes_Size(p) < 10 ? PyBytes_Size(p) : 10);

	size = PyBytes_Size(p);
	str = PyBytes_AsString(p);

	for (i = 0; i < size && i < 10; i++)
	{
		printf("%02x", (unsigned char)str[i]);
		if (i + 1 < size && i + 1 < 10)
			printf(" ");
	}
	printf("\n");
}

/**
 * print_python_list - Print basic info about Python lists
 * @p: Python list object
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *item;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < PyList_Size(p); i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);

		if (PyBytes_Check(item))
			print_python_bytes(item);
	}
}
