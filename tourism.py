import sys
import tourismMethods as tm  

def main():
    if len(sys.argv) == 1:
        print("please input t, p, s, a")
    else:
        if sys.argv[1] == 't':
            tm.tourismForTurkey() 
        elif sys.argv[1] == 'p':
            tm.tourismForPoland()
        elif sys.argv[1] == 's':
            tm.tourismForSpain()
        elif sys.argv[1] == "a":
            tm.allcountries()
        else:
            print("please input t, p, s, a")             

main()


#tourismForPoland(df)




