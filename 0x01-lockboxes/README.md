OPEN ALL BOXES

This project provides a solution to determine if all the locked boxes can be opened based on the keys contained within the boxes.

PROBLEM DESCRIPTION

You are given n locked boxes, each numbered sequentially from 0 to n - 1. Each box may contain keys to other boxes. A key with the same number as a box can open that box. The first box, boxes[0], is unlocked. The task is to determine if all boxes can be opened.

APPROACH

The solution uses a depth-first search (DFS) algorithm to explore the boxes and their corresponding keys. It starts with the first box, marks it as visited, and adds its keys to a stack. The algorithm continues to iterate until the stack is empty or all boxes have been visited.

USAGE

Clone the repository:

git clone <https://github.com/Nanagyamera/alx-interview.git>

Navigate to the project directory:

cd 0x01-lockboxes

Run the program by executing the following command:

python 0-lockboxes.py

Modify the boxes list in the open_boxes.py file to test different scenarios.

The program will output True if all boxes can be opened, and False otherwise.

DEPENDENCIES

The project does not have any external dependencies. It is written in Python 3 and uses only built-in libraries.

CONTRIBUTIONS

Contributions to this project are welcome. If you encounter any issues or have suggestions for improvement, please open an issue or submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for more information.

AUTHOR
Nana Gyamera - nanagyamera3@gmail.com
