#x < 18.5, 18.5 - <25, 25 - <30, 30 - <40, 40 < x

import math


def height(x=None, m=None, y=None):
    ht = 0
    h = m
    if h == "1":
        h1 = x
        try:
            h1 = int(h1)
            if h1 < 0:
                return "unacceptable input '{}' is negative".format(h1)
        except:
            return "unacceptable input '{}' is not an integer".format(h1)
        h2 = y
        try:
            if h2 < 0:
                return "unacceptable input '{}' is negative".format(h2)
        except:
            return "unacceptable input '{}' is not an integer".format(h2)
        ht = h1*12 + h2
        if ht == 0:
            return "unacceptable inputs total height is zero inches"
        else:
           ht = ht * 0.0254
    elif h == "2":
        h1 = x
        try:
            if h1 <= 0:
                return "unacceptable input '{}' is negative or zero".format(h1)
        except:
            return "unacceptable input '{}' is not an integer".format(h1)
        ht = h1 / 100
    else:
        return "unacceptable input '{}' is not an accepted method".format(h)
    return ht


def weight(x=None, m=None):
    wt = 0
    w = m
    if w == "1":
        w1 = x
        try:
            if w1 < 0:
                return "unacceptable input '{}' is negative".format(w1)
        except:
            return "unacceptable input '{}' is not an integer".format(w1)
        wt = w1
        if wt == 0:
            return "unacceptable inputs total height is zero pounds"
        else:
            wt = wt * 0.453592
    elif w == "2":
        w1 = x
        try:
            if w1 <= 0:
                return "unacceptable input '{}' is negative or zero".format(w1)
        except:
            return "unacceptable input '{}' is not an integer".format(w1)
        wt = w1
    else:
        return "unacceptable input '{}' try again".format(m)
    return wt


def manual():
    hloop = True
    wloop = True
    while hloop:
        m = input("First we will define your height\nplease select either standard(1) or metric(2):")
        ht1 = 0
        ht2 = 0
        if m == "1":
            ht1 = input("Please enter your height's feet measurement:")
            ht2 = input("Please enter your height's inch measurement:")
        elif m == "2":
            ht1 = input("Please enter your height's centimeter measurement:")
            ht2 = 0
        else:
            print("test")
            print("unacceptable input '{}' try again".format(m))
        ht = height(ht1, m, ht2)
        if type(ht) is float:
            print(ht, "meters tall")
            hloop = False
        else:
            print(ht)
    while wloop:
        m = input("Next we will define your weight\nplease select either standard(1) or metric(2):")
        if m == "1":
            wt1 = input("Please enter your weight in pounds:")
        elif m == "2":
            wt1 = input("Please enter your weight in kilograms:")
        else:
            print("unacceptable input '{}' try again".format(m))
        wt = weight(wt1, m)
        if type(wt) is float:
            print(wt, "kilograms")
            wloop = False
        else:
            print(ht)
    ht2 = math.pow(ht, 2)
    bmi = wt / ht2
    if 0 < bmi < 18.5:
        print("bmi of %.2f is considered underweight" % bmi)
    elif 18.5 <= bmi < 25:
        print("bmi of %.2f is considered normal weight" % bmi)
    elif 25 <= bmi < 30:
        print("bmi of %.2f is considered overweight" % bmi)
    elif 30 <= bmi < 40:
        print("bmi of %.2f is considered obese" % bmi)
    elif 40 <= bmi:
        print("bmi of %.2f is considered extremely obese" % bmi)
    else:
        print("bmi of zero or less is impossible")


def auto(funtar, ht1, mh, ht2=0, wt1=0, mw=0):
    if funtar == 1:
        return (height(ht1, mh, ht2))
    if funtar == 2:
        return (weight(ht1, mh))
    if funtar == 3:
        h = height(ht1, mh, ht2)
        w = weight(wt1, mw)
        if isinstance(h, str):
            return h
        if isinstance(w, str):
            return w
        h2 = math.pow(h, 2)
        bmi = w / h2
        if 0 < bmi < 18.5:
            return ("bmi of %.2f is considered underweight" % bmi)
        elif 18.5 <= bmi < 25:
            return ("bmi of %.2f is considered normal weight" % bmi)
        elif 25 <= bmi < 30:
            return ("bmi of %.2f is considered overweight" % bmi)
        elif 30 <= bmi < 40:
            return ("bmi of %.2f is considered obese" % bmi)
        elif 40 <= bmi:
            return("bmi of %.2f is considered extremely obese" % bmi)
        else:
            return("bmi of zero or less is impossible")


def main():
    manual()


if __name__ == "__main__":
    main()
