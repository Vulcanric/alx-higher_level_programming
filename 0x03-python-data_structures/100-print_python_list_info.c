#include <Python.h>
#include <stdio.h>

void print_python_list_info(PyObject *p);
/**
 * print_python_list_info - prints basic information about Python list
 * @p: pointer to a PyObject type (list)
 * Return: Nothing
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t i; /* Index / Iterator */
	Py_ssize_t list_size;
	PyListObject *list_Obj; /* pointer to a list object type */

	/* Checking if the object passed is a list type */
	if (PyObject_TypeCheck(p, &PyList_Type))
	{
		/* Typecasting p to be a list type */
		list_Obj = (PyListObject *)p;

		list_size = PyList_GET_SIZE(p); /* getting the amount of items in the list */
		printf("[*] Size of the Python List = %zd\n", list_size);
		printf("[*] Allocated = %zd\n", list_Obj->allocated);

		for (i = 0; i < list_size; i++)
		{
			/* Check if the item at particular index is a particular type */
			if (PyList_Check(list_Obj->ob_item[i]))
				printf("Element %zd: list\n", i);

			else if (PyTuple_Check(list_Obj->ob_item[i]))
				printf("Element %zd: tuple\n", i);

			else if (PyUnicode_Check(list_Obj->ob_item[i]))
				printf("Element %zd: str\n", i);

			else if (PyBytes_Check(list_Obj->ob_item[i]))
				printf("Element %zd: char\n", i);

			else if (PyLong_Check(list_Obj->ob_item[i]))
				printf("Element %zd: int\n", i);

			else if (PyFloat_Check(list_Obj->ob_item[i]))
				printf("Element %zd: float\n", i);

			else if (PyBool_Check(list_Obj->ob_item[i]))
				printf("Element %zd: bool\n", i);

			else if (PyDict_Check(list_Obj->ob_item[i]))
				printf("Element %zd: dict\n", i);

			else if (PySet_Check(list_Obj->ob_item[i]))
				printf("Element %zd: set\n", i);

			else if (PyFrozenSet_Check(list_Obj->ob_item[i]))
				printf("Element %zd: frozenset\n", i);

			else if (PyComplex_Check(list_Obj->ob_item[i]))
				printf("Element %zd: complex\n", i);

			else if (PyCallable_Check(list_Obj->ob_item[i]))
				printf("Element %zd: callable\n", i);

			else
				printf("Element %zd: unknown\n", i);
		}
	}
	/*
	 * else   If it is not a Python list object type ...
		PyErr_SetString(PyExc_TypeError, "Expected a list object\n");
	*/
}
