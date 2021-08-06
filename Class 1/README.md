<h3>Array or List in Python
<h6>An array is a data structure consisting of a collection of elements (values or variables), each identified by at least one array index or key. In Python it is called List.
A list is a data structure in Python that is a mutable, or changeable, ordered sequence of elements. Each element or value that is inside of a list is called an item. Just as strings are defined as characters between quotes, lists are defined by having values between square brackets [ ].
  
<h3>How to create a list?  
<h6>In Python programming, a list is created by placing all the items (elements) inside square brackets [], separated by commas.

It can have any number of items and they may be of different types (integer, float, string etc.).

      # empty list
      my_list = []

      # list of integers
      my_list = [1, 2, 3]

      # list with mixed data types
      my_list = [1, "Hello", 3.4]  
  
 A list can also have another list as an item. This is called a nested list.
  
      # nested list
      my_list = ["mouse", [8, 4, 6], ['a']]
  
<h3>Access List Elements
<h6>There are various ways in which we can access the elements of a list.
  
      # List indexing

      my_list = ['p', 'r', 'o', 'b', 'e']

      # Output: p
      print(my_list[0])

      # Output: o
      print(my_list[2])

      # Output: e
      print(my_list[4])

      # Nested List
      n_list = ["Happy", [2, 0, 1, 5]]

      # Nested indexing
      print(n_list[0][1])

      print(n_list[1][3])

      # Error! Only integer can be used for indexing
      print(my_list[4.0])  
  
Output
  
      p
      o
      e
      a
      5
      Traceback (most recent call last):
        File "<string>", line 21, in <module>
      TypeError: list indices must be integers or slices, not float
  
<h4>Negative indexing
<h6>Python allows negative indexing for its sequences. The index of -1 refers to the last item, -2 to the second last item and so on.

      # Negative indexing in lists
      my_list = ['p','r','o','b','e']

      print(my_list[-1])

      print(my_list[-5])
  
When we run the above program, we will get the following output:

      e
      p  

  ![Alt Text](https://cdn.programiz.com/sites/tutorial2program/files/python-list-index.png)
  
  ><h3>For more details https://www.programiz.com/python-programming/list
  
<h3>Complexity of an algorithm
<h6>Complexity of an algorithm is a measure of the amount of time and/or space required by an algorithm for an input of a given size (n).
<h4>Types of complexity
<h6>  
     1. Time Complexity
     2. Space Complexity
  
