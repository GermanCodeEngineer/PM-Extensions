# Classes Extension

**The classes extension** by [GermanCodeEngineer](https://github.com/GermanCodeEngineer/) provides Python-like **functions, classes, methods, variables** and many other features of Object Orientated Programming.

Please do not forget to read the [features](#features).

Thanks to [jwklong](https://github.com/jwklong), [DogeisCut](https://github.com/dogeiscut), [Sharkpool](https://github.com/SharkPool-SP) and especially [**VeryGoodScratcher42**](https://github.com/Lego7set) for inspiration.

# Features

# Blocks

## Scoped Variables
---
```scratch
set var [myVar] to [my value] in current scope::#428af5
```
- Creates or updates a variable in the current scope.

---
```scratch
(get var [myVar]::#428af5)
```
- Gets the value of a variable visible from the current or outer scopes.

---
```scratch
<var [myVar] exists in [all scopes v]?::#428af5>
<var [myVar] exists in [local scope v]?::#428af5>
<var [myVar] exists in [global scope v]?::#428af5>
```
- Checks whether a variable exists in the selected scope range.

---
```scratch
delete var [myVar] in current scope::#428af5
```
- Deletes a variable from the current scope.

---
```scratch
(all variables in [all scopes v]::#428af5)
(all variables in [local scope v]::#428af5)
(all variables in [global scope v]::#428af5)
```
- Returns all variable names visible in the selected scope range as an array.

---
```scratch
create local variable scope {
}::#428af5
```
- Runs the enclosed blocks inside a new local variable scope.

---
```scratch
bind [non-local v] variable [myVar] to current scope::#428af5
bind [global v] variable [myVar] to current scope::#428af5
```
- Links a global or non-local variable into the current scope.

<br><br>
## Define Classes

---
```scratch
create class at var [MyClass] (class being created::#428af5) {
}::#428af5
```
- Creates a new class, stores it in the chosen variable.

---
```scratch
create subclass at var [MySubclass] with superclass [MyClass] (class being created::#428af5) {
}::#428af5
```
- Creates a subclass with the given superclass, stores it in a variable.

---
```scratch
create class named [MyClass] (class being created::#428af5) {

}::#428af5
```
- *Note: This block is really a reporter with a branch, but it can not be rendered accurately here.*
- Creates and returns a new class with the given name.

---
```scratch
create subclass named [MySubclass] with superclass [MyClass] (class being created::#428af5) {
}::#428af5
```
- *Note: This block is really a reporter with a branch, but it can not be rendered accurately here.*
- Creates and returns a new subclass with the given superclass.

---
```scratch
on class [MyClass] (class being created::#428af5) {
}::#428af5
```
- Runs the enclosed blocks as if they were inside the selected class definition. This allows you to e.g. add methods to already defined classes.

---
```scratch
(class being created::#428af5)
```
- Returns the class currently being defined.

<br><br>
## Use Classes

---
```scratch
<is [MySubclass] a subclass of [MyClass] ?::#428af5>
```
- Checks whether one class inherits from another.

---
```scratch
(get superclass of [MySubclass]::#428af5)
```
- Returns the superclass of a class, or Nothing if it has none.

<br><br>
## Class Members

### Define Instance Methods

---
```scratch
definẹ instance method [myMethod] (self::#428af5) {
}::#428af5
```
- Defines an instance method on the current class.

---
```scratch
definẹ [init v] instance method (self::#428af5) {
}::#428af5
definẹ [as string v] instance method (self::#428af5) {
}::#428af5
```
- Defines a special instance method.

---
```scratch
(self::#428af5)
```
- Reports the current instance inside a method.

---
```scratch
(call super method [myMethod] with positional args (parse [\["argument1", "argument2"\]] as an array::#ff513d)::#428af5)
```
- Calls an instance method from the superclass of the current object.

---
```scratch
(call super init method with positional args (parse [\["argument1", "argument2"\]] as an array::#ff513d)::#428af5)
```
- Calls the superclass init method for the current object.

<br><br>
### Define Getters & Setters

---
```scratch
definẹ getter [myAttr] (self::#428af5) {
}::#428af5
```
- Defines a getter method for an attribute on the current class.

---
```scratch
definẹ setter [myAttr] (self::#428af5) (value::#428af5) {
}::#428af5
```
- Defines a setter method for an attribute on the current class.

---
```scratch
(value::#428af5)
```
- Reports the incoming value inside a setter method.

<br><br>
### Define Operator Methods

---
```scratch
definẹ operator method [left add v] (other value::#428af5) {
}::#428af5
definẹ operator method [right add v] (other value::#428af5) {
}::#428af5
// AND MANY MORE
definẹ operator method [right mod v] (other value::#428af5) {
}::#428af5
definẹ operator method [greater or equal v] (other value::#428af5) {
}::#428af5
// AND MANY MORE
```
- Defines custom behavior for an operator on instances of the current class.

---
```scratch
(other value::#428af5)
```
- Reports the other operand inside an operator method.

<br><br>
### Define Static Methods & Class Variables

---
```scratch
on [MyClass] set class variable [myVariable] to [my value]::#428af5
```
- Sets a class variable on the selected class.

---
```scratch
(get class variable [myVariable] of [MyClass]::#428af5)
```
- Gets a class variable from the selected class.

---
```scratch
on [MyClass] delete class variable [myVariable]::#428af5
```
- Deletes a class variable from the selected class.

---
```scratch
definẹ static method [myMethod] {
}::#428af5
```
- Defines a static method on the current class.

---
```scratch
([instance method v] names of class [MyClass]::#428af5)
([static method v] names of class [MyClass]::#428af5)
([getter method v] names of class [MyClass]::#428af5)
([setter method v] names of class [MyClass]::#428af5)
([operator method v] names of class [MyClass]::#428af5)
([class variable v] names of class [MyClass]::#428af5)
```
- Returns the names of members of the selected type for a class.

<br><br>
## Working with Instances

<br><br>
### Create & Inspect

---
```scratch
(create instance of class [MyClass] with positional args (parse [\["argument1", "argument2"\]] as an array::#ff513d)::#428af5)
```
- Creates an instance of a class and passes the given positional arguments to its init method.

---
```scratch
<is [my instance] an instance of [MyClass] ?::#428af5>
```
- Checks whether an instance belongs to a class or one of its subclasses.

---
```scratch
(get class of [my instance]::#428af5)
```
- Returns the class that created an instance.

<br><br>
### Attributes

---
```scratch
on [my instance] set attribute [myAttr] to [my value]::#428af5
```
- Sets an attribute on an instance or calls its setter if one exists.

---
```scratch
(attribute [myAttr] of [my instance]::#428af5)
```
- Gets an attribute from an instance or calls its getter if one exists.

---
```scratch
(all attributes of [my instances]::#428af5)
```
- Returns all direct instance attributes as an object.

<br><br>
### Call Methods

---
```scratch
(on [my instance] call method [myMethod] with positional args (parse [\["argument1", "argument2"\]] as an array::#ff513d)::#428af5)
```
- Calls an instance method on an object with positional arguments.

---
```scratch
(on [MyClass] call static method [myMethod] with positional args (parse [\["argument1", "argument2"\]] as an array::#ff513d)::#428af5)
```
- Calls a static method on a class with positional arguments.

---
```scratch
(get static method [myMethod] of [MyClass] as function::#428af5)
```
- Returns a static method from a class as a callable function value.

<br><br>
## Functions

<br><br>
### Configure Before Define

---
```scratch
configure next function: argument names (parse [\["person", "message"\]] as an array::#ff513d) defaults (parse [\["Hello World!"\]] as an array::#ff513d)::#428af5
```
- Configures the argument names and default values used by the next function or method definition.

<br><br>
### Define

---
```scratch
create function at var [myFunction] {
}::#428af5
```
- Creates a function and stores it in the chosen variable.

---
```scratch
create function named [myFunction] {
}::#428af5
```
- *Note: This block is really a reporter with a branch, but it can not be rendered accurately here.*
- Creates and returns a function with the given name.

<br><br>
### Inside Functions & Methods

---
```scratch
return [my value]::#428af5 cap
```
- Returns a value from the current function or method and exits it.

---
```scratch
(call function [myFunction] with positional args (parse [\["Bob", "Goodbye."\]] as an array::#ff513d)::#428af5)
```
- Calls a function value with positional arguments.

<br><br>
### Utilities

---
```scratch
([my instance] as string::#428af5)
```
- Converts a value to its string form, using a class's special as string method when available.

---
```scratch
(typeof <true::operators>::#428af5)
(typeof (blank array::#ff513d)::#428af5)
(typeof (blank object::#f9bb58)::#428af5)
(typeof [my instance]::#428af5)
// And many more
```
- Returns a readable type name for a value.

---
```scratch
<[my instance] is [other instance] ?::#428af5>
```
- Checks whether two values are exactly the same value (the same instance).

---
```scratch
(Nothing::#428af5)
```
- Returns the cool Nothing value like None in python.

---
```scratch
execute expression (call function [myFunction] with positional args (parse [\["Bob", "Goodbye."\]] as an array::#ff513d)::#428af5)::#428af5
```
- Evaluates the input expression without performing any additional action. This allows you to e.g. use the function call block (a reporter) in a script.
