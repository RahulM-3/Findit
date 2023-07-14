#!/bin/bash
source ~/findit/./status_bar.sh


if [ "$1" == "display" ]; then
	display "$2 $3" "$4 $5" "$6 $7" "$8 $9"
elif [ "$1" == "destroy" ]; then
	destroy
elif [ "$1" == "clear" ]; then
	clear_progress_bar
fi
