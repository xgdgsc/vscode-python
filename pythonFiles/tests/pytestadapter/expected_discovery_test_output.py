# change to fit for everyone
TEST_DATA_PATH = (
    "/Users/eleanorboyd/vscode-python/pythonFiles/tests/pytestadapter/.data"
)
UNITTEST_FOLDER_PATH = "/Users/eleanorboyd/vscode-python/pythonFiles/tests/pytestadapter/.data/unittest_folder"

# This is the expected output for the empty_discovery.py file.
# └──

empty_discovery_pytest_expected_output = {
    "name": ".data",
    "path": TEST_DATA_PATH,
    "type_": "folder",
    "children": [],
    "id_": TEST_DATA_PATH,
}

# This is the expected output for the simple_pytest.py file.
# └── simple_pytest.py
#    └── test_function

simple_discovery_pytest_expected_output = {
    "name": ".data",
    "path": TEST_DATA_PATH,
    "type_": "folder",
    "children": [
        {
            "name": "simple_pytest.py",
            "path": f"{TEST_DATA_PATH}/simple_pytest.py",
            "type_": "file",
            "id_": f"{TEST_DATA_PATH}/simple_pytest.py",
            "children": [
                {
                    "name": "test_function",
                    "path": f"{TEST_DATA_PATH}/simple_pytest.py",
                    "lineno": "5",
                    "type_": "test",
                    "id_": "simple_pytest.py::test_function",
                    "runID": "simple_pytest.py::test_function",
                }
            ],
        }
    ],
    "id_": TEST_DATA_PATH,
}

# This is the expected output for the unittest_pytest_same_file.py file.
# ├── unittest_pytest_same_file.py
#   ├── TestExample
#   │   └── test_true_unittest
#   └── test_true_pytest

unit_pytest_same_file_discovery_expected_output = {
    "name": ".data",
    "path": TEST_DATA_PATH,
    "type_": "folder",
    "children": [
        {
            "name": "unittest_pytest_same_file.py",
            "path": TEST_DATA_PATH + "/unittest_pytest_same_file.py",
            "type_": "file",
            "id_": TEST_DATA_PATH + "/unittest_pytest_same_file.py",
            "children": [
                {
                    "name": "TestExample",
                    "path": TEST_DATA_PATH + "/unittest_pytest_same_file.py",
                    "type_": "class",
                    "children": [
                        {
                            "name": "test_true_unittest",
                            "path": TEST_DATA_PATH + "/unittest_pytest_same_file.py",
                            "lineno": "8",
                            "type_": "test",
                            "id_": "unittest_pytest_same_file.py::TestExample::test_true_unittest",
                            "runID": "unittest_pytest_same_file.py::TestExample::test_true_unittest",
                        }
                    ],
                    "id_": "unittest_pytest_same_file.py::TestExample",
                },
                {
                    "name": "test_true_pytest",
                    "path": TEST_DATA_PATH + "/unittest_pytest_same_file.py",
                    "lineno": "12",
                    "type_": "test",
                    "id_": "unittest_pytest_same_file.py::test_true_pytest",
                    "runID": "unittest_pytest_same_file.py::test_true_pytest",
                },
            ],
        }
    ],
    "id_": TEST_DATA_PATH,
}

# This is the expected output for the unittest_folder tests
# └── unittest_folder
#    ├── test_add.py
#    │   └── TestAddFunction
#    │       ├── test_add_negative_numbers
#    │       └── test_add_positive_numbers
#    └── test_subtract.py
#        └── TestSubtractFunction
#            ├── test_subtract_negative_numbers
#            └── test_subtract_positive_numbers

