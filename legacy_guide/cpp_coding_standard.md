# C++ Coding Standard

## Naming System

### Variable

- Use **lower_case** naming system _(ex: `distance`, `kick_direction`)_.
- For **class's attribute**, use **lower_case** with `m_` prefix _(ex: `m_device`, `m_nearest_player`)_.

- For **constant** Variable, use **lower_case** with `k_` prefix _(ex: `k_pi`, `k_broadcast_id`)_.
  :::{Note}
  For **class's constant atribute**, choose `k_` prefix instead of `m_` prefix or both prefixes.
  :::

- For **global** variable, use **lower_case** with `g_` prefix _(ex: `g_standard_input`, `g_config`)_.
  :::{Note}
  For **global constant** variable, choose `g_` prefix instead of `k_` prefix or both prefixes.
  :::

### Function

- Use **camelCase** naming system _(ex: `calculateDistance()`, `isEnable()`)_.
  :::{Note}
  It is recommended to use a **function** name that has at least 2 words to prevent conflict with a **variable** name.
  :::
  :::{Note}
  An abbreviations should not be all in uppercase, _(ex: `getId()` instead of `getID()`)_.
  :::

### Enum

- Use **PascalCase** naming system with `e` prefix _(ex: `ePacketId`, `eRole`)_.
- For **enum label**, Use **PascalCase** without any prefix _(ex: `eRole::Striker`, `eRole::LeftWing`)_.
  :::{Note}
  An abbreviations should not be all in uppercase, _(ex: `PacketId` instead of `PacketID`)_.
  :::

### Class

- Use **PascalCase** naming system _(ex: `Ball`, `ColorClassifier`)_.
  :::{Note}
  An abbreviations should not be all in uppercase, _(ex: `UdpController` instead of `UDPController`)_.
  :::

### Namespace

- Use **lower_case** naming system with only single word. _(ex: `kuro`, `eigen`)_.
  :::{Note}
  It is recommended to abbreviates a longer **namespace** word _(ex: `dynamixel` to `dxl`)_.
  :::

### Macro

- Use **UPPER_CASE** naming system _(ex: `LINUX`, `CUDA_ENABLE`)_.

## File System

### C++ Header File

- Use **lower_case** naming system with `.hpp` extension _(ex: `device.hpp`. `robot.hpp`)_.
- It must be placed in `include` directory according to it hierarchy _(ex: place `camera.hpp` in `include/device/camera.hpp`)_.
- Should not contains macro and definition of function/method, except for single line function/method.
- Always add header guard in the header file.
  Header guard must be written in **UPPER_CASE** and consists of `<PROJECT_NAME>_<HIERARCHY>_<HEADER_NAME>_HPP_`. Example of `include/device/camera.hpp` header file for **Test** project:
  ``` c++
  #ifndef TEST_DEVICE_CAMERA_HPP_
  #define TEST_DEVICE_CAMERA_HPP_

  // write code here

  #endif
  ```

:::{Note}
A **C++** header file should only contain declaration of one class.
> Although subclass is fine in this condition, if the subclass contains more methods and attributes, it is better to put it in another **C++** header file.
:::

### C++ Source File

- use **lower_case** naming system with `.cpp` extension _(ex: `device.cpp`, `robot.cpp`)_.
- It must be placed in `source` directory.
- Should only contains definition of function/method.
- May contains macro.

:::{Note}
If the **C++** source file is not for executable _(containing `main()`)_, then the **C++** source file should only contains definition of the corresponding **C++** header file.
:::

### CMake File

- Use `CMakeLists.txt` for the main **CMake** file. Place it in the project root directory.
- Use **PascalCase** naming system with `.cmake` extension for additional **CMake** file.

## Comment Rule

- Use single line comment instead of block comment, even for comment with multiple line. Example:
  ``` c++
    // comment for single line

    // comment for
    // multiple line
  ```
- **Separate the comment mark with the comment content**.
  So it should be `// comment content` instead of `//comment content`.
