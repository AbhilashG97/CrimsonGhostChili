# Ghidra Tutorial

This post will contain my notes on how to use Ghidra to reverse engineer executables. 

## Introduction

> Ghidra is a free and open source reverse engineering tool developed by the National Security Agency. The binaries were released at RSA Conference in March 2019; the sources were published one month later on GitHub. 

Ghidra is free and open source. 

## Using Ghidra

This section will contain a brief tutorial on how to load a binary into Ghidra and how to analyse the binary. 

1.  Create a new project in Ghidra for the binary you want to examine. 
    1. Select the non-shared project for now.
1.  Open the project that you created. 
1.  Import the binary into the project.
    1.  This can be done clicking on the ```File``` menu and selecting the ```Import file``` option. 
1.  Importing the file will present you with a few options. 
    1.  Keep the default options, ghidra will select the best options for you.
1.  Double click on the imported binary to analyze it.  
    1.  Select the ```Decompiler Parameter ID``` option in the ```Analyse options``` window. 
1.  To analyse the binary load the main function into the decompiler view.
    1.  Ghidra unlike IDA Pro uses the listing view and decompiler view to analyze the binary. IDA Pro focuses more on the control flow graph. 
    1.  Go to the ```symbols tree window``` present on the left side and search for ```main```. The search results will display ```main``` function. Double click the main function to view the decompiled code.    
    1.  The psuedocode can be made better by adding the necessary ```C Standard Syntax```to the main function.  
1. Have fun!

This is a very short introduction to ghidra and how to analyse the binary. 

## Installation and other things

Download ghidra, unzip it and place the unzipped folder in ```/opt```.

To create a desktop icon for ghidra, paste this file in ```/usr/share/applications```. The file should end with ```.desktop``` extension. 

```bash
[Desktop Entry]
Categories=Application;Development;
Comment[en_US]=Ghidra Software Reverse Engineering Suite
Comment=Ghidra Software Reverse Engineering Suite
Exec=/opt/ghidra/ghidraRun
GenericName[en_US]=Ghidra Software Reverse Engineering Suite
GenericName=Ghidra Software Reverse Engineering Suite
Icon=/opt/ghidra/support/ghidra.ico
MimeType=
Name[en_US]=Ghidra 9.1.1
Name=Ghidra 9.1.1
Path=/opt/ghidra/
StartupNotify=false
Terminal=false
TerminalOptions=
Type=Application
Version=1.0
X-DBUS-ServiceName=
X-DBUS-StartupType=none
X-KDE-SubstituteUID=false
X-KDE-Username=
```