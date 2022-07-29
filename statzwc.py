from typing import List
import math


def zcount(list: List[float]) -> float:
    return float(len(list))

def zmean(list: List[float]) -> float:
    return sum(list)/ zcount(list)

def zmode(list: List[float]) -> float:
    return max(set(list), key=list.count)

def zmedian(list: List[float]) -> float:
    n= (len(list)-1)
    if n %2 != 0:
       index= n//2
       return list[index]
    else:
        index= list[n//2 - 1]
        index2= list[n// 2]
        return (index+index2)/2

def zvariance(list: List[float]) -> float:
    n= zcount(list)-1
    mean= sum(list)/n
    deviations = []
    for xi in list:
        deviations.append( abs(mean - xi) ** 2)
    variance = sum(deviations) / n
    return variance

def zstddev(list: List[float]) -> float:
    return  math.sqrt((zvariance(list)))


def zstderr(list: List[float]) -> float:
    return  zstddev(list) / math.sqrt(zcount(list))

def cov(listx: List[float], listy: List[float]) -> float:
   sum = 0
   if zcount(listx)== zcount(listy):
    for i in range(0, zcount(listx)):
        sum += ((listx[i] - zmean(listx)) * (listy[i] - zmean(listy)))
    cov = sum/(zcount(listx)-1)
   return cov

def zcorr(listx: List[float], listy: List[float]) -> float:
    return cov(listx, listy)/ zstddev(listx) * zstddev(listy)

