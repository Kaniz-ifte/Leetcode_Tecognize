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
  
<h1>:bookmark:OOP principles/Main features of OOP/Fundamental concepts of OOP
<h6>Now, there are four fundamental concepts of Object-oriented programming – 
  
  1. Inheritance
  2. Encapsulation 
  3. Polymorphism
  4. Data abstraction
  
<h3>:label:Inheritance in Python Class
  
<h6>Inheritance is the procedure in which one class inherits the attributes and methods of another class.  The class whose properties and methods are inherited is known as Parent class. And the class that inherits the properties from the parent class is the Child class.

The interesting thing is, along with the inherited properties and methods, a child class can have its own properties and methods.

How to inherit a parent class? Use the following syntax:
  
        class parent_class:
            body of parent class

        class child_class( parent_class):
            body of child class
  
Let’s see the implementation-
  
        class Car:          #parent class

            def __init__(self, name, mileage):
                self.name = name 
                self.mileage = mileage 

            def description(self):                
                return f"The {self.name} car gives the mileage of {self.mileage}km/l"

        class BMW(Car):     #child class
            pass

        class Audi(Car):     #child class
            def audi_desc(self):
                return "This is the description method of class Audi."  
  
  
        obj1 = BMW("BMW 7-series",39.53)
        print(obj1.description())

        obj2 = Audi("Audi A8 L",14)
        print(obj2.description())
        print(obj2.audi_desc())
  
