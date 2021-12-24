#!/bin/bash

pre="/usr/local/bin/"

case $1 in
	install|"")
		echo "mkdir -p $pre"
		mkdir -p $pre

		echo "cp screenrecorder.py "$pre"screenrecorder"
		cp screenrecorder.py "$pre"screenrecorder

		echo "chmod +x "$pre"screenrecorder"
		chmod +x "$pre"screenrecorder

		if [ $? -eq 0 ];then
			printf "\e[1;32mInstallation completed.\e[0m\n"
		else
			printf "\e[1;31mError during installation.\e[0m\n"
		fi
		;;
	uninstall|remove)
		echo $pre"screenrecorder"
		rm "$pre"screenrecorder

		if [ $? -eq 0 ];then
			printf "\e[1;32mUninstallation completed.\e[0m\n"
		else
			printf "\e[1;31mError during uninstallation.\e[0m\n"
		fi
		;;
esac
