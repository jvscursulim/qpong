# QPong - 12 Days of Qiskit

![Image](https://github.com/jvscursulim/qpong/blob/master/assets/images/Logo.png)

## Description
Reproducing an implementation of a quantum verison of the game pong called QPong.

## How to install and run

* Step 1: Clone this repository
```bash
git clone https://github.com/jvscursulim/qpong.git
```

* Step 2: Access the folder with the files of the game
```bash
cd qpong
```

* Step 3: Create a virtual environment

```bash
python -m venv env
```

* Step 4: Activate your virtual environment
Windows (Powershell)
```bash
env/Scripts/Activate.ps1
```
Linux
```bash
source env/bin/activate
```

* Step 5: Install pipenv

```bash
pip install -r requirements.txt
```
OR
```bash
pip install pipenv
```

* Step 6: Install the requiments using pipenv
```bash
pipenv install
```

* Step 7: Run the game using the following command
```bash
python qpong.py
```

* Step 8: Have fun and learn a little bit about quantum computing! :)

## Instructions

### Cursor movement
* W: UP
* S: DOWN
* A: LEFT
* D: RIGHT

### Apply quantum gates to move the paddle
* Z: Apply a Z gate
* X: Apply a X gate
* Y: Apply a Y gate
* H: Apply a Hadamard gate
* Z + C: Apply a CZ gate
* X + C: Apply a CNOT gate
* Y + C: Apply a CY gate
* H + C: Apply a controlled Hadamard gate
* Z + LEFT/RIGHT ARROW: Apply Rz gate (You can change the rotation angle pressing LEFT/RIGHT ARROW)
* X + LEFT/RIGHT ARROW: Apply Rx gate (You can change the rotation angle pressing LEFT/RIGHT ARROW)
* Y + LEFT/RIGHT ARROW: Apply Ry gate (You can change the rotation angle pressing LEFT/RIGHT ARROW)
* Z + LEFT/RIGHT ARROW + C: Apply a controlled Rz gate
* X + LEFT/RIGHT ARROW + C: Apply a controlled Rx gate
* Y + LEFT/RIGHT ARROW + C: Apply a controlled Ry gate
* The combination of keys that produce a controlled gate + UP/DOWN ARROW: Changes the control qubit of the gate.
* SPACE: Reset the quantum circuit

## Printscreens

![Image](https://github.com/jvscursulim/qpong/blob/master/assets/images/Logo.png)
![Image](https://github.com/jvscursulim/qpong/blob/master/assets/images/Logo.png)
![Image](https://github.com/jvscursulim/qpong/blob/master/assets/images/Logo.png)

## References:

1. [QPong from scratch - Part 1](https://www.youtube.com/watch?v=C-tCZAC1Qq8&t=6s)
2. [QPong from scracth - Part 2](https://www.youtube.com/watch?v=PYthycN_Tq8&t=3360s)
3. [QPong version 1](https://github.com/qpong/qpong)
4. [QPong Unity version](https://github.com/QPong/QPong-Unity)
5. [QPong 12 Days of Qiskit Livestream code](https://github.com/QPong/qpong-livestream/tree/reference)
