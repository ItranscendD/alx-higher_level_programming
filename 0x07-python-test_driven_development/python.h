#ifndef PYTHON_H
#define PYTHON_H

typedef struct
{
	PyObject_VAR_HEAD
	long ob_shash;
	int ob_sstate;
	int ob_sval;
} PyASCIIObject;

typedef struct
{
	PyObject_VAR_HEAD
	Py_ssize_t ob_allocated;
	union
	{
		struct
	{
		PyObject_VAR_HEAD
	} ob_base;
		struct
	{
		unsigned char ob_digit[1];
	} ob_digit;
	};
} PyLongObject;

typedef struct
{
	PyObject_VAR_HEAD
	long ob_shash;
	int ob_sstate;
	int ob_sval;
} PyCompactUnicodeObject;

typedef struct
{
	PyObject_VAR_HEAD
	Py_ssize_t ob_allocated;
	union
	{
		struct
	{
		PyObject_VAR_HEAD
	} ob_base;
		struct
	{
		unsigned char ob_digit[1];
	} ob_digit;
	};
} PyASCIIStringObject;

typedef struct
{
	PyObject_VAR_HEAD
	int ob_shash;
	int ob_sstate;
	int ob_sval;
} PyCompactStringObject;

typedef struct
{
	PyObject_VAR_HEAD
	Py_ssize_t ob_allocated;
	union
	{
		struct
		{
		PyObject_VAR_HEAD
		} ob_base;
		struct
		{
			unsigned char ob_digit[1];
		} ob_digit;
	};
} PyCompactByteArrayObject;

typedef struct
{
	PyObject_VAR_HEAD
	Py_ssize_t ob_allocated;
	union
	{
		struct
		{
			PyObject_VAR_HEAD
		} ob_base;
		struct
		{
		unsigned char ob_digit[1];
		} ob_digit;
	};
} PyCompactTupleObject;

typedef struct
{
	PyObject_VAR_HEAD
	Py_ssize_t ob_allocated;
	union
	{
		struct
		{
			PyObject_VAR_HEAD
		} ob_base;
		struct
		{
		unsigned char ob_digit[1];
		} ob_digit;
	};
} PyCompactListObject;

typedef struct
{
	PyObject_VAR_HEAD
	Py_ssize_t ob_allocated;
	union
	{
		struct
		{
			PyObject_VAR_HEAD
		} ob_base;
		struct
		{
		unsigned char ob_digit[1];
		} ob_digit;
	};
} PyCompactSetObject;

typedef struct
{
	PyObject_VAR_HEAD
	Py_ssize_t ob_allocated;
	union
	{
		struct
		{
			PyObject_VAR_HEAD
		} ob_base;
		struct
		{
		unsigned char ob_digit[1];
		} ob_digit;
	};
} PyCompactDictObject;

void print_python_string(PyObject *p);

#endif /* PYTHON_H */
