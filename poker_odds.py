import argparse
from tkinter import *

win = Tk()


canvas= Canvas(win, width= 750, height= 500, bg="Black")
canvas.create_text(200,10,text="Calcumalate them odds, son.", fill="green", font=('Helvetica 15 bold'))

label= Label(win, text= "Select any One Language!", font= ("", 10))
label.pack(pady=30)

#Access the Menu Widget using StringVar function
clicked= StringVar()
#Create an instance of Menu in the frame
main_menu = OptionMenu(win, clicked, "C++", "Java", "Python", "Rust","Go","Ruby")
main_menu.pack()
win.mainloop()
# w=Button(master, option=value)


def main(args):
    print("There are ", args, " players.")

cards=['Ac', 'Kc', 'Qc', 'Jc', '10c', '9c', '8c', '7c',
       '6c', '5c', '4c', '3c', '2c',
       'As', 'Ks', 'Qs', 'Js', '10s', '9s', '8s', '7s',
       '6s', '5s', '4s', '3s', '2s',
       'Ah', 'Kh', 'Qh', 'Jh', '10h', '9h', '8h', '7h',
       '6h', '5h', '4h', '3h', '2h',
       'Ad', 'Kd', 'Qd', 'Jd', '10d', '9d', '8d', '7d',
       '6d', '5d', '4d', '3d', '2d'
       ]

if __name__ == '__main__':
    description = 'Set up poker env'
    parser = argparse.ArgumentParser(description=description)

    # parser.add_argument("infile", type=str, help="Input file name")
    parser.add_argument("-p", "--players", type=float, choices=range(2, 10),
    help="# of players")
    parser.add_argument("-c", "--cards_i", type=str, choices=cards,
                        help="Pick yo damn cards")

    args = parser.parse_args()
    main(args)