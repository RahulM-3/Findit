#!/bin/bash
# https://github.com/pollev/bash_progress_bar - See license at end of file



# Constants
CODE_SAVE_CURSOR="\033[s"
CODE_RESTORE_CURSOR="\033[u"
CODE_CURSOR_IN_SCROLL_AREA="\033[1A"

# Variables

CURRENT_NR_LINES=0

setup() {
	tput civis
    # If trapping is enabled, we will want to activate it whenever we setup the scroll area and remove it when we break the scroll area
    
	lines=$(tput lines)
    CURRENT_NR_LINES=$lines
    let lines=$lines-4
    # Scroll down a bit to avoid visual glitch when the screen area shrinks by one row
    echo -en "\n"

    # Save cursor
    echo -en "$CODE_SAVE_CURSOR"
    # Set scroll region (this will place the cursor in the top left)
    echo -en "\033[0;${lines}r"

    # Restore cursor but ensure its inside the scrolling area
    echo -en "$CODE_RESTORE_CURSOR"
    echo -en "$CODE_CURSOR_IN_SCROLL_AREA"

}

display() {
	
	setup

    lines=$(tput lines)
    let l=$lines-3

    # Save cursor
    echo -en "$CODE_SAVE_CURSOR"
	
	# remove old stat from status bar
	echo -en "\033[${l};0f"
	tput el
	echo "$1"
	
	tput el
	echo "$2"
	
	tput el
	echo "$3"

	tput el
	echo "$4"

    # Restore cursor position
    echo -en "$CODE_RESTORE_CURSOR"
}

clear_progress_bar() {
	
	lines=$(tput lines)
   
   	let l=$lines

    # Save cursor
    echo -en "$CODE_SAVE_CURSOR"
	
	# remove old stat from status bar
	echo -en "\033[${l};0f"
	tput el

	let l=$lines-1
	echo -en "\033[${l};0f"
	tput el

	let l=$lines-2
	echo -en "\033[${l};0f"
	tput el

	let l=$lines-3
	echo -en "\033[${l};0f"
	tput el

    # Restore cursor position
    echo -en "$CODE_RESTORE_CURSOR"
	echo -en "$CODE_CURSOR_IN_SCROLL_AREA"
	
	echo -en "\n\n"
	/bin/bash && exit 1
}



# SPDX-License-Identifier: MIT
#
# Copyright (c) 2018--2020 Polle Vanhoof
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