unittest_folder_discovery_expected_output = {
    "name": ".data",
    "path": "/Users/eleanorboyd/vscode-python/pythonFiles/tests/pytestadapter/.data",
    "type_": "folder",
    "children": [
        {
            "name": "unittest_folder",
            "path": UNITTEST_FOLDER_PATH,
            "type_": "folder",
            "id_": UNITTEST_FOLDER_PATH,
            "children": [
                {
                    "name": "test_add.py",
                    "path": UNITTEST_FOLDER_PATH + "/test_add.py",
                    "type_": "file",
                    "id_": UNITTEST_FOLDER_PATH + "/test_add.py",
                    "children": [
                        {
                            "name": "TestAddFunction",
                            "path": UNITTEST_FOLDER_PATH + "/test_add.py",
                            "type_": "class",
                            "children": [
                                {
                                    "name": "test_add_negative_numbers",
                                    "path": UNITTEST_FOLDER_PATH + "/test_add.py",
                                    "lineno": "15",
                                    "type_": "test",
                                    "id_": "unittest_folder/test_add.py::TestAddFunction::test_add_negative_numbers",
                                    "runID": "unittest_folder/test_add.py::TestAddFunction::test_add_negative_numbers",
                                },
                                {
                                    "name": "test_add_positive_numbers",
                                    "path": UNITTEST_FOLDER_PATH + "/test_add.py",
                                    "lineno": "11",
                                    "type_": "test",
                                    "id_": "unittest_folder/test_add.py::TestAddFunction::test_add_positive_numbers",
                                    "runID": "unittest_folder/test_add.py::TestAddFunction::test_add_positive_numbers",
                                },
                            ],
                            "id_": "unittest_folder/test_add.py::TestAddFunction",
                        }
                    ],
                },
                {
                    "name": "test_subtract.py",
                    "path": UNITTEST_FOLDER_PATH + "/test_subtract.py",
                    "type_": "file",
                    "id_": UNITTEST_FOLDER_PATH + "/test_subtract.py",
                    "children": [
                        {
                            "name": "TestSubtractFunction",
                            "path": UNITTEST_FOLDER_PATH + "/test_subtract.py",
                            "type_": "class",
                            "children": [
                                {
                                    "name": "test_subtract_negative_numbers",
                                    "path": UNITTEST_FOLDER_PATH + "/test_subtract.py",
                                    "lineno": "15",
                                    "type_": "test",
                                    "id_": "unittest_folder/test_subtract.py::TestSubtractFunction::test_subtract_negative_numbers",
                                    "runID": "unittest_folder/test_subtract.py::TestSubtractFunction::test_subtract_negative_numbers",
                                },
                                {
                                    "name": "test_subtract_positive_numbers",
                                    "path": UNITTEST_FOLDER_PATH + "/test_subtract.py",
                                    "lineno": "11",
                                    "type_": "test",
                                    "id_": "unittest_folder/test_subtract.py::TestSubtractFunction::test_subtract_positive_numbers",
                                    "runID": "unittest_folder/test_subtract.py::TestSubtractFunction::test_subtract_positive_numbers",
                                },
                            ],
                            "id_": "unittest_folder/test_subtract.py::TestSubtractFunction",
                        }
                    ],
                },
            ],
        }
    ],
    "id_": "/Users/eleanorboyd/vscode-python/pythonFiles/tests/pytestadapter/.data",
}

# This is the expected output for the dual_level_nested_folder tests
#   |- dual_level_nested_folder
#  |  |- test_top_folder.py
#  |  |  |- test_top_function_t
#  |  |  |- test_top_function_f
#  |  |
#  |  |- nested_folder_one
#  |     |- test_bottom_folder.py
#  |        |- test_bottom_function_t
#  |        |- test_bottom_function_f