- **Write comments as you code**. Because you will never go back later and write a comment in your code.
- **Let the code explains itself First**. Do not explain everything that the code does in the comment.
- **Write comments so anyone could easily know what the code does**.
  You could do it by giving note on _"why is it doing this and not else?"_, "_what this variable exactly is?"_, etc.
- **Only comment if it is necessary to**. If you ever find some unnecessary comment, just remove it, or adjust it with better words.

## Class Rule

- **Each class must have an implementation in a header file and in a source file** _(only if there is still a method that has not been defined in the header file)_. Except for subclass of another class.
- **Always initialize an attribute in the class**. Except for non pointer class attribute.
- **Class's member label** must be ordered by **public**, **protected**, then **private**.
  A label shouldn't be indented. Example:
  ``` c++
  class Foo
  {
  public:

    Foo();

  protected:

    int getId() { return m_id; }

  private:

    int m_id;
  }
  ```
  :::{Note}
  The same rule also apply for class definition in the **source file**.
  :::

- **Class's member** must be ordered by **constructor**, **destructor**, **static method**, **method**, **enum**,  **constant attribute**, **static attribute**, then **attribute**. Example:
  :::{Note}
  A **class** calls its member variable as an **attribute** and its member function as a **method**.
  :::
  ``` c++
  class Foo
  {
  public:

    // constructor
    Foo()
    Foo(int a);

    // destructor
    ~Foo();

    // static method
    static int getA();

    // method
    void setB(int val);

  private:

    // enum
    enum eType
    {
      BigFoo  = 0,
      BigGoo  = 1
    }

    // constant attribute
    const int k_c_value = 255;

    // static attribute
    static int m_a_value = 0;

    // attribute
    int m_b_value = 0;
  }
  ```
  :::{Note}
  The same rule also apply for class definition in the **source file**.
  :::

## Braces Rule

- **Place brace under and inline with keywords**.
  Never place initial brace on the same line and the trailing brace inline on its own line with the keyword.
  :::{Note}
  The reason of this rule is with placing the initial and the trailing brace in the same indentation could make it easy to know where the block of code start and end. Example:
  ``` c++
  // do
  if (condition)
  {
    // do something
  }

  // don't
  if (condition) {
    // do something
  }
  ```
  :::
- **Always use block of code**. Except for single statement, place it under the condition with indentation. Example:
  :::{Note}
  This rule does not apply for else with single statement if there are braces above it.
  :::
  ``` c++
  if (condition)
    // single statement

  if (condition)
    // single statement
  else
    // single statement

  if (condition)
  {
    // long
    // statement
  }
  else
  {
    // single statement
  }
  ```

## Indentation Rule

- **Indentation should only use 2 spaces for each level**.
  :::{Note}
  The reason of this rule is larger indentation could limit code writing and 2 space is actually enough to distinguish between indentations.
  :::
- **The label of switch statement should not be indented**. Example:
  :::{Note}
  The reason of this rule is because switch actually should work just as multiple if else. Just think of each case as an if statement. that is why identation is not needed.
  :::
  ``` c++
  switch (a)
  {
  case 0:
    // do something
    break;

  case 1:
    // do something
    break;
  }
  ```
- **The contents of a namespace should not be indented**. Example:
  ``` c++
  namespace goo
  {
  static const int k_something = 0;

  class Foo
  {
    // definition
  };
  }
  ```

## Parenthesis Rule

- **Do not put parenthesis next to keywords**. Put a space betwen. Example:
  :::{Note}
  The reason of this rule is because keywords are not functions. By putting parenthesis next to keywords, keywords and function names are made to look alike.
  :::
  ``` c++
  // do
  if (condition)
    // do something

  // don't
  if(condition)
    // do something
  ```
- **Put parenthesis in a complex mathematical operation**.
  ``` c++
  // do
  int a = b * (c / d);

  // don't
  int a = b * c / d;
  ```
