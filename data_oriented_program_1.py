# # data oriented programming with python

# def sort_by_name(students):
#     """
#     sorts a list of names of the students 
#     """
#     students.sort(key = lambda student:student["name"])

#     return students

# # main program

# def main():
#     """ The main program """
#     students = [

#         {
#             "name":"John",
#             "age":34
#         }
#         ,
#         {
#             "name":"Roshan",
#             "age":23
#         }
#         ,
#         {
#             "name":"Alice",
#             "age":43
#         },

#         {
#             "name":"Babe",
#             "age":23
#         }
#     ]

#     sorted_students = sort_by_name(students)


# # driver code 

# if __name__ =="__main__":
#     main()

def sort_by_name(students):
  """Sorts a list of students by their name.

  Args:
    students: A list of students.

  Returns:
    A list of students sorted by their name.
  """

  students.sort(key=lambda student: student["name"])

  return students


def main():
  """The main function."""

  students = [
      {
          "name": "Alice",
          "age": 18,
      },
      {
          "name": "Bob",
          "age": 19,
      },
      {
          "name": "Carol",
          "age": 20,
      },
  ]

  sorted_students = sort_by_name(students)

  print(sorted_students)


if __name__ == "__main__":
  main()

