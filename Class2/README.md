<h1>:bookmark:Basic OOP
<h6>Object-Oriented Programming(OOP), is all about creating “objects”. An object is a group of interrelated variables and functions. These variables are often referred to as properties of the object and functions are referred to as the behavior of the objects. These objects provide a better and clear structure for the program.

For example, a car can be an object. If we consider the car as an object then its properties would be – its color, its model, its price, its brand, etc. And its behavior/function would be acceleration, slowing down, gear change.

Another example- If we consider a dog as an object then its properties would be- his color, his breed, his name, his weight, etc. And his behavior/function would be walking, barking, playing, etc.

Object-Oriented programming is famous because it implements the real-world entities like objects, hiding, inheritance, etc in programming. It makes visualization easier because it is close to real-world scenarios.

<h3>1. What is a Class?  
<h6>A straight forward answer to this question is- A class is a collection of objects.  Unlike the primitive data structures, <h5>classes are data structures that the user defines. <h6>They make the code more manageable. 

Let’s see how to define a class below:
  
     class class_name:
         class body

We define a class with a keyword “class” following the class_name and semicolon. And we consider everything you write under this after using indentation as its body. To make this more understandable let’s see an example.

Consider the case of a car showroom. You want to store the details of each car. Let’s start by defining a class first-

     class Car:
         pass
  
That’s it!  
  
<h3>2. Objects and object instantiation
  
<h6>When we define a class only the description or a blueprint of the object is created. There is no memory allocation until we create its object. The object or instance contains real data or information.

Instantiation is nothing but creating a new object/instance of a class. Let’s create the object of the above class we defined-
  
     obj1 = Car()
  
Try printing this object-

     print(obj1)
  
![Alt Text](https://cdn.analyticsvidhya.com/wp-content/uploads/2020/08/a1.png)

Since our class was empty, it returns the address where the object is stored i.e 0x7fc5e677b6d8
  
<h3>Class constructor
<h6>The job of the class constructor is to assign the values to the data members of the class when an object of the class is created.In Python the __init__() method is called the constructor and is always called when an object is created.
  
There can be various properties of a car such as its name, color, model, brand name, engine power, weight, price, etc. We’ll choose only a few for understanding purposes:
  
      class Car:
          def __init__(self, name, color):
              self.name = name
              self.color = color 
  
Now let’s talk about the parameter of__init__() method. So, the first parameter of this method has to be self. Then only will the rest of the parameters come.  

The two statements inside the constructor method are –

1. self.name = name
2. self.color = color
  
This will create new attributes namely name and color and then assign the value of the respective parameters to them. The “self” keyword represents the instance of the class. By using the “self” keyword we can access the attributes and methods of the class. It is useful in method definitions and in variable initialization. The “self” is explicitly used every time we define a method.

Note: You can create attributes outside of this__init__() method also. But those attributes will be universal to the whole class and you will have to assign the value to them.

Suppose all the cars in your showroom are Sedan and instead of specifying it again and again you can fix the value of car_type as Sedan by creating an attribute outside the__init__() .  
  
        class Car:
            car_type = "Sedan"                 #class attribute
            
            def __init__(self, name, color):
                self.name = name               #instance attribute   
                self.color = color             #instance attribute  
  
Here, Instance attributes refer to the attributes inside the constructor method i.e self.name and self.color. And, Class attributes refer to the attributes outside the constructor method i.e car_type.  Class attributes are the variables defined directly in the class that are shared by all objects of the class. Instance attributes are attributes or properties attached to an instance of a class. Instance attributes are defined in the constructor.
 
  
<h1>:bookmark:Mutable and Immutable in Python
<h3>Mutable
<h6>Mutable is when something is changeable or has the ability to change. In Python, ‘mutable’ is the ability of objects to change their values. These are often the objects that store a collection of data.
  
Objects of built-in type that are mutable are:

  1. Lists
  2. Sets
  3. Dictionaries
  4. User-Defined Classes (It purely depends upon the user to define the characteristics)  
  
<h3>Immutable
<h6>Immutable is the when no change is possible over time. In Python, if the value of an object cannot be changed over time, then it is known as immutable. Once created, the value of these objects is permanent.
  
Objects of built-in type that are immutable are:

  1. Numbers (Integer, Rational, Float, Decimal, Complex & Booleans)
  2. Strings
  3. Tuples
  4. Frozen Sets
  5. User-Defined Classes (It purely depends upon the user to define the characteristics)

Object mutability is one of the characteristics that makes Python a dynamically typed language. Though Mutable and Immutable in Python is a very basic concept, it can at times be a little confusing due to the intransitive nature of immutability.  
  
  
  
<h3>Referrences

<h6>https://www.analyticsvidhya.com/blog/2020/09/object-oriented-programming/

  https://www.javatpoint.com/abstraction-in-python
  
  https://www.mygreatlearning.com/blog/understanding-mutable-and-immutable-in-python/#1a
  
  https://guides.github.com/features/mastering-markdown/
  
  
