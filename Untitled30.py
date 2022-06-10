{
  "metadata": {
    "language_info": {
      "codemirror_mode": {
        "name": "python",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.8"
    },
    "kernelspec": {
      "name": "python",
      "display_name": "Pyolite",
      "language": "python"
    }
  },
  "nbformat_minor": 4,
  "nbformat": 4,
  "cells": [
    {
      "cell_type": "code",
      "source": "\ndef getPairs(arr, n, sum):\n \n    count = 0  \n    for i in range(0, n):\n        for j in range(i + 1, n):\n            if arr[i] + arr[j] == sum:\n                count += 1\n \n    return count\n \narr = [1, 5, 7, -1, 5]\nn = len(arr)\nsum = 6\nprint(\"Pair is : \",\n      getPairs(arr, n, sum))",
      "metadata": {
        "trusted": true
      },
      "execution_count": 1,
      "outputs": [
        {
          "name": "stdout",
          "text": "Pair is :  3\n",
          "output_type": "stream"
        }
      ]
    },
    {
      "cell_type": "code",
      "source": "def rl(a, start, end):\n    while start < end:\n        a[start], a[end] = a[end], a[start]\n        start += 1\n        end -= 1\n \na = [3, 4, 5, 6, 7, 8]\nprint(a)\nrl(a, 0, 5)\nprint(\"RL is: \")\nprint(a)",
      "metadata": {
        "trusted": true
      },
      "execution_count": 3,
      "outputs": [
        {
          "name": "stdout",
          "text": "[3, 4, 5, 6, 7, 8]\nRL is: \n[8, 7, 6, 5, 4, 3]\n",
          "output_type": "stream"
        }
      ]
    },
    {
      "cell_type": "code",
      "source": "def areRotations(string1, string2):\n    size1 = len(string1)\n    size2 = len(string2)\n    temp = ''\n \n    \n    if size1 != size2:\n        return 0\n \n    \n    temp = string1 + string1\n \n    \n    if (temp.count(string2)> 0):\n        return 1\n    else:\n        return 0\n \n\nstring1 = \"NAMAN\"\nstring2 = \"NAMAN\"\n \nif areRotations(string1, string2):\n    print (\"Strings are rotations of each other\")\nelse:\n    print (\"Strings are not rotations of each other\")",
      "metadata": {
        "trusted": true
      },
      "execution_count": 4,
      "outputs": [
        {
          "name": "stdout",
          "text": "Strings are rotations of each other\n",
          "output_type": "stream"
        }
      ]
    },
    {
      "cell_type": "code",
      "source": "NO_OF_CHARS = 256\n \n\ndef getCharCountArray(string):\n    count = [0] * NO_OF_CHARS\n    for i in string:\n        count[ord(i)]+= 1\n    return count\n \n\ndef firstNonRepeating(string):\n    count = getCharCountArray(string)\n    index = -1\n    k = 0\n \n    for i in string:\n        if count[ord(i)] == 1:\n            index = k\n            break\n        k += 1\n \n    return index\n \n\nstring = \"Chromecast build-in\"\nindex = firstNonRepeating(string)\nif index == 1:\n    print (\"Either all characters are repeating or string is empty\")\nelse:\n    print (\"First non-repeating character is\" , string[index])\n ",
      "metadata": {
        "trusted": true
      },
      "execution_count": 5,
      "outputs": [
        {
          "name": "stdout",
          "text": "First non-repeating character is C\n",
          "output_type": "stream"
        }
      ]
    },
    {
      "cell_type": "code",
      "source": "def TowerOfHanoi(n , from_rod, to_rod, aux_rod):\n    if n == 0:\n        return\n    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)\n    print(\"Move disk\",n,\"from rod\",from_rod,\"to rod\",to_rod)\n    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)\n         \nn = 4\nTowerOfHanoi(n, 'A', 'C', 'B')",
      "metadata": {
        "trusted": true
      },
      "execution_count": 6,
      "outputs": [
        {
          "name": "stdout",
          "text": "Move disk 1 from rod A to rod B\nMove disk 2 from rod A to rod C\nMove disk 1 from rod B to rod C\nMove disk 3 from rod A to rod B\nMove disk 1 from rod C to rod A\nMove disk 2 from rod C to rod B\nMove disk 1 from rod A to rod B\nMove disk 4 from rod A to rod C\nMove disk 1 from rod B to rod C\nMove disk 2 from rod B to rod A\nMove disk 1 from rod C to rod A\nMove disk 3 from rod B to rod C\nMove disk 1 from rod A to rod B\nMove disk 2 from rod A to rod C\nMove disk 1 from rod B to rod C\n",
          "output_type": "stream"
        }
      ]
    },
    {
      "cell_type": "code",
      "source": "s = \"*-A/BC-/AKL\"\n \n\nstack = []\n \noperators = set(['+', '-', '*', '/', '^'])\n \ns = s[::-1]\n\nfor i in s:\n \n   \n    if i in operators:\n \n        a = stack.pop()\n        b = stack.pop()\n \n        temp = a+b+i\n        stack.append(temp)\n \n\n    else:\n        stack.append(i)\n \n\nprint(*stack)",
      "metadata": {
        "trusted": true
      },
      "execution_count": 7,
      "outputs": [
        {
          "name": "stdout",
          "text": "ABC/-AK/L-*\n",
          "output_type": "stream"
        }
      ]
    },
    {
      "cell_type": "code",
      "source": "def prefixToInfix(prefix):\n    stack = []\n     \n    \n    i = len(prefix) - 1\n    while i >= 0:\n        if not isOperator(prefix[i]):\n             \n            \n            stack.append(prefix[i])\n            i -= 1\n        else:\n           \n            \n            str = \"(\" + stack.pop() + prefix[i] + stack.pop() + \")\"\n            stack.append(str)\n            i -= 1\n     \n    return stack.pop()\n \ndef isOperator(c):\n    if c == \"*\" or c == \"+\" or c == \"-\" or c == \"/\" or c == \"^\" or c == \"(\" or c == \")\":\n        return True\n    else:\n        return False\n \n\nif __name__==\"__main__\":\n    str = \"*-A/BC-/AKL\"\n    print(prefixToInfix(str))",
      "metadata": {
        "trusted": true
      },
      "execution_count": 8,
      "outputs": [
        {
          "name": "stdout",
          "text": "((A-(B/C))*((A/K)-L))\n",
          "output_type": "stream"
        }
      ]
    },
    {
      "cell_type": "code",
      "source": "\ndef areBracketsBalanced(expr):\n    stack = []\n \n    \n    for char in expr:\n        if char in [\"(\", \"{\", \"[\"]:\n \n           \n            stack.append(char)\n        else:\n \n            if not stack:\n                return False\n            current_char = stack.pop()\n            if current_char == '(':\n                if char != \")\":\n                    return False\n            if current_char == '{':\n                if char != \"}\":\n                    return False\n            if current_char == '[':\n                if char != \"]\":\n                    return False\n \n    \n    if stack:\n        return False\n    return True\n \n \n\nif __name__ == \"__main__\":\n    expr = \"{()}[]\"\n \n   \n    if areBracketsBalanced(expr):\n        print(\"Balanced\")\n    else:\n        print(\"Not Balanced\")",
      "metadata": {
        "trusted": true
      },
      "execution_count": 9,
      "outputs": [
        {
          "name": "stdout",
          "text": "Balanced\n",
          "output_type": "stream"
        }
      ]
    },
    {
      "cell_type": "code",
      "source": "class StackNode:\n     \n    def __init__(self, data):\n         \n        self.data = data\n        self.next = None\n \nclass Stack:\n     \n    def __init__(self):\n          \n        self.top = None\n      \n    # Push and pop operations\n    def push(self, data):\n     \n        if (self.top == None):\n            self.top = StackNode(data)\n            return\n         \n        s = StackNode(data)\n        s.next = self.top\n        self.top = s\n      \n    def pop(self):\n     \n        s = self.top\n        self.top = self.top.next\n        return s\n  \n    # Prints contents of stack\n    def display(self):\n     \n        s = self.top\n         \n        while (s != None):\n            print(s.data, end = ' ')\n            s = s.next\n         \n    # Reverses the stack using simple\n    # linked list reversal logic.\n    def reverse(self):\n \n        prev = self.top\n        cur = self.top\n        cur = cur.next\n        succ = None\n        prev.next = None\n         \n        while (cur != None):\n            succ = cur.next\n            cur.next = prev\n            prev = cur\n            cur = succ\n         \n        self.top = prev\n     \n# Driver code\nif __name__=='__main__':\n     \n    s = Stack()\n    s.push(1)\n    s.push(2)\n    s.push(3)\n    s.push(4)\n     \n    print(\"Original Stack\")\n    s.display()\n    print()\n      \n    # Reverse\n    s.reverse()\n  \n    print(\"Reversed Stack\")\n    s.display()\n      ",
      "metadata": {
        "trusted": true
      },
      "execution_count": 11,
      "outputs": [
        {
          "name": "stdout",
          "text": "Original Stack\n4 3 2 1 \nReversed Stack\n1 2 3 4 ",
          "output_type": "stream"
        }
      ]
    },
    {
      "cell_type": "code",
      "source": "# Class to make a Node\nclass Node:\n\t# Constructor which assign argument to nade's value\n\tdef __init__(self, value):\n\t\tself.value = value\n\t\tself.next = None\n\n\t# This method returns the string representation of the object.\n\tdef __str__(self):\n\t\treturn \"Node({})\".format(self.value)\n\t\n\t# __repr__ is same as __str__\n\t__repr__ = __str__\n\n\nclass Stack:\n\t# Stack Constructor initialise top of stack and counter.\n\tdef __init__(self):\n\t\tself.top = None\n\t\tself.count = 0\n\t\tself.minimum = None\n\t\t\n\t# This method returns the string representation of the object (stack).\n\tdef __str__(self):\n\t\ttemp = self.top\n\t\tout = []\n\t\twhile temp:\n\t\t\tout.append(str(temp.value))\n\t\t\ttemp = temp.next\n\t\tout = '\\n'.join(out)\n\t\treturn ('Top {} \\n\\nStack :\\n{}'.format(self.top,out))\n\t\t\n\t# __repr__ is same as __str__\n\t__repr__=__str__\n\t\n\t# This method is used to get minimum element of stack\n\tdef getMin(self):\n\t\tif self.top is None:\n\t\t\treturn \"Stack is empty\"\n\t\telse:\n\t\t\tprint(\"Minimum Element in the stack is: {}\" .format(self.minimum))\n\n\n\n\t# Method to check if Stack is Empty or not\n\tdef isEmpty(self):\n\t\t# If top equals to None then stack is empty\n\t\tif self.top == None:\n\t\t\treturn True\n\t\telse:\n\t\t# If top not equal to None then stack is empty\n\t\t\treturn False\n\n\t# This method returns length of stack\t\n\tdef __len__(self):\n\t\tself.count = 0\n\t\ttempNode = self.top\n\t\twhile tempNode:\n\t\t\ttempNode = tempNode.next\n\t\t\tself.count+=1\n\t\treturn self.count\n\n\t# This method returns top of stack\t\n\tdef peek(self):\n\t\tif self.top is None:\n\t\t\tprint (\"Stack is empty\")\n\t\telse:\n\t\t\tif self.top.value < self.minimum:\n\t\t\t\tprint(\"Top Most Element is: {}\" .format(self.minimum))\n\t\t\telse:\n\t\t\t\tprint(\"Top Most Element is: {}\" .format(self.top.value))\n\n\t# This method is used to add node to stack\n\tdef push(self,value):\n\t\tif self.top is None:\n\t\t\tself.top = Node(value)\n\t\t\tself.minimum = value\n\t\t\n\t\telif value < self.minimum:\n\t\t\ttemp = (2 * value) - self.minimum\n\t\t\tnew_node = Node(temp)\n\t\t\tnew_node.next = self.top\n\t\t\tself.top = new_node\n\t\t\tself.minimum = value\n\t\telse:\n\t\t\tnew_node = Node(value)\n\t\t\tnew_node.next = self.top\n\t\t\tself.top = new_node\n\t\tprint(\"Number Inserted: {}\" .format(value))\n\n\t# This method is used to pop top of stack\n\tdef pop(self):\n\t\tif self.top is None:\n\t\t\tprint( \"Stack is empty\")\n\t\telse:\n\t\t\tremovedNode = self.top.value\n\t\t\tself.top = self.top.next\n\t\t\tif removedNode < self.minimum:\n\t\t\t\tprint (\"Top Most Element Removed :{} \" .format(self.minimum))\n\t\t\t\tself.minimum = ( ( 2 * self.minimum ) - removedNode )\n\t\t\telse:\n\t\t\t\tprint (\"Top Most Element Removed : {}\" .format(removedNode))\n\n\t\t\t\t\n\t\t\t\n\t\n# Driver program to test above class\nstack = Stack()\n\nstack.push(3)\nstack.push(5)\nstack.getMin()\nstack.push(2)\nstack.push(1)\nstack.getMin()\t\nstack.pop()\nstack.getMin()\nstack.pop()\nstack.peek()\n\n\n",
      "metadata": {
        "trusted": true
      },
      "execution_count": 12,
      "outputs": [
        {
          "name": "stdout",
          "text": "Number Inserted: 3\nNumber Inserted: 5\nMinimum Element in the stack is: 3\nNumber Inserted: 2\nNumber Inserted: 1\nMinimum Element in the stack is: 1\nTop Most Element Removed :1 \nMinimum Element in the stack is: 2\nTop Most Element Removed :2 \nTop Most Element is: 5\n",
          "output_type": "stream"
        }
      ]
    },
    {
      "cell_type": "code",
      "source": "",
      "metadata": {},
      "execution_count": null,
      "outputs": []
    }
  ]
}