dual_level_nested_folder_expected_output = {
    "name": ".data",
    "path": TEST_DATA_PATH,
    "type_": "folder",
    "children": [
        {
            "name": "dual_level_nested_folder",
            "path": f"{TEST_DATA_PATH}/dual_level_nested_folder",
            "type_": "folder",
            "id_": f"{TEST_DATA_PATH}/dual_level_nested_folder",
            "children": [
                {
                    "name": "test_top_folder.py",
                    "path": f"{TEST_DATA_PATH}/dual_level_nested_folder/test_top_folder.py",
                    "type_": "file",
                    "id_": f"{TEST_DATA_PATH}/dual_level_nested_folder/test_top_folder.py",
                    "children": [
                        {
                            "name": "test_top_function_t",
                            "path": f"{TEST_DATA_PATH}/dual_level_nested_folder/test_top_folder.py",
                            "lineno": "5",
                            "type_": "test",
                            "id_": "dual_level_nested_folder/test_top_folder.py::test_top_function_t",
                            "runID": "dual_level_nested_folder/test_top_folder.py::test_top_function_t",
                        },
                        {
                            "name": "test_top_function_f",
                            "path": f"{TEST_DATA_PATH}/dual_level_nested_folder/test_top_folder.py",
                            "lineno": "9",
                            "type_": "test",
                            "id_": "dual_level_nested_folder/test_top_folder.py::test_top_function_f",
                            "runID": "dual_level_nested_folder/test_top_folder.py::test_top_function_f",
                        },
                    ],
                },
                {
                    "name": "nested_folder_one",
                    "path": f"{TEST_DATA_PATH}/dual_level_nested_folder/nested_folder_one",
                    "type_": "folder",
                    "id_": f"{TEST_DATA_PATH}/dual_level_nested_folder/nested_folder_one",
                    "children": [
                        {
                            "name": "test_bottom_folder.py",
                            "path": f"{TEST_DATA_PATH}/dual_level_nested_folder/nested_folder_one/test_bottom_folder.py",
                            "type_": "file",
                            "id_": f"{TEST_DATA_PATH}/dual_level_nested_folder/nested_folder_one/test_bottom_folder.py",
                            "children": [
                                {
                                    "name": "test_bottom_function_t",
                                    "path": f"{TEST_DATA_PATH}/dual_level_nested_folder/nested_folder_one/test_bottom_folder.py",
                                    "lineno": "5",
                                    "type_": "test",
                                    "id_": "dual_level_nested_folder/nested_folder_one/test_bottom_folder.py::test_bottom_function_t",
                                    "runID": "dual_level_nested_folder/nested_folder_one/test_bottom_folder.py::test_bottom_function_t",
                                },
                                {
                                    "name": "test_bottom_function_f",
                                    "path": f"{TEST_DATA_PATH}/dual_level_nested_folder/nested_folder_one/test_bottom_folder.py",
                                    "lineno": "9",
                                    "type_": "test",
                                    "id_": "dual_level_nested_folder/nested_folder_one/test_bottom_folder.py::test_bottom_function_f",
                                    "runID": "dual_level_nested_folder/nested_folder_one/test_bottom_folder.py::test_bottom_function_f",
                                },
                            ],
                        }
                    ],
                },
            ],
        }
    ],
    "id_": TEST_DATA_PATH,
}

# This is the expected output for the double_nested_folder tests
# └── double_nested_folder
#    └── nested_folder_one
#        └── nested_folder_two
#            └── test_nest.py
#                └── test_function

double_nested_folder_expected_output = {
    "name": ".data",
    "path": TEST_DATA_PATH,
    "type_": "folder",
    "children": [
        {
            "name": "double_nested_folder",
            "path": f"{TEST_DATA_PATH}/double_nested_folder",
            "type_": "folder",
            "id_": f"{TEST_DATA_PATH}/double_nested_folder",
            "children": [
                {
                    "name": "nested_folder_one",
                    "path": f"{TEST_DATA_PATH}/double_nested_folder/nested_folder_one",
                    "type_": "folder",
                    "id_": f"{TEST_DATA_PATH}/double_nested_folder/nested_folder_one",
                    "children": [
                        {
                            "name": "nested_folder_two",
                            "path": f"{TEST_DATA_PATH}/double_nested_folder/nested_folder_one/nested_folder_two",
                            "type_": "folder",
                            "id_": f"{TEST_DATA_PATH}/double_nested_folder/nested_folder_one/nested_folder_two",
                            "children": [
                                {
                                    "name": "test_nest.py",
                                    "path": f"{TEST_DATA_PATH}/double_nested_folder/nested_folder_one/nested_folder_two/test_nest.py",
                                    "type_": "file",
                                    "id_": f"{TEST_DATA_PATH}/double_nested_folder/nested_folder_one/nested_folder_two/test_nest.py",
                                    "children": [
                                        {
                                            "name": "test_function",
                                            "path": f"{TEST_DATA_PATH}/double_nested_folder/nested_folder_one/nested_folder_two/test_nest.py",
                                            "lineno": "5",
                                            "type_": "test",
                                            "id_": "double_nested_folder/nested_folder_one/nested_folder_two/test_nest.py::test_function",
                                            "runID": "double_nested_folder/nested_folder_one/nested_folder_two/test_nest.py::test_function",
                                        }
                                    ],
                                }
                            ],
                        }
                    ],
                }
            ],
        }
    ],
    "id_": TEST_DATA_PATH,
}