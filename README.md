# image-encryption-system
This is a desktop-primarily based GUI software for encrypting and decrypting pictures the usage of chaos idea. The utility is built the usage of Python and leverages libraries such as tkinter for the GUI and Pillow for photograph manipulation.

Features

Encrypt and decrypt .Jpg and .Png images using chaos-based totally encryption techniques.

Simple and intuitive GUI with grid format.

Automatically resizes pix for show in the utility.

Prerequisites

Python three.Eight or better ought to be set up.

Download Python

Install required dependencies by way of jogging the subsequent command:

pip deploy -r necessities.Txt

How to Run

Clone this repository:

git clone https://github.Com/charan618-sys/image-encryption-system.Git

Navigate to the mission directory:

cd image-encryption-system

Run the gui.Py record to launch the utility:

python gui.Py

Usage Instructions

Launch the software using the instructions above.

Use the "Select Image" button to choose an image report (.Jpg or .Png) out of your gadget.

Enter an encryption key (need to be 80 bits or 10 characters lengthy).

Click "Encrypt Image" to encrypt the chosen photo.

The encrypted image will be displayed and saved as abc.Png in the contemporary directory.

Click "Decrypt Image" to decrypt the formerly encrypted image.

The decrypted photograph will be displayed and saved as dabc.Png within the current listing.

Troubleshooting

Common Errors:

ModuleNotFoundError: No module named 'Chaos'

Ensure the sys.Course.Append line is blanketed in gui.Py:

import sys
import os
sys.Course.Append(os.Course.Join(os.Getcwd(), "Chaos"))

pip isn't recognized as an internal or outside command

Ensure Python and pip are added for your system's PATH during set up.

AttributeError: module 'PIL.Image' has no attribute 'ANTIALIAS'

Replace Image.ANTIALIAS with Image.LANCZOS within the code.

Dependencies

tkinter: For GUI advent.

Pillow: For picture manipulation.

Os: To manipulate record paths and directories.

Install all dependencies the usage of the following command:

pip install -r requirements.Txt

License

This assignment is licensed beneath the MIT License.

Acknowledgments

Special thanks to the participants and the network for their guide in implementi