![Alt Text](https://cdn.analyticsvidhya.com/wp-content/uploads/2020/08/a13.png)
  
We have created two child classes namely “BMW” and “Audi” who have inherited the methods and properties of the parent class “Car”.  We have provided no additional features and methods in the class BMW. Whereas one additional method inside the class Audi.

Notice how the instance method description() of the parent class is accessible by the objects of child classes with the help of obj1.description() and obj2.description(). And also the separate method of class Audi is also accessible using obj2.audi_desc().
  
<h3>:label:Encapsulation
<h6>Basically, it hides the data from the access of outsiders. Such as if an organization wants to protect an object/information from unwanted access by clients or any unauthorized person then encapsulation is the way to ensure this.

You can declare the methods or the attributes protected by using a single underscore ( _ ) before their names. Such as- self._name or def _method( ); Both of these lines tell that the attribute and method are protected and should not be used outside the access of the class and sub-classes but can be accessed by class methods and objects.

Though Python uses ‘ _ ‘ just as a coding convention, it tells that you should use these attributes/methods within the scope of the class. But you can still access the variables and methods which are defined as protected, as usual.

Now for actually preventing the access of attributes/methods from outside the scope of a class, you can use “private members“. In order to declare the attributes/method as private members, use double underscore ( __ ) in the prefix. Such as – self.__name or def __method(); Both of these lines tell that the attribute and method are private and access is not possible from outside the class.
  
      class car:

          def __init__(self, name, mileage):
              self._name = name                #protected variable
              self.mileage = mileage 

          def description(self):                
              return f"The {self._name} car gives the mileage of {self.mileage}km/l"  
  
  
      obj = car("BMW 7-series",39.53)

      #accessing protected variable via class method 
      print(obj.description())

      #accessing protected variable directly from outside
      print(obj._name)
  
      print(obj.mileage) 
  
![Alt Text](https://cdn.analyticsvidhya.com/wp-content/uploads/2020/08/a7.png)    
  
Notice how we accessed the protected variable without any error. It is clear that access to the variable is still public. Let us see how encapsulation works-
  
      class Car:

          def __init__(self, name, mileage):
              self.__name = name              #private variable        
              self.mileage = mileage 

          def description(self):                
              return f"The {self.__name} car gives the mileage of {self.mileage}km/l"
      obj = Car("BMW 7-series",39.53)

      #accessing private variable via class method 
      print(obj.description())

      #accessing private variable directly from outside
      print(obj.mileage)
      print(obj.__name)  
  
![Alt Text](https://cdn.analyticsvidhya.com/wp-content/uploads/2020/08/a8.png)  
  
When we tried accessing the private variable using the description() method, we encountered no error. But when we tried accessing the private variable directly outside the class, then Python gave us an error stating: car object has no attribute ‘__name’.

You can still access this attribute directly using its mangled name. Name mangling is a mechanism we use for accessing the class members from outside. The Python interpreter rewrites any identifier with “__var” as “_ClassName__var”. And using this you can access the class member from outside as well.
  
      class Car:

          def __init__(self, name, mileage):
              self.__name = name              #private variable        
              self.mileage = mileage 

          def description(self):                
              return f"The {self.__name} car gives the mileage of {self.mileage}km/l"
      obj = Car("BMW 7-series",39.53)

      #accessing private variable via class method 
      print(obj.description())

      #accessing private variable directly from outside
      print(obj.mileage)
      print(obj._Car__name)      #mangled name  
  
![Alt Text](https://cdn.analyticsvidhya.com/wp-content/uploads/2020/08/a9.png)

Note that the mangling rule’s design mostly avoids accidents. But it is still possible to access or modify a variable that is considered private. This can even be useful in special circumstances, such as in the debugger.  
 
> [Note:]The class members declared as private can be accessed only by the functions inside the class. ... The class member declared as Protected are inaccessible outside the class but they can be accessed by any subclass(derived class) of that class.  
  
<h3>:label:Polymorphism
<h6>This is a Greek word. If we break the term Polymorphism, we get “poly”-many and “morph”-forms. So Polymorphism means having many forms. In OOP it refers to the functions having the same names but carrying different functionalities.
  
      class Audi:
        def description(self):
          print("This the description function of class AUDI.")

      class BMW:
        def description(self):
          print("This the description function of class BMW.")
      audi = Audi()
      bmw = BMW()
      for car in (audi,bmw):
       car.description()  
 
![At Text](https://cdn.analyticsvidhya.com/wp-content/uploads/2020/08/b1.png)

When the function is called using the object audi then the function of class Audi is called and when it is called using the object bmw then the function of class BMW is called.
  
<h3>:label:Data abstraction
<h6>Abstraction is used to hide the internal functionality of the function from the users. The users only interact with the basic implementation of the function, but inner working is hidden. User is familiar with that "what function does" but they don't know "how it does."
  
  
Any class with at least one abstract function is an abstract class. In order to create an abstraction class first, you need to import ABC class from abc module. This lets you create abstract methods inside it. ABC stands for Abstract Base Class. We use the @abstractmethod decorator to define an abstract method or if we don't provide the definition to the method, it automatically becomes the abstract method. Let's understand the following example. 
  
> In Python, an abstraction is used to hide the irrelevant data/class in order to reduce the complexity. It also enhances the application efficiency. Next, we will learn how we can achieve abstraction using the Python program.An abstract base class is the common application program of the interface for a set of subclasses. It can be used by the third-party, which will provide the implementations such as with plugins. It is also beneficial when we work with the large code-base hard to remember all the classes.
  
      # Python program demonstrate  
      # abstract base class work   
      from abc import ABC, abstractmethod   
      class Car(ABC):   
          def mileage(self):   
              pass  

      class Tesla(Car):   
          def mileage(self):   
              print("The mileage is 30kmph")   
      class Suzuki(Car):   
          def mileage(self):   
              print("The mileage is 25kmph ")   
      class Duster(Car):   
           def mileage(self):   
                print("The mileage is 24kmph ")   

      class Renault(Car):   
          def mileage(self):   
                  print("The mileage is 27kmph ")   

      # Driver code   
      t= Tesla ()   
      t.mileage()   

      r = Renault()   
      r.mileage()   

      s = Suzuki()   
      s.mileage()   
      d = Duster()   
      d.mileage()    
  
In the above code, we have imported the abc module to create the abstract base class. We created the Car class that inherited the ABC class and defined an abstract method named mileage(). We have then inherited the base class from the three different subclasses and implemented the abstract method differently. We created the objects to call the abstract method.
  

> Below are the points which we should remember about the abstract base class in Python.

   1. An Abstract class can contain the both method normal and abstract method.
   2. An Abstract cannot be instantiated; we cannot create objects for the abstract class.
  
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
  
  
