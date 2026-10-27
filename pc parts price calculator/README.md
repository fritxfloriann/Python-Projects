# PC Parts Price Calculator

A price calculator program for calculating the price of each PC component based on your price entry. This program is lightweight and should only be for basic calculations for prices of PC parts. It is interactive and can calculate the total cost of the prices you have entered in the calculations. This program is for tech enthusiasts, PC builders, and those who need help with calculating the costs of their PC build.

Caution: Enter prices wisely and accurately. One mistake can give the wrong answer, the wrong price, and may lead to loss of progress with your entries. If you think you made a mistake, you can restart the program and try again. Future commits will provide fail-safes, more error handling, and a feature to reset your work.

## Installation

To run this program, you need Python 3.10 or newer, alongside a basic terminal or a command prompt. If you want to modify the PPPC code, have a code editor to tinker with PPPC.

Reminder: The program uses Python's built-in libraries and the math module. No need to install other dependencies or other components.

**First, download the file.**

Clone the repository using Git:

`git clone https://github.com/fritxfloriann/pc_parts_price_calculator.git`

Alternatively, download the repository as a ZIP archive and extract it.

**Second, open the project directory.**

Enter the following command:

`cd interactive_pc_price_calculator`

**More importantly, check your Python version.**

You can check your Python version with the following command:

`python --version`

*If you are on systems that use Python 3, type the following command:*

`python3 --version`

*Remember, PPPC requires Python 3.10 or newer to run.*

**Lastly, locate the file.**

The file name for PPPC is called `interactive_pc_price_calculator.py`. Remember where you downloaded it. It should be in your `Recent` or `Downloads` directory if you are on Windows. If you're in any other operation systems like Linux or macOS, the file should be available on your file explorer.

Once you are inside the program, a prompt will show up, prompting you to enter your component model and the price for it. If you're unsure on what to do, the section below shows the instructions of the program and how to use it.

## Instructions & Usage

In this section, you will learn how to use PPPC to calculate the total cost of your PC build. The code in the file totals up the cost of the entered prices and gives you the results upon typing all of the prices of eight components listed. Whenever you want to calculate new prices or total up the price of a new build, you can always use the program to total up the cost.

**First, launch the `.py` file.**

Once you have located the file `interactive_pc_price_calculator.py`, you should open it in your terminal or command prompt to run the program.

It will launch your terminal or command prompt and initialize its introduction, interface, and the starting price of the CPU.

**Second, enter the prices of each component.**

In the following questions given by the program, you must give a price for the given component in the prompt.

Here is an example to get a clue.

`Welcome to PC Price Calculator! Enter wisely to get the most accurate answer.`

`Enter each component's model and price in United States Dollars (USD).`

`CPU model`

`Enter model: AMD Ryzen 5 7500.`

`CPU price`

`Enter Price: $299.`

*The entries are for demonstration only. It is not included in the answers or entries in the actual program.*

Click Enter and continue adding prices to each component. Once you have answered the prices of all eight components, the program automatically ends the prompts and starts calculating the total costs.

**Lastly, it will print out a formatted text with the costs and the total prices.**

Once you are done entering the prices of all eight components, hitting Enter will result in the program calculating the total costs of the build.

It should look something like this:

---

PC Build Price Breakdown

Component
  Model
  Price

CPU
Model
$199.00

GPU
Model
$150.00

Motherboard
Model
$ 99.00

RAM
Model
$ 99.00

Storage
Model
$199.00

Case
Model
$299.00

Cooling
Model
$ 55.00
PSU
Model
$ 23.00


Total
$1123.00


---

*The prices shown in the example are just a hypothetical build.*

There you have it! You have the total price of the entire PC Build. And of course, this does not account for other important parts like thermal paste, accessories, etc. But for a basic program for calculating the costs of a PC Build, this is more than enough.

The latest commit (October 19, 2026) introduced a component model prompt, which gives the final price breakdown the exact model of what the component is.

## IMPORTANT!!

The `pc price calculator.py` is deprecated and is only for testing purposes and basic functionality. You can still use it for basic calculations, but the new PPPC is superior and has more features than the original calculator. This makes it stand out from the source code and gives clearer instructions on which file to use. I recommend using the newer build, known as `interactive_pc_price_calculator.py`, to calculate your PC build!

The source code is for testing and archival purposes only. Feel free to experiment with the original code for PPPC. Thank you for your understanding.
