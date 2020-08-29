{\rtf1\ansi\ansicpg1252\cocoartf2512
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 ArialMT;}
{\colortbl;\red255\green255\blue255;\red46\green49\blue51;}
{\*\expandedcolortbl;;\cssrgb\c23529\c25098\c26275;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs28 \cf2 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 import jogovelha\
import sys\
\
erroInicializar = False\
jogo = jogovelha.inicializar()\
\
if len(jogo) != 3:\
	erroInicializar = True\
else:\
	for linha in jogo:\
		if len(linha) != 3:\
			erroInicializar = True\
		else:\
			for elemento in linha:\
				if elemento != '.':\
					erroInicializar = True\
if erroInicializar:\
	sys.exit(1)\
else:\
	sys.exit(0)}