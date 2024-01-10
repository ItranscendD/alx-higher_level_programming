#include <Python.h>

/**
 * print_python_string - Prints Python strings
 * @p: Pointer to a Python object
 */
void print_python_string(PyObject *p)
{
	const char *str;
	Py_ssize_t len;

	printf("[.] string object info\n");
	if (!PyUnicode_Check(p))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	str = PyUnicode_AsUTF8AndSize(p, &len);

	printf("  type: %s\n", Py_TYPE(p)->tp_name);
	printf("  length: %ld\n", len);
	printf("  value: %s\n", str);
}
