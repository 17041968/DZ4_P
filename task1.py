#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
import math

def CheckNumbers(number):
	flag = True
	for i in range(2, math.ceil(math.sqrt(number))):
		flag = bool(number % i)
		if not flag:
			break
	return flag 

def FindDivager(number):
	divagers = []
	for i in range(2, number//2):
		while CheckNumbers(i) and number % i == 0:
			if number % i == 0:
				divagers.append(i)
				number /= i
	print(divagers)

number = 60
FindDivager(number)