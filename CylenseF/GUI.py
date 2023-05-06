import time
import tkinter as tk
import os
from Game import Game


class GUI:
    def __init__(self, game) -> None:
        self.game = game
        self.root = tk.Tk()

        # window size
        self.root.geometry("1920x1080")
        self.root.state("zoomed")

        # title and logo
        self.root.title("Cylense")
        self.root.iconphoto(True, tk.PhotoImage(file=os.path.abspath("logo.png")))

        # make window unresizable
        self.root.resizable(False, False)

        # set background image
        self.bg_image = tk.PhotoImage(file=os.path.abspath("background.png"))
        self.bg_label = tk.Label(self.root, image=self.bg_image)
        self.bg_label.place(relwidth=1, relheight=1)

        # calculate position of the window
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.x = int((self.screen_width - 1920) / 2)
        self.y = int((self.screen_height - 1080) / 2)

        # set window position
        self.root.geometry("+{}+{}".format(self.x, self.y))
        self.root.protocol("WM_DELETE_WINDOW", game.set_game_state("game_over"))

        # set button position and size
        self.button_width = 250
        self.button_height = 75
        self.button_y = int((1080 - self.button_height) / 2.5)

        self.button_image_normal = tk.PhotoImage(  # hover image switching
            file=os.path.abspath("button_1.png")
        )
        self.button_image_hover = tk.PhotoImage(
            file=os.path.abspath("button_1_hover.png")
        )
        self.button_image_normal_2 = tk.PhotoImage(file=os.path.abspath("button_2.png"))
        self.button_image_hover_2 = tk.PhotoImage(
            file=os.path.abspath("button_2_hover.png")
        )
        self.button_image_normal_3 = tk.PhotoImage(file=os.path.abspath("button_3.png"))
        self.button_image_hover_3 = tk.PhotoImage(
            file=os.path.abspath("button_3_hover.png")
        )
        self.button_image_normal_4 = tk.PhotoImage(
            file=os.path.abspath("attack_button.png")
        )
        self.button_image_hover_4 = tk.PhotoImage(
            file=os.path.abspath("attack_button_hover.png")
        )
        self.button_image_normal_5 = tk.PhotoImage(
            file=os.path.abspath("place_button.png")
        )
        self.button_image_hover_5 = tk.PhotoImage(
            file=os.path.abspath("place_button_hover.png")
        )
        self.button_image_normal_6 = tk.PhotoImage(
            file=os.path.abspath("gamble_button.png")
        )
        self.button_image_hover_6 = tk.PhotoImage(
            file=os.path.abspath("gamble_button_hover.png")
        )
        self.button_image_normal_7 = tk.PhotoImage(
            file=os.path.abspath("draw_button.png")
        )
        self.button_image_hover_7 = tk.PhotoImage(
            file=os.path.abspath("draw_button_hover.png")
        )
        self.button_image_normal_8 = tk.PhotoImage(
            file=os.path.abspath("play_button.png")
        )
        self.button_image_hover_8 = tk.PhotoImage(
            file=os.path.abspath("play_button_hover.png")
        )
        self.button_image_normal_9 = tk.PhotoImage(
            file=os.path.abspath("exit_button.png")
        )
        self.button_image_hover_9 = tk.PhotoImage(
            file=os.path.abspath("exit_button_hover.png")
        )

        self.opponent_life_points_label = tk.Label(
            self.root,
            text="Opponent's life points: " + str(self.game.bot_life),
        )
        self.opponent_life_points_label.pack(side="top", anchor="ne", padx=10, pady=10)

        self.text_widget = tk.Frame(
            self.root, bg="black", highlightthickness=0, bd=0
        )  # text widget/frame properties

        self.input_widet = tk.Frame(self.root, bg="black", highlightthickness=0, bd=0)

        self.text_widget = tk.Text(
            self.root,
            font=("Lemon Milk Pro Regular", 17),
            bg="#343541",
            fg="white",
            wrap="word",
            bd=0,
            highlightthickness=0,
        )

        self.input_widget = tk.Text(
            self.root,
            font=("Lemon Milk Pro Regular", 17),
            bg="#343541",
            fg="white",
            wrap="word",
            bd=0,
            highlightthickness=0,
        )
        self.button = tk.Button(  # button properties
            self.root,
            image=self.button_image_normal,
            width=self.button_width,
            height=self.button_height,
            bd=0,
            relief="sunken",
            highlightthickness=0,
            activebackground="white",
        )

        self.button_2 = tk.Button(
            self.root,
            image=self.button_image_normal_2,
            width=self.button_width,
            height=self.button_height,
            bd=0,
            relief="sunken",
            highlightthickness=0,
            activebackground="white",
        )

        self.button_3 = tk.Button(
            self.root,
            image=self.button_image_normal_3,
            width=self.button_width,
            height=self.button_height,
            bd=0,
            relief="sunken",
            highlightthickness=0,
            activebackground="white",
        )

        self.button_4 = tk.Button(
            self.root,
            image=self.button_image_normal_4,
            width=232,
            height=114,
            bd=0,
            relief="sunken",
            highlightthickness=0,
            activebackground="white",
        )

        self.button_5 = tk.Button(
            self.root,
            image=self.button_image_normal_5,
            width=232,
            height=114,
            bd=0,
            relief="sunken",
            highlightthickness=0,
            activebackground="white",
        )

        self.button_6 = tk.Button(
            self.root,
            image=self.button_image_normal_6,
            width=232,
            height=114,
            bd=0,
            relief="sunken",
            highlightthickness=0,
            activebackground="white",
        )

        self.button_7 = tk.Button(
            self.root,
            image=self.button_image_normal_7,
            width=232,
            height=114,
            bd=0,
            relief="sunken",
            highlightthickness=0,
            activebackground="white",
        )

        self.button_8 = tk.Button(
            self.root,
            image=self.button_image_normal_8,
            width=244,
            height=116,
            bd=0,
            relief="sunken",
            highlightthickness=0,
            activebackground="white",
        )
        self.button_9 = tk.Button(
            self.root,
            image=self.button_image_normal_9,
            width=244,
            height=116,
            bd=0,
            relief="sunken",
            highlightthickness=0,
            activebackground="white",
        )

        self.button_x = int((1920 - self.button_width) / 2.012)
        button_y = int((1080 - self.button_height) / 2.5)

        self.button.place(x=self.button_x, y=self.button_y, anchor="nw")

        self.button_2.place(
            x=self.button_x, y=button_y + self.button_height + 28, anchor="nw"
        )

        self.button_3.place(
            x=self.button_x, y=button_y + (2 * self.button_height) + 56, anchor="nw"
        )

        self.button.bind("<Enter>", self.switch_button_image)
        self.button.bind("<Leave>", self.switch_button_image_back)
        self.button.bind("<Button-1>", self.clear_gui_1)

        self.button_2.bind("<Enter>", self.switch_button_image_2)
        self.button_2.bind("<Leave>", self.switch_button_image_back_2)
        self.button_2.bind("<Button-1>", self.clear_gui_2)

        self.button_3.bind("<Enter>", self.switch_button_image_3)
        self.button_3.bind("<Leave>", self.switch_button_image_back_3)
        self.button_3.bind("<Button-1>", self.exit_gui)

        self.button_4.bind("<Enter>", self.switch_button_image_4)
        self.button_4.bind("<Leave>", self.switch_button_image_back_4)
        self.button_4.bind(
            "<Button-1>",
            lambda event: self.clearInputAndAttack()
            if self.game.game_state == "player_attack"
            else self.game.startAttackPhase(),
        )

        self.button_5.bind("<Enter>", self.switch_button_image_5)
        self.button_5.bind("<Leave>", self.switch_button_image_back_5)
        self.button_5.bind(
            "<Button-1>",
            lambda event: self.clearInputAndPlaceCard()
            if self.game.game_state == "player_place"
            else self.game.startPlayerPlace(),
        )

        self.button_6.bind("<Enter>", self.switch_button_image_6)
        self.button_6.bind("<Leave>", self.switch_button_image_back_6)
        self.button_6.bind("<Button-1>", lambda event: self.game.playerGamble())

        self.button_7.bind("<Enter>", self.switch_button_image_7)
        self.button_7.bind("<Leave>", self.switch_button_image_back_7)
        self.button_7.bind("<Button-1>", lambda event: self.game.playerDraw())

    # define function to switch button image on mouse hover
    def switch_button_image_3(self, event):
        self.button_3.config(image=self.button_image_hover_3)

    def switch_button_image_back_3(self, event):
        self.button_3.config(image=self.button_image_normal_3)

    # define function to switch button image on mouse hover
    def switch_button_image_2(self, event):
        self.button_2.config(image=self.button_image_hover_2)

    def switch_button_image_back_2(self, event):
        self.button_2.config(image=self.button_image_normal_2)

    # define function to switch button image on mouse hover
    def switch_button_image(self, event):
        self.button.config(image=self.button_image_hover)

    def switch_button_image_back(self, event):
        self.button.config(image=self.button_image_normal)

    # define function to switch button image on mouse hover
    def switch_button_image_5(self, event):
        self.button_5.config(image=self.button_image_hover_5)

    def switch_button_image_back_5(self, event):
        self.button_5.config(image=self.button_image_normal_5)

    # define function to switch button image on mouse hover
    def switch_button_image_4(self, event):
        self.button_4.config(image=self.button_image_hover_4)

    def switch_button_image_back_4(self, event):
        self.button_4.config(image=self.button_image_normal_4)

    # define function to switch button image on mouse hover
    def switch_button_image_6(self, event):
        self.button_6.config(image=self.button_image_hover_6)

    def switch_button_image_back_6(self, event):
        self.button_6.config(image=self.button_image_normal_6)

        # define function to switch button image on mouse hover

    def switch_button_image_7(self, event):
        self.button_7.config(image=self.button_image_hover_7)

    def switch_button_image_back_7(self, event):
        self.button_7.config(image=self.button_image_normal_7)

    def start_game_loop(self):
        # run the GUI
        self.root.mainloop()

    def update_information(self):
        self.opponent_life_points_label.config(
            text="Opponent Life Points: " + str(self.game.bot_life)
        )
        return

    def clearInputAndAttack(self):
        try:
            input_value = self.input_widget.get("1.0", "end-1c")
            self.game.playerAttack(input_value)
            self.input_widget.delete("1.0", "end")
            print("input_value: " + input_value)
        except:
            input_value = ""
            self.input_widget.delete("1.0", "end")
            self.game.playerAttack(input_value)

    def clearInputAndPlaceCard(self):
        print("clearInputAndPlaceCard")
        try:
            input_value = self.input_widget.get("1.0", "end-1c")
            self.game.playerPlace(input_value)
            self.input_widget.delete("1.0", "end")
            print("input_value: " + input_value)
        except:
            input_value = ""
            self.input_widget.delete("1.0", "end")
            self.game.playerPlace(input_value)

    def clear_gui_1(self, event):  # action after clicking "play"
        # destroy all buttons
        self.button.destroy()
        self.button_2.destroy()
        self.button_3.destroy()
        # change background image
        bg_image = tk.PhotoImage(file="background_ingame.png")
        self.bg_label.config(image=bg_image)
        self.bg_label.image = bg_image

        """self.button_4.config(width=244, height=116)
        self.button_5.config(width=244, height=116)
        self.button_6.config(width=244, height=116)
        self.button_7.config(width=244, height=116)"""

        # reposition the button and place it on the window
        self.button_4.place(x=142, y=730, anchor="nw")

        # reposition the button and place it on the window
        self.button_5.place(x=406, y=730, anchor="nw")

        # reposition the button and place it on the window
        self.button_6.place(x=142, y=866, anchor="nw")

        # reposition the button and place it on the window
        self.button_7.place(x=406, y=866, anchor="nw")
        self.text_widget.pack()
        self.text_widget.place(
            relx=0.41, rely=0.373, relwidth=0.67, relheight=0.56, anchor="center"
        )

        self.input_widget.pack()
        self.input_widget.place(
            relx=0.565, rely=0.75, relwidth=0.20, relheight=0.10, anchor="center"
        )

        is_my_turn = self.game.startGame()
        if is_my_turn:
            self.append_text("You may start, as you've drawn a faster hand!")
        else:
            self.append_text("Your opponent starts, as he's drawn a faster hand!")
            self.game.start_opponent_turn()

    def clear_gui_2(self, event):
        self.button.destroy()
        self.button_2.destroy()
        self.button_3.destroy()
        bg_image = tk.PhotoImage(file="background_info.png")
        self.bg_label.config(image=bg_image)
        self.bg_label.image = bg_image
        self.text_widget.pack()
        self.text_widget.place(
            relx=0.5, rely=0.3915, relwidth=0.85, relheight=0.57, anchor="center"
        )

    # define function to exit the GUI
    def exit_gui(self, event):
        time.sleep(1)
        self.root.destroy()

    def append_text(self, text):
        self.text_widget.insert(tk.END, text + "\n")
        self.text_widget.see(tk.END)


game = Game()
print(game)
gui = GUI(game)
game.gui = gui
gui.start_game_loop()